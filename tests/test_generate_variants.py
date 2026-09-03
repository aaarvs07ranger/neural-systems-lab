"""Contract tests for the severity-ladder generator.

These pin the properties the benchmark's validity rests on. Run with::

    python tests/test_generate_variants.py     # no pytest needed
    python -m pytest tests/test_generate_variants.py -q

The house used is the real committed ``data/house_a.json``; only the material
and asset pools are synthetic, so the tests run offline (no ProcTHOR dataset,
no Unity).
"""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from envs.generate_variants import (  # noqa: E402
    DISTRACTOR_TAG,
    LEVELS,
    MAX_DISTRACTORS_PER_HOST,
    _iter_objects,
    _object_type,
    assert_structurally_identical,
    build_variant,
)

TARGET = "Fridge"
SEED = 1337

# Frozen synthetic pools: the L1 hash below is only meaningful against these.
POOLS = {
    "walls":    [f"Wall{i}" for i in range(12)],
    "floors":   [f"Floor{i}" for i in range(9)],
    "ceilings": [f"Ceil{i}" for i in range(5)],
    "skyboxes": [f"Sky{i}" for i in range(7)],
}
# The exact L1 house produced by the pre-ladder generator. If this changes,
# every committed baseline result stops being reproducible from source.
L1_SHA256 = "8c2b616ea511f978546a967f6c50a7a90d78c5647062830da9deda8efaafdadb"


def house_a():
    return json.loads((Path(__file__).resolve().parents[1] / "data/house_a.json").read_text())


def asset_pool(house):
    """Types present in the house get alternatives; extra types are L3 candidates."""
    present = {t for t in (_object_type(o) for o in _iter_objects(house["objects"])) if t}
    pool = {t: sorted({f"{t}_{i}" for i in (3, 7, 19)}) for t in present}
    pool.update({k: [f"{k}_1"] for k in
                 ("Vase", "Mug", "Book", "Toaster", "Bowl", "Candle", "Plate")})
    return pool


def build(level, house=None, n_distractors=8, seed=SEED):
    house = house or house_a()
    return build_variant(house, POOLS, seed, level=level, asset_pool=asset_pool(house),
                         target_object_type=TARGET, n_distractors=n_distractors)


def distractors(house):
    return [o for o in _iter_objects(house.get("objects", []))
            if DISTRACTOR_TAG in str(o.get("id", ""))]


def by_id(house):
    return {o["id"]: o for o in _iter_objects(house.get("objects", [])) if "id" in o}


# --------------------------------------------------------------------------
# L1: the rung every committed result was produced at
# --------------------------------------------------------------------------
def test_l1_output_is_byte_stable() -> None:
    """The single most important test in this file: refactors must not move L1."""
    b, _ = build("L1")
    got = hashlib.sha256(json.dumps(b, sort_keys=True).encode()).hexdigest()
    assert got == L1_SHA256, f"L1 output changed! {got} != {L1_SHA256}"


def test_l1_leaves_objects_completely_untouched() -> None:
    b, _ = build("L1")
    assert b["objects"] == house_a()["objects"]


# --------------------------------------------------------------------------
# Rungs stack
# --------------------------------------------------------------------------
def test_levels_are_cumulative() -> None:
    a = house_a()
    l1, _ = build("L1"); l2, _ = build("L2"); l3, _ = build("L3")
    # L2 and L3 carry L1's material change
    assert l2["walls"][0]["material"] == l1["walls"][0]["material"] != a["walls"][0]["material"]
    assert l3["walls"][0]["material"] == l1["walls"][0]["material"]
    # L3 carries L2's asset swaps
    l2_assets = {o["id"]: o["assetId"] for o in _iter_objects(l2["objects"]) if "id" in o}
    for obj in _iter_objects(l3["objects"]):
        if "id" in obj and DISTRACTOR_TAG not in obj["id"]:
            assert obj["assetId"] == l2_assets[obj["id"]]


# --------------------------------------------------------------------------
# L2: object appearance only
# --------------------------------------------------------------------------
def test_l2_changes_assets() -> None:
    a, (b, rep) = house_a(), build("L2")
    before = {o["id"]: o["assetId"] for o in _iter_objects(a["objects"]) if "id" in o}
    after = {o["id"]: o["assetId"] for o in _iter_objects(b["objects"]) if "id" in o}
    assert rep["l2_asset_swaps"], "no swaps recorded"
    assert any(before[k] != after[k] for k in before)


def test_l2_preserves_identity_and_placement() -> None:
    """Same objects, same ids, same places -- only their appearance differs."""
    a, (b, _) = house_a(), build("L2")
    ida, idb = by_id(a), by_id(b)
    assert set(ida) == set(idb), "object ids changed"
    for oid, obj_a in ida.items():
        for field in ("position", "rotation"):
            if field in obj_a:
                assert obj_a[field] == idb[oid][field], f"{oid}.{field} moved"


def test_l2_preserves_per_type_counts() -> None:
    a, (b, _) = house_a(), build("L2")
    def counts(h):
        out = {}
        for o in _iter_objects(h["objects"]):
            t = _object_type(o)
            if t:
                out[t] = out.get(t, 0) + 1
        return out
    assert counts(a) == counts(b)


# --------------------------------------------------------------------------
# L3: clutter, and the rules that keep it honest
# --------------------------------------------------------------------------
def test_l3_never_adds_the_target_type() -> None:
    """A second fridge would change 'find the fridge' into 'find A fridge'."""
    b, _ = build("L3")
    assert all(_object_type(d) != TARGET for d in distractors(b))
    n = lambda h: sum(1 for o in _iter_objects(h["objects"]) if _object_type(o) == TARGET)
    assert n(house_a()) == n(b) == 1


def test_l3_never_places_clutter_on_the_target() -> None:
    """Clutter on the fridge changes the target's own look -- that is L2's axis."""
    b, rep = build("L3")
    assert TARGET not in [str(h).split("|")[0] for h in rep["l3_hosts"]]
    for host in b["objects"]:
        if _object_type(host) == TARGET:
            assert not [c for c in host.get("children", [])
                        if DISTRACTOR_TAG in str(c.get("id", ""))]


def test_l3_places_on_surfaces_not_the_floor() -> None:
    """Distractors must be children of a receptacle; floor objects would block
    navigation and break the paired-start protocol."""
    b, _ = build("L3")
    top_level_ids = {str(o.get("id", "")) for o in b["objects"]}
    assert not any(DISTRACTOR_TAG in i for i in top_level_ids)
    assert distractors(b), "no distractors were added"


def test_l3_scales_count_to_available_surfaces() -> None:
    b, rep = build("L3", n_distractors=8)
    assert len(distractors(b)) == len(rep["l3_distractors"])
    assert len(distractors(b)) <= MAX_DISTRACTORS_PER_HOST * len(rep["l3_hosts"])
    assert len(distractors(b)) <= rep["l3_requested"]


def test_l3_leaves_the_original_scene_untouched() -> None:
    a, (b, _) = house_a(), build("L3")
    ida, idb = by_id(a), by_id(b)
    assert set(ida) <= set(idb)
    for oid, obj_a in ida.items():
        for field in ("position", "rotation"):
            if field in obj_a:
                assert obj_a[field] == idb[oid][field], f"{oid}.{field} moved"


# --------------------------------------------------------------------------
# Reproducibility
# --------------------------------------------------------------------------
def test_same_seed_reproduces_every_level() -> None:
    for level in LEVELS:
        assert build(level, seed=7)[0] == build(level, seed=7)[0]


def test_different_seeds_differ() -> None:
    assert build("L3", seed=1)[0] != build("L3", seed=2)[0]


# --------------------------------------------------------------------------
# The structural check must actually catch things
# --------------------------------------------------------------------------
def test_structural_check_passes_for_each_level() -> None:
    a = house_a()
    for level in LEVELS:
        b, _ = build(level)
        assert_structurally_identical(a, b, level=level, target_object_type=TARGET)


def test_structural_check_catches_a_moved_object() -> None:
    a = house_a()
    b, _ = build("L2")
    b["objects"][0]["position"]["x"] += 0.5      # geometry tampering
    try:
        assert_structurally_identical(a, b, level="L2", target_object_type=TARGET)
    except AssertionError:
        return
    raise AssertionError("a moved object slipped past the structural check")


def test_structural_check_catches_an_extra_target() -> None:
    a = house_a()
    b, _ = build("L3")
    clone = copy.deepcopy([o for o in b["objects"] if _object_type(o) == TARGET][0])
    clone["id"] = "Fridge|9|9"
    b["objects"].append(clone)
    try:
        assert_structurally_identical(a, b, level="L3", target_object_type=TARGET)
    except AssertionError:
        return
    raise AssertionError("a second target slipped past the structural check")


# --------------------------------------------------------------------------
# Argument validation
# --------------------------------------------------------------------------
def test_rejects_unknown_level_and_missing_inputs() -> None:
    a = house_a()
    for kwargs in (
        dict(level="L9", asset_pool={"x": ["y"]}, target_object_type=TARGET),
        dict(level="L2", asset_pool=None, target_object_type=TARGET),
        dict(level="L3", asset_pool={"x": ["y"]}, target_object_type=None),
    ):
        try:
            build_variant(a, POOLS, SEED, **kwargs)
        except ValueError:
            continue
        raise AssertionError(f"build_variant accepted bad args: {kwargs}")


def test_l3_distractors_are_never_placed_on_top_of_each_other() -> None:
    """Clutter dropped inside other clutter gets ejected onto the floor.

    Placement used to anchor on an existing item +/- 0.18 m with no check
    against the items already placed, so several could land within 25 cm of one
    another. Physics resolves that overlap by throwing one out, usually onto the
    floor, where it blocks navigation. pair1 L3 blocked an evaluation start pose
    that way on 2026-09-03, with three items piled inside 25 cm.
    """
    from envs.generate_variants import MIN_DISTRACTOR_SPACING

    for seed in range(12):
        variant, _ = build("L3", seed=seed)
        pts = [o["position"] for o in distractors(variant)]
        for i, a in enumerate(pts):
            for b in pts[i + 1:]:
                d = ((a["x"] - b["x"]) ** 2 + (a["z"] - b["z"]) ** 2) ** 0.5
                assert d >= MIN_DISTRACTOR_SPACING - 1e-9, (
                    f"seed {seed}: two distractors {d:.3f} m apart, "
                    f"minimum is {MIN_DISTRACTOR_SPACING} m"
                )


def test_l3_distractors_are_kinematic() -> None:
    """Clutter must not be physics-enabled.

    Physics-enabled clutter was the most persistent source of failure in this
    benchmark: an item slides off its surface, a round one rolls to a slightly
    different resting place each load, and on the floor it blocks cells the
    agent must start from. Because the outcome varies per load, a house could
    pass the C1-C3 gate three times and fail on the fourth -- which is what
    broke a live grid run on 2026-09-03 (eval seed 10016, pair1 L3). Freezing
    the object makes the file the ground truth.
    """
    for seed in (SEED, 7, 99):
        variant, _ = build("L3", seed=seed)
        placed = distractors(variant)
        assert placed, f"seed {seed} placed no distractors to check"
        for obj in placed:
            assert obj.get("kinematic") is True, (
                f"{obj['id']} is not kinematic — it can fall onto the floor "
                "and block a start pose"
            )


if __name__ == "__main__":
    fns = [(n, f) for n, f in sorted(globals().items())
           if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in fns:
        try:
            fn()
            print(f"PASS  {name}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL  {name}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    raise SystemExit(1 if failed else 0)
