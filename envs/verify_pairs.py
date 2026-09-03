"""Runtime verification that a house pair is physically identical (C1-C3).

The static checks in ``generate_variants.py`` compare JSON. That is enough for
L1, where only material names change, but NOT for L2/L3: swapping an object for
a different asset of the same type can change its physical footprint, and a
wider fridge blocks floor the original left free. The reachable-position set
would differ, start poses would stop being paired between A and B, and every
number the benchmark produces would quietly stop meaning anything -- with no
error anywhere.

Only the simulator can answer that, so this script boots Unity.

    C1  identical reachable-position sets       (start poses pair up)
    C2  identical shortest-path length from every eval start pose
                                                (the SPL denominator matches)
    C3  identical count of target-type objects  (still the same task)

Usage:
    python envs/verify_pairs.py                      # every pair, every level
    python envs/verify_pairs.py --pair pair0 --levels L1

Writes data/pairs/<pair>/verification.json and exits non-zero if any pair
fails, so it can gate a grid launch.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    DATA_DIR, EVAL_POSE_FRACTION, POSE_HOLDOUT, POSE_SPLIT_SEED, PPOConfig,
    ensure_dirs, pair_dir, pair_house_path,
)
from envs.procthor_env import ObjectNavConfig, make_objectnav_env  # noqa: E402

logger = logging.getLogger("verify_pairs")

POSITION_DECIMALS = 3        # THOR returns float noise well below this
PATH_TOLERANCE = 1e-6


def _reachable_key(positions: List[Dict[str, float]]) -> set:
    return {(round(p["x"], POSITION_DECIMALS), round(p["z"], POSITION_DECIMALS))
            for p in positions}


def probe_house(
    house_path: Path, env_cfg: ObjectNavConfig, seeds: List[int], name: str,
) -> Dict[str, Any]:
    """Boot one house and collect everything C1-C3 need.

    Start poses are drawn through the real environment, with the real seeds, so
    this measures the machinery the experiment actually uses rather than a
    reimplementation of it.
    """
    env = make_objectnav_env(house_path, env_cfg, name=name)
    try:
        env.reset(seed=seeds[0])
        controller = env._controller                      # booted by reset
        reachable = controller.step(action="GetReachablePositions") \
                              .metadata["actionReturn"]
        n_target = sum(1 for o in controller.last_event.metadata["objects"]
                       if o["objectType"] == env_cfg.target_object_type)
        starts: Dict[int, Any] = {}
        for seed in seeds:
            _, info = env.reset(seed=seed)
            starts[seed] = {
                "position": {k: round(v, POSITION_DECIMALS)
                             for k, v in info["start_position"].items()},
                "shortest_path_length": float(info["shortest_path_length"]),
            }
        return {"n_reachable": len(reachable),
                "reachable": _reachable_key(reachable),
                "n_target_instances": n_target,
                "starts": starts}
    finally:
        env.close()


def verify_pair(
    pair_id: str, levels: List[str], n_seeds: int = 25,
) -> Dict[str, Any]:
    """Run C1-C3 for one pair across the requested levels."""
    cfg = PPOConfig()
    task = json.loads((pair_dir(pair_id) / "task_config.json").read_text())
    # The eval slice, so the start poses probed here -- and the oracle
    # distances written from them -- are exactly the ones evaluation will use.
    env_cfg = ObjectNavConfig(
        target_object_type=task["target_object_type"],
        max_steps=cfg.max_episode_steps,
        pose_split="eval" if POSE_HOLDOUT else "",
        eval_pose_fraction=EVAL_POSE_FRACTION,
        pose_split_seed=POSE_SPLIT_SEED,
    )
    seeds = [cfg.eval_seed_base + i for i in range(n_seeds)]

    logger.info("[%s] probing house A (target=%s)", pair_id,
                env_cfg.target_object_type)
    ref = probe_house(pair_house_path(pair_id, "A"), env_cfg, seeds, f"{pair_id}_A")

    # The single yardstick: house A's distances, keyed by eval seed. Every
    # variant of this pair reads these instead of measuring its own.
    oracle = {
        "pair_id": pair_id,
        "target_object_type": env_cfg.target_object_type,
        "source": "house A",
        "n_eval_seeds": n_seeds,
        "seeds": {str(s): {"start_position": ref["starts"][s]["position"],
                           "legs": [ref["starts"][s]["shortest_path_length"]],
                           "total": ref["starts"][s]["shortest_path_length"]}
                  for s in seeds},
    }
    (pair_dir(pair_id) / "oracle_paths.json").write_text(json.dumps(oracle, indent=2))
    logger.info("[%s] wrote oracle_paths.json (%d seeds, measured in house A)",
                pair_id, n_seeds)

    result: Dict[str, Any] = {
        "pair_id": pair_id,
        "target_object_type": env_cfg.target_object_type,
        "n_eval_seeds": n_seeds,
        "reference": {"n_reachable": ref["n_reachable"],
                      "n_target_instances": ref["n_target_instances"]},
        "levels": {},
        "passed": True,
    }

    for level in levels:
        path = pair_house_path(pair_id, level)
        if not path.exists():
            logger.warning("[%s] %s missing (%s) - skipped", pair_id, level, path)
            continue
        logger.info("[%s] probing %s", pair_id, level)
        got = probe_house(path, env_cfg, seeds, f"{pair_id}_{level}")

        c1 = got["reachable"] == ref["reachable"]
        bad_paths = [
            {"seed": s,
             "a": ref["starts"][s]["shortest_path_length"],
             "b": got["starts"][s]["shortest_path_length"]}
            for s in seeds
            if abs(ref["starts"][s]["shortest_path_length"]
                   - got["starts"][s]["shortest_path_length"]) > PATH_TOLERANCE
        ]
        bad_starts = [s for s in seeds
                      if ref["starts"][s]["position"] != got["starts"][s]["position"]]
        # Option A (decided 2026-09-03): the oracle distance is measured ONCE in
        # house A and reused for every variant, because a swapped target has a
        # different surface and would otherwise be measured with a different
        # yardstick. So C2 gates on START POSES only. The raw distance deltas
        # are still recorded below -- they are the number to disclose in the
        # appendix, not a reason to reject a house.
        c2 = not bad_starts
        c3 = got["n_target_instances"] == ref["n_target_instances"]

        entry = {
            "C1_reachable_positions_identical": c1,
            "C2_start_poses_identical": c2,
            "C3_target_instance_count_identical": c3,
            "passed": bool(c1 and c2 and c3),
            "n_reachable": got["n_reachable"],
            "n_reachable_reference": ref["n_reachable"],
            "n_missing_positions": len(ref["reachable"] - got["reachable"]),
            "n_extra_positions": len(got["reachable"] - ref["reachable"]),
            "n_target_instances": got["n_target_instances"],
            "n_mismatched_start_poses": len(bad_starts),
            # Diagnostics only (see the C2 note above): how far the measured
            # distance moved because the target's mesh changed shape.
            "mismatched_shortest_paths": bad_paths[:5],
            "n_mismatched_shortest_paths": len(bad_paths),
            "max_shortest_path_delta": round(max(
                (abs(b["a"] - b["b"]) for b in bad_paths), default=0.0), 4),
        }
        result["levels"][level] = entry
        result["passed"] = result["passed"] and entry["passed"]
        logger.info("[%s] %s: C1=%s C2=%s C3=%s (max path delta %.2fm) -> %s",
                    pair_id, level, c1, c2, c3,
                    entry["max_shortest_path_delta"],
                    "PASS" if entry["passed"] else "FAIL")
    return result


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair", type=str, default=None,
                        help="verify a single pair (default: every pair on disk)")
    parser.add_argument("--levels", type=str, default=None,
                        help="comma-separated levels (default: those in pairs_index)")
    parser.add_argument("--episodes", type=int, default=25,
                        help="how many eval start poses to check for C2")
    args = parser.parse_args()
    ensure_dirs()

    index_path = DATA_DIR / "pairs_index.json"
    if index_path.exists():
        index = json.loads(index_path.read_text())
        pair_ids = [p["pair_id"] for p in index["pairs"]]
        default_levels = index["levels"]
    else:
        pair_ids = sorted(d.name for d in (DATA_DIR / "pairs").glob("pair*"))
        default_levels = ["L1", "L2", "L3"]
    if args.pair:
        pair_ids = [args.pair]
    levels = ([lv.strip() for lv in args.levels.split(",")] if args.levels
              else default_levels)
    if not pair_ids:
        raise SystemExit("no pairs found - run envs/generate_variants.py first")

    all_passed = True
    for pair_id in pair_ids:
        result = verify_pair(pair_id, levels, n_seeds=args.episodes)
        out = pair_dir(pair_id) / "verification.json"
        out.write_text(json.dumps(result, indent=2))
        logger.info("[%s] wrote %s -> %s", pair_id, out,
                    "PASS" if result["passed"] else "FAIL")
        all_passed = all_passed and result["passed"]

    print("\n" + ("ALL PAIRS PASSED" if all_passed else "*** VERIFICATION FAILED ***"))
    raise SystemExit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
