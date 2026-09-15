"""Experiment tracker: canonical run-level records + rendered summary.

Requested by Vishwas (meeting 2026-08-12): one place that consolidates every
run with full provenance, so results never live only in scattered artifacts.

Files
-----
results/tracker/runs.csv    canonical store — one row per trained agent per
                            rung it was evaluated on (legacy sweep runs have
                            one rung, so one row)
results/tracker/houses.csv  per-house facts (house pair x rung), incl. how much
                            the image changed
results/tracker/summary.md  generated view — aggregates + full table
                            (never edit by hand; rerun `render`)
EXPERIMENT_TRACKER.md       column glossary + how-to (repo root)

Metric columns are ALWAYS ingested from the run's *_transfer_summary.csv —
numbers are never typed by hand.

Subcommands
-----------
  rebuild       rebuild runs.csv + houses.csv from EVERY committed result (use this)
  backfill      (re)ingest the legacy protocol-v1 runs only
  ingest-sweep  add all seed<N>/ runs of one sweep directory
  add           add a single run from one *_transfer_summary.csv
  render        rewrite summary.md from runs.csv

Typical post-sweep flow (after rsyncing results/sweeps/<name>/seed*/ back):
  python scripts/tracker.py ingest-sweep results/sweeps/ppo_aug \
      --prefix ppo_aug --baseline ppo_aug --date 2026-08-24 \
      --git-commit <sha> --slurm-job <jobid> \
      --recipe "SB3 PPO defaults + photometric jitter, 150k env steps"
  python scripts/tracker.py render
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import PROJECT_ROOT  # noqa: E402

TRACKER_DIR = PROJECT_ROOT / "results" / "tracker"
RUNS_CSV = TRACKER_DIR / "runs.csv"
SUMMARY_MD = TRACKER_DIR / "summary.md"

COLUMNS = [
    "experiment_id", "date", "baseline", "architecture_class", "cohort",
    "seed", "house_pair", "shift_level", "environment_parameters",
    "object_parameters", "task", "training_recipe", "train_steps",
    "eval_episodes", "eval_seed_base", "git_commit", "slurm_job",
    "A_success", "B_success", "relative_success_drop",
    "A_SPL", "B_SPL", "relative_SPL_drop",
    "A_episode_length", "B_episode_length", "episode_length_ratio",
    "status", "results_path", "notes",
]

ARCH_CLASS = {
    "ppo": "model-free on-policy",
    "ppo_aug": "model-free on-policy + photometric augmentation",
    "dreamerv3": "reconstruction world model",
    "tdmpc2": "decoder-free latent world model + planner",
}

# Shared context of every run so far: the single L1 pair built by
# envs/generate_variants.py (see data/variants_summary.md).
PAIR0 = dict(
    house_pair="pair0",
    shift_level="L1",
    environment_parameters=("procthor10k-train house 0; 1 room; B = wall/floor/"
                            "ceiling material remap + warm dimmed lights + "
                            "skybox swap (variant seed 1337)"),
    object_parameters="target=Fridge",
    task="objectnav",
)

# --- severity-ladder grid provenance -------------------------------------------
RUNG_DESC = {
    "L1": "wall/floor materials + lighting + skybox changed",
    "L2noT": "L1 + every object's appearance changed EXCEPT the target",
    "L2": "L1 + every object's appearance changed, target included when swappable",
    "L3": "L2 + {clutter} distractor objects",
}
BASE_RECIPE = {
    "ppo": "SB3 PPO defaults",
    "ppo_aug": "SB3 PPO defaults + photometric jitter (training only)",
    "dreamerv3": "DreamerV3 train_ratio=512",
    "tdmpc2": "TD-MPC2 upstream defaults",
}
PROTOCOL_V2 = "protocol v2 (held-out start poses, pinned eval poses, static scene)"
MIN_A = 0.5  # house-A success floor for relative-drop comparisons (rule fixed 2026-09-05)

# Which job trained each cell, and the repo state when it was submitted (last
# commit before the submission timestamp; recovered 2026-09-15 from the session
# transcript and git log). Cells not listed use the per-baseline default.
GRID_JOBS = {
    150_000: {"default": {"ppo": ("39573420", "28f0c5f"), "ppo_aug": ("39573421", "28f0c5f"),
                          "dreamerv3": ("39573422", "28f0c5f"), "tdmpc2": ("39573423", "28f0c5f")}},
    300_000: {
        "default": {"ppo": ("39720495", "ad21a37"), "ppo_aug": ("39720496", "ad21a37"),
                    "dreamerv3": ("39720497+39945496", "ad21a37"),
                    "tdmpc2": ("39720498", "ad21a37")},
        ("dreamerv3", "pair1", 0): ("39666403", "b95a196"),
        ("dreamerv3", "pair2", 0): ("39666403", "b95a196"),
        ("dreamerv3", "pair2", 3): ("39666403", "b95a196"),
        ("dreamerv3", "pair3", 1): ("39666403", "b95a196"),
        ("dreamerv3", "pair4", 3): ("39666403", "b95a196"),
        ("dreamerv3", "pair1", 4): ("39945496_9", "720cb4d"),
        ("tdmpc2", "pair0", 3): ("40063012_3", "3e4cede"),
        ("tdmpc2", "pair4", 0): ("40063012_20", "3e4cede"),
        ("tdmpc2", "pair3", 1): ("40086264_16", "973687d"),
    },
}
GRID_JOB_NOTES = {
    ("dreamerv3", "pair1", 0): "diagnostic run at 300k (job 39666403), folded into the grid; saved model later deleted by mistake",
    ("dreamerv3", "pair2", 0): "diagnostic run at 300k (job 39666403), folded into the grid; saved model later deleted by mistake",
    ("dreamerv3", "pair2", 3): "diagnostic run at 300k (job 39666403), folded into the grid; saved model later deleted by mistake",
    ("dreamerv3", "pair3", 1): "diagnostic run at 300k (job 39666403), folded into the grid; saved model later deleted by mistake",
    ("dreamerv3", "pair4", 3): "diagnostic run at 300k (job 39666403), folded into the grid; saved model later deleted by mistake",
    ("tdmpc2", "pair3", 1): "earlier attempts 39720498_16 (CUDA fault), 40063012_16 and 40083026 (truncated checkpoint) failed; scratch cleared before this run",
    ("tdmpc2", "pair0", 3): "first attempt 39720498_3 hit a CUDA illegal-memory fault",
    ("tdmpc2", "pair4", 0): "first attempt 39720498_20 hit a CUDA illegal-memory fault",
}
EVALONLY_JOBS = {"ppo": "40083091", "ppo_aug": "40083092", "dreamerv3": "40083093", "tdmpc2": "40083094"}
EVALONLY_COMMIT = "1eaafc6"
RERUN_JOBS = {  # (baseline, pair, seed) -> slurm job; all submitted at 973687d
    ("dreamerv3", "pair1", 0): "40086262_5", ("dreamerv3", "pair2", 0): "40086262_10",
    ("dreamerv3", "pair2", 3): "40086262_13", ("dreamerv3", "pair3", 1): "40086262_16",
    ("dreamerv3", "pair4", 3): "40086262_23", ("dreamerv3", "pair1", 4): "40086263_9",
    ("tdmpc2", "pair2", 0): "40086264_10",
}
RERUN_COMMIT = "973687d"


def pair_context(pair: str, level: str) -> Dict[str, str]:
    """environment/object description of one house pair at one rung, from data/pairs."""
    import json
    d = PROJECT_ROOT / "data" / "pairs" / pair
    idx = {p["pair_id"]: p for p in json.loads((PROJECT_ROOT / "data" / "pairs_index.json").read_text())["pairs"]}[pair]
    cells = json.loads((d / "verification.json").read_text())["reference"]["n_reachable"]
    swappable = bool(json.loads((d / "safe_assets.json").read_text()).get("target_swappable"))
    clutter = json.loads((d / "l3_prune.json").read_text())["n_kept"]
    return dict(
        house_pair=pair, shift_level=level, task="objectnav",
        environment_parameters=(f"procthor-10k train house {idx['house_index']}; {idx['n_rooms']} room(s); "
                                f"{cells} reachable cells; {RUNG_DESC[level].format(clutter=clutter)}; "
                                f"variant seed {idx['variant_seed']}"),
        object_parameters=f"target={idx['target_object_type']}; target swappable at L2={'yes' if swappable else 'no'}",
    )


def first_commit_date(path: Path) -> str:
    """Date the file first entered the repo: an upper bound on when the run finished."""
    out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ad", "--date=short", "--", str(path)],
                         capture_output=True, text=True, cwd=PROJECT_ROOT).stdout.split()
    if not out:
        raise RuntimeError(f"{path} is not committed; commit results before ingesting them")
    return out[-1]


# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------
def read_metrics(summary_csv: Path, level: str = "L1") -> Dict[str, float]:
    """Pull A/B metrics from a <prefix>_transfer_summary.csv (never hand-typed).

    Summaries written after the severity ladder landed carry one row per rung
    plus a ``level`` column, so ``level`` picks which rung plays the role of B.
    Older summaries have exactly two rows and no ``level`` column; they are read
    the way they always were, so every committed result still ingests
    identically.
    """
    df = pd.read_csv(summary_csv)
    if "level" in df.columns:
        rows = {str(r["level"]): r for _, r in df.iterrows()}
        if level not in rows:
            raise KeyError(
                f"{summary_csv} has no level '{level}' "
                f"(present: {sorted(rows)})"
            )
        a, b = rows["A"], rows[level]
    else:
        by = {("A" if str(r["variant"]).startswith("A") else "B"): r
              for _, r in df.iterrows()}
        a, b = by["A"], by["B"]
    a_succ, b_succ = float(a["success_rate"]), float(b["success_rate"])
    a_spl, b_spl = float(a["spl"]), float(b["spl"])
    a_len, b_len = float(a["mean_episode_length"]), float(b["mean_episode_length"])
    return dict(
        A_success=a_succ, B_success=b_succ,
        relative_success_drop=(a_succ - b_succ) / a_succ if a_succ > 0 else float("nan"),
        A_SPL=a_spl, B_SPL=b_spl,
        relative_SPL_drop=(a_spl - b_spl) / a_spl if a_spl > 0 else float("nan"),
        A_episode_length=a_len, B_episode_length=b_len,
        episode_length_ratio=b_len / a_len if a_len > 0 else float("nan"),
        eval_episodes=int(a["episodes"]),
    )


def load_runs() -> pd.DataFrame:
    if RUNS_CSV.exists():
        return pd.read_csv(RUNS_CSV, dtype={"seed": "Int64"})
    return pd.DataFrame(columns=COLUMNS)


def upsert(df: pd.DataFrame, row: Dict[str, Any]) -> pd.DataFrame:
    """Insert or replace by experiment_id (idempotent re-ingestion).

    Re-ingesting the SAME experiment is the point. Silently replacing a
    DIFFERENT one that happens to collide is not: on 2026-09-05 the first grid
    ingest generated `ppo_pair0_L1_s0` -- byte-identical to the legacy sweep row
    of the same baseline/pair/rung/seed -- and quietly overwrote 15 committed
    results before anyone looked. Same cell, different PROTOCOL, different
    experiment. A cross-cohort collision now raises.
    """
    clash = df[(df["experiment_id"] == row["experiment_id"])
               & (df["cohort"] != row["cohort"])] if not df.empty else df
    if len(clash):
        raise ValueError(
            f"experiment_id {row['experiment_id']!r} already exists in cohort "
            f"{clash.iloc[0]['cohort']!r} and this row is cohort "
            f"{row['cohort']!r}. Two different experiments cannot share an id -- "
            "give one a recipe_tag (e.g. the protocol version)."
        )
    df = df[df["experiment_id"] != row["experiment_id"]]
    if df.empty:
        return pd.DataFrame([row])
    return pd.concat([df, pd.DataFrame([row])], ignore_index=True)


def save_runs(df: pd.DataFrame) -> None:
    TRACKER_DIR.mkdir(parents=True, exist_ok=True)
    df = df.reindex(columns=COLUMNS).sort_values(
        ["date", "baseline", "cohort", "seed"]).reset_index(drop=True)
    df.to_csv(RUNS_CSV, index=False)
    print(f"wrote {RUNS_CSV} ({len(df)} runs)")


def make_row(*, summary_csv: Path, baseline: str, seed: int, date: str,
             git_commit: str, slurm_job: str, recipe: str, cohort: str,
             results_path: str, train_steps: int = 150_000,
             eval_seed_base: int = 10_000, id_suffix: str = "",
             status: str = "complete", notes: str = "",
             recipe_tag: str = "", **pair_ctx: Any) -> Dict[str, Any]:
    ctx = {**PAIR0, **pair_ctx}
    tag = f"-{recipe_tag}" if recipe_tag else ""
    suffix = f"_{id_suffix}" if id_suffix else ""
    return dict(
        experiment_id=f"{baseline}{tag}_{ctx['house_pair']}_{ctx['shift_level']}_s{seed}{suffix}",
        date=date, baseline=baseline,
        architecture_class=ARCH_CLASS.get(baseline, "?"), cohort=cohort,
        seed=seed, training_recipe=recipe, train_steps=train_steps,
        eval_seed_base=eval_seed_base, git_commit=git_commit,
        slurm_job=slurm_job, status=status, results_path=results_path,
        notes=notes, **ctx,
        # The rung this row measures. Legacy two-row summaries have no `level`
        # column and read_metrics ignores it; ladder summaries carry four rungs
        # and this is what selects the right one. PAIR0's default is "L1", which
        # is also read_metrics' default, so every pre-existing caller is
        # unchanged.
        **read_metrics(summary_csv, ctx["shift_level"]),
    )


def ingest_sweep(df: pd.DataFrame, sweep_dir: Path, prefix: str,
                 **meta: Any) -> pd.DataFrame:
    # Resolve first: results_path below is stored relative to PROJECT_ROOT, and
    # relative_to() fails on a CLI-supplied relative path like results/sweeps/x.
    sweep_dir = sweep_dir.resolve()
    seed_dirs = sorted(sweep_dir.glob("seed*"))
    if not seed_dirs:
        raise FileNotFoundError(f"no seed*/ dirs under {sweep_dir}")
    for sd in seed_dirs:
        seed = int(sd.name.replace("seed", ""))
        row = make_row(
            summary_csv=sd / f"{prefix}_transfer_summary.csv", seed=seed,
            results_path=str(sd.relative_to(PROJECT_ROOT)), **meta,
        )
        df = upsert(df, row)
        print(f"  ingested {row['experiment_id']}")
    return df


def ingest_grid(df: pd.DataFrame, grid_dir: Path, **meta: Any) -> pd.DataFrame:
    """Ingest the severity-ladder grid: one row per (run, RUNG).

    Layout is `results/grid/<baseline>/<pair>_seed<N>/<baseline>_transfer_summary.csv`,
    and each summary carries four rungs. A run is one trained agent; a ROW is
    that agent measured against one rung, because `shift_level` is a column in
    this schema and a run that produced four measurements is four observations.

    Every rung is scored against the SAME house-A reference from its own run, so
    the A_* columns repeat across a run's four rows by construction -- that is
    the pairing, not duplication.
    """
    grid_dir = grid_dir.resolve()
    cells = sorted(grid_dir.glob("*/*_seed*"))
    if not cells:
        raise FileNotFoundError(f"no <baseline>/<pair>_seed<N>/ cells under {grid_dir}")
    n = 0
    for cell in cells:
        baseline = cell.parent.name
        pair, seed = cell.name.split("_seed")
        summary = cell / f"{baseline}_transfer_summary.csv"
        if not summary.exists():
            print(f"  SKIP {cell.name}: no summary (run may have failed)")
            continue
        levels = set(pd.read_csv(summary)["level"].astype(str)) - {"A"}
        for level in sorted(levels):
            row = make_row(
                summary_csv=summary, baseline=baseline, seed=int(seed),
                house_pair=pair, shift_level=level,
                results_path=str(cell.relative_to(PROJECT_ROOT)),
                **{k: v for k, v in meta.items() if k != "baseline"},
            )
            df = upsert(df, row)
            n += 1
    print(f"  ingested {n} (run, rung) rows from {len(cells)} cells")
    return df


def ingest_ladder(df: pd.DataFrame, budget: int) -> pd.DataFrame:
    """Severity-ladder grid at one budget: one row per (original agent, rung).

    Tree `results/grid` (150k) or `results/grid_<budget>`; rungs L1/L2/L3 from the
    committed grid table. At 300k the L2noT rung is added per agent from the table
    that holds BOTH L2noT and L2 for that agent in one evaluation (the same
    `source_for` the target test uses), so the tracker and the paper can never
    disagree. The 7 cells whose saved models were gone get their L2noT from a
    retrained agent: those go in cohort rerun_300k, never in the grid cohort.
    """
    tree = "grid" if budget == 150_000 else f"grid_{budget}"
    tag = "v2" if budget == 150_000 else f"v2-{budget // 1000}k"
    cohort = f"grid_{budget // 1000}k"
    jobs = GRID_JOBS[budget]
    cells = sorted((PROJECT_ROOT / "results" / tree).glob("*/*_seed*"))
    if len(cells) != 100:
        raise ValueError(f"expected 100 cells under results/{tree}, found {len(cells)}")
    n = 0
    for cell in cells:
        baseline = cell.parent.name
        pair, seed_s = cell.name.split("_seed")
        seed = int(seed_s)
        summary = cell / f"{baseline}_transfer_summary.csv"
        job, commit = jobs.get((baseline, pair, seed), jobs["default"][baseline])
        base_note = GRID_JOB_NOTES.get((baseline, pair, seed), "") if budget == 300_000 else ""
        recipe = f"{BASE_RECIPE[baseline]}; {PROTOCOL_V2}; {budget // 1000}k env steps"
        for level in ("L1", "L2", "L3"):
            row = make_row(summary_csv=summary, baseline=baseline, seed=seed, cohort=cohort,
                           date=first_commit_date(summary), git_commit=commit, slurm_job=job,
                           recipe=recipe, recipe_tag=tag, train_steps=budget,
                           results_path=str(cell.relative_to(PROJECT_ROOT)),
                           **pair_context(pair, level))
            row["notes"] = _competency_note(row, base_note)
            df = upsert(df, row); n += 1
        if budget != 300_000:
            continue
        # L2noT for the ORIGINAL agent, when its model still existed
        if (baseline, pair, seed) in RERUN_JOBS:
            continue
        src = _l2not_source(baseline, cell.name)
        from_evalonly = "evalonly_300000" in str(src)
        row = make_row(summary_csv=src, baseline=baseline, seed=seed, cohort=cohort,
                       date=first_commit_date(src),
                       git_commit=EVALONLY_COMMIT if from_evalonly else commit,
                       slurm_job=EVALONLY_JOBS[baseline] if from_evalonly else job,
                       recipe=recipe, recipe_tag=tag, train_steps=budget,
                       results_path=str(src.parent.relative_to(PROJECT_ROOT)),
                       **pair_context(pair, "L2noT"))
        extra = ("L2noT measured later from the same saved model (eval-only sweep); "
                 "A_* in this row come from that same evaluation") if from_evalonly else \
                "L2noT measured in the run's own evaluation"
        row["notes"] = _competency_note(row, "; ".join(x for x in (base_note, extra) if x))
        df = upsert(df, row); n += 1
    print(f"  {cohort}: {n} (agent, rung) rows from {len(cells)} cells")
    return df


def ingest_reruns(df: pd.DataFrame) -> pd.DataFrame:
    """Retrained agents (saved model was gone). Never the headline; all five rungs."""
    n = 0
    for (baseline, pair, seed), job in sorted(RERUN_JOBS.items()):
        cell = PROJECT_ROOT / "results" / "rerun_300000" / baseline / f"{pair}_seed{seed}"
        summary = cell / f"{baseline}_transfer_summary.csv"
        recipe = f"{BASE_RECIPE[baseline]}; {PROTOCOL_V2}; 300k env steps"
        for level in ("L1", "L2noT", "L2", "L3"):
            row = make_row(summary_csv=summary, baseline=baseline, seed=seed, cohort="rerun_300k",
                           date=first_commit_date(summary), git_commit=RERUN_COMMIT, slurm_job=job,
                           recipe=recipe, recipe_tag="v2-300k", id_suffix="rerun", train_steps=300_000,
                           results_path=str(cell.relative_to(PROJECT_ROOT)),
                           **pair_context(pair, level))
            row["notes"] = _competency_note(
                row, "retrain of a cell whose saved model was deleted; same seed, different agent; "
                     "the original in grid_300k stays the headline; used for this cell's L2noT "
                     "comparison and as rerun-variance evidence")
            df = upsert(df, row); n += 1
    print(f"  rerun_300k: {n} (agent, rung) rows from {len(RERUN_JOBS)} retrained agents")
    return df


def _l2not_source(baseline: str, cell: str) -> Path:
    sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
    from test_target_effect import source_for
    return source_for(baseline, cell)


def _competency_note(row: Dict[str, Any], note: str) -> str:
    if row["A_success"] < MIN_A:
        flag = (f"house-A success {row['A_success']:.2f} < {MIN_A}: left out of relative-drop "
                "comparisons (rule fixed 2026-09-05)")
        note = f"{note}; {flag}" if note else flag
    return note


def write_houses() -> None:
    """Per-house facts (one row per pair x rung): what the agent saw, not what it did."""
    import json
    shift = {(r["pair"], r["level"]): r for r in
             json.loads((PROJECT_ROOT / "results" / "tables" / "visual_shift.json").read_text())}
    rows = []
    for i in range(5):
        pair = f"pair{i}"
        d = PROJECT_ROOT / "data" / "pairs" / pair
        ver = json.loads((d / "verification.json").read_text())
        idx = {p["pair_id"]: p for p in json.loads((PROJECT_ROOT / "data" / "pairs_index.json").read_text())["pairs"]}[pair]
        for level in ("L1", "L2noT", "L2", "L3"):
            v = ver["levels"].get(level)
            sh = shift[(pair, level)]
            rows.append(dict(
                house_pair=pair, shift_level=level, house_index=idx["house_index"],
                target=idx["target_object_type"],
                target_swappable=bool(json.loads((d / "safe_assets.json").read_text()).get("target_swappable")),
                reachable_cells=ver["reference"]["n_reachable"],
                clutter_kept=json.loads((d / "l3_prune.json").read_text())["n_kept"] if level == "L3" else 0,
                gate_C1_C3_passed=(v["passed"] if v else "not recorded in verification.json"),
                max_shortest_path_delta_m=(v["max_shortest_path_delta"] if v else ""),
                image_mean_pixel_diff=sh["mean_abs_diff"],
                image_frac_pixels_changed=sh["frac_pixels_changed"],
                image_hist_l1=sh["hist_l1"],
            ))
    out = TRACKER_DIR / "houses.csv"
    pd.DataFrame(rows).to_csv(out, index=False)
    print(f"wrote {out} ({len(rows)} house x rung rows)")


# ---------------------------------------------------------------------------
# Historical backfill — provenance from the committed artifacts + session log.
# git_commit values for cluster runs are the documented repo state at launch;
# all commits in each range are code-identical for the training/eval pipeline
# (intervening commits added results/locks only). See EXPERIMENT_TRACKER.md.
# ---------------------------------------------------------------------------
def cmd_backfill(_: argparse.Namespace) -> None:
    df = load_runs()
    r = PROJECT_ROOT

    df = ingest_sweep(df, r / "results/sweeps/ppo", "ppo",
                      baseline="ppo", cohort="sweep", date="2026-07-30",
                      git_commit="668268e", slurm_job="37923582",
                      recipe="SB3 PPO defaults, 150k env steps")
    df = ingest_sweep(df, r / "results/sweeps/dreamerv3_512", "dreamerv3",
                      baseline="dreamerv3", cohort="sweep", date="2026-07-31",
                      git_commit="596ebb4", slurm_job="37948923",
                      recipe="DreamerV3 train_ratio=512, 150k env steps",
                      recipe_tag="r512")
    df = ingest_sweep(df, r / "results/sweeps/tdmpc2", "tdmpc2",
                      baseline="tdmpc2", cohort="sweep", date="2026-08-01",
                      git_commit="d78f62a", slurm_job="37982716+37997516",
                      recipe="TD-MPC2 upstream defaults, 150k env steps")
    # Originally added with `ingest-sweep` on 2026-08-24 and never listed here, so
    # a rebuild silently dropped it (caught by the 2026-09-15 rebuild check).
    # Metadata copied verbatim from that ingest.
    df = ingest_sweep(df, r / "results/sweeps/ppo_aug", "ppo_aug",
                      baseline="ppo_aug", cohort="sweep", date="2026-08-24",
                      git_commit="8177846", slurm_job="38800341,38801317,38806927",
                      recipe="SB3 PPO defaults + train-time photometric jitter "
                             "(0.4/0.4/0.4, hue 36deg, per-episode), 150k env steps",
                      notes="augmentation/domain-randomization class; no detectable "
                            "transfer benefit vs ppo (exact permutation p=0.68); seeds "
                            "1,2,3 needed reruns after shared-node CloudRendering failures")

    singles = [
        dict(summary_csv=r / "results/tables/ppo_transfer_summary.csv",
             baseline="ppo", seed=0, date="2026-07-14",
             git_commit="8e6c7f3", slurm_job="local (M4 Air)", cohort="main",
             recipe="SB3 PPO defaults, 150k env steps", id_suffix="main",
             results_path="results/tables",
             notes="original n=1 run; LUCKY transfer seed (8.3% drop) — "
                   "superseded by the 5-seed sweep (32.4% +/- 29.6)"),
        dict(summary_csv=r / "results/tables/dreamerv3_transfer_summary.csv",
             baseline="dreamerv3", seed=0, date="2026-07-30",
             git_commit="668268e", slurm_job="37923581", cohort="main",
             recipe="DreamerV3 train_ratio=512, 150k env steps",
             recipe_tag="r512", id_suffix="parity",
             results_path="results/tables",
             notes="ratio-512 parity run (fairness-rule gate); B slightly "
                   "above A, within the sweep's seed range"),
        dict(summary_csv=r / "results/tables/tdmpc2_transfer_summary.csv",
             baseline="tdmpc2", seed=0, date="2026-08-01",
             git_commit="d78f62a", slurm_job="37982715+37997515", cohort="main",
             recipe="TD-MPC2 upstream defaults, 150k env steps",
             id_suffix="main", results_path="results/tables",
             notes="main-seed run; resumed at ~140k after buffer-wraparound "
                   "fix (VENDOR.md patch #10)"),
        dict(summary_csv=r / "results/archive/dreamerv3_ratio128/dreamerv3_transfer_summary.csv",
             baseline="dreamerv3", seed=0, date="2026-07-16",
             git_commit="pre-git (code later committed at 9fe95b6)",
             slurm_job="local (M4 Air)", cohort="archive",
             recipe="DreamerV3 train_ratio=128 — UNDERTRAINED (1/4 of "
                    "published recipe)", recipe_tag="r128",
             id_suffix="archived", status="superseded",
             results_path="results/archive/dreamerv3_ratio128",
             notes="undertraining artifact (18.2% drop reversed at ratio "
                   "512) — the run that motivated the fairness rule"),
        dict(summary_csv=r / "results/archive/dreamerv3_ratio32_collapsed/dreamerv3_transfer_summary.csv",
             baseline="dreamerv3", seed=0, date="2026-07-14",
             git_commit="pre-git (code later committed at 9fe95b6)",
             slurm_job="local (M4 Air)", cohort="archive",
             recipe="DreamerV3 train_ratio=32 — ACTOR COLLAPSE",
             recipe_tag="r32", id_suffix="collapsed", status="invalid",
             results_path="results/archive/dreamerv3_ratio32_collapsed",
             notes="policy obs-blind (zero actor grad); A==B bit-identical; "
                   "NOT a transfer data point"),
    ]
    for s in singles:
        df = upsert(df, make_row(**s))
        print(f"  ingested single run ({s['baseline']} {s.get('id_suffix','')})")
    save_runs(df)


# ---------------------------------------------------------------------------
# CLI: ingest-sweep / add
# ---------------------------------------------------------------------------
def cmd_rebuild(_: argparse.Namespace) -> None:
    """Rebuild runs.csv from every committed artifact, from scratch.

    Starts empty (so cohort renames cannot trip the collision guard), ingests the
    legacy runs exactly as `backfill` does, then both ladder budgets and the
    reruns, then writes houses.csv. Idempotent.
    """
    global load_runs
    original = load_runs
    load_runs = lambda: pd.DataFrame(columns=COLUMNS)  # noqa: E731  start from nothing
    try:
        cmd_backfill(_)                    # legacy sweep/main/archive rows
    finally:
        load_runs = original
    df = pd.read_csv(RUNS_CSV, dtype={"seed": "Int64"})
    df = ingest_ladder(df, 150_000)
    df = ingest_ladder(df, 300_000)
    df = ingest_reruns(df)
    save_runs(df)
    write_houses()


def cmd_ingest_grid(a: argparse.Namespace) -> None:
    df = load_runs()
    # recipe_tag "v2" keeps grid ids distinct from the protocol-v1 sweep rows
    # of the same baseline/pair/rung/seed. Same cell, different protocol
    # (held-out starts, pinned poses, static scene), different experiment.
    df = ingest_grid(df, Path(a.grid_dir), cohort="grid", date=a.date,
                     git_commit=a.git_commit, slurm_job=a.slurm_job,
                     recipe=a.recipe, recipe_tag=a.recipe_tag, notes=a.notes)
    save_runs(df)


def cmd_ingest_sweep(a: argparse.Namespace) -> None:
    df = ingest_sweep(load_runs(), Path(a.sweep_dir), a.prefix,
                      baseline=a.baseline, cohort="sweep", date=a.date,
                      git_commit=a.git_commit, slurm_job=a.slurm_job,
                      recipe=a.recipe, recipe_tag=a.recipe_tag,
                      house_pair=a.house_pair, shift_level=a.shift_level,
                      notes=a.notes)
    save_runs(df)


def cmd_add(a: argparse.Namespace) -> None:
    df = upsert(load_runs(), make_row(
        summary_csv=Path(a.summary), baseline=a.baseline, seed=a.seed,
        date=a.date, git_commit=a.git_commit, slurm_job=a.slurm_job,
        recipe=a.recipe, recipe_tag=a.recipe_tag, cohort=a.cohort,
        id_suffix=a.id_suffix, results_path=str(Path(a.summary).parent),
        house_pair=a.house_pair, shift_level=a.shift_level, notes=a.notes))
    save_runs(df)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def _pm(vals: pd.Series, fmt: str = "{:.3f}") -> str:
    m, s = vals.mean(), vals.std(ddof=1) if len(vals) > 1 else 0.0
    return f"{fmt.format(m)} ± {fmt.format(s)}"


def _pm_pct(vals: pd.Series) -> str:
    m = vals.mean() * 100
    s = (vals.std(ddof=1) if len(vals) > 1 else 0.0) * 100
    return f"{m:.1f}% ± {s:.1f}"


def cmd_render(_: argparse.Namespace) -> None:
    df = load_runs()
    if df.empty:
        sys.exit("runs.csv is empty — run `backfill` or `ingest-sweep` first")
    try:
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True,
                              cwd=PROJECT_ROOT).stdout.strip()
    except OSError:
        head = "?"

    lines = [
        "# Experiment tracker — summary",
        "",
        f"_Generated by `python scripts/tracker.py render` at "
        f"{datetime.now():%Y-%m-%d %H:%M} (repo @ `{head}`). Do not edit by "
        f"hand — the canonical store is [`runs.csv`](runs.csv); column "
        f"glossary in [`EXPERIMENT_TRACKER.md`](../../EXPERIMENT_TRACKER.md)._",
        "",
        f"**{len(df)} runs** — cohorts: "
        + ", ".join(f"{k} ({v})" for k, v in df["cohort"].value_counts().items())
        + ".",
        "",
        "## Legacy single-house sweep (protocol v1, pair0 L1 only; superseded by the grids)",
        "",
        "Relative drops are computed per seed, then averaged (matches the "
        "committed sweep aggregates).",
        "",
    ]
    agg_rows = []
    sweeps = df[df["cohort"] == "sweep"]
    for (baseline, recipe, pair, level), g in sweeps.groupby(
            ["baseline", "training_recipe", "house_pair", "shift_level"]):
        agg_rows.append({
            "baseline": baseline, "pair": pair, "shift": level,
            "seeds": f"n={len(g)}",
            "A success": _pm(g["A_success"]), "B success": _pm(g["B_success"]),
            "rel. success drop": _pm_pct(g["relative_success_drop"]),
            "A SPL": _pm(g["A_SPL"]), "B SPL": _pm(g["B_SPL"]),
            "rel. SPL drop": _pm_pct(g["relative_SPL_drop"]),
            "ep-len ratio (B/A)": _pm(g["episode_length_ratio"], "{:.1f}"),
        })
    order = {"ppo": 0, "ppo_aug": 1, "dreamerv3": 2, "tdmpc2": 3}
    agg_rows.sort(key=lambda r: order.get(r["baseline"], 9))
    lines += [pd.DataFrame(agg_rows).to_markdown(index=False), ""]

    for cohort, title in (("grid_300k", "Severity-ladder grid, 300k env steps (HEADLINE)"),
                          ("grid_150k", "Severity-ladder grid, 150k env steps (appendix)")):
        g = df[df["cohort"] == cohort]
        if g.empty:
            continue
        lines += [f"## {title}", "",
                  "One row per trained agent per rung. `success` columns use every agent; "
                  f"`share of A lost` uses agents with house-A success ≥ {MIN_A} (count shown). "
                  "L2noT is deliberately NOT pooled here: for 7 cells it was measured on a retrained "
                  "agent (`rerun_300k`), so an L2noT row would average different agents than the rows "
                  "beside it. Its rows are in `runs.csv`; its analysis, each agent against itself, is "
                  "`results/tables/target_effect_tests.md`.", ""]
        agg = []
        for (b_, lvl), x in g[g["shift_level"] != "L2noT"].groupby(["baseline", "shift_level"]):
            ok = x[x["A_success"] >= MIN_A]
            agg.append({"agent": b_, "rung": lvl, "agents": len(x),
                        "A success": f"{x['A_success'].mean():.3f}",
                        "rung success": f"{x['B_success'].mean():.3f}",
                        "share of A lost": f"{100 * ok['relative_success_drop'].mean():.1f}% (n={len(ok)})",
                        "SPL share lost": f"{100 * ok['relative_SPL_drop'].mean():.1f}%"})
        rung_order = {"L1": 0, "L2noT": 1, "L2": 2, "L3": 3}
        agg.sort(key=lambda r: (order.get(r["agent"], 9), rung_order.get(r["rung"], 9)))
        lines += [pd.DataFrame(agg).to_markdown(index=False), ""]

    rr = df[df["cohort"] == "rerun_300k"]
    if not rr.empty:
        lines += ["## Retrained agents (`rerun_300k`) — never the headline", "",
                  "Same seed as a grid cell whose saved model was deleted; a different agent. Compare "
                  "with the original's row of the same id minus `_rerun`.", ""]
        view_r = rr.pivot_table(index=["baseline", "house_pair", "seed"], columns="shift_level",
                                values="B_success").reset_index()
        view_r.insert(3, "A", rr.groupby(["baseline", "house_pair", "seed"])["A_success"].first().values)
        lines += [view_r.round(2).to_markdown(index=False), ""]

    houses = TRACKER_DIR / "houses.csv"
    if houses.exists():
        lines += ["## Houses (`houses.csv`) — what the agents saw, not what they did", "",
                  pd.read_csv(houses).to_markdown(index=False), ""]

    lines += ["## All runs", ""]
    view = df.copy()
    for col in ("A_success", "B_success", "A_SPL", "B_SPL"):
        view[col] = view[col].map("{:.3f}".format)
    for col in ("relative_success_drop", "relative_SPL_drop"):
        view[col] = (view[col] * 100).map("{:.1f}%".format)
    view["episode_length_ratio"] = view["episode_length_ratio"].map("{:.1f}x".format)
    cols = ["experiment_id", "date", "cohort", "seed", "A_success", "B_success",
            "relative_success_drop", "A_SPL", "B_SPL", "relative_SPL_drop",
            "episode_length_ratio", "status", "git_commit", "slurm_job"]
    lines += [view[cols].to_markdown(index=False), "",
              "_Full provenance (recipes, env/object parameters, notes, result "
              "paths) lives in `runs.csv`._", ""]
    SUMMARY_MD.write_text("\n".join(lines))
    print(f"wrote {SUMMARY_MD}")


# ---------------------------------------------------------------------------
def main() -> None:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("backfill", help="(re)ingest all historical committed results")

    s = sub.add_parser("ingest-sweep", help="ingest every seed<N>/ of a sweep dir")
    s.add_argument("sweep_dir")
    s.add_argument("--prefix", required=True, help="table filename prefix, e.g. ppo_aug")
    s.add_argument("--baseline", required=True)
    s.add_argument("--date", required=True)
    s.add_argument("--git-commit", required=True)
    s.add_argument("--slurm-job", required=True)
    s.add_argument("--recipe", required=True)
    s.add_argument("--recipe-tag", default="")
    s.add_argument("--house-pair", default=PAIR0["house_pair"])
    s.add_argument("--shift-level", default=PAIR0["shift_level"])
    s.add_argument("--notes", default="")

    a = sub.add_parser("add", help="add one run from a *_transfer_summary.csv")
    a.add_argument("--summary", required=True)
    a.add_argument("--baseline", required=True)
    a.add_argument("--seed", type=int, required=True)
    a.add_argument("--date", required=True)
    a.add_argument("--git-commit", required=True)
    a.add_argument("--slurm-job", default="")
    a.add_argument("--recipe", required=True)
    a.add_argument("--recipe-tag", default="")
    a.add_argument("--cohort", default="main", choices=("sweep", "main", "archive"))
    a.add_argument("--id-suffix", default="")
    a.add_argument("--house-pair", default=PAIR0["house_pair"])
    a.add_argument("--shift-level", default=PAIR0["shift_level"])
    a.add_argument("--notes", default="")

    g = sub.add_parser("ingest-grid",
                       help="ingest results/grid: one row per (run, rung)")
    g.add_argument("grid_dir")
    g.add_argument("--date", required=True)
    g.add_argument("--git-commit", required=True)
    g.add_argument("--slurm-job", default="")
    g.add_argument("--recipe", default="protocol v2: held-out starts, pinned "
                                       "eval poses, static scene; 150k env steps")
    g.add_argument("--recipe-tag", default="v2",
                   help="distinguishes these ids from earlier protocols")
    g.add_argument("--notes", default="")

    sub.add_parser("rebuild", help="rebuild runs.csv + houses.csv from every committed result")
    sub.add_parser("render", help="rewrite summary.md from runs.csv")

    args = p.parse_args()
    {"backfill": cmd_backfill, "ingest-sweep": cmd_ingest_sweep,
     "ingest-grid": cmd_ingest_grid, "add": cmd_add, "rebuild": cmd_rebuild,
     "render": cmd_render}[args.cmd](args)


if __name__ == "__main__":
    main()
