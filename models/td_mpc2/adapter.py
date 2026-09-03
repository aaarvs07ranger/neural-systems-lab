"""TD-MPC2 baseline adapter — implements ``models.common.BaselineAdapter``.

Drives the vendored nicklashansen/tdmpc2 agent (``vendor/``, pinned commit in
``vendor/VENDOR.md``) on our fixed ProcTHOR ObjectNav task so that
``main.py --baseline tdmpc2`` reuses the exact PPO/DreamerV3 transfer-eval
protocol and reporting code.

Design notes
------------
* ``train()`` is a faithful re-implementation of the upstream
  ``trainer/online_trainer.py`` loop (episodic mode) minus wandb/video and the
  interleaved eval env (a second Unity process — same reasoning as the
  DreamerV3 adapter). The recipe is upstream's published default: 1 gradient
  update per env step after ``seed_steps`` random steps, plus a
  ``seed_steps``-update pretrain burst; rgb obs = 64x64, 3-frame stack.
* Discrete actions ride the continuous relaxation in ``thor_env.py``
  (Box(-1,1,(5,)) -> argmax at the env boundary).
* Preemption safety: every episode is persisted to
  ``logs/tdmpc2/train_eps/ep_*.pt`` and ``latest.pt`` stores model+optims+step.
  A requeued job rebuilds the replay buffer from disk and resumes at the
  checkpointed step (same contract as the DreamerV3 adapter).
* Episodes with < horizon+1 transitions (trivial spawns) cannot be sliced by
  the buffer sampler (``strict_length=True``) and are excluded from replay —
  counted and logged; see vendor/VENDOR.md behavioral notes.
* Eval determinism caveat: upstream's ``ShiftAug`` is active at eval, so
  eval actions are mildly stochastic even with ``deterministic=True``
  (documented in VENDOR.md; the paired-seed env protocol is unaffected).
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Optional, Tuple

# Must precede any torch import (some ops lack Metal kernels).
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import numpy as np

from config import (
    CHECKPOINTS_DIR,
    LOGS_DIR,
    TDMPC2Config,
    get_device,
)
from envs.procthor_env import make_objectnav_env
from envs.task_setup import build_env_config
from models.td_mpc2.thor_env import TDMPC2THOREnv, frame_to_chw

logger = logging.getLogger("tdmpc2_adapter")

TDM_CKPT_DIR = CHECKPOINTS_DIR / "tdmpc2"
TDM_LOG_DIR = LOGS_DIR / "tdmpc2"
FINAL_MODEL_PATH = TDM_CKPT_DIR / "tdmpc2_final.pt"
LATEST_PATH = TDM_CKPT_DIR / "latest.pt"


class _Cfg(SimpleNamespace):
    """Attribute namespace with the ``.get`` the vendored code expects."""

    def get(self, key: str, default: Any = None) -> Any:
        return getattr(self, key, default)


def _tdmpc2_device() -> str:
    """CUDA > CPU. MPS is deliberately excluded for this baseline: on torch
    2.2.2 the TD-MPC2 update graph intermittently produces inf/nan losses on
    MPS (async-execution race; CPU/CUDA verified clean — see
    vendor/VENDOR.md). Local runs are smoke-scale; real runs are CUDA."""
    device = get_device()
    if device == "mps":
        logger.warning(
            "TD-MPC2 on MPS is numerically unreliable on torch 2.2 — "
            "falling back to CPU (fine for smoke; use CUDA for real runs)"
        )
        return "cpu"
    return device


def _make_tdmpc2_config(tdm_cfg: TDMPC2Config, num_actions: int) -> _Cfg:
    """Mirror upstream ``parser.parse_cfg`` output for the vendored modules."""
    from models.td_mpc2.vendor.common import MODEL_SIZE

    episode_length = tdm_cfg.max_episode_steps
    seed_steps = (
        tdm_cfg.seed_steps
        if tdm_cfg.seed_steps is not None
        else max(1000, 5 * episode_length)  # upstream formula (envs/__init__.py)
    )
    cfg = _Cfg(
        # Task / obs
        task="procthor-objectnav",
        task_title="ProcTHOR ObjectNav",
        obs="rgb",
        obs_shape={"rgb": (3 * tdm_cfg.frame_stack, tdm_cfg.image_size, tdm_cfg.image_size)},
        action_dim=int(num_actions),
        episode_length=episode_length,
        episodic=True,          # ObjectNav terminates on success
        multitask=False,
        tasks=["procthor-objectnav"],
        task_dim=0,
        # Budget / replay
        steps=int(tdm_cfg.total_timesteps),
        seed_steps=int(seed_steps),
        batch_size=tdm_cfg.batch_size,
        buffer_size=tdm_cfg.buffer_size,
        horizon=tdm_cfg.horizon,
        # Optimisation (upstream defaults)
        lr=tdm_cfg.lr,
        enc_lr_scale=tdm_cfg.enc_lr_scale,
        grad_clip_norm=tdm_cfg.grad_clip_norm,
        tau=tdm_cfg.tau,
        rho=tdm_cfg.rho,
        consistency_coef=tdm_cfg.consistency_coef,
        reward_coef=tdm_cfg.reward_coef,
        value_coef=tdm_cfg.value_coef,
        termination_coef=tdm_cfg.termination_coef,
        entropy_coef=tdm_cfg.entropy_coef,
        discount_denom=tdm_cfg.discount_denom,
        discount_min=tdm_cfg.discount_min,
        discount_max=tdm_cfg.discount_max,
        # Planning (MPPI)
        mpc=True,
        iterations=tdm_cfg.iterations,
        num_samples=tdm_cfg.num_samples,
        num_elites=tdm_cfg.num_elites,
        num_pi_trajs=tdm_cfg.num_pi_trajs,
        min_std=tdm_cfg.min_std,
        max_std=tdm_cfg.max_std,
        temperature=tdm_cfg.temperature,
        # Actor / critic heads
        log_std_min=tdm_cfg.log_std_min,
        log_std_max=tdm_cfg.log_std_max,
        num_bins=tdm_cfg.num_bins,
        vmin=tdm_cfg.vmin,
        vmax=tdm_cfg.vmax,
        bin_size=(tdm_cfg.vmax - tdm_cfg.vmin) / (tdm_cfg.num_bins - 1),
        # Architecture (model_size expands like upstream parser)
        model_size=tdm_cfg.model_size,
        num_enc_layers=2,
        enc_dim=256,
        mlp_dim=512,
        latent_dim=512,
        num_channels=tdm_cfg.num_channels,
        num_q=5,
        dropout=tdm_cfg.dropout,
        simnorm_dim=tdm_cfg.simnorm_dim,
        # Device / misc
        device=_tdmpc2_device(),
        compile=False,  # no inductor-MPS on torch 2.2; enable on CUDA only after smoke
        seed=tdm_cfg.seed,
    )
    for key, value in MODEL_SIZE[tdm_cfg.model_size].items():
        setattr(cfg, key, value)
    return cfg


class TDMPC2Adapter:
    """Trainable TD-MPC2 baseline satisfying the BaselineAdapter protocol."""

    name = "tdmpc2"

    def __init__(self, tdm_cfg: Optional[TDMPC2Config] = None) -> None:
        self._cfg = tdm_cfg or TDMPC2Config()
        self._agent: Optional[Any] = None
        self._frames: Optional[list] = None
        self._t0: bool = True

    # ------------------------------------------------------------------
    # Training (mirrors vendored trainer/online_trainer.py, episodic mode)
    # ------------------------------------------------------------------
    def train(self, house_a_path: Path, total_timesteps: int, seed: int,
              pair=None) -> Path:
        import torch
        from tensordict.tensordict import TensorDict

        from models.td_mpc2.vendor.common.buffer import Buffer
        from models.td_mpc2.vendor.common.seed import set_seed
        from models.td_mpc2.vendor.tdmpc2 import TDMPC2

        tdm_cfg = self._cfg
        if total_timesteps != tdm_cfg.total_timesteps:
            tdm_cfg = replace(tdm_cfg, total_timesteps=total_timesteps)

        TDM_CKPT_DIR.mkdir(parents=True, exist_ok=True)
        eps_dir = TDM_LOG_DIR / "train_eps"  # replay episodes (.pt, gitignored)
        eps_dir.mkdir(parents=True, exist_ok=True)

        set_seed(seed)
        env_cfg = build_env_config(tdm_cfg, pair, split="train")
        env = TDMPC2THOREnv(
            make_objectnav_env(house_a_path, env_cfg, name="variant_a"),
            image_size=tdm_cfg.image_size,
            frame_stack=tdm_cfg.frame_stack,
            seed=seed,
            max_episode_steps=tdm_cfg.max_episode_steps,
        )
        cfg = _make_tdmpc2_config(tdm_cfg, env.num_actions)
        cfg.seed = seed

        logger.info(
            "building TD-MPC2 agent on device=%s (model_size=%dM, batch=%d, "
            "horizon=%d, seed_steps=%d, budget=%d env steps)",
            cfg.device, cfg.model_size, cfg.batch_size, cfg.horizon,
            cfg.seed_steps, cfg.steps,
        )
        buffer = Buffer(cfg)
        agent = TDMPC2(cfg)

        def to_td(obs, action=None, reward=None, terminated=None) -> TensorDict:
            """Upstream OnlineTrainer.to_td, verbatim semantics."""
            obs = obs.unsqueeze(0).cpu()
            if action is None:
                action = torch.full((env.num_actions,), float("nan"))
            if reward is None:
                reward = torch.tensor(float("nan"))
            if terminated is None:
                terminated = torch.tensor(float("nan"))
            return TensorDict(
                dict(
                    obs=obs,
                    action=action.unsqueeze(0),
                    reward=reward.unsqueeze(0),
                    terminated=terminated.unsqueeze(0),
                ),
                batch_size=(1,),
            )

        # --- Resume: rebuild replay from on-disk episodes, restore weights ---
        step, ep_count, dropped_short = 0, 0, 0
        ep_files = sorted(eps_dir.glob("ep_*.pt"))
        for f in ep_files:
            td = torch.load(f)
            ep_count += 1
            if td.shape[0] >= cfg.horizon + 1:
                buffer.add(td)
            else:
                dropped_short += 1
        if LATEST_PATH.exists():
            ckpt = torch.load(LATEST_PATH, map_location=cfg.device)
            agent.model.load_state_dict(ckpt["model"])
            agent.optim.load_state_dict(ckpt["optim"])
            agent.pi_optim.load_state_dict(ckpt["pi_optim"])
            agent.scale.load_state_dict(ckpt["scale"])
            step = int(ckpt["step"])
            logger.info(
                "resumed from %s at env step %d (%d episodes on disk)",
                LATEST_PATH, step, ep_count,
            )
        elif ep_files:
            # Episodes without a checkpoint (crash before first save):
            # count their steps so the budget stays honest.
            step = sum(max(0, torch.load(f).shape[0] - 1) for f in ep_files)

        def save_checkpoint(path: Path) -> None:
            torch.save(
                {
                    "model": agent.model.state_dict(),
                    "optim": agent.optim.state_dict(),
                    "pi_optim": agent.pi_optim.state_dict(),
                    "scale": agent.scale.state_dict(),
                    "step": step,
                },
                path,
            )

        start = time.time()
        last_save = step
        done, tds, ep_returns = True, [], []
        while step <= cfg.steps:
            if done:
                if len(tds) > 1:
                    td = torch.cat(tds)
                    torch.save(td, eps_dir / f"ep_{ep_count:06d}.pt")
                    ep_count += 1
                    if td.shape[0] >= cfg.horizon + 1:
                        buffer.add(td)
                    else:
                        dropped_short += 1
                    ep_return = float(
                        torch.stack([t["reward"][0] for t in tds[1:]]).sum()
                    )
                    ep_returns.append(ep_return)
                    if ep_count % 25 == 0:
                        logger.info(
                            "episode %d: return=%.2f len=%d success=%.0f "
                            "(short-dropped so far: %d)",
                            ep_count, ep_return, len(tds) - 1,
                            info["success"], dropped_short,
                        )
                obs = env.reset()
                tds = [to_td(obs)]

            if step > cfg.seed_steps:
                action = agent.act(obs, t0=len(tds) == 1)
            else:
                action = env.rand_act()
            obs, reward, done, info = env.step(action)
            tds.append(to_td(obs, action, reward, info["terminated"]))

            if step >= cfg.seed_steps and buffer.num_eps > 0:
                if step == cfg.seed_steps:
                    num_updates = cfg.seed_steps
                    logger.info("pretraining agent on seed data (%d updates)...", num_updates)
                else:
                    num_updates = 1
                for _ in range(num_updates):
                    metrics = agent.update(buffer)
                if step % tdm_cfg.log_every == 0:
                    logger.info(
                        "[%d/%d] %s",
                        step, cfg.steps,
                        " / ".join(f"{k} {float(v):.3f}" for k, v in metrics.items()),
                    )

            step += 1
            if step - last_save >= tdm_cfg.save_every:
                save_checkpoint(LATEST_PATH)
                last_save = step
                logger.info(
                    "checkpointed at env step %d/%d (%.1f min elapsed)",
                    step, cfg.steps, (time.time() - start) / 60.0,
                )

        save_checkpoint(LATEST_PATH)
        agent.save(FINAL_MODEL_PATH)  # upstream format: {"model": state_dict}
        env.close()
        logger.info(
            "training finished in %.1f min (%d episodes, %d short-dropped) — "
            "final model: %s",
            (time.time() - start) / 60.0, ep_count, dropped_short, FINAL_MODEL_PATH,
        )
        return FINAL_MODEL_PATH

    # ------------------------------------------------------------------
    # Frozen-policy evaluation interface
    # ------------------------------------------------------------------
    def load(self, model_path: Path) -> None:
        from models.td_mpc2.vendor.tdmpc2 import TDMPC2

        env_cfg = build_env_config(self._cfg)
        cfg = _make_tdmpc2_config(self._cfg, len(env_cfg.actions))
        agent = TDMPC2(cfg)
        agent.load(Path(model_path))
        agent.model.eval()
        self._agent = agent
        self.reset_episode()
        logger.info("loaded frozen TD-MPC2 model from %s", model_path)

    def reset_episode(self) -> None:
        """Clear the frame stack and planner warm-start at episode boundaries."""
        self._frames = None
        self._t0 = True
        if self._agent is not None:
            self._agent._prev_mean.zero_()

    def predict(
        self, observation: np.ndarray, deterministic: bool = True
    ) -> Tuple[int, None]:
        """Discrete action for one RGB frame (SB3-style ``(action, state)``)."""
        assert self._agent is not None, "call load() before predict()"
        import torch

        frame = frame_to_chw(observation, self._cfg.image_size)
        if self._frames is None:
            self._frames = [frame] * self._cfg.frame_stack
        else:
            self._frames = self._frames[1:] + [frame]
        obs = torch.from_numpy(np.concatenate(self._frames))
        with torch.no_grad():
            action = self._agent.act(obs, t0=self._t0, eval_mode=deterministic)
        self._t0 = False
        return int(torch.as_tensor(action).argmax().item()), None
