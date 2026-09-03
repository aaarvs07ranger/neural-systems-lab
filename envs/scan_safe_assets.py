"""Find which object substitutions preserve the navigation mesh (L2 whitelist).

Two assets of the same object type -- Fridge_19 and Fridge_3 -- are both
fridges, but they have different collision footprints. Substituting one for the
other can free or block floor cells, which changes the set of positions the
agent can stand in. Start poses then stop being paired between house A and
house B, and every number the benchmark produces quietly stops meaning
anything, with no error raised anywhere.

Only the simulator knows which substitutions are safe, so this script asks it:
for each object, swap in one candidate asset at a time, reload the scene, and
compare the reachable-position set against the untouched house. Survivors go
into a per-pair whitelist that ``_apply_l2`` then draws from.

Cost is one scene reload per candidate (~1-3s). One controller is reused for
every test, so this is minutes per house, run once.

Usage:
    python envs/scan_safe_assets.py                    # every pair
    python envs/scan_safe_assets.py --pair pair0 --max-candidates 6

Writes data/pairs/<pair>/safe_assets.json.
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import DATA_DIR, GenerationConfig, ensure_dirs, pair_dir, pair_house_path  # noqa: E402
from envs.generate_variants import (  # noqa: E402
    _iter_objects, _object_type, harvest_asset_pool,
)
from envs.procthor_env import ObjectNavConfig, _resolve_thor_platform  # noqa: E402

logger = logging.getLogger("scan_safe_assets")

POSITION_DECIMALS = 3


def _reachable(controller, house: Dict[str, Any]) -> Set:
    """Reload a house and return its reachable floor cells."""
    controller.reset(scene=house)
    event = controller.step(action="GetReachablePositions")
    return {(round(p["x"], POSITION_DECIMALS), round(p["z"], POSITION_DECIMALS))
            for p in event.metadata["actionReturn"]}


def _make_controller(cfg: ObjectNavConfig, house: Dict[str, Any]):
    from ai2thor.controller import Controller

    platform = _resolve_thor_platform()
    kwargs: Dict[str, Any] = {}
    if platform is not None:
        kwargs["platform"] = platform
        kwargs["gpu_device"] = 0
    return Controller(
        scene=house, **kwargs, agentMode="default", gridSize=cfg.grid_size,
        snapToGrid=False, rotateStepDegrees=cfg.rotate_step_degrees,
        visibilityDistance=cfg.visibility_distance, width=cfg.width,
        height=cfg.height, fieldOfView=cfg.field_of_view,
        renderDepthImage=False, renderInstanceSegmentation=False,
    )


def scan_pair(
    pair_id: str, asset_pool: Dict[str, List[str]], max_candidates: int,
    target_candidates: int = 40,
) -> Dict[str, Any]:
    """Test every candidate substitution in one house; return the whitelist."""
    task = json.loads((pair_dir(pair_id) / "task_config.json").read_text())
    house_a = json.loads(pair_house_path(pair_id, "A").read_text())
    cfg = ObjectNavConfig(target_object_type=task["target_object_type"])

    controller = _make_controller(cfg, house_a)
    try:
        reference = _reachable(controller, house_a)
        logger.info("[%s] reference: %d reachable cells", pair_id, len(reference))

        objects: Dict[str, Any] = {}
        n_tested = n_safe = 0
        for obj in _iter_objects(house_a.get("objects", [])):
            obj_id = str(obj.get("id", ""))
            obj_type = _object_type(obj)
            current = obj.get("assetId")
            if not obj_id or not obj_type or not isinstance(current, str):
                continue
            # The target object gets an exhaustive search. Swapping it is the
            # whole point of L2 -- it asks whether the policy learned "this
            # fridge's appearance" or "fridge-ness" -- and large floor-standing
            # furniture is exactly what tends to change footprint, so a small
            # sample would give up on it too easily.
            limit = (target_candidates if obj_type == cfg.target_object_type
                     else max_candidates)
            candidates = [a for a in asset_pool.get(obj_type, [])
                          if a != current][:limit]
            if not candidates:
                continue

            safe: List[str] = []
            unsafe: List[str] = []
            for candidate in candidates:
                probe = copy.deepcopy(house_a)
                for probe_obj in _iter_objects(probe.get("objects", [])):
                    if str(probe_obj.get("id", "")) == obj_id:
                        probe_obj["assetId"] = candidate
                        break
                n_tested += 1
                try:
                    got = _reachable(controller, probe)
                except Exception as exc:            # a bad asset can crash the scene
                    logger.warning("[%s] %s -> %s raised: %s",
                                   pair_id, obj_id, candidate, exc)
                    unsafe.append(candidate)
                    continue
                (safe if got == reference else unsafe).append(candidate)
            n_safe += len(safe)
            objects[obj_id] = {"type": obj_type, "original": current,
                               "safe": safe, "unsafe": unsafe}
            logger.info("[%s] %-28s %-22s %d/%d safe", pair_id, obj_id, obj_type,
                        len(safe), len(candidates))

        is_target = [o for o, v in objects.items()
                     if v["type"] == cfg.target_object_type]
        target_swappable = any(objects[o]["safe"] for o in is_target)
        return {
            "pair_id": pair_id,
            "target_object_type": cfg.target_object_type,
            "reference_reachable": len(reference),
            "n_candidates_tested": n_tested,
            "n_safe": n_safe,
            "target_swappable": target_swappable,
            "objects": objects,
        }
    finally:
        controller.stop()


def harvest_pickupable_types(controller, dataset, n_houses: int = 40) -> Set[str]:
    """Ask the simulator which object types can be picked up.

    L3 clutter has to be small enough to rest on a counter. "Appears on a
    surface in the dataset" was not a tight enough filter: it admitted a
    Television and a Desktop, which overhang the counter, fall to the floor and
    block navigation. THOR already knows the answer -- pickupable objects are
    exactly the hand-sized ones -- so read it off the metadata rather than
    hand-listing sizes.
    """
    pickupable: Set[str] = set()
    for idx in range(min(n_houses, len(dataset))):
        try:
            controller.reset(scene=dataset[idx])
        except Exception:
            continue
        for obj in controller.last_event.metadata["objects"]:
            if obj.get("pickupable"):
                pickupable.add(obj["objectType"])
    logger.info("pickupable object types (valid L3 clutter): %d", len(pickupable))
    return pickupable


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair", type=str, default=None)
    parser.add_argument("--max-candidates", type=int, default=6,
                        help="candidate assets to test per object")
    parser.add_argument("--pickupable-houses", type=int, default=40,
                        help="dataset houses to scan for the pickupable-type list")
    parser.add_argument("--target-candidates", type=int, default=40,
                        help="candidates to test for the TARGET type (searched "
                             "exhaustively: keeping the target swappable is what "
                             "makes L2 a semantics-vs-appearance test)")
    args = parser.parse_args()
    ensure_dirs()

    index_path = DATA_DIR / "pairs_index.json"
    pair_ids = ([args.pair] if args.pair
                else [p["pair_id"] for p in json.loads(index_path.read_text())["pairs"]])

    import prior  # deferred: the asset pool comes from the dataset

    gen_cfg = GenerationConfig()
    dataset = prior.load_dataset(gen_cfg.dataset,
                                 revision=gen_cfg.dataset_revision)[gen_cfg.split]
    asset_pool = harvest_asset_pool(dataset, gen_cfg.scan_limit)

    # One shared list for every pair; written before the per-pair scans so a
    # later crash still leaves it usable.
    first_house = json.loads(pair_house_path(pair_ids[0], "A").read_text())
    probe_cfg = ObjectNavConfig()
    probe = _make_controller(probe_cfg, first_house)
    try:
        pickupable = harvest_pickupable_types(probe, dataset, args.pickupable_houses)
    finally:
        probe.stop()
    (DATA_DIR / "pickupable_types.json").write_text(
        json.dumps({"n_houses_scanned": args.pickupable_houses,
                    "types": sorted(pickupable)}, indent=2))
    logger.info("wrote %s", DATA_DIR / "pickupable_types.json")

    for pair_id in pair_ids:
        result = scan_pair(pair_id, asset_pool, args.max_candidates,
                           target_candidates=args.target_candidates)
        out = pair_dir(pair_id) / "safe_assets.json"
        out.write_text(json.dumps(result, indent=2))
        logger.info("[%s] %d/%d substitutions safe; target swappable: %s -> %s",
                    pair_id, result["n_safe"], result["n_candidates_tested"],
                    result["target_swappable"], out)


if __name__ == "__main__":
    main()
