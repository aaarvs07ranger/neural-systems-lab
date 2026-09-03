"""One place that turns a baseline config + a house pair into an env config.

Before this module the assembly was copy-pasted into three files
(``scripts/train_ppo.py`` and both world-model adapters) and had already
drifted: the adapters never picked up ``target_sequence`` (T2) or
``oracle_path_table``, so DreamerV3 and TD-MPC2 would have silently run a
different task from PPO on the same pair. Every caller now goes through
``build_env_config``, so the protocol is identical across baselines by
construction rather than by vigilance.
"""
from __future__ import annotations

import json
import logging
from typing import Any, Optional

from config import (
    EVAL_POSE_FRACTION, POSE_HOLDOUT, POSE_SPLIT_SEED, PairPaths,
    resolve_pair,
)
from envs.procthor_env import ObjectNavConfig

logger = logging.getLogger("task_setup")


def build_env_config(
    cfg: Any, pair: Optional[PairPaths] = None, split: str = "",
) -> ObjectNavConfig:
    """Assemble the task config written by ``envs/generate_variants.py``.

    ``cfg`` is any baseline config dataclass; only ``max_episode_steps`` is
    read, so the episode budget stays identical across baselines.

    ``split`` is "train" or "eval" and only takes effect when the protocol-v2
    pose holdout is enabled (see ``config.POSE_HOLDOUT``); otherwise both
    slices are the whole floor, exactly as before.
    """
    pair = pair if pair is not None else resolve_pair()
    if not pair.task_config.exists():
        raise FileNotFoundError(
            f"{pair.task_config} not found — run `python envs/generate_variants.py` "
            "(or `python main.py --stage generate`) first."
        )
    task = json.loads(pair.task_config.read_text())

    # T2 (sequential ObjectNav) is opt-in per house: a "target_sequence" key in
    # the task config turns the task into an ordered itinerary. Absent, this is
    # T1 and behaves exactly as it always has -- T1 is the one-leg case of T2.
    sequence = tuple(task.get("target_sequence", ()) or ())

    # One oracle distance table per pair, measured in house A and shared by
    # every variant, so A and B are scored with the same yardstick. Absent
    # during training in A, where the env measures its own -- the same number
    # by construction.
    return ObjectNavConfig(
        target_object_type=task["target_object_type"],
        target_sequence=sequence,
        max_steps=cfg.max_episode_steps,
        oracle_path_table=str(pair.oracle_table) if pair.oracle_table else None,
        pose_split=split if POSE_HOLDOUT else "",
        eval_pose_fraction=EVAL_POSE_FRACTION,
        pose_split_seed=POSE_SPLIT_SEED,
    )
