#!/usr/bin/env python
"""End-to-end pipeline: environment generation -> training -> zero-shot eval.

Stages (run all, or pick one with --stage):
    generate   build house_a/house_b visual variants (no Unity required)
    train      train the selected baseline on variant A
    eval       zero-shot transfer evaluation A vs B (frozen weights)

Baselines:
    ppo        stable-baselines3 PPO (implemented)
    dreamerv3  vendored NM512 DreamerV3 world model (implemented)
    tdmpc2     world-model baseline (adapter stub — next milestone)

Examples:
    python main.py --smoke                 # fast end-to-end pipeline check
    python main.py                         # full PPO transfer experiment
    python main.py --baseline dreamerv3    # full DreamerV3 transfer experiment
    python main.py --stage eval            # re-run eval on the saved model
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
import time
from pathlib import Path

# Must precede any torch import (SB3 uses ops without Metal kernels yet).
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import (  # noqa: E402
    HOUSE_A_PATH,
    HOUSE_B_PATH,
    LOGS_DIR,
    DreamerV3Config,
    PPOConfig,
    SmokeDreamerV3Config,
    SmokePPOConfig,
    ensure_dirs,
)

logger = logging.getLogger("main")

IMPLEMENTED_BASELINES = ("ppo", "dreamerv3")
PLANNED_BASELINES = ("tdmpc2",)

# (baseline, smoke) -> config dataclass
CONFIG_CLASSES = {
    ("ppo", False): PPOConfig,
    ("ppo", True): SmokePPOConfig,
    ("dreamerv3", False): DreamerV3Config,
    ("dreamerv3", True): SmokeDreamerV3Config,
}


def stage_generate(force: bool) -> None:
    """Create the paired visual variants unless they already exist."""
    if HOUSE_A_PATH.exists() and HOUSE_B_PATH.exists() and not force:
        logger.info("house variants already exist — skipping generation "
                    "(use --force-generate to rebuild)")
        return
    from envs.generate_variants import generate

    generate()


def stage_train(baseline: str, cfg) -> None:
    if baseline == "ppo":
        from scripts.train_ppo import train

        train(cfg)
    elif baseline == "dreamerv3":
        from models.dreamer_v3.adapter import DreamerV3Adapter

        DreamerV3Adapter(cfg).train(
            HOUSE_A_PATH, total_timesteps=cfg.total_timesteps, seed=cfg.seed
        )
    else:
        raise NotImplementedError(
            f"baseline '{baseline}' is the next milestone; implemented: "
            f"{IMPLEMENTED_BASELINES}"
        )


def stage_eval(baseline: str, cfg) -> None:
    if baseline in IMPLEMENTED_BASELINES:
        from scripts.evaluate_transfer import run_transfer_eval

        result = run_transfer_eval(cfg, baseline=baseline)
        logger.info(
            "SUCCESS-RATE DROP A->B: %.3f absolute — see results/tables + plots",
            result["success_drop_abs"],
        )
    else:
        raise NotImplementedError(f"baseline '{baseline}' not implemented yet")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", choices=("all", "generate", "train", "eval"),
                        default="all")
    parser.add_argument("--baseline", choices=IMPLEMENTED_BASELINES + PLANNED_BASELINES,
                        default="ppo")
    parser.add_argument("--total-steps", type=int, default=None,
                        help="override training timesteps")
    parser.add_argument("--episodes", type=int, default=None,
                        help="override eval episodes per variant")
    parser.add_argument("--seed", type=int, default=None,
                        help="override the training seed (slurm seed sweeps; "
                             "pair with NSL_RESULTS_DIR for isolated outputs)")
    parser.add_argument("--train-ratio", type=int, default=None,
                        help="override DreamerV3 train_ratio (e.g. 512 on "
                             "cluster GPUs; ignored by baselines without it)")
    parser.add_argument("--smoke", action="store_true",
                        help="tiny end-to-end run to verify pipeline mechanics")
    parser.add_argument("--force-generate", action="store_true",
                        help="regenerate house variants even if present")
    args = parser.parse_args()

    ensure_dirs()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOGS_DIR / "pipeline.log"),
        ],
    )

    cfg = CONFIG_CLASSES[(args.baseline, args.smoke)]()
    overrides = {}
    if args.total_steps is not None:
        overrides["total_timesteps"] = args.total_steps
    if args.episodes is not None:
        overrides["eval_episodes"] = args.episodes
    if args.seed is not None:
        overrides["seed"] = args.seed
    if args.train_ratio is not None:
        if not hasattr(cfg, "train_ratio"):
            parser.error(f"--train-ratio does not apply to baseline '{args.baseline}'")
        overrides["train_ratio"] = args.train_ratio
    if overrides:
        cfg = type(cfg)(**{**cfg.__dict__, **overrides})

    start = time.time()
    logger.info("pipeline start: stage=%s baseline=%s smoke=%s",
                args.stage, args.baseline, args.smoke)
    if args.stage in ("all", "generate"):
        stage_generate(force=args.force_generate)
    if args.stage in ("all", "train"):
        stage_train(args.baseline, cfg)
    if args.stage in ("all", "eval"):
        stage_eval(args.baseline, cfg)
    logger.info("pipeline done in %.1f min", (time.time() - start) / 60.0)


if __name__ == "__main__":
    main()
