"""Train the PPO baseline (stable-baselines3) on visual variant A.

Trains a CnnPolicy on the fixed ObjectNav task in house A, with periodic
checkpoints and CSV episode logs. The saved final model is then consumed by
``scripts/evaluate_transfer.py`` for the zero-shot A->B comparison.

Usage:
    python scripts/train_ppo.py [--total-steps N] [--smoke]
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Union

# MPS fallback must be set before torch is imported anywhere downstream:
# a few ops used by SB3 are not yet implemented on Metal and fall back to CPU.
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    CHECKPOINTS_DIR,
    HOUSE_A_PATH,
    LOGS_DIR,
    TASK_CONFIG_PATH,
    PPOConfig,
    SmokePPOConfig,
    ensure_dirs,
    get_device,
)
from envs.procthor_env import ObjectNavConfig, make_objectnav_env  # noqa: E402

logger = logging.getLogger("train_ppo")

PPO_CKPT_DIR = CHECKPOINTS_DIR / "ppo"
PPO_LOG_DIR = LOGS_DIR / "ppo"
FINAL_MODEL_PATH = PPO_CKPT_DIR / "ppo_final"


def build_env_config(ppo_cfg: PPOConfig) -> ObjectNavConfig:
    """Assemble the task config saved by envs/generate_variants.py."""
    if not TASK_CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"{TASK_CONFIG_PATH} not found — run `python envs/generate_variants.py` "
            "(or `python main.py --stage generate`) first."
        )
    task = json.loads(TASK_CONFIG_PATH.read_text())
    return ObjectNavConfig(
        target_object_type=task["target_object_type"],
        max_steps=ppo_cfg.max_episode_steps,
    )


def train(ppo_cfg: PPOConfig) -> Path:
    """Run PPO training on variant A; returns the final model path."""
    from stable_baselines3 import PPO
    from stable_baselines3.common.callbacks import CheckpointCallback
    from stable_baselines3.common.monitor import Monitor

    ensure_dirs()
    PPO_CKPT_DIR.mkdir(parents=True, exist_ok=True)
    PPO_LOG_DIR.mkdir(parents=True, exist_ok=True)

    env_cfg = build_env_config(ppo_cfg)
    env = Monitor(
        make_objectnav_env(HOUSE_A_PATH, env_cfg, name="variant_a"),
        filename=str(PPO_LOG_DIR / "train_variant_a"),
        info_keywords=("success", "spl"),
    )
    # Seed the start-pose RNG once; training episodes then vary reproducibly.
    env.reset(seed=ppo_cfg.seed)

    device = get_device()
    logger.info(
        "training PPO on device=%s for %d steps (target=%s)",
        device, ppo_cfg.total_timesteps, env_cfg.target_object_type,
    )
    model = PPO(
        "CnnPolicy",
        env,
        n_steps=ppo_cfg.n_steps,
        batch_size=ppo_cfg.batch_size,
        n_epochs=ppo_cfg.n_epochs,
        learning_rate=ppo_cfg.learning_rate,
        gamma=ppo_cfg.gamma,
        gae_lambda=ppo_cfg.gae_lambda,
        ent_coef=ppo_cfg.ent_coef,
        clip_range=ppo_cfg.clip_range,
        seed=ppo_cfg.seed,
        device=device,
        verbose=1,
    )
    checkpoint_cb = CheckpointCallback(
        save_freq=ppo_cfg.checkpoint_freq,
        save_path=str(PPO_CKPT_DIR),
        name_prefix="ppo",
    )

    start = time.time()
    model.learn(total_timesteps=ppo_cfg.total_timesteps, callback=checkpoint_cb)
    elapsed = time.time() - start
    logger.info("training finished in %.1f min", elapsed / 60.0)

    model.save(str(FINAL_MODEL_PATH))
    env.close()
    logger.info("saved final model to %s.zip", FINAL_MODEL_PATH)
    return FINAL_MODEL_PATH


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--total-steps", type=int, default=None,
                        help="override total training timesteps")
    parser.add_argument("--smoke", action="store_true",
                        help="tiny run to verify pipeline mechanics")
    args = parser.parse_args()

    cfg: Union[PPOConfig, SmokePPOConfig] = SmokePPOConfig() if args.smoke else PPOConfig()
    if args.total_steps is not None:
        # dataclass is frozen; rebuild with the override
        cfg = type(cfg)(**{**cfg.__dict__, "total_timesteps": args.total_steps})
    train(cfg)


if __name__ == "__main__":
    main()
