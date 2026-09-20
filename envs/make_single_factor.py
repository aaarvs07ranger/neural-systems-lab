"""Single-change evaluation houses: each one changes exactly ONE thing.

The severity ladder is CUMULATIVE -- L1 repaints the room, L2 adds new object
appearances on top of that, L3 adds clutter on top of that. It answers "how far
can we push this before the agent breaks", but it cannot say which individual
change did the damage, because every rung above L1 contains all the rungs below
it. Vishwas asked for the other half (2026-09-19): change one thing at a time.

    A + materials          A + lighting          A + sky
    A + other objects      A + the target        A + clutter

**These are DERIVED from the frozen houses, never redrawn.** Each factor copies
the fields it owns out of the already-verified stacked house and writes them
into house A. The single change is then byte-identical to the change the ladder
applied, so a single-change result and a ladder result are directly comparable.
Redrawing the change with a fresh random seed would produce a DIFFERENT repaint,
and any difference in damage could then be blamed on the draw rather than on the
factor.

That design also gives an exact self-test, which this module refuses to write
without:

    A + materials + lighting + sky                        == the frozen L1
    ... + other objects + target                          == the frozen L2
    ... + clutter                                         == the frozen L3

If those three comparisons hold byte-for-byte, the factors are complete (nothing
the ladder changes is missing) and disjoint (no factor changes anything another
one owns). No training is needed: the agent only ever trains in house A, so
these are extra houses to EVALUATE existing checkpoints in.

    python envs/make_single_factor.py               # every pair
    python envs/make_single_factor.py --pairs pair0
"""
from __future__ import annotations

import argparse
import copy
import json
import logging
import sys
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import GenerationConfig, pair_dir, pair_house_path  # noqa: E402
from envs.generate_variants import (  # noqa: E402
    DISTRACTOR_TAG,
    House,
    _iter_objects,
    _object_type,
    assert_structurally_identical,
)

logger = logging.getLogger("single_factor")

# factor -> (house it is copied out of, structural rule it is checked under,
#            one-line description for the paper)
FACTORS: Dict[str, Tuple[str, str, str]] = {
    "F_mat":   ("L1", "L1", "wall, floor and ceiling materials"),
    "F_light": ("L1", "L1", "light colour and intensity"),
    "F_sky":   ("L1", "L1", "the sky seen through the windows"),
    "F_obj":   ("L2", "L2", "the look of every object except the target"),
    "F_tgt":   ("L2", "L2", "the look of the target only"),
    "F_clut":  ("L3", "L3", "added clutter"),
}
# Order matters: composing them in this order must rebuild L1, then L2, then L3.
ORDER: Tuple[str, ...] = ("F_mat", "F_light", "F_sky", "F_obj", "F_tgt", "F_clut")
CHECKPOINTS: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
    ("L1", ("F_mat", "F_light", "F_sky")),
    ("L2", ("F_mat", "F_light", "F_sky", "F_obj", "F_tgt")),
    ("L3", ORDER),
)


# ---------------------------------------------------------------------------
# The six factors. Each writes INTO `dst` (a copy of house A), taking values
# from `src` (a frozen stacked house). None of them touches anything else.
# ---------------------------------------------------------------------------
def _by_id(objects: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {str(o.get("id")): o for o in _iter_objects(objects)}


def f_mat(dst: House, src: House, target: str) -> Dict[str, Any]:
    """Wall, floor and ceiling materials."""
    changed: List[str] = []
    for key, dst_items, src_items in (
        ("material", dst.get("walls", []), src.get("walls", [])),
        ("floorMaterial", dst.get("rooms", []), src.get("rooms", [])),
    ):
        src_by_id = {str(i.get("id")): i for i in src_items}
        for item in dst_items:
            other = src_by_id.get(str(item.get("id")))
            if other is None or key not in other:
                continue
            if item.get(key) != other[key]:
                changed.append(f"{item.get('id')}.{key}")
            item[key] = copy.deepcopy(other[key])
    d_params = dst.setdefault("proceduralParameters", {})
    s_params = src.get("proceduralParameters", {})
    if "ceilingMaterial" in s_params:
        if d_params.get("ceilingMaterial") != s_params["ceilingMaterial"]:
            changed.append("ceilingMaterial")
        d_params["ceilingMaterial"] = copy.deepcopy(s_params["ceilingMaterial"])
    return {"fields_changed": changed}


def f_light(dst: House, src: House, target: str) -> Dict[str, Any]:
    """Light colour and intensity. The whole list is copied, so ids stay aligned."""
    d_params = dst.setdefault("proceduralParameters", {})
    s_lights = src.get("proceduralParameters", {}).get("lights")
    if s_lights is None:
        return {"n_lights": 0}
    changed = sum(1 for a, b in zip(d_params.get("lights", []), s_lights) if a != b)
    d_params["lights"] = copy.deepcopy(s_lights)
    return {"n_lights": len(s_lights), "n_changed": changed}


def f_sky(dst: House, src: House, target: str) -> Dict[str, Any]:
    d_params = dst.setdefault("proceduralParameters", {})
    s_params = src.get("proceduralParameters", {})
    before, after = d_params.get("skyboxId"), s_params.get("skyboxId")
    if "skyboxId" in s_params:
        d_params["skyboxId"] = copy.deepcopy(after)
    return {"before": before, "after": after, "changed": before != after}


def _copy_assets(dst: House, src: House, target: str, want_target: bool) -> Dict[str, Any]:
    src_by_id = _by_id(src.get("objects", []))
    swaps: List[Dict[str, str]] = []
    for obj in _iter_objects(dst.get("objects", [])):
        other = src_by_id.get(str(obj.get("id")))
        if other is None or "assetId" not in other:
            continue
        is_target = _object_type(obj) == target
        if is_target != want_target:
            continue
        if obj.get("assetId") != other["assetId"]:
            swaps.append({"id": str(obj.get("id")), "type": _object_type(obj) or "",
                          "before": obj.get("assetId"), "after": other["assetId"]})
        obj["assetId"] = other["assetId"]
    return {"n_swapped": len(swaps), "swaps": swaps}


def f_obj(dst: House, src: House, target: str) -> Dict[str, Any]:
    """Every object's appearance EXCEPT the target's."""
    return _copy_assets(dst, src, target, want_target=False)


def f_tgt(dst: House, src: House, target: str) -> Dict[str, Any]:
    """The target's appearance only. A no-op where the target has no
    footprint-safe alternative (pair2), which is why that pair gets no F_tgt
    house -- an identical copy of A is not a test."""
    return _copy_assets(dst, src, target, want_target=True)


def f_clut(dst: House, src: House, target: str) -> Dict[str, Any]:
    """The clutter L3 added, inserted under the same hosts, in the same order.

    Clutter was placed on the L2 house, whose surfaces are different ASSETS of
    the same type. Positions are copied unchanged (they are what L3 verified),
    and every distractor is kinematic, so nothing can fall; whether a surface of
    a different mesh still sits under it is a question only the simulator can
    answer, which is what the C1-C3 gate is for.
    """
    dst_by_id = _by_id(dst.get("objects", []))
    added: List[Dict[str, Any]] = []

    def walk(src_objects: List[Dict[str, Any]], host_id: Optional[str]) -> None:
        for obj in src_objects:
            oid = str(obj.get("id"))
            if DISTRACTOR_TAG in oid:
                host = dst_by_id.get(host_id) if host_id else None
                bucket = host.setdefault("children", []) if host else dst.setdefault("objects", [])
                bucket.append(copy.deepcopy(obj))
                added.append({"id": oid, "host": host_id,
                              "asset": obj.get("assetId")})
                continue
            walk(obj.get("children", []) or [], oid)

    walk(src.get("objects", []), None)
    return {"n_added": len(added), "distractors": added}


BUILDERS: Dict[str, Callable[[House, House, str], Dict[str, Any]]] = {
    "F_mat": f_mat, "F_light": f_light, "F_sky": f_sky,
    "F_obj": f_obj, "F_tgt": f_tgt, "F_clut": f_clut,
}


# ---------------------------------------------------------------------------
def _load(path: Path) -> House:
    return json.loads(path.read_text())


def _apply(base: House, factors: Tuple[str, ...], sources: Dict[str, House],
           target: str) -> Tuple[House, Dict[str, Any]]:
    house = copy.deepcopy(base)
    report: Dict[str, Any] = {}
    for name in factors:
        src_level = FACTORS[name][0]
        report[name] = BUILDERS[name](house, sources[src_level], target)
    return house, report


def build_pair(pair_id: str, write: bool = True) -> Dict[str, Any]:
    """Build every single-change house for one pair. Returns the provenance record."""
    d = pair_dir(pair_id)
    house_a = _load(pair_house_path(pair_id, "A"))
    sources = {lvl: _load(pair_house_path(pair_id, lvl)) for lvl in ("L1", "L2", "L3")}
    target = json.loads((d / "task_config.json").read_text())["target_object_type"]

    # --- the self-test, BEFORE anything is written -------------------------
    # Composing the factors in order must rebuild each frozen house exactly. If
    # it does, the six factors are complete and disjoint by demonstration.
    recomposition: Dict[str, bool] = {}
    for level, factors in CHECKPOINTS:
        rebuilt, _ = _apply(house_a, factors, sources, target)
        ok = rebuilt == sources[level]
        recomposition[level] = ok
        if not ok:
            raise AssertionError(
                f"{pair_id}: composing {' + '.join(factors)} onto house A does NOT "
                f"reproduce the frozen {level}. The factors do not account for "
                f"everything that rung changes, so a single-change result could "
                f"not be compared with the ladder. Nothing written."
            )

    record: Dict[str, Any] = {
        "pair": pair_id, "target": target, "derived_from": "committed a/b_L1/b_L2/b_L3",
        "recomposition_exact": recomposition, "factors": {},
    }
    for name in ORDER:
        house, rep = _apply(house_a, (name,), sources, target)
        detail = rep[name]
        if house == house_a:
            # Only legitimate case: pair2's target has no footprint-safe
            # alternative, so "change the target only" is not a change at all.
            record["factors"][name] = {"written": False, "reason": "identical to house A",
                                       **detail}
            logger.warning("%s %s: identical to house A, not written", pair_id, name)
            continue
        assert_structurally_identical(house_a, house, level=FACTORS[name][1],
                                      target_object_type=target)
        record["factors"][name] = {"written": True, "description": FACTORS[name][2],
                                   **detail}
        if write:
            out = pair_house_path(pair_id, name)
            out.write_text(json.dumps(house, indent=2) + "\n")
            logger.info("%s %s -> %s", pair_id, name, out.name)
    if write:
        (d / "single_factor.json").write_text(json.dumps(record, indent=2) + "\n")
    return record


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", default="",
                    help="comma-separated pair ids (default: every pair)")
    ap.add_argument("--dry-run", action="store_true", help="check only, write nothing")
    args = ap.parse_args()
    pairs = ([p.strip() for p in args.pairs.split(",") if p.strip()]
             or [f"pair{i}" for i in range(GenerationConfig().n_pairs)])
    for pid in pairs:
        rec = build_pair(pid, write=not args.dry_run)
        written = [n for n, f in rec["factors"].items() if f["written"]]
        skipped = [n for n, f in rec["factors"].items() if not f["written"]]
        print(f"{pid}: recomposition exact for L1/L2/L3 | wrote {len(written)}: "
              f"{', '.join(written)}" + (f" | skipped {', '.join(skipped)}" if skipped else ""))


if __name__ == "__main__":
    main()
