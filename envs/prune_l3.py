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
from envs.generate_variants import DISTRACTOR_TAG, variant_path  # noqa: E402
from envs.procthor_env import ObjectNavConfig  # noqa: E402
from envs.scan_safe_assets import _make_controller, _reachable  # noqa: E402

logger = logging.getLogger("prune_l3")

# How many times a configuration must come back clean before it is accepted.
#
# Unity's physics settle is not bit-deterministic, so an object balanced near an
# edge stays put on some loads and falls on others. A single clean reading is
# therefore not evidence that a house IS clean -- only that it was clean once.
# Observed 2026-09-03: prune certified pair1 L3 with all 4 distractors kept, and
# the verification gate immediately after found a blocked floor cell in the same
# file. Certification reloads the scene this many times and takes the UNION of
# defects, so a flaky object is treated as a defect rather than a coin flip.
STABILITY_TRIALS = 3

# How far a distractor may move between two loads and still count as "in one
# place", in metres. Well under the 0.25 m navigation grid, so anything that
# could change which cell it occupies is caught.
SETTLE_TOLERANCE = 0.02

House = Dict[str, Any]


def _pinned_poses(pair_id: str) -> List[Dict[str, Any]]:
    """The eval start poses recorded in house A, if the table exists yet."""
    path = pair_dir(pair_id) / "oracle_paths.json"
    if not path.exists():
        logger.warning("[%s] no oracle_paths.json -- pruning on the floor check "
                       "alone. Run `verify_pairs.py --oracle-only` first to also "
                       "check that every eval start pose stays reachable.",
                       pair_id)
        return []
    table = json.loads(path.read_text()).get("seeds", {})
    return [{"seed": s, "position": e["start_position"],
             "rotation": e.get("start_rotation", 0.0)}
            for s, e in sorted(table.items())
            if "start_position" in e]


def _settled_positions(controller, house: House) -> Dict[str, Dict[str, float]]:
    """Where each distractor actually comes to rest after physics settles."""
    controller.reset(scene=house)
    out = {}
    for obj in controller.last_event.metadata["objects"]:
        if DISTRACTOR_TAG in str(obj.get("objectId", "")) \
                or DISTRACTOR_TAG in str(obj.get("name", "")):
            out[str(obj.get("objectId"))] = dict(obj["position"])
    return out


def _unstable_distractors(controller, house: House, trials: int) -> Dict[str, float]:
    """Distractors that do not land in the same place on every load.

    A benchmark object has to be in one place. An item balanced on an edge is
    not: it stays put on some loads and falls on others, and whether it blocks a
    floor cell then becomes a coin flip that no amount of re-checking can
    settle. Rather than sampling that coin more times, drop the object.

    Returns {objectId: largest distance it moved between loads, in metres}.
    """
    readings = [_settled_positions(controller, house) for _ in range(max(2, trials))]
    ids = set().union(*[set(r) for r in readings]) if readings else set()
    drift = {}
    for oid in ids:
        pts = [r[oid] for r in readings if oid in r]
        if len(pts) != len(readings):
            drift[oid] = float("inf")        # present on some loads, not others
            continue
        worst = max(
            ((a["x"] - b["x"]) ** 2 + (a["y"] - b["y"]) ** 2 + (a["z"] - b["z"]) ** 2) ** 0.5
            for a in pts for b in pts
        )
        if worst > SETTLE_TOLERANCE:
            drift[oid] = worst
    return drift


def _blocked_poses(controller, poses: List[Dict[str, Any]]) -> List[str]:
    """Which pinned start poses cannot be teleported into in the loaded house.

    A cell can appear in GetReachablePositions and still refuse a Teleport: the
    navmesh query and the agent's collision capsule do not agree once an object
    has settled on the floor. That gap is what broke pair1 L3 on 2026-09-03 --
    C1 passed, the teleport failed, the retry drew a different pose, and the two
    variants silently stopped being paired.
    """
    blocked = []
    for pose in poses:
        event = controller.step(
            action="Teleport", position=pose["position"],
            rotation={"x": 0.0, "y": pose["rotation"], "z": 0.0},
            horizon=0.0, standing=True,
        )
        if not event.metadata["lastActionSuccess"]:
            blocked.append(pose["seed"])
    return blocked


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
    poses = _pinned_poses(pair_id)
    candidates = _distractor_ids(house_l3)

    # Drop anything that does not land in the same place every time, BEFORE
    # asking what blocks what. An unstable object makes every later measurement
    # a coin flip, so removing it first is what makes the rest meaningful.
    # Compare load against load, never the house file against the simulator.
    # The file records where an object is PLACED and the simulator reports where
    # its centre ends up, and those differ by roughly half the object's height:
    # measured 2026-09-04, a DeskLamp read 0.27 m "displaced", a BaseballBat
    # 0.21, a Mug 0.05 -- ordered by size, all of them perfectly stationary. A
    # check against the file therefore condemns big objects for being big. It
    # emptied L3 in two pairs before it was caught. Load-to-load drift uses one
    # convention on both sides and cannot make that mistake.
    drift = _unstable_distractors(controller, house_l3, STABILITY_TRIALS)
    # THOR's runtime objectId is not always the house-JSON id verbatim, so match
    # on the unique distractor tag both share.
    dropped: List[Dict[str, Any]] = []
    unstable = set()
    for cand in sorted(candidates):
        hits = [v for k, v in drift.items() if cand in k or k in cand]
        if not hits:
            continue
        unstable.add(cand)
        worst = min(hits)
        dropped.append({"id": cand, "max_drift_m": None if worst == float("inf")
                        else round(worst, 4),
                        "reason": "does not settle in the same place on every load"})
        logger.info("[%s] dropping %s (moves up to %s m between loads)",
                    pair_id, cand, dropped[-1]["max_drift_m"])
    keep = set(candidates) - unstable

    def defects(drop: Set[str], trials: int = 1) -> Tuple[Set, Set, List[str]]:
        """Floor cells lost, floor cells gained, and pinned poses blocked.

        With ``trials > 1`` the scene is reloaded repeatedly and the UNION of
        every reading is returned: a defect that appears in any load is a defect,
        because the grid will load these houses hundreds of times.
        """
        missing: Set = set()
        extra: Set = set()
        blocked: List[str] = []
        for _ in range(max(1, trials)):
            current = _reachable(controller, _without(house_l3, drop))
            missing |= reference - current
            extra |= current - reference
            for seed in _blocked_poses(controller, poses):
                if seed not in blocked:
                    blocked.append(seed)
        return missing, extra, blocked

    for _ in range(len(candidates) + 1):
        # Certification is the expensive, repeated reading. Ranking candidates
        # below uses a single reading -- it only has to order them, and a wrong
        # order costs one extra iteration, not a bad house.
        missing, extra, blocked = defects(set(candidates) - keep,
                                          trials=STABILITY_TRIALS)
        if not missing and not extra and not blocked:
            logger.info("[%s] clean on %d consecutive loads with %d distractors",
                        pair_id, STABILITY_TRIALS, len(keep))
            break
        if not keep:
            # Nothing left to remove and it still differs: the fault is not the
            # clutter, so stop rather than silently shipping a bad house.
            logger.error("[%s] still defective with zero distractors "
                         "(%d cells missing, %d extra, %d start poses blocked) "
                         "-- L2 or the house itself is at fault, not L3",
                         pair_id, len(missing), len(extra), len(blocked))
            break
        # Remove whichever single distractor frees the most blocked cells.
        before = len(missing) + len(blocked)
        best_id, best_freed, best_before = None, -1, before
        for obj_id in sorted(keep):
            t_missing, _, t_blocked = defects(
                (set(candidates) - keep) | {obj_id}
            )
            # Count blocked poses alongside blocked cells: a distractor that
            # frees no floor but unblocks a start pose is exactly the one to go.
            freed = before - (len(t_missing) + len(t_blocked))
            if freed > best_freed:
                best_id, best_freed = obj_id, freed
        if best_freed <= 0:
            # No single removal helps: the blockage is joint, so drop them all.
            logger.warning("[%s] no single distractor explains the %d defects "
                           "-- dropping all %d remaining",
                           pair_id, before, len(keep))
            for obj_id in sorted(keep):
                dropped.append({"id": obj_id, "cells_freed": 0,
                                "reason": "joint blockage"})
            keep = set()
            continue
        dropped.append({"id": best_id, "defects_freed": best_freed,
                        "defects_before": best_before,
                        "reason": "blocked floor or a pinned eval start pose"})
        keep.discard(best_id)
        logger.info("[%s] dropping %s (fixes %d of %d defects: %d cells, "
                    "%d start poses)", pair_id, best_id, best_freed, before,
                    len(missing), len(blocked))

    pruned = _without(house_l3, set(candidates) - keep)
    # Houses are written compact, matching envs/generate_variants.py.
    with l3_path.open("w") as f:
        json.dump(pruned, f)
    # generate_variants.py holds the invariant "pair0 is mirrored byte-identically
    # to the legacy flat data/house_*.json paths". Pruning writes only into
    # data/pairs/, so without this the flat copy keeps the UNPRUNED house -- a
    # stale, unverified artifact sitting in the repo looking authoritative.
    # Observed 2026-09-03: data/house_b_L3.json kept 4 distractors while the
    # verified pair0/b_L3.json had 2.
    if pair_id == "pair0":
        legacy = variant_path("L3")
        if legacy.exists():
            with legacy.open("w") as f:
                json.dump(pruned, f)
            logger.info("[%s] mirrored the pruned house to the legacy path %s",
                        pair_id, legacy)
    report = {
        "pair": pair_id,
        "n_placed": len(candidates),
        "n_kept": len(keep),
        "kept": sorted(keep),
        "dropped": dropped,
        "n_unstable_dropped": len(unstable),
        "settle_tolerance_m": SETTLE_TOLERANCE,
        "n_reachable_reference": len(reference),
        "n_pinned_poses_checked": len(poses),
        "stability_trials": STABILITY_TRIALS,
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
