"""Generate two ProcTHOR houses: identical structure, different visuals.

Variant A is a house taken verbatim from the ProcTHOR-10k train split.
Variant B is a deep copy of A with ONLY appearance-level fields rewritten:

* every wall material            -> remapped to a different (valid) material
* every room floor material      -> remapped to a different (valid) material
* ceiling material               -> remapped
* every procedural light         -> re-tinted (warm hue shift) and dimmed
* skybox                         -> swapped when an alternative id is known

Replacement material names are harvested from *other* ProcTHOR-10k houses, so
every name is guaranteed to exist in the THOR asset database (no guessing).
Geometry, object placement, and therefore the task graph are untouched — the
script asserts structural identity before writing anything.

Outputs (all under data/):
    house_a.json           training visual variant
    house_b.json           zero-shot transfer visual variant
    task_config.json       target object type + provenance + seeds
    variants_summary.md    human-readable diff of every visual change

Usage:
    python envs/generate_variants.py [--house-index N] [--seed S]

Requires network on first run (prior downloads the procthor-10k dataset).
No Unity/AI2-THOR process is launched — this is pure JSON manipulation.
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

# Make `config` importable when run as a script from anywhere.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    DATA_DIR,
    HOUSE_A_PATH,
    HOUSE_B_PATH,
    TASK_CONFIG_PATH,
    GenerationConfig,
    ensure_dirs,
)

logger = logging.getLogger("generate_variants")

House = Dict[str, Any]


# ---------------------------------------------------------------------------
# Material helpers — ProcTHOR stores materials either as plain strings or as
# {"name": ...} dicts depending on dataset vintage; handle both.
# ---------------------------------------------------------------------------
def _material_name(value: Any) -> Optional[str]:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return value.get("name")
    return None


def _with_material_name(value: Any, new_name: str) -> Any:
    """Return `value` rewritten to reference `new_name`, preserving format."""
    if isinstance(value, dict):
        out = dict(value)
        out["name"] = new_name
        return out
    return new_name


# ---------------------------------------------------------------------------
# Dataset scanning
# ---------------------------------------------------------------------------
def _object_types(house: House) -> Set[str]:
    """Infer THOR object types present in a house from asset ids.

    ProcTHOR asset ids look like 'Television_10' / 'Sofa_207_2'; the prefix
    before the first underscore is the runtime objectType.
    """
    types: Set[str] = set()
    stack: List[Dict[str, Any]] = list(house.get("objects", []))
    while stack:
        obj = stack.pop()
        asset_id = obj.get("assetId", "")
        if "_" in asset_id:
            types.add(asset_id.split("_")[0])
        stack.extend(obj.get("children", []))
    return types


def pick_house(
    dataset: Sequence[House], gen_cfg: GenerationConfig, forced_index: Optional[int]
) -> Tuple[int, House, str]:
    """Pick a small house containing one of the preferred target types."""
    if forced_index is not None:
        house = dataset[forced_index]
        types = _object_types(house)
        for target in gen_cfg.preferred_targets:
            if target in types:
                return forced_index, house, target
        raise ValueError(
            f"House {forced_index} contains none of {gen_cfg.preferred_targets}; "
            f"available types: {sorted(types)}"
        )

    for idx in range(min(gen_cfg.scan_limit, len(dataset))):
        house = dataset[idx]
        if len(house.get("rooms", [])) > gen_cfg.max_rooms:
            continue
        types = _object_types(house)
        for target in gen_cfg.preferred_targets:
            if target in types:
                logger.info(
                    "selected house %d: %d room(s), target '%s'",
                    idx, len(house["rooms"]), target,
                )
                return idx, house, target
    raise RuntimeError(
        f"No house with <= {gen_cfg.max_rooms} rooms and a preferred target "
        f"found in the first {gen_cfg.scan_limit} houses."
    )


def harvest_pools(
    dataset: Sequence[House], scan_limit: int
) -> Dict[str, List[str]]:
    """Collect valid material/skybox names from real houses (sorted for determinism)."""
    walls: Set[str] = set()
    floors: Set[str] = set()
    ceilings: Set[str] = set()
    skyboxes: Set[str] = set()
    for idx in range(min(scan_limit, len(dataset))):
        house = dataset[idx]
        for wall in house.get("walls", []):
            name = _material_name(wall.get("material"))
            if name:
                walls.add(name)
        for room in house.get("rooms", []):
            name = _material_name(room.get("floorMaterial"))
            if name:
                floors.add(name)
        params = house.get("proceduralParameters", {})
        name = _material_name(params.get("ceilingMaterial"))
        if name:
            ceilings.add(name)
        skybox = params.get("skyboxId")
        if isinstance(skybox, str):
            skyboxes.add(skybox)
    pools = {
        "walls": sorted(walls),
        "floors": sorted(floors),
        "ceilings": sorted(ceilings),
        "skyboxes": sorted(skyboxes),
    }
    logger.info(
        "material pools: %d wall, %d floor, %d ceiling, %d skybox",
        len(pools["walls"]), len(pools["floors"]),
        len(pools["ceilings"]), len(pools["skyboxes"]),
    )
    return pools


# ---------------------------------------------------------------------------
# Variant construction
# ---------------------------------------------------------------------------
def _remap(
    originals: List[str], pool: List[str], rng: random.Random
) -> Dict[str, str]:
    """Map each original material to a DIFFERENT material drawn from `pool`."""
    candidates = [m for m in pool if m not in set(originals)]
    if not candidates:
        candidates = pool[:]  # degenerate pool; still shuffle below
    rng.shuffle(candidates)
    return {orig: candidates[i % len(candidates)] for i, orig in enumerate(originals)}


def build_variant_b(
    house_a: House, pools: Dict[str, List[str]], seed: int
) -> Tuple[House, Dict[str, Any]]:
    """Deep-copy house A and rewrite only appearance fields. Returns (B, report)."""
    rng = random.Random(seed)
    house_b = copy.deepcopy(house_a)
    report: Dict[str, Any] = {}

    # --- walls -------------------------------------------------------------
    wall_orig: List[str] = []
    for wall in house_b.get("walls", []):
        name = _material_name(wall.get("material"))
        if name and name not in wall_orig:
            wall_orig.append(name)
    wall_map = _remap(wall_orig, pools["walls"], rng)
    for wall in house_b.get("walls", []):
        name = _material_name(wall.get("material"))
        if name:
            wall["material"] = _with_material_name(wall["material"], wall_map[name])
    report["wall_materials"] = wall_map

    # --- floors ------------------------------------------------------------
    floor_orig: List[str] = []
    for room in house_b.get("rooms", []):
        name = _material_name(room.get("floorMaterial"))
        if name and name not in floor_orig:
            floor_orig.append(name)
    floor_map = _remap(floor_orig, pools["floors"], rng)
    for room in house_b.get("rooms", []):
        name = _material_name(room.get("floorMaterial"))
        if name:
            room["floorMaterial"] = _with_material_name(
                room["floorMaterial"], floor_map[name]
            )
    report["floor_materials"] = floor_map

    # --- ceiling / lights / skybox ------------------------------------------
    params = house_b.setdefault("proceduralParameters", {})
    ceiling_name = _material_name(params.get("ceilingMaterial"))
    if ceiling_name and pools["ceilings"]:
        ceiling_map = _remap([ceiling_name], pools["ceilings"], rng)
        params["ceilingMaterial"] = _with_material_name(
            params["ceilingMaterial"], ceiling_map[ceiling_name]
        )
        report["ceiling_material"] = ceiling_map

    # Warm-tinted, dimmer lighting: a strong global appearance shift that
    # leaves geometry and object semantics untouched.
    light_report: List[Dict[str, Any]] = []
    for light in params.get("lights", []):
        before = {"rgb": dict(light.get("rgb", {})), "intensity": light.get("intensity")}
        rgb = light.setdefault("rgb", {"r": 1.0, "g": 1.0, "b": 1.0})
        rgb["r"] = 1.0
        rgb["g"] = round(rng.uniform(0.62, 0.78), 3)
        rgb["b"] = round(rng.uniform(0.42, 0.58), 3)
        if "intensity" in light and isinstance(light["intensity"], (int, float)):
            light["intensity"] = round(light["intensity"] * rng.uniform(0.55, 0.75), 4)
        light_report.append(
            {"id": light.get("id"), "before": before,
             "after": {"rgb": dict(rgb), "intensity": light.get("intensity")}}
        )
    report["lights"] = light_report

    skybox = params.get("skyboxId")
    others = [s for s in pools["skyboxes"] if s != skybox]
    if isinstance(skybox, str) and others:
        params["skyboxId"] = rng.choice(others)
        report["skybox"] = {"before": skybox, "after": params["skyboxId"]}

    return house_b, report


# ---------------------------------------------------------------------------
# Structural-identity check (rigor for the paper: ONLY visuals may differ)
# ---------------------------------------------------------------------------
_VISUAL_WALL_KEYS = ("material",)
_VISUAL_ROOM_KEYS = ("floorMaterial",)
_VISUAL_PARAM_KEYS = ("ceilingMaterial", "lights", "skyboxId")


def _strip_visuals(house: House) -> House:
    stripped = copy.deepcopy(house)
    for wall in stripped.get("walls", []):
        for key in _VISUAL_WALL_KEYS:
            wall.pop(key, None)
    for room in stripped.get("rooms", []):
        for key in _VISUAL_ROOM_KEYS:
            room.pop(key, None)
    params = stripped.get("proceduralParameters", {})
    for key in _VISUAL_PARAM_KEYS:
        params.pop(key, None)
    return stripped


def assert_structurally_identical(house_a: House, house_b: House) -> None:
    if _strip_visuals(house_a) != _strip_visuals(house_b):
        raise AssertionError(
            "Variant B differs from A beyond the whitelisted visual fields!"
        )
    logger.info("structural identity verified: A == B modulo visual fields")


# ---------------------------------------------------------------------------
# Summary writer
# ---------------------------------------------------------------------------
def write_summary(
    path: Path, house_index: int, target: str, seed: int, report: Dict[str, Any]
) -> None:
    lines = [
        "# Visual Variant Summary",
        "",
        f"- Source: ProcTHOR-10k train split, house index **{house_index}**",
        f"- Target object type (ObjectNav): **{target}**",
        f"- Variant seed: `{seed}`",
        "- Structural identity (geometry, objects, doors, windows): **verified**",
        "",
        "## Wall materials (A -> B)",
        "",
    ]
    for old, new in report.get("wall_materials", {}).items():
        lines.append(f"- `{old}` -> `{new}`")
    lines += ["", "## Floor materials (A -> B)", ""]
    for old, new in report.get("floor_materials", {}).items():
        lines.append(f"- `{old}` -> `{new}`")
    if "ceiling_material" in report:
        lines += ["", "## Ceiling material (A -> B)", ""]
        for old, new in report["ceiling_material"].items():
            lines.append(f"- `{old}` -> `{new}`")
    lines += ["", "## Lighting (warm tint + dimming)", ""]
    for entry in report.get("lights", []):
        lines.append(
            f"- `{entry['id']}`: rgb {entry['before']['rgb']} -> {entry['after']['rgb']}, "
            f"intensity {entry['before']['intensity']} -> {entry['after']['intensity']}"
        )
    if "skybox" in report:
        sky = report["skybox"]
        lines += ["", f"## Skybox: `{sky['before']}` -> `{sky['after']}`"]
    lines.append("")
    path.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def generate(forced_index: Optional[int] = None, seed: Optional[int] = None) -> None:
    """Full generation pass; safe to re-run (outputs are overwritten)."""
    gen_cfg = GenerationConfig()
    if seed is None:
        seed = gen_cfg.variant_seed
    ensure_dirs()

    import prior  # deferred: downloads dataset on first use

    logger.info("loading %s @ %s (%s split)...",
                gen_cfg.dataset, gen_cfg.dataset_revision[:8], gen_cfg.split)
    dataset = prior.load_dataset(
        gen_cfg.dataset, revision=gen_cfg.dataset_revision
    )[gen_cfg.split]
    logger.info("dataset ready: %d houses", len(dataset))

    house_index, house_a, target = pick_house(dataset, gen_cfg, forced_index)
    pools = harvest_pools(dataset, gen_cfg.scan_limit)
    house_b, report = build_variant_b(house_a, pools, seed)
    assert_structurally_identical(house_a, house_b)

    with open(HOUSE_A_PATH, "w") as f:
        json.dump(house_a, f)
    with open(HOUSE_B_PATH, "w") as f:
        json.dump(house_b, f)
    task_config = {
        "dataset": gen_cfg.dataset,
        "dataset_revision": gen_cfg.dataset_revision,
        "split": gen_cfg.split,
        "house_index": house_index,
        "target_object_type": target,
        "variant_seed": seed,
        "house_a": str(HOUSE_A_PATH.name),
        "house_b": str(HOUSE_B_PATH.name),
    }
    with open(TASK_CONFIG_PATH, "w") as f:
        json.dump(task_config, f, indent=2)
    write_summary(DATA_DIR / "variants_summary.md", house_index, target, seed, report)

    logger.info("wrote %s, %s, %s", HOUSE_A_PATH, HOUSE_B_PATH, TASK_CONFIG_PATH)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--house-index", type=int, default=None,
                        help="force a specific procthor-10k train house index")
    parser.add_argument("--seed", type=int, default=None,
                        help="override the visual-variant RNG seed")
    args = parser.parse_args()
    generate(forced_index=args.house_index, seed=args.seed)


if __name__ == "__main__":
    main()
