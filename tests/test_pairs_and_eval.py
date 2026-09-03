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
