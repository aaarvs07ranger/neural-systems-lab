"""Drop the L3 distractors that block floor, so the navigation mesh survives.

L3 adds clutter to surfaces. The clutter is meant to be *irrelevant*: something
extra for the agent to look at, changing nothing about where it can walk. But a
planned position on a countertop is only a request -- Unity settles physics when
the scene loads, and an object that overhangs an edge, interpenetrates a
neighbour, or is simply too big for its perch ends up on the floor, where it
blocks cells the agent could stand in. The reachable-position sets of A and B
then differ, start poses stop being paired, and every number the benchmark
produces quietly stops meaning anything.

Filtering by object type is not enough, and neither is filtering by size: the
same mug is fine on a wide counter and falls off a crowded one. Placement is
what decides, so only the simulator can answer, and this script asks it:

    load the house -> compare floor cells against house A
    -> if they differ, remove the single distractor that frees the most
       blocked cells, reload, and repeat until the floor matches

Objects are dropped one at a time rather than all at once so L3 keeps as much
clutter as it can while still being physically identical to A. Each pair's
summary records what was dropped and why, because the surviving distractor
count is a property of the house (how much free surface it has) and varies
across pairs -- that heterogeneity is real and gets disclosed, not hidden.

Cost is one scene reload per attempt (~1-3s), a handful per pair.

Usage:
    python envs/prune_l3.py                 # every pair
    python envs/prune_l3.py --pair pair0

Rewrites data/pairs/<pair>/b_L3.json in place and writes l3_prune.json.
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import GenerationConfig, PPOConfig, pair_dir, pair_house_path  # noqa: E402
from envs.generate_variants import DISTRACTOR_TAG  # noqa: E402
from envs.procthor_env import ObjectNavConfig  # noqa: E402
from envs.scan_safe_assets import _make_controller, _reachable  # noqa: E402

logger = logging.getLogger("prune_l3")

House = Dict[str, Any]


def _distractor_ids(house: House) -> List[str]:
    """Every id L3 added, at any nesting depth, in document order."""
    found: List[str] = []

    def walk(objects: List[Dict[str, Any]]) -> None:
        for obj in objects:
            if DISTRACTOR_TAG in str(obj.get("id", "")):
                found.append(str(obj["id"]))
            walk(obj.get("children", []) or [])

    walk(house.get("objects", []))
    return found


def _without(house: House, drop: Set[str]) -> House:
    """Copy of the house with the named distractors removed."""
    out = copy.deepcopy(house)

    def prune(objects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        kept = []
        for obj in objects:
            if str(obj.get("id", "")) in drop:
                continue
            if obj.get("children"):
                obj["children"] = prune(obj["children"])
            kept.append(obj)
        return kept

    out["objects"] = prune(out.get("objects", []))
    return out


def prune_pair(
    pair_id: str, env_cfg: ObjectNavConfig, controller_holder: Dict[str, Any],
) -> Dict[str, Any]:
    """Remove blocking distractors from one pair's L3 house. Rewrites it."""
    house_a = json.loads(pair_house_path(pair_id, "A").read_text())
    l3_path = pair_house_path(pair_id, "L3")
    house_l3 = json.loads(l3_path.read_text())

    if controller_holder.get("controller") is None:
        controller_holder["controller"] = _make_controller(env_cfg, house_a)
    controller = controller_holder["controller"]

    reference = _reachable(controller, house_a)
    candidates = _distractor_ids(house_l3)
    dropped: List[Dict[str, Any]] = []
    keep = set(candidates)

    for _ in range(len(candidates) + 1):
        current = _reachable(controller, _without(house_l3, set(candidates) - keep))
        missing = reference - current
        extra = current - reference
        if not missing and not extra:
            break
        if not keep:
            # Nothing left to remove and the floor still differs: the fault is
            # not the clutter, so stop rather than silently shipping a bad house.
            logger.error("[%s] floor still differs with zero distractors "
                         "(%d missing, %d extra) -- L2 or the house itself is "
                         "at fault, not L3", pair_id, len(missing), len(extra))
            break
        # Remove whichever single distractor frees the most blocked cells.
        best_id, best_freed, best_missing = None, -1, None
        for obj_id in sorted(keep):
            trial = _reachable(
                controller, _without(house_l3, (set(candidates) - keep) | {obj_id})
            )
            freed = len(missing - (reference - trial))
            if freed > best_freed:
                best_id, best_freed, best_missing = obj_id, freed, len(missing)
        if best_freed <= 0:
            # No single removal helps: the blockage is joint, so drop them all.
            logger.warning("[%s] no single distractor explains the %d blocked "
                           "cells -- dropping all %d remaining",
                           pair_id, len(missing), len(keep))
            for obj_id in sorted(keep):
                dropped.append({"id": obj_id, "cells_freed": 0,
                                "reason": "joint blockage"})
            keep = set()
            continue
        dropped.append({"id": best_id, "cells_freed": best_freed,
                        "cells_blocked_before": best_missing,
                        "reason": "blocked floor the agent can stand on"})
        keep.discard(best_id)
        logger.info("[%s] dropping %s (frees %d of %d blocked cells)",
                    pair_id, best_id, best_freed, best_missing)

    pruned = _without(house_l3, set(candidates) - keep)
    # Houses are written compact, matching envs/generate_variants.py.
    with l3_path.open("w") as f:
        json.dump(pruned, f)
    report = {
        "pair": pair_id,
        "n_placed": len(candidates),
        "n_kept": len(keep),
        "kept": sorted(keep),
        "dropped": dropped,
        "n_reachable_reference": len(reference),
    }
    (pair_dir(pair_id) / "l3_prune.json").write_text(json.dumps(report, indent=2))
    logger.info("[%s] L3 distractors: %d placed -> %d kept", pair_id,
                len(candidates), len(keep))
    return report


def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair", default=None,
                        help="only prune this pair (default: every pair)")
    args = parser.parse_args()

    gen_cfg = GenerationConfig()
    pairs = ([args.pair] if args.pair
             else [f"pair{i}" for i in range(gen_cfg.n_pairs)])

    holder: Dict[str, Any] = {"controller": None}
    reports = []
    try:
        for pair_id in pairs:
            if not pair_house_path(pair_id, "L3").exists():
                logger.warning("[%s] no b_L3.json -- skipping", pair_id)
                continue
            task = json.loads((pair_dir(pair_id) / "task_config.json").read_text())
            env_cfg = ObjectNavConfig(
                target_object_type=task["target_object_type"],
                max_steps=PPOConfig().max_episode_steps,
            )
            reports.append(prune_pair(pair_id, env_cfg, holder))
    finally:
        if holder.get("controller") is not None:
            holder["controller"].stop()

    print("\nL3 distractors kept per pair:")
    for r in reports:
        print(f"  {r['pair']}: {r['n_kept']}/{r['n_placed']}")


if __name__ == "__main__":
    main()
