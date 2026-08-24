"""Experiment tracker: canonical run-level records + rendered summary.

Requested by Vishwas (meeting 2026-08-12): one place that consolidates every
run with full provenance, so results never live only in scattered artifacts.

Files
-----
results/tracker/runs.csv    canonical store — ONE ROW PER TRAINING RUN
                            (a training run = one baseline trained with one
                            training seed on one house pair at one shift
                            level; its paired A/B eval fills the metrics)
results/tracker/summary.md  generated view — aggregates + full table
                            (never edit by hand; rerun `render`)
EXPERIMENT_TRACKER.md       column glossary + how-to (repo root)

Metric columns are ALWAYS ingested from the run's *_transfer_summary.csv —
numbers are never typed by hand.

Subcommands
-----------
  backfill      (re)ingest every historical committed result (idempotent)
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


# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------
def read_metrics(summary_csv: Path) -> Dict[str, float]:
    """Pull A/B metrics from a <prefix>_transfer_summary.csv (never hand-typed)."""
    df = pd.read_csv(summary_csv)
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
    """Insert or replace by experiment_id (idempotent re-ingestion)."""
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
        notes=notes, **ctx, **read_metrics(summary_csv),
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
        "## Aggregates (mean ± std over training seeds; `sweep` cohort only)",
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

    sub.add_parser("render", help="rewrite summary.md from runs.csv")

    args = p.parse_args()
    {"backfill": cmd_backfill, "ingest-sweep": cmd_ingest_sweep,
     "add": cmd_add, "render": cmd_render}[args.cmd](args)


if __name__ == "__main__":
    main()
