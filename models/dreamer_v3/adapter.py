"""DreamerV3 baseline adapter — implements ``models.common.BaselineAdapter``.

Drives the vendored NM512/dreamerv3-torch agent (``vendor/``) on our fixed
ProcTHOR ObjectNav task so that ``main.py --baseline dreamerv3`` reuses the
exact PPO transfer-eval protocol and reporting code.

Design notes
------------
* The upstream ``dreamer.py:main()`` loop is NOT reused: it unconditionally
  boots a second eval environment (a second Unity process — too heavy on the
  M4 Air) and hardcodes suite dispatch. ``train()`` below is a faithful,
  slimmed re-implementation of that loop: prefill with a random one-hot
  policy -> replay-buffered ``tools.simulate`` -> periodic ``latest.pt``
  checkpoints, minus the interleaved eval.
* MPS compatibility is config-only: ``device=mps``, ``compile=False`` (no
  inductor backend for MPS on torch 2.2), ``precision=32`` (AMP contexts
  become no-ops), ``video_pred_log=False`` (avoids the moviepy/ffmpeg path in
  TensorBoard video summaries). ``PYTORCH_ENABLE_MPS_FALLBACK=1`` covers the
  few ops without Metal kernels.
* DreamerV3 is recurrent: the eval loop must call :meth:`reset_episode`
  at every episode boundary so the latent state and ``is_first`` flag are
  cleared (scripts/evaluate_transfer.py does this via ``hasattr``).

TensorBoard training curves land in ``results/logs/dreamerv3``
(``tensorboard --logdir results/logs/dreamerv3``).
"""
from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, Optional, Tuple

# Must precede any torch import (some ops lack Metal kernels).
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import numpy as np
import yaml

from config import (
    CHECKPOINTS_DIR,
    LOGS_DIR,
    TASK_CONFIG_PATH,
    DreamerV3Config,
    get_device,
)
from envs.procthor_env import ObjectNavConfig, make_objectnav_env
from models.dreamer_v3.thor_env import DreamerTHOREnv

logger = logging.getLogger("dreamerv3_adapter")

VENDOR_DIR = Path(__file__).resolve().parent / "vendor"
DV3_CKPT_DIR = CHECKPOINTS_DIR / "dreamerv3"
DV3_LOG_DIR = LOGS_DIR / "dreamerv3"
FINAL_MODEL_PATH = DV3_CKPT_DIR / "dreamer_final.pt"

# Fixed discrete-action recipe from upstream configs.yaml (atari100k/crafter).
_DISCRETE_OVERRIDES = {"actor": {"dist": "onehot", "std": "none"},
                       "imag_gradient": "reinforce"}


def _build_env_config(dv3_cfg: DreamerV3Config) -> ObjectNavConfig:
    """Same task assembly as scripts/train_ppo.py (identical protocol)."""
    if not TASK_CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"{TASK_CONFIG_PATH} not found — run `python main.py --stage generate` first."
        )
    task = json.loads(TASK_CONFIG_PATH.read_text())
    return ObjectNavConfig(
        target_object_type=task["target_object_type"],
        max_steps=dv3_cfg.max_episode_steps,
    )


def _coerce_scalars(node: Any) -> Any:
    """Recursively convert scientific-notation strings ('1e-4') to floats.

    Upstream parses configs.yaml with ruamel (YAML 1.2, where 1e-4 IS a
    float); pyyaml follows YAML 1.1 and yields the *string* '1e-4', which
    would blow up inside torch.optim. Non-numeric strings pass through.
    """
    if isinstance(node, dict):
        return {k: _coerce_scalars(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_coerce_scalars(v) for v in node]
    if isinstance(node, str):
        try:
            return float(node)
        except ValueError:
            return node
    return node


def _make_dreamer_config(
    dv3_cfg: DreamerV3Config, num_actions: int
) -> SimpleNamespace:
    """Vendored configs.yaml defaults + our overrides -> attribute namespace."""
    cfg: Dict[str, Any] = _coerce_scalars(
        yaml.safe_load((VENDOR_DIR / "configs.yaml").read_text())["defaults"]
    )

    def merge(base: Dict[str, Any], update: Dict[str, Any]) -> None:
        for key, value in update.items():
            if isinstance(value, dict) and isinstance(base.get(key), dict):
                merge(base[key], value)
            else:
                base[key] = value

    merge(cfg, _DISCRETE_OVERRIDES)
    merge(
        cfg,
        {
            # Run control
            "seed": dv3_cfg.seed,
            "steps": int(dv3_cfg.total_timesteps),
            "action_repeat": 1,       # THOR nav actions must not be repeated
            "envs": 1,
            "parallel": False,
            "prefill": dv3_cfg.prefill,
            "time_limit": dv3_cfg.max_episode_steps,
            "eval_episode_num": 0,    # transfer eval is external & paired
            "log_every": dv3_cfg.log_every,
            # Device (M4 MPS)
            "device": get_device(),
            "compile": False,         # torch.compile has no MPS backend (2.2)
            "precision": 32,
            "video_pred_log": False,  # TB video needs moviepy/ffmpeg — skip
            # Observation / replay / optimisation
            "size": [dv3_cfg.image_size, dv3_cfg.image_size],
            "batch_size": dv3_cfg.batch_size,
            "batch_length": dv3_cfg.batch_length,
            "train_ratio": dv3_cfg.train_ratio,
            "pretrain": dv3_cfg.pretrain,
            "dataset_size": dv3_cfg.dataset_size,
            # Model size (upstream defaults = the small DMC-scale model)
            "dyn_hidden": dv3_cfg.dyn_hidden,
            "dyn_deter": dv3_cfg.dyn_deter,
            "units": dv3_cfg.units,
            "encoder": {"cnn_depth": dv3_cfg.cnn_depth},
            "decoder": {"cnn_depth": dv3_cfg.cnn_depth},
        },
    )
    ns = SimpleNamespace(**cfg)
    ns.num_actions = int(num_actions)  # upstream main() sets this post-hoc too
    return ns


class DreamerV3Adapter:
    """Trainable DreamerV3 baseline satisfying the BaselineAdapter protocol."""

    name = "dreamerv3"

    def __init__(self, dv3_cfg: Optional[DreamerV3Config] = None) -> None:
        self._cfg = dv3_cfg or DreamerV3Config()
        self._agent: Optional[Any] = None          # vendored dreamer.Dreamer
        self._state: Optional[Tuple[Any, Any]] = None  # (latent, action)
        self._is_first: bool = True

    # ------------------------------------------------------------------
    # Training (mirrors vendored dreamer.py:main, single env, no interleaved eval)
    # ------------------------------------------------------------------
    def train(self, house_a_path: Path, total_timesteps: int, seed: int) -> Path:
        import torch

        from models.dreamer_v3.vendor import tools
        from models.dreamer_v3.vendor.dreamer import (
            Dreamer,
            count_steps,
            make_dataset,
        )
        from models.dreamer_v3.vendor.parallel import Damy

        dv3_cfg = self._cfg
        if total_timesteps != dv3_cfg.total_timesteps:
            from dataclasses import replace

            dv3_cfg = replace(dv3_cfg, total_timesteps=total_timesteps)

        DV3_CKPT_DIR.mkdir(parents=True, exist_ok=True)
        DV3_LOG_DIR.mkdir(parents=True, exist_ok=True)
        traindir = DV3_LOG_DIR / "train_eps"  # replay episodes (npz, gitignored)
        traindir.mkdir(parents=True, exist_ok=True)

        tools.set_seed_everywhere(seed)

        env_cfg = _build_env_config(dv3_cfg)
        thor_env = DreamerTHOREnv(
            make_objectnav_env(house_a_path, env_cfg, name="variant_a"),
            image_size=dv3_cfg.image_size,
            seed=seed,
        )
        env = Damy(thor_env)
        config = _make_dreamer_config(dv3_cfg, thor_env.num_actions)
        config.seed = seed

        # Resume-aware step accounting: replayed episodes on disk count
        # toward the budget, exactly like upstream.
        dreamer_logger = tools.Logger(DV3_LOG_DIR, step=count_steps(traindir))
        train_eps = tools.load_episodes(traindir, limit=config.dataset_size)

        prefill = max(0, config.prefill - count_steps(traindir))
        state = None
        if prefill:
            logger.info("prefilling replay buffer with %d random steps", prefill)
            random_actor = tools.OneHotDist(
                torch.zeros(config.num_actions).repeat(config.envs, 1)
            )

            def random_agent(obs, done, agent_state):
                action = random_actor.sample()
                logprob = random_actor.log_prob(action)
                return {"action": action, "logprob": logprob}, None

            state = tools.simulate(
                random_agent, [env], train_eps, traindir, dreamer_logger,
                limit=config.dataset_size, steps=prefill,
            )
            dreamer_logger.step += prefill

        dataset = make_dataset(train_eps, config)
        logger.info(
            "building DreamerV3 agent on device=%s "
            "(train_ratio=%d, batch=%dx%d, budget=%d env steps)",
            config.device, config.train_ratio, config.batch_size,
            config.batch_length, config.steps,
        )
        agent = Dreamer(
            thor_env.observation_space, thor_env.action_space,
            config, dreamer_logger, dataset,
        ).to(config.device)
        agent.requires_grad_(requires_grad=False)

        latest = DV3_CKPT_DIR / "latest.pt"
        if latest.exists():
            checkpoint = torch.load(latest, map_location=config.device)
            agent.load_state_dict(checkpoint["agent_state_dict"])
            tools.recursively_load_optim_state_dict(
                agent, checkpoint["optims_state_dict"]
            )
            agent._should_pretrain._once = False
            logger.info("resumed from %s at env step %d", latest, agent._step)

        def checkpoint_payload() -> Dict[str, Any]:
            return {
                "agent_state_dict": agent.state_dict(),
                "optims_state_dict": tools.recursively_collect_optim_state_dict(agent),
            }

        start = time.time()
        while agent._step < config.steps:
            chunk = min(dv3_cfg.save_every, config.steps - agent._step)
            state = tools.simulate(
                agent, [env], train_eps, traindir, dreamer_logger,
                limit=config.dataset_size, steps=chunk, state=state,
            )
            torch.save(checkpoint_payload(), latest)
            logger.info(
                "checkpointed at env step %d/%d (%.1f min elapsed)",
                agent._step, config.steps, (time.time() - start) / 60.0,
            )
        torch.save(checkpoint_payload(), FINAL_MODEL_PATH)
        env.close()
        logger.info(
            "training finished in %.1f min — final model: %s",
            (time.time() - start) / 60.0, FINAL_MODEL_PATH,
        )
        return FINAL_MODEL_PATH

    # ------------------------------------------------------------------
    # Frozen-policy evaluation interface
    # ------------------------------------------------------------------
    def load(self, model_path: Path) -> None:
        import torch

        from models.dreamer_v3.vendor import tools
        from models.dreamer_v3.vendor.dreamer import Dreamer

        env_cfg = _build_env_config(self._cfg)
        num_actions = len(env_cfg.actions)
        config = _make_dreamer_config(self._cfg, num_actions)

        # Static spaces (identical to DreamerTHOREnv) — no Unity boot needed.
        from gymnasium import spaces

        size = self._cfg.image_size
        obs_space = spaces.Dict(
            {
                "image": spaces.Box(0, 255, (size, size, 3), dtype=np.uint8),
                "is_first": spaces.Box(0, 1, (), dtype=bool),
                "is_last": spaces.Box(0, 1, (), dtype=bool),
                "is_terminal": spaces.Box(0, 1, (), dtype=bool),
            }
        )
        act_space = spaces.Box(0.0, 1.0, (num_actions,), dtype=np.float32)

        eval_logdir = DV3_LOG_DIR / "eval_logger"  # throwaway TB sink
        eval_logdir.mkdir(parents=True, exist_ok=True)
        dreamer_logger = tools.Logger(eval_logdir, step=0)

        agent = Dreamer(obs_space, act_space, config, dreamer_logger, dataset=None)
        checkpoint = torch.load(Path(model_path), map_location=config.device)
        agent.load_state_dict(checkpoint["agent_state_dict"])
        agent.to(config.device)
        agent.requires_grad_(requires_grad=False)

        self._agent = agent
        self.reset_episode()
        logger.info("loaded frozen DreamerV3 model from %s", model_path)

    def reset_episode(self) -> None:
        """Clear recurrent latent state — call at every episode boundary."""
        self._state = None
        self._is_first = True

    def predict(self, observation: np.ndarray, deterministic: bool = True
                ) -> Tuple[int, None]:
        """Action for one RGB frame (SB3-compatible ``(action, state)`` tuple)."""
        assert self._agent is not None, "call load() before predict()"
        import cv2
        import torch

        size = self._cfg.image_size
        frame = observation
        if frame.shape[0] != size or frame.shape[1] != size:
            frame = cv2.resize(frame, (size, size), interpolation=cv2.INTER_AREA)
        obs = {
            "image": frame[None].astype(np.uint8),
            "is_first": np.array([self._is_first]),
            "is_last": np.array([False]),
            "is_terminal": np.array([False]),
        }
        with torch.no_grad():
            policy_output, self._state = self._agent._policy(
                obs, self._state, training=not deterministic
            )
        self._is_first = False
        action = policy_output["action"][0].detach().cpu().numpy()
        return int(np.argmax(action)), None
