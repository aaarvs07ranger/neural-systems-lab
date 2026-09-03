"""Contract tests for pair resolution and the severity-ladder evaluation.

Dependency-free runner (the pinned env has no pytest):
    python tests/test_pairs_and_eval.py
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd  # noqa: E402

import config  # noqa: E402
from config import EVAL_LEVELS, resolve_pair  # noqa: E402


def test_legacy_layout_is_the_default() -> None:
    """No pair id => the flat data/house_*.json paths every old result used."""
    os.environ.pop("NSL_PAIR", None)
    pair = resolve_pair()
    assert pair.pair_id == ""
    assert pair.house_a == config.HOUSE_A_PATH
    assert pair.task_config == config.TASK_CONFIG_PATH
    levels = [lvl for lvl, _ in pair.eval_houses]
    # The flat layout only ever held A and L1; higher rungs live in data/pairs/.
    assert levels == ["A", "L1"]
    assert dict(pair.eval_houses)["L1"] == config.HOUSE_B_PATH


def test_env_var_selects_the_pair() -> None:
    """Slurm array tasks pick their cell with NSL_PAIR, not a CLI flag."""
    os.environ["NSL_PAIR"] = "pair3"
    try:
        assert resolve_pair().pair_id == "pair3"
        # An explicit argument still wins over the environment.
        assert resolve_pair("pair1").pair_id == "pair1"
    finally:
        os.environ.pop("NSL_PAIR", None)


def test_pair_layout_walks_the_whole_ladder() -> None:
    pair = resolve_pair("pair2")
    levels = [lvl for lvl, _ in pair.eval_houses]
    assert levels == ["A"] + list(EVAL_LEVELS)
    by = dict(pair.eval_houses)
    assert by["A"].name == "a.json"
    assert by["L2"].name == "b_L2.json"
    assert pair.task_config == config.pair_dir("pair2") / "task_config.json"


def test_levels_can_be_narrowed() -> None:
    """A pair with only L1 generated must not demand L2/L3 files."""
    pair = resolve_pair("pair0", levels=("L1",))
    assert [lvl for lvl, _ in pair.eval_houses] == ["A", "L1"]


def test_oracle_table_is_optional() -> None:
    """Absent oracle table => None, and the env falls back to measuring."""
    pair = resolve_pair("pair_that_does_not_exist")
    assert pair.oracle_table is None


def test_tracker_reads_both_summary_formats() -> None:
    """Legacy two-row summaries and new per-level summaries must agree."""
    from scripts.tracker import read_metrics

    with tempfile.TemporaryDirectory() as tmp:
        legacy = Path(tmp) / "legacy_transfer_summary.csv"
        pd.DataFrame([
            {"variant": "A (train visuals)", "success_rate": 1.0, "spl": 0.8,
             "mean_episode_length": 20.0, "episodes": 25},
            {"variant": "B (zero-shot visuals)", "success_rate": 0.8, "spl": 0.6,
             "mean_episode_length": 40.0, "episodes": 25},
        ]).to_csv(legacy, index=False)

        ladder = Path(tmp) / "ladder_transfer_summary.csv"
        pd.DataFrame([
            {"level": "A", "variant": "A (train visuals)", "success_rate": 1.0,
             "spl": 0.8, "mean_episode_length": 20.0, "episodes": 25},
            {"level": "L1", "variant": "B_L1", "success_rate": 0.8, "spl": 0.6,
             "mean_episode_length": 40.0, "episodes": 25},
            {"level": "L2", "variant": "B_L2", "success_rate": 0.5, "spl": 0.3,
             "mean_episode_length": 90.0, "episodes": 25},
        ]).to_csv(ladder, index=False)

        old = read_metrics(legacy)
        new = read_metrics(ladder)                 # defaults to L1
        assert old == new, "L1 must ingest exactly as the old B row did"
        assert abs(new["relative_success_drop"] - 0.2) < 1e-9

        harder = read_metrics(ladder, level="L2")
        assert abs(harder["relative_success_drop"] - 0.5) < 1e-9
        # Every rung is scored against the SAME in-domain reference.
        assert harder["A_success"] == new["A_success"]


def test_one_env_config_builder_serves_every_baseline() -> None:
    """The three baselines must assemble the task identically.

    They each used to keep their own copy, and the world-model copies had
    already drifted out of sync with PPO's (no target_sequence, no oracle
    table), which would have silently run a different task on the same house.
    """
    import envs.task_setup as task_setup
    import models.dreamer_v3.adapter as dv3
    import models.td_mpc2.adapter as tdm
    import scripts.train_ppo as train_ppo

    assert dv3.build_env_config is task_setup.build_env_config
    assert tdm.build_env_config is task_setup.build_env_config
    # train_ppo re-exports a thin wrapper (evaluate_transfer imports it there).
    assert train_ppo.build_env_config.__module__ == "scripts.train_ppo"


def test_level_labels_cover_every_rung() -> None:
    from scripts.evaluate_transfer import LEVEL_LABELS

    for level in ("A",) + tuple(EVAL_LEVELS):
        assert level in LEVEL_LABELS, f"no table/figure label for {level}"


# ---------------------------------------------------------------------------
# Protocol v2: held-out evaluation start poses
# ---------------------------------------------------------------------------
def _env(split: str, **kw):
    """An env object with no Unity behind it (the controller boots lazily)."""
    from envs.procthor_env import ObjectNavConfig, ProcTHORObjectNavEnv

    return ProcTHORObjectNavEnv(
        {"objects": []}, ObjectNavConfig(pose_split=split, **kw), name="test",
    )


def _cells(n: int):
    return [{"x": float(i), "y": 0.9, "z": 0.0} for i in range(n)]


def test_holdout_is_off_by_default() -> None:
    """Committed results must stay reproducible: no silent protocol change."""
    assert config.POSE_HOLDOUT is False
    cells = _cells(50)
    assert _env("")._split_poses(cells) == cells


def test_train_and_eval_slices_partition_the_floor() -> None:
    cells = _cells(100)
    train = {c["x"] for c in _env("train")._split_poses(cells)}
    held = {c["x"] for c in _env("eval")._split_poses(cells)}
    assert not (train & held), "an eval start was also available to training"
    assert train | held == {c["x"] for c in cells}
    assert len(held) == 20                      # eval_pose_fraction 0.2


def test_split_does_not_move_with_the_training_seed() -> None:
    """The partition must be identical across baselines, seeds and rungs.

    It is drawn from a fixed constant, never the training seed -- otherwise two
    seeds of the same baseline would be evaluated on different floors and could
    not be averaged.
    """
    cells = _cells(200)
    first = _env("eval")._split_poses(cells)
    for _ in range(3):
        assert _env("eval")._split_poses(cells) == first
    # A different split seed must give a different partition (the knob works).
    other = _env("eval", pose_split_seed=1)._split_poses(cells)
    assert other != first


def test_split_survives_reordering_only_through_the_sorted_set() -> None:
    """Slices are positional, so the caller's deterministic sort is load-bearing."""
    cells = _cells(40)
    a = _env("eval")._split_poses(cells)
    b = _env("eval")._split_poses(list(cells))
    assert a == b


def test_bad_split_name_is_rejected() -> None:
    try:
        _env("holdout")._split_poses(_cells(10))
    except ValueError as exc:
        assert "pose_split" in str(exc)
    else:
        raise AssertionError("a typo'd split name must not silently pass")


def test_tiny_house_refuses_to_leave_training_with_nothing() -> None:
    try:
        _env("train", eval_pose_fraction=1.0)._split_poses(_cells(4))
    except ValueError as exc:
        assert "eval_pose_fraction" in str(exc)
    else:
        raise AssertionError("a fraction that empties training must raise")


# ---------------------------------------------------------------------------
# Pinned evaluation start poses
# ---------------------------------------------------------------------------
def _env_with_table(table: dict):
    import json as _json
    import tempfile
    from envs.procthor_env import ObjectNavConfig, ProcTHORObjectNavEnv

    fh = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    _json.dump(table, fh)
    fh.close()
    return ProcTHORObjectNavEnv(
        {"objects": []},
        ObjectNavConfig(oracle_path_table=fh.name), name="test",
    )


_TABLE = {"seeds": {
    "10000": {"start_position": {"x": 1.0, "y": 0.9, "z": 2.0},
              "start_rotation": 90.0, "legs": [1.5], "total": 1.5},
    # written before poses were pinned: position but no rotation
    "10001": {"start_position": {"x": 2.0, "y": 0.9, "z": 3.0},
              "legs": [2.0], "total": 2.0},
}}


def test_covered_eval_seed_is_pinned() -> None:
    pos, yaw = _env_with_table(_TABLE)._pinned_pose(10000)
    assert pos == {"x": 1.0, "y": 0.9, "z": 2.0}
    assert yaw == 90.0


def test_training_episodes_are_never_pinned() -> None:
    """Training passes no explicit seed, so it must keep sampling freely.

    Pinning training would collapse it onto 25 start poses and destroy the run.
    """
    assert _env_with_table(_TABLE)._pinned_pose(None) is None


def test_uncovered_seed_falls_back_to_sampling() -> None:
    assert _env_with_table(_TABLE)._pinned_pose(99999) is None


def test_table_without_rotation_is_treated_as_uncovered() -> None:
    """A pre-pinning table must degrade to the old behaviour, not half-apply.

    Teleporting to the right cell facing an arbitrary way would diverge from
    house A on step one, which is worse than not pinning at all.
    """
    assert _env_with_table(_TABLE)._pinned_pose(10001) is None


def test_legacy_flat_paths_mirror_pair0_exactly() -> None:
    """data/house_*.json must be byte-identical to pair0's files.

    generate_variants.py holds this invariant so every result committed before
    the multi-pair layout existed still reproduces from the paths it was
    produced with. prune_l3.py broke it once by rewriting only data/pairs/,
    leaving an UNPRUNED house at the flat path that looked authoritative.
    """
    import hashlib

    pairs = {"a.json": "house_a.json", "b_L1.json": "house_b.json",
             "b_L2.json": "house_b_L2.json", "b_L3.json": "house_b_L3.json"}
    for src, dst in pairs.items():
        a, b = config.pair_dir("pair0") / src, config.DATA_DIR / dst
        if not (a.exists() and b.exists()):
            continue                       # rung not generated in this checkout
        da = hashlib.sha256(a.read_bytes()).hexdigest()
        db = hashlib.sha256(b.read_bytes()).hexdigest()
        assert da == db, f"{dst} has drifted from pair0/{src}"


def test_every_committed_variant_is_verified() -> None:
    """No house may sit in the repo without a passing C1-C3 record."""
    import json as _json

    for i in range(config.GenerationConfig().n_pairs):
        vp = config.pair_dir(f"pair{i}") / "verification.json"
        if not vp.exists():
            continue
        rec = _json.loads(vp.read_text())
        assert rec.get("passed"), f"pair{i} verification.json says not passed"
        for level, entry in rec["levels"].items():
            assert entry["passed"], f"pair{i} {level} did not pass"


def main() -> None:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in tests:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL  {fn.__name__}: {type(exc).__name__}: {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
