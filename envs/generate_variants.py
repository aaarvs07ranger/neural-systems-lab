"""Generate paired ProcTHOR houses: identical structure, escalating visual shift.

Variant A is a house taken verbatim from the ProcTHOR-10k train split. Each
variant B is a deep copy of A with progressively more appearance rewritten.
The rungs are CUMULATIVE, which is what makes the benchmark's x-axis a ladder
rather than a set of unrelated conditions:

* **L1** (mild)  every wall / room-floor / ceiling material remapped to a
                 different valid material; every procedural light re-tinted
                 (warm) and dimmed; skybox swapped.
* **L2**         L1 + every object's ``assetId`` swapped for a DIFFERENT asset
                 of the SAME objectType (Fridge_19 -> Fridge_3). ``id``,
                 ``position`` and ``rotation`` are preserved exactly, so the
                 task graph is untouched while object appearance changes.
                 Separates semantic identity from appearance binding.
* **L3**         L2 + distractor objects of types ABSENT from A, placed as
                 children of existing receptacles (surface placement keeps them
                 off the floor navmesh). Never adds an instance of the target
                 type -- that would change the task itself.

Replacement material and asset names are harvested from *other* ProcTHOR-10k
houses, so every name is guaranteed to exist in the THOR asset database.

Static structural checks run before anything is written (see
``assert_structurally_identical``). They are necessary but NOT sufficient for
L2/L3: different assets can have different physical footprints, which would
change the reachable-position set and silently break the paired-start
protocol. Detecting that requires booting Unity and belongs to the separate
runtime verification pass (C1-C3), not this script.

Outputs (all under data/):
    house_a.json           training variant
    house_b.json           zero-shot variant, L1 (path kept for compatibility)
    house_b_L2.json        zero-shot variant, L2
    house_b_L3.json        zero-shot variant, L3
    task_config.json       target object type + provenance + seeds + levels
    variants_summary.md    human-readable diff of every change, per level

Usage:
    python envs/generate_variants.py [--house-index N] [--seed S] [--levels L1,L2,L3]

Requires network on first run (prior downloads the procthor-10k dataset).
No Unity/AI2-THOR process is launched -- this is pure JSON manipulation.
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

# Severity rungs, in cumulative order. L4 (layout perturbation) is deliberately
# absent: it changes geometry, so paired starts and SPL stop being comparable.
LEVELS: Tuple[str, ...] = ("L1", "L2", "L3")

# Marker embedded in the `id` of every object L3 adds, so the structural check
# and any later analysis can identify (and strip) distractors unambiguously.
DISTRACTOR_TAG = "|distractor|"

# Cap per surface so a sparse house never gets an impossible pile.
MAX_DISTRACTORS_PER_HOST = 4


def _iter_objects(objects: Sequence[Dict[str, Any]]):
    """Yield every object and nested child in stable document order.

    Order matters: L2/L3 draw from the RNG once per object, so a
    non-deterministic traversal would make generation unreproducible.
    """
    for obj in objects:
        yield obj
        for child in _iter_objects(obj.get("children", [])):
            yield child


def _object_type(obj: Dict[str, Any]) -> Optional[str]:
    """Runtime objectType of a single object.

    The ``id`` field is authoritative ('Fridge|2|1' -> 'Fridge'); the assetId
    prefix is the fallback. NOTE: deliberately NOT used by ``_object_types``
    below, which stays assetId-based because house SELECTION depends on it --
    changing that could select a different house and invalidate every
    committed result.
    """
    oid = obj.get("id")
    if isinstance(oid, str) and "|" in oid:
        return oid.split("|")[0]
    asset_id = obj.get("assetId", "")
    return asset_id.split("_")[0] if "_" in asset_id else None



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


def harvest_asset_pool(
    dataset: Sequence[House], scan_limit: int
) -> Dict[str, List[str]]:
    """Collect valid assetIds per objectType from real houses (L2/L3 source).

    Returns e.g. {"Fridge": ["Fridge_10", "Fridge_19", ...], ...}. Sorted for
    determinism, exactly like ``harvest_pools``. Every name is guaranteed to
    exist in the THOR asset database because it was read out of a shipped
    house, never constructed.
    """
    pool: Dict[str, Set[str]] = {}
    for idx in range(min(scan_limit, len(dataset))):
        for obj in _iter_objects(dataset[idx].get("objects", [])):
            obj_type = _object_type(obj)
            asset_id = obj.get("assetId")
            if obj_type and isinstance(asset_id, str) and asset_id:
                pool.setdefault(obj_type, set()).add(asset_id)
    out = {t: sorted(v) for t, v in sorted(pool.items())}
    multi = sum(1 for v in out.values() if len(v) > 1)
    logger.info(
        "asset pool: %d object types, %d with >1 asset (swappable at L2)",
        len(out), multi,
    )
    return out


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


def _apply_l1(
    house_b: House,
    pools: Dict[str, List[str]],
    rng: random.Random,
    report: Dict[str, Any],
) -> None:
    """Rung L1, in place: wall/floor/ceiling materials, lighting, skybox.

    Extracted verbatim from the original ``build_variant_b``. The statement
    order -- and therefore the sequence of RNG draws -- is unchanged, so L1
    output stays byte-identical to the variant that produced every committed
    result. Do not reorder these blocks.
    """

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


def _apply_l2(
    house_b: House,
    asset_pool: Dict[str, List[str]],
    rng: random.Random,
    report: Dict[str, Any],
) -> None:
    """Rung L2, in place: swap every object's asset for a different one of the
    SAME objectType.

    ``id``, ``position``, ``rotation`` and the children list are untouched, so
    the task graph, the target lookup and the paired-start machinery are all
    unaffected at the JSON level. Physical footprint is NOT guaranteed
    unchanged -- that is what the runtime C1 check exists to catch.
    """
    swaps: List[Dict[str, Any]] = []
    unswappable: List[Dict[str, Any]] = []
    for obj in _iter_objects(house_b.get("objects", [])):
        obj_type = _object_type(obj)
        current = obj.get("assetId")
        if not obj_type or not isinstance(current, str) or not current:
            continue
        alternatives = [a for a in asset_pool.get(obj_type, []) if a != current]
        if not alternatives:
            unswappable.append({"id": obj.get("id"), "type": obj_type,
                                "asset": current, "reason": "no alternative asset in pool"})
            continue
        replacement = rng.choice(alternatives)
        obj["assetId"] = replacement
        swaps.append({"id": obj.get("id"), "type": obj_type,
                      "before": current, "after": replacement})
    report["l2_asset_swaps"] = swaps
    report["l2_unswappable"] = unswappable
    logger.info("L2: swapped %d object assets, %d had no alternative",
                len(swaps), len(unswappable))


def _apply_l3(
    house_b: House,
    asset_pool: Dict[str, List[str]],
    rng: random.Random,
    target_object_type: str,
    n_distractors: int,
    report: Dict[str, Any],
) -> None:
    """Rung L3, in place: add distractor objects on top of existing receptacles.

    Two hard rules, both load-bearing:

    * **Never add an instance of the target type.** That would turn "find the
      fridge" into "find *a* fridge" -- a different, easier task, and the B
      column would improve for a reason unrelated to appearance.
    * **Surface placement only.** Distractors become children of receptacles
      that already carry children, so they rest on surfaces rather than on the
      floor navmesh. This is how the schema already represents countertop
      clutter, and it keeps the reachable-position set intact by construction.
    """
    present = {t for t in (_object_type(o)
                           for o in _iter_objects(house_b.get("objects", []))) if t}
    absent = sorted(t for t in asset_pool
                    if t not in present and t != target_object_type)
    fallback = sorted(t for t in present if t != target_object_type)
    candidates = absent or fallback

    # The target is never a host. Clutter resting ON the fridge occludes it and
    # changes its silhouette, which is L2's axis (object appearance), not L3's
    # (irrelevant scene content). Measured before this exclusion: 53% of
    # distractors landed on the target, because this house has only two
    # surfaces. That is a systematic bias, not noise -- more house pairs would
    # estimate a confounded quantity more precisely.
    hosts = [o for o in house_b.get("objects", [])
             if o.get("children") and _object_type(o) != target_object_type]

    # Scale to the space actually available. Excluding the target can leave a
    # sparse house with a single surface, and piling every distractor onto it
    # would interpenetrate -- physics settling could then drop items on the
    # floor, changing the reachable set and failing the runtime C1 check.
    requested = int(n_distractors)
    n_to_place = min(requested, MAX_DISTRACTORS_PER_HOST * len(hosts)) if hosts else 0

    added: List[Dict[str, Any]] = []
    report["l3_requested"] = requested
    report["l3_hosts"] = [h.get("id") for h in hosts]
    if not candidates or not hosts:
        report["l3_distractors"] = added
        report["l3_note"] = ("no candidate types" if not candidates
                             else "no non-target surface to place on")
        logger.warning("L3: nothing added (%s)", report["l3_note"])
        return
    if n_to_place < requested:
        report["l3_note"] = (f"scaled {requested} -> {n_to_place}: only "
                             f"{len(hosts)} non-target surface(s) available")
        logger.info("L3: %s", report["l3_note"])

    # Shuffle once for variety, then cycle: deterministic given the seed.
    order = list(candidates)
    rng.shuffle(order)
    for i in range(n_to_place):
        obj_type = order[i % len(order)]
        assets = asset_pool.get(obj_type, [])
        if not assets:
            continue
        host = rng.choice(hosts)
        anchor_child = rng.choice(host["children"])
        position = dict(anchor_child["position"])
        # Offset within the receptacle surface so distractors do not spawn
        # exactly on top of an existing item.
        position["x"] = round(position["x"] + rng.uniform(-0.18, 0.18), 6)
        position["z"] = round(position["z"] + rng.uniform(-0.18, 0.18), 6)
        distractor = {
            "assetId": rng.choice(assets),
            "id": f"{obj_type}{DISTRACTOR_TAG}{i}",
            "kinematic": False,
            "position": position,
            "rotation": {"x": -0.0, "y": float(rng.randrange(0, 360, 30)), "z": -0.0},
        }
        host["children"].append(distractor)
        added.append({"id": distractor["id"], "type": obj_type,
                      "asset": distractor["assetId"], "host": host.get("id"),
                      "novel_type": obj_type in absent})
    report["l3_distractors"] = added
    logger.info("L3: added %d distractors (%d of types absent from A)",
                len(added), sum(1 for d in added if d["novel_type"]))


def build_variant(
    house_a: House,
    pools: Dict[str, List[str]],
    seed: int,
    level: str = "L1",
    asset_pool: Optional[Dict[str, List[str]]] = None,
    target_object_type: Optional[str] = None,
    n_distractors: int = 8,
) -> Tuple[House, Dict[str, Any]]:
    """Deep-copy house A and apply every rung up to ``level``. Returns (B, report).

    Rungs are cumulative: L2 output contains L1's changes, L3 contains both.
    A single ``random.Random(seed)`` is threaded through all rungs, so a given
    (seed, level) pair always reproduces the same house.
    """
    if level not in LEVELS:
        raise ValueError(f"level={level!r} not in {LEVELS}")
    if level in ("L2", "L3") and not asset_pool:
        raise ValueError(f"level {level} requires asset_pool (see harvest_asset_pool)")
    if level == "L3" and not target_object_type:
        raise ValueError("level L3 requires target_object_type to protect it")

    rng = random.Random(seed)
    house_b = copy.deepcopy(house_a)
    report: Dict[str, Any] = {"level": level}

    _apply_l1(house_b, pools, rng, report)
    if level in ("L2", "L3"):
        _apply_l2(house_b, asset_pool or {}, rng, report)
    if level == "L3":
        _apply_l3(house_b, asset_pool or {}, rng,
                  str(target_object_type), n_distractors, report)
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


def _strip_asset_ids(house: House) -> House:
    """Drop every ``assetId`` so two houses can be compared modulo appearance."""
    stripped = copy.deepcopy(house)
    for obj in _iter_objects(stripped.get("objects", [])):
        obj.pop("assetId", None)
    return stripped


def _strip_distractors(house: House) -> House:
    """Remove every object L3 added, at any nesting depth."""
    stripped = copy.deepcopy(house)

    def prune(objects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        kept = []
        for obj in objects:
            if DISTRACTOR_TAG in str(obj.get("id", "")):
                continue
            if obj.get("children"):
                obj["children"] = prune(obj["children"])
            kept.append(obj)
        return kept

    stripped["objects"] = prune(stripped.get("objects", []))
    return stripped


def _count_type(house: House, obj_type: str) -> int:
    return sum(1 for o in _iter_objects(house.get("objects", []))
               if _object_type(o) == obj_type)


def assert_structurally_identical(
    house_a: House, house_b: House, level: str = "L1",
    target_object_type: Optional[str] = None,
) -> None:
    """Static structural check, per rung. Raises AssertionError on violation.

    What is compared, and why it weakens as the rung climbs:

    * **L1** -- everything except the whitelisted visual fields must be
      byte-identical. Materials are the only thing that changed.
    * **L2** -- as L1, but ``assetId`` is also stripped before comparing,
      because swapping assets is the point. Everything else about every object
      (``id``, ``position``, ``rotation``, nesting) must still match exactly.
    * **L3** -- as L2, after removing the tagged distractors from B. The
      original scene must survive untouched underneath the added clutter.

    A static pass CANNOT prove the physical footprint is unchanged: two assets
    of the same type may have different collision bounds, which would alter the
    reachable-position set and silently break paired starts. That is the job of
    the runtime C1/C2 checks, which need Unity. This function is the cheap
    necessary condition, not the sufficient one.
    """
    if level not in LEVELS:
        raise ValueError(f"level={level!r} not in {LEVELS}")

    left, right = house_a, house_b
    if level == "L3":
        right = _strip_distractors(right)
    if level in ("L2", "L3"):
        left, right = _strip_asset_ids(left), _strip_asset_ids(right)
    if _strip_visuals(left) != _strip_visuals(right):
        raise AssertionError(
            f"Variant B ({level}) differs from A beyond the fields that rung "
            f"is allowed to change!"
        )

    # C3, static half: the task itself must be unchanged.
    if target_object_type is not None:
        n_a = _count_type(house_a, target_object_type)
        n_b = _count_type(house_b, target_object_type)
        if n_a != n_b:
            raise AssertionError(
                f"target type {target_object_type!r} count changed A={n_a} "
                f"B={n_b} at {level} -- the task is no longer the same task."
            )

    logger.info("structural identity verified for %s%s", level,
                f" (target {target_object_type} x{_count_type(house_a, target_object_type)} preserved)"
                if target_object_type else "")


# ---------------------------------------------------------------------------
# Summary writer
# ---------------------------------------------------------------------------
def variant_path(level: str) -> Path:
    """Output path for a variant. L1 keeps the legacy filename on purpose: the
    committed baseline results were produced from ``data/house_b.json`` and must
    stay reproducible from that exact path."""
    return HOUSE_B_PATH if level == "L1" else DATA_DIR / f"house_b_{level}.json"


def write_summary(
    path: Path, house_index: int, target: str, seed: int,
    reports: Dict[str, Dict[str, Any]],
) -> None:
    """Human-readable diff of every change, one section per rung."""
    lines = [
        "# Visual Variant Summary",
        "",
        f"- Source: ProcTHOR-10k train split, house index **{house_index}**",
        f"- Target object type (ObjectNav): **{target}**",
        f"- Variant seed: `{seed}`",
        f"- Levels generated: **{', '.join(sorted(reports))}**",
        "- Structural identity (geometry, object placement, task graph): **verified per level**",
        "",
        "> Rungs are cumulative: L2 includes L1's changes, L3 includes both.",
        "> Static checks cannot prove physical footprints are unchanged for",
        "> L2/L3 -- the runtime C1/C2 navmesh verification does that.",
    ]

    l1 = reports.get("L1", {})
    if l1:
        lines += ["", "## L1 -- materials and lighting", "", "### Wall materials (A -> B)", ""]
        for old, new in l1.get("wall_materials", {}).items():
            lines.append(f"- `{old}` -> `{new}`")
        lines += ["", "### Floor materials (A -> B)", ""]
        for old, new in l1.get("floor_materials", {}).items():
            lines.append(f"- `{old}` -> `{new}`")
        if "ceiling_material" in l1:
            lines += ["", "### Ceiling material (A -> B)", ""]
            for old, new in l1["ceiling_material"].items():
                lines.append(f"- `{old}` -> `{new}`")
        lines += ["", "### Lighting (warm tint + dimming)", ""]
        for entry in l1.get("lights", []):
            lines.append(
                f"- `{entry['id']}`: rgb {entry['before']['rgb']} -> {entry['after']['rgb']}, "
                f"intensity {entry['before']['intensity']} -> {entry['after']['intensity']}"
            )
        if "skybox" in l1:
            sky = l1["skybox"]
            lines += ["", f"### Skybox: `{sky['before']}` -> `{sky['after']}`"]

    l2 = reports.get("L2") or reports.get("L3") or {}
    if l2.get("l2_asset_swaps") is not None:
        swaps = l2["l2_asset_swaps"]
        lines += ["", "## L2 -- object appearance (same type, different asset)", "",
                  f"{len(swaps)} object(s) swapped.", ""]
        for sw in swaps:
            lines.append(f"- `{sw['id']}` ({sw['type']}): `{sw['before']}` -> `{sw['after']}`")
        unsw = l2.get("l2_unswappable", [])
        if unsw:
            lines += ["", f"**{len(unsw)} object(s) had no alternative asset and were left "
                          "unchanged:**", ""]
            for u in unsw:
                lines.append(f"- `{u['id']}` ({u['type']}): `{u['asset']}`")

    l3 = reports.get("L3", {})
    if l3.get("l3_distractors") is not None:
        added = l3["l3_distractors"]
        novel = sum(1 for d in added if d.get("novel_type"))
        lines += ["", "## L3 -- distractor objects", "",
                  f"{len(added)} distractor(s) added, {novel} of a type absent from A. "
                  "All placed on receptacle surfaces; none of the target type.", ""]
        for d in added:
            lines.append(f"- `{d['id']}` ({d['type']}, `{d['asset']}`) on `{d['host']}`")
        if l3.get("l3_note"):
            lines += ["", f"_Note: {l3['l3_note']}_"]

    lines.append("")
    path.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def generate(
    forced_index: Optional[int] = None,
    seed: Optional[int] = None,
    levels: Optional[Sequence[str]] = None,
) -> None:
    """Full generation pass; safe to re-run (outputs are overwritten)."""
    gen_cfg = GenerationConfig()
    if seed is None:
        seed = gen_cfg.variant_seed
    requested = tuple(levels) if levels else tuple(gen_cfg.levels)
    unknown = [lv for lv in requested if lv not in LEVELS]
    if unknown:
        raise ValueError(f"unknown level(s) {unknown}; valid: {LEVELS}")
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
    # Only harvested when a rung actually needs it; L1-only runs stay as cheap
    # as they were before the ladder existed.
    asset_pool = (harvest_asset_pool(dataset, gen_cfg.scan_limit)
                  if any(lv in ("L2", "L3") for lv in requested) else {})

    reports: Dict[str, Dict[str, Any]] = {}
    for level in requested:
        house_b, report = build_variant(
            house_a, pools, seed, level=level, asset_pool=asset_pool,
            target_object_type=target, n_distractors=gen_cfg.n_distractors,
        )
        assert_structurally_identical(house_a, house_b, level=level,
                                      target_object_type=target)
        out_path = variant_path(level)
        with open(out_path, "w") as f:
            json.dump(house_b, f)
        reports[level] = report
        logger.info("wrote %s (%s)", out_path, level)

    with open(HOUSE_A_PATH, "w") as f:
        json.dump(house_a, f)
    task_config = {
        "dataset": gen_cfg.dataset,
        "dataset_revision": gen_cfg.dataset_revision,
        "split": gen_cfg.split,
        "house_index": house_index,
        "target_object_type": target,
        "variant_seed": seed,
        "house_a": str(HOUSE_A_PATH.name),
        "house_b": str(HOUSE_B_PATH.name),
        "levels": {lv: variant_path(lv).name for lv in requested},
        "n_distractors": gen_cfg.n_distractors,
    }
    with open(TASK_CONFIG_PATH, "w") as f:
        json.dump(task_config, f, indent=2)
    write_summary(DATA_DIR / "variants_summary.md", house_index, target, seed, reports)

    logger.info("wrote %s, %s, %s", HOUSE_A_PATH,
                ", ".join(str(variant_path(lv)) for lv in requested),
                TASK_CONFIG_PATH)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--house-index", type=int, default=None,
                        help="force a specific procthor-10k train house index")
    parser.add_argument("--seed", type=int, default=None,
                        help="override the visual-variant RNG seed")
    parser.add_argument("--levels", type=str, default=None,
                        help=f"comma-separated severity rungs to generate "
                             f"(default: all of {','.join(LEVELS)})")
    args = parser.parse_args()
    levels = [lv.strip() for lv in args.levels.split(",")] if args.levels else None
    generate(forced_index=args.house_index, seed=args.seed, levels=levels)


if __name__ == "__main__":
    main()
