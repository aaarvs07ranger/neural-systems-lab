"""Train the PPO-family baselines (stable-baselines3) on visual variant A.

Covers both ``ppo`` (vanilla) and ``ppo_aug`` (train-time photometric jitter,
the augmentation/domain-randomization baseline). The two share the exact same
recipe, budget, and protocol; ``cfg.augment`` is the ONLY difference, and it
applies to the TRAINING env only — ``scripts/evaluate_transfer.py`` always
builds raw, un-augmented eval envs, so the paired A/B protocol is identical
across all baselines.

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


def ckpt_dir(baseline_name: str = "ppo") -> Path:
    """Checkpoint directory for a PPO-family baseline ('ppo' / 'ppo_aug')."""
    return CHECKPOINTS_DIR / baseline_name


def final_model_path(baseline_name: str = "ppo") -> Path:
    """Final SB3 model path (without the .zip suffix SB3 appends on save)."""
    return ckpt_dir(baseline_name) / "ppo_final"


def build_env_config(ppo_cfg: PPOConfig) -> ObjectNavConfig:
    """Assemble the task config saved by envs/generate_variants.py."""
    if not TASK_CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"{TASK_CONFIG_PATH} not found — run `python envs/generate_variants.py` "
            "(or `python main.py --stage generate`) first."
        )
    task = json.loads(TASK_CONFIG_PATH.read_text())
    # T2 (sequential ObjectNav) is opt-in per house: a "target_sequence" key in
    # the task config turns the task into an ordered itinerary. Absent, this is
    # T1 and behaves exactly as it always has.
    sequence = tuple(task.get("target_sequence", ()) or ())
    return ObjectNavConfig(
        target_object_type=task["target_object_type"],
        target_sequence=sequence,
        max_steps=ppo_cfg.max_episode_steps,
    )


def train(ppo_cfg: PPOConfig) -> Path:
    """Run PPO training on variant A; returns the final model path."""
    from stable_baselines3 import PPO
    from stable_baselines3.common.callbacks import CheckpointCallback
    from stable_baselines3.common.monitor import Monitor

    ensure_dirs()
    name = getattr(ppo_cfg, "baseline_name", "ppo")
    ckpt = ckpt_dir(name)
    log_dir = LOGS_DIR / name
    ckpt.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    env_cfg = build_env_config(ppo_cfg)
    env = make_objectnav_env(HOUSE_A_PATH, env_cfg, name="variant_a")
    if getattr(ppo_cfg, "augment", False):
        from envs.augmentation import PhotometricJitter

        env = PhotometricJitter(
            env,
            brightness=ppo_cfg.aug_brightness,
            contrast=ppo_cfg.aug_contrast,
            saturation=ppo_cfg.aug_saturation,
            hue_degrees=ppo_cfg.aug_hue_degrees,
            resample=ppo_cfg.aug_resample,
            seed=ppo_cfg.seed,
        )
        logger.info(
            "train-time photometric jitter ACTIVE (b=%.2f c=%.2f s=%.2f "
            "hue=+/-%.0fdeg, resample per %s) — eval stays un-augmented",
            ppo_cfg.aug_brightness, ppo_cfg.aug_contrast,
            ppo_cfg.aug_saturation, ppo_cfg.aug_hue_degrees,
            ppo_cfg.aug_resample,
        )
    env = Monitor(
        env,
        filename=str(log_dir / "train_variant_a"),
        info_keywords=("success", "spl"),
    )
    # Seed the start-pose RNG once; training episodes then vary reproducibly.
    env.reset(seed=ppo_cfg.seed)

    device = get_device()
    logger.info(
        "training %s on device=%s for %d steps (target=%s)",
        name, device, ppo_cfg.total_timesteps, env_cfg.target_object_type,
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
        save_path=str(ckpt),
        name_prefix="ppo",
    )

    start = time.time()
    model.learn(total_timesteps=ppo_cfg.total_timesteps, callback=checkpoint_cb)
    elapsed = time.time() - start
    logger.info("training finished in %.1f min", elapsed / 60.0)

    final = final_model_path(name)
    model.save(str(final))
    env.close()
    logger.info("saved final model to %s.zip", final)
    return final


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
