"""Paper tables from the original ladder, generated -- never transcribed.

Every number in the paper comes from here, so a table can be regenerated from
the committed CSVs and can never drift from them. For each budget:

  results/tables/grid_main_<budget>.md     main-body tables, pooled over houses
  results/tables/grid_by_pair_<budget>.md  appendix: every house, every agent type

Rules the tables follow:
  * Success RATES and DROPS in success rate, in percentage points. Never "loss"
    or "share of success lost" (Vishwas found it confusing, 2026-09-29); a
    relative drop appears only in brackets.
  * Every pooled number carries a 95% CI (stratified bootstrap, from
    `scripts/robust_stats.py`, so the two files can never disagree) AND the
    range of the per-house means. PPO's L1 drop runs from 6 to 88 points across
    the five houses, so a pooled mean alone would describe no house.
  * In-domain success (house A) sits beside every transfer number.
  * Success rates use every run. Drops use runs that learned house A (house-A
    success >= 0.5, rule fixed 2026-09-05): a run that never learned it has
    nothing to drop from. The number of runs counted is printed.
  * A, L1, L2, L3 come from each run's own evaluation. The L2noT control is
    reported separately (section 4), each agent compared with itself.

    python scripts/make_tables.py                      # 300k (headline)
    python scripts/make_tables.py --grid ladder_150k   # 150k (appendix)
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import pandas as pd  # noqa: E402

from config import (  # noqa: E402
    AGENT_NAME, AGENT_ORDER, GenerationConfig, LADDER_300K, TABLES_DIR, pair_dir,
)

RUNGS = ["A", "L1", "L2", "L3"]
SHIFTED = ["L1", "L2", "L3"]
ORDER = list(AGENT_ORDER)
NICE = AGENT_NAME
CLASS = {"ppo": "model-free, vision learned from scratch",
         "ppo_aug": "model-free + colour augmentation",
         "ppo_jepa": "model-free, frozen pretrained encoder (predicts representations)",
         "ppo_mae": "model-free, frozen pretrained encoder (predicts pixels)",
         "ppo_dino": "model-free, frozen pretrained encoder (self-distillation, LVD-142M)",
         "dreamerv3": "world model (redraws the image)",
         "tdmpc2": "world model (no image decoder), plans ahead",
         "tdmpc2_dino": "world model that plans, on the frozen DINOv2 encoder"}
MIN_A = 0.5
RUNG_NAME = {"A": "A (training house)", "L1": "L1 walls/floor/ceiling + light + sky",
             "L2": "L2 + object looks", "L3": "L3 + clutter"}


def budget_tag(grid: str) -> str:
    from config import budget_tag as _tag
    return _tag(grid)


def load(grid: str) -> pd.DataFrame:
    """One row per (agent run, rung) from the committed ladder tree."""
    rows = []
    for f in sorted(glob.glob(str(ROOT / "results" / grid / "*" / "*" / "*_transfer_summary.csv"))):
        p = Path(f)
        baseline = p.parents[1].name
        pair, seed = p.parent.name.split("_seed")
        df = pd.read_csv(f).set_index("level")
        A, AS = df.loc["A", "success_rate"], df.loc["A", "spl"]
        for rung in RUNGS:
            if rung not in df.index:
                raise ValueError(f"{f} has no {rung} row")
            s, sp = df.loc[rung, "success_rate"], df.loc[rung, "spl"]
            rows.append(dict(
                baseline=baseline, pair=pair, seed=int(seed), rung=rung,
                A_success=A, A_spl=AS, success=s, spl=sp,
                drop_pts=100 * (A - s), spl_drop_pts=100 * (AS - sp),
                drop=(A - s) / A if A else float("nan"),          # relative, for brackets
                spl_drop=(AS - sp) / AS if AS else float("nan"),
            ))
    return pd.DataFrame(rows)


def pair_meta() -> dict:
    out = {}
    for i in range(GenerationConfig().n_pairs):
        pid = f"pair{i}"
        v = json.loads((pair_dir(pid) / "verification.json").read_text())
        s = json.loads((pair_dir(pid) / "safe_assets.json").read_text())
        t = json.loads((pair_dir(pid) / "task_config.json").read_text())
        l3 = json.loads((pair_dir(pid) / "l3_prune.json").read_text())
        out[pid] = dict(cells=v["reference"]["n_reachable"],
                        target=t["target_object_type"],
                        swappable=bool(s.get("target_swappable")),
                        clutter=l3.get("n_kept"))
    return out


def house_range(s: pd.DataFrame, col: str, fmt) -> str:
    per_house = s.groupby("pair")[col].mean()
    return f"{fmt(per_house.min())}–{fmt(per_house.max())}"


def f2(v: float) -> str:
    return f"{v:.2f}"


def r0(v: float) -> str:
    t = f"{v:.0f}"
    return "0" if t == "-0" else t


def ci2(c) -> str:
    return f"{c[0]:.2f} [{c[1]:.2f}, {c[2]:.2f}]"


def ci0(c) -> str:
    return f"{r0(c[0])} [{r0(c[1])}, {r0(c[2])}]"


def main_table(d: pd.DataFrame, grid: str, tag: str, target: dict, ci: dict) -> str:
    import robust_stats as rs
    present = [b for b in ORDER if b in set(d.baseline)]
    n_pairs, n_seeds = d.pair.nunique(), d.seed.nunique()
    L = [f"# Original ladder — main tables ({tag} environment steps)", "",
         "Generated by `scripts/make_tables.py` — do not edit by hand. "
         f"{n_pairs} house pairs × {n_seeds} training seeds per agent type. "
         "Square brackets = 95% CI (stratified bootstrap over seeds within each house, from "
         "`scripts/robust_stats.py`); 'houses' = lowest–highest of the five per-house means.", "",
         "The ladder is CUMULATIVE: L1 changes walls, floor and ceiling materials, the lighting "
         "and the sky; L2 also changes every object's look; L3 also adds clutter. Same floor "
         "plan, objects and start poses throughout.", "",
         "## 1. Success rate (every run)", "",
         "| agent | type | runs | " + " | ".join(RUNG_NAME[r] for r in RUNGS) + " |",
         "|---|---|---|" + "---|" * len(RUNGS)]
    for b in present:
        sub = d[d.baseline == b]
        n = sub[sub.rung == "A"].shape[0]
        L.append(f"| {NICE[b]} | {CLASS[b]} | {n} | " + " | ".join(
            f"{ci2(ci[b][r]['success'])}; houses {house_range(sub[sub.rung == r], 'success', f2)}"
            for r in RUNGS) + " |")

    L += ["", f"## 2. Drop in success rate from house A (percentage points; runs with house-A "
          f"success ≥ {MIN_A})", "",
          "Drop = house-A success minus success at the rung, same agent. In round brackets: "
          "the drop as a share of house-A success.", "",
          "| agent | runs counted | house-A success | " +
          " | ".join(RUNG_NAME[r] for r in SHIFTED) + " |",
          "|---|---|---|" + "---|" * len(SHIFTED)]
    for b in present:
        sub = d[(d.baseline == b) & (d.A_success >= MIN_A)]
        n = sub[sub.rung == "A"].shape[0]
        total = d[(d.baseline == b) & (d.rung == "A")].shape[0]
        cells = []
        for r in SHIFTED:
            c = ci[b][r]
            cells.append(f"{ci0(c['drop_points'])} ({r0(100 * c['relative_drop'])}%); "
                         f"houses {house_range(sub[sub.rung == r], 'drop_pts', r0)}")
        L.append(f"| {NICE[b]} | {n} of {total} | "
                 f"{sub[sub.rung == 'A'].success.mean():.2f} | " + " | ".join(cells) + " |")
    for b in present:
        if "drop_points_every_run" in ci[b]["L1"]:
            L.append(f"| {NICE[b]}, every run | {ci[b]['L1']['runs_every']} | "
                     f"{d[(d.baseline == b) & (d.rung == 'A')].success.mean():.2f} | "
                     + " | ".join(ci0(ci[b][r]["drop_points_every_run"]) for r in SHIFTED) + " |")

    # SPL: same machinery as robust_stats, own labels, so the numbers are stable.
    L += ["", f"## 3. SPL (success weighted by path length; runs with house-A success ≥ {MIN_A})",
          "", "Drop in SPL from house A, in points (SPL × 100), same agent.", "",
          "| agent | house-A SPL | " + " | ".join(RUNG_NAME[r] for r in SHIFTED) + " |",
          "|---|---|" + "---|" * len(SHIFTED)]
    rd = rs.load_set(grid)
    for b in present:
        sub = d[(d.baseline == b) & (d.A_success >= MIN_A)]
        cells = []
        for r in SHIFTED:
            c = [100 * v for v in rs.ci(rs.drops(rd, b, r, col="spl"), f"{grid}|spl_drop|{b}|{r}")]
            cells.append(f"{ci0(c)}; houses {house_range(sub[sub.rung == r], 'spl_drop_pts', r0)}")
        L.append(f"| {NICE[b]} | {sub[sub.rung == 'A'].spl.mean():.2f} | " + " | ".join(cells) + " |")

    if target:
        gc = ci.get("_goal_control", {})
        L += ["", "## 4. Goal-object control: does changing ONLY the goal object's look hurt?", "",
              "Each agent compared with itself in one evaluation; 20 agents per type in the four "
              "houses where the goal object could be swapped. Effect in points with 95% CI; p from "
              f"the exact sign-flip test, Holm-corrected over {len(target)} agent types. The CI is "
              "not adjusted for testing several agent types and p is, so a CI just clear of 0 "
              "beside a large p is not a contradiction. Full detail: "
              "`results/tables/target_effect_tests.md`.", "",
              "| agent | success, goal unchanged (L2noT) | success, goal changed (L2) | "
              "effect (points) | p (Holm) |",
              "|---|---|---|---|---|"]
        for b in present:
            r = target[b]
            p = r["p_holm"]
            p_txt = "<0.0001" if p < 1e-4 else f"{p:.3f}"
            eff = ci0(gc[b]["effect_points"]) if b in gc else f"{100 * r['effect']:+.0f}"
            L.append(f"| {NICE[b]} | {r['L2noT']:.2f} | {r['L2']:.2f} | {eff} | {p_txt} |")
    return "\n".join(L) + "\n"


def by_pair_table(d: pd.DataFrame, meta: dict, tag: str, per_house_target: dict) -> str:
    L = [f"# Original ladder — per-house breakdown ({tag} environment steps, appendix)", "",
         "Generated by `scripts/make_tables.py` — do not edit by hand. "
         "Mean ± s.d. over the 5 training seeds, every run. `goal swapped` records whether "
         "the goal object had an alternative asset with the same footprint; where it did "
         "not (pair2), L2 changes everything except the goal object.", ""]
    pairs = sorted(d.pair.unique(), key=lambda p: meta[p]["cells"])
    present = [b for b in ORDER if b in set(d.baseline)]
    for pid in pairs:
        m = meta[pid]
        L += [f"## {pid} — {m['target']}, {m['cells']} reachable cells, "
              f"{m['clutter']} clutter objects, goal swapped at L2: "
              f"**{'yes' if m['swappable'] else 'NO'}**", "",
              "| agent | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |",
              "|---|---|---|---|---|---|---|---|---|"]
        for b in present:
            s = d[(d.baseline == b) & (d.pair == pid)]
            cells = []
            for col in ("success", "spl"):
                for rung in RUNGS:
                    r = s[s.rung == rung][col]
                    cells.append(f"{r.mean():.2f} ± {r.std():.2f}")
            L.append("| " + NICE[b] + " | " + " | ".join(cells) + " |")
        if per_house_target:
            L += ["", "Goal-object control (same agent, one evaluation; mean over 5 agents):", "",
                  "| agent | L2noT success | L2 success | difference |", "|---|---|---|---|"]
            for b in present:
                l2n, l2 = per_house_target[b][pid]
                L.append(f"| {NICE[b]} | {l2n:.2f} | {l2:.2f} | {l2n - l2:+.2f} |")
        L.append("")
    return "\n".join(L) + "\n"


def target_results(tag: str):
    """L2noT results for the 300k ladder only (the 150k ladder has no L2noT rung)."""
    if tag != "300k":
        return {}, {}
    import test_target_effect as tte
    _l, res = tte.analyse("success_rate", draws=200_000, seed=20260915)
    data = tte.load("success_rate")
    per_house = {a: {h: (sum(r[2] for r in rows) / len(rows), sum(r[3] for r in rows) / len(rows))
                     for h, rows in data[a].items()} for a in data}
    return res["within"], per_house


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--grid", default=LADDER_300K,
                    help="results/<set>: ladder_300k (headline) or ladder_150k (appendix)")
    args = ap.parse_args()
    d = load(args.grid)
    if d.empty:
        raise SystemExit(f"no results under results/{args.grid}/")
    counts = d[d.rung == "A"].groupby("baseline").size()
    if set(counts) != {25}:
        raise SystemExit(f"incomplete grid, cells per agent: {dict(counts)}")
    unknown = set(counts.index) - set(ORDER)
    if unknown:
        raise SystemExit(f"agent(s) not in config.AGENT_ORDER: {sorted(unknown)}")
    tag = budget_tag(args.grid)
    import robust_stats as rs
    res = rs.ladder(args.grid)
    ci = dict(res["agents"])
    ci["_goal_control"] = res.get("goal_control", {})
    target, per_house = target_results(tag)
    meta = pair_meta()
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    for name, text in ((f"grid_main_{tag}.md", main_table(d, args.grid, tag, target, ci)),
                       (f"grid_by_pair_{tag}.md", by_pair_table(d, meta, tag, per_house))):
        (TABLES_DIR / name).write_text(text)
        print(f"  wrote {TABLES_DIR / name}")
    print(f"  cells per agent: {dict(counts)}")


if __name__ == "__main__":
    main()
