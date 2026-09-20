"""Contract tests for the single-change evaluation houses.

Run with::

    python tests/test_single_factor.py          # no pytest needed
    python -m pytest tests/test_single_factor.py -q

These run against the real committed houses, offline -- no ProcTHOR dataset and
no Unity. What they pin:

  * the six factors RECOMPOSE into the frozen L1, L2 and L3 exactly, so they are
    complete (nothing the ladder changes is missing) and disjoint;
  * each factor changes only the fields it owns, which is what makes a
    single-change result attributable;
  * the recomposition test can actually FAIL (negative control) -- a self-test
    that cannot fail is not a self-test.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from config import GenerationConfig, pair_house_path, pair_dir  # noqa: E402
from envs.generate_variants import (  # noqa: E402
    DISTRACTOR_TAG, _iter_objects, _object_type, assert_structurally_identical,
)
from envs.make_single_factor import (  # noqa: E402
    CHECKPOINTS, FACTORS, ORDER, _apply, build_pair,
)

PAIRS = [f"pair{i}" for i in range(GenerationConfig().n_pairs)]


def _load(pair: str, level: str):
    return json.loads(pair_house_path(pair, level).read_text())


def _sources(pair: str):
    return {lvl: _load(pair, lvl) for lvl in ("L1", "L2", "L3")}


def _target(pair: str) -> str:
    return json.loads((pair_dir(pair) / "task_config.json").read_text())["target_object_type"]


def test_factors_recompose_into_every_frozen_house() -> None:
    """The whole design rests on this: composing the single changes must give
    back the cumulative house, byte for byte, in every pair."""
    for pair in PAIRS:
        a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
        for level, factors in CHECKPOINTS:
            rebuilt, _ = _apply(a, factors, src, tgt)
            assert rebuilt == src[level], f"{pair}: {factors} != frozen {level}"


def test_recomposition_test_can_fail() -> None:
    """Negative control: drop one factor and the check must notice."""
    pair = PAIRS[0]
    a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
    rebuilt, _ = _apply(a, ("F_mat", "F_light"), src, tgt)   # sky left out
    assert rebuilt != src["L1"], "recomposition passed with a factor missing"


def test_each_factor_changes_only_its_own_fields() -> None:
    for pair in PAIRS:
        a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
        params_a = a.get("proceduralParameters", {})
        for name in ORDER:
            h, _ = _apply(a, (name,), src, tgt)
            p = h.get("proceduralParameters", {})
            objs_a = {o["id"]: o for o in _iter_objects(a["objects"])}
            objs_h = {o["id"]: o for o in _iter_objects(h["objects"])}

            if name == "F_light":
                assert p.get("skyboxId") == params_a.get("skyboxId")
                assert p.get("ceilingMaterial") == params_a.get("ceilingMaterial")
            if name == "F_sky":
                assert p.get("lights") == params_a.get("lights")
            if name in ("F_mat", "F_light", "F_sky"):
                assert set(objs_h) == set(objs_a), f"{pair} {name} touched objects"
                for oid, obj in objs_h.items():
                    assert obj.get("assetId") == objs_a[oid].get("assetId")
            if name in ("F_obj", "F_tgt", "F_clut"):
                assert p.get("lights") == params_a.get("lights")
                assert p.get("skyboxId") == params_a.get("skyboxId")
                assert h.get("walls") == a.get("walls")


def test_target_factor_moves_exactly_the_target() -> None:
    for pair in PAIRS:
        a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
        h, _ = _apply(a, ("F_tgt",), src, tgt)
        objs_a = {o["id"]: o for o in _iter_objects(a["objects"])}
        changed = {oid for oid, o in ((o["id"], o) for o in _iter_objects(h["objects"]))
                   if o.get("assetId") != objs_a[oid].get("assetId")}
        types = {oid: _object_type(objs_a[oid]) for oid in changed}
        assert all(t == tgt for t in types.values()), f"{pair}: F_tgt moved {types}"
        # And the complementary factor must never move the target.
        h2, _ = _apply(a, ("F_obj",), src, tgt)
        for o in _iter_objects(h2["objects"]):
            if _object_type(o) == tgt:
                assert o.get("assetId") == objs_a[o["id"]].get("assetId"), \
                    f"{pair}: F_obj changed the target"


def test_clutter_factor_only_adds_tagged_objects() -> None:
    for pair in PAIRS:
        a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
        h, rep = _apply(a, ("F_clut",), src, tgt)
        ids_a = {o["id"] for o in _iter_objects(a["objects"])}
        ids_h = {o["id"] for o in _iter_objects(h["objects"])}
        assert ids_a <= ids_h, f"{pair}: F_clut removed objects"
        added = ids_h - ids_a
        assert all(DISTRACTOR_TAG in i for i in added), f"{pair}: untagged additions {added}"
        assert len(added) == rep["F_clut"]["n_added"]
        # Clutter must never be an instance of the target type, or the task
        # becomes "find A fridge" instead of "find THE fridge".
        for o in _iter_objects(h["objects"]):
            if DISTRACTOR_TAG in str(o.get("id")):
                assert _object_type(o) != tgt, f"{pair}: clutter of the target type"
                assert o.get("kinematic") is True, f"{pair}: clutter can move"


def test_written_houses_match_what_the_builder_reports() -> None:
    """Every file on disk must equal a fresh build, and pass its structural rule."""
    for pair in PAIRS:
        a, src, tgt = _load(pair, "A"), _sources(pair), _target(pair)
        rec = json.loads((pair_dir(pair) / "single_factor.json").read_text())
        for name in ORDER:
            path = pair_house_path(pair, name)
            if not rec["factors"][name]["written"]:
                assert not path.exists(), f"{pair}: {name} reported unwritten but exists"
                continue
            fresh, _ = _apply(a, (name,), src, tgt)
            assert json.loads(path.read_text()) == fresh, f"{pair}: {name} on disk differs"
            assert fresh != a, f"{pair}: {name} is identical to house A"
            assert_structurally_identical(a, fresh, level=FACTORS[name][1],
                                          target_object_type=tgt)


def test_unswappable_target_pair_has_no_target_factor() -> None:
    """pair2's target has no footprint-safe alternative, so 'change the target
    only' is not a change. It must be reported and skipped, not written as a
    copy of house A -- the same validity check L2noT passed."""
    rec = json.loads((pair_dir("pair2") / "single_factor.json").read_text())
    assert rec["factors"]["F_tgt"]["written"] is False
    assert not pair_house_path("pair2", "F_tgt").exists()
    for pair in [p for p in PAIRS if p != "pair2"]:
        rec = json.loads((pair_dir(pair) / "single_factor.json").read_text())
        assert rec["factors"]["F_tgt"]["written"] is True, f"{pair} lost its target factor"


def test_build_is_deterministic() -> None:
    """No randomness anywhere: rebuilding must reproduce the same bytes."""
    for pair in PAIRS:
        before = {n: pair_house_path(pair, n).read_text()
                  for n in ORDER if pair_house_path(pair, n).exists()}
        build_pair(pair, write=False)
        after = {n: pair_house_path(pair, n).read_text()
                 for n in ORDER if pair_house_path(pair, n).exists()}
        assert before == after


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
