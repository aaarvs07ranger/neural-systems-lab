"""Interval estimates for every evaluation, following Agarwal et al. (NeurIPS 2021).

Why this exists. The earlier tables reported point estimates and "share of
house-A success lost" with Holm-corrected p-values. Two problems, both raised
2026-09-29: Vishwas found "success lost" confusing, and the paper he pointed us
to (Agarwal et al., "Deep RL at the Edge of the Statistical Precipice") argues
that with a handful of runs one should report INTERVAL estimates and effect
sizes rather than significant/not-significant verdicts. So this reports, per
agent and house:

  * success rate          mean over runs, 95% CI
  * drop in success rate  house A minus the changed house, in percentage points,
                          paired within each run (the same agent in both), 95% CI;
                          the relative drop (drop / house-A success) follows in
                          brackets, as a point estimate only
  * IQM success rate      interquartile mean (mean of the middle 50% of runs):
                          robust to the runs that never learned (ladder only)
  * gap in drop           drop of agent X minus drop of agent Y, 95% CI: how many
                          points less agent Y gives up (between agents)
  * P(X > Y)              probability that a run of agent X succeeds more often
                          than a run of agent Y in the same house

Wording rule for everything downstream: success RATES and DROPS in success rate.
Never "loss", never "share of success lost" as the headline; a relative figure,
if shown at all, goes in brackets.

WHICH RUNS. Statistics of the success rate itself (success, IQM, P(X > Y)) use
every run. Statistics of a DROP use runs whose house-A success is at least 0.5
(rule fixed 2026-09-05): a run that never learned house A has nothing to drop
from, and its drop of about zero would read as perfect robustness. At 300k only
DreamerV3 has such runs (5 of 25); its every-run drop is printed beside for
transparency. (The first version of this script, 2026-09-29, used every run for
drops too; changed 2026-09-30 for exactly that reason.)

CIs are 95% percentile STRATIFIED bootstrap intervals: the training seeds are
resampled with replacement within each of the 5 houses, the statistic is
recomputed over the resampled runs, 10,000 times. Stratifying by house is what
Agarwal et al. recommend for few runs over several tasks -- our houses are their
tasks -- and it keeps the between-house spread out of the resampling.

RANDOM NUMBERS. Each interval draws from its own stream, seeded from SEED and a
label naming that interval, so adding an agent never moves another agent's
interval. (With one shared stream it did, by up to 0.01.)

Three evaluation sets, one table each (300k steps):
  grid_ci_300k.md               original ladder A -> L1 -> L2 -> L3, + goal-object control
  reordered_ladder_ci_300k.md   reordered ladder (least to most damaging), + each rung alone
  single_change_ci_300k.md      one change at a time: the ablation table

    python scripts/robust_stats.py                     # all three, 300k
    python scripts/robust_stats.py --set ladder_150k   # the 150k ladder only
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
import zlib
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from config import (  # noqa: E402
    AGENT_NAME, AGENT_ORDER, LADDER_300K, REORDERED_ALONE, REORDERED_LADDER,
    REORDERED_LADDER_300K, SINGLE_CHANGE_300K, TABLES_DIR, budget_tag,
)

B = 10_000
SEED = 20260929
MIN_A = 0.5
NAME = AGENT_NAME
ORDER = list(AGENT_ORDER)
LADDER = ["A", "L1", "L2", "L3"]
SHIFTED = ["L1", "L2", "L3"]
LADDER_NAME = {"A": "A (training house)", "L1": "L1 walls/floor/ceiling + light + sky",
               "L2": "L2 + object looks", "L3": "L3 + clutter"}
# One change at a time, in the order the ablation table lists them: L1's three
# parts, L2's parts, then L3's. (code, plain name)
SINGLE = [("F_mat", "walls, floor & ceiling"), ("F_light", "lighting"), ("F_sky", "sky"),
          ("F_obj", "object looks, goal unchanged"), ("F_tgt", "goal object's look only"),
          ("F_objall", "all object looks"), ("F_clut", "clutter")]


# ----------------------------------------------------------------------- data
def load_set(name: str) -> pd.DataFrame:
    """One row per (agent run, house) from results/<name>/<agent>/<pair>_seed<N>/."""
    rows = []
    for f in sorted(glob.glob(str(ROOT / "results" / name / "*" / "*" / "*_transfer_summary.csv"))):
        p = Path(f)
        pair, seed = p.parent.name.split("_seed")
        df = pd.read_csv(f)
        for r in df.itertuples():
            rows.append(dict(baseline=p.parents[1].name, pair=pair, seed=int(seed),
                             level=r.level, success=r.success_rate, spl=r.spl))
    if not rows:
        raise SystemExit(f"no results under results/{name}/")
    return pd.DataFrame(rows)


def per_house(d: pd.DataFrame, agent: str, level: str, col: str = "success") -> Dict[str, np.ndarray]:
    """house -> that house's runs, in seed order."""
    s = d[(d.baseline == agent) & (d.level == level)]
    return {h: g.sort_values("seed")[col].to_numpy(float) for h, g in s.groupby("pair")}


def drops(d: pd.DataFrame, agent: str, level: str, col: str = "success",
          min_a: Optional[float] = MIN_A, relative: bool = False) -> Dict[str, np.ndarray]:
    """house -> per-run drop from house A (A minus the level), paired within run.

    Runs with house-A success below `min_a` are left out (None keeps every run).
    """
    s = d[d.baseline == agent]
    a = s[s.level == "A"].set_index(["pair", "seed"])
    b = s[s.level == level].set_index(["pair", "seed"])
    j = pd.DataFrame({"a": a[col], "a_success": a["success"]}).join(b[col].rename("b"),
                                                                    how="inner")
    if min_a is not None:
        j = j[j["a_success"] >= min_a]
    out = {}
    for h, g in j.groupby(level=0):
        g = g.sort_index()
        v = g["a"] - g["b"]
        out[h] = (v / g["a"]).to_numpy(float) if relative else v.to_numpy(float)
    return out


# ------------------------------------------------------------------ bootstrap
def rng_for(label: str) -> np.random.Generator:
    """An independent, reproducible stream per interval (crc32: stable across runs)."""
    return np.random.default_rng([SEED, zlib.crc32(label.encode())])


def _resample(groups: Sequence[np.ndarray], rng: np.random.Generator) -> np.ndarray:
    """(B, N): every draw resamples each house's runs within that house."""
    return np.concatenate([g[rng.integers(0, len(g), (B, len(g)))] for g in groups if len(g)],
                          axis=1)


def iqm(x: np.ndarray) -> np.ndarray:
    """Interquartile mean along the last axis: mean of the middle 50% of values."""
    x = np.sort(np.asarray(x, dtype=float), axis=-1)
    n = x.shape[-1]
    lo, hi = int(np.floor(0.25 * n)), int(np.ceil(0.75 * n))
    return x[..., lo:hi].mean(axis=-1)


def _mean(x: np.ndarray) -> np.ndarray:
    return x.mean(axis=-1)


def ci(groups: Dict[str, np.ndarray], label: str,
       stat: Callable[[np.ndarray], np.ndarray] = _mean) -> List[float]:
    """[point, lo, hi]: stat over all runs pooled, 95% stratified bootstrap CI."""
    g = [groups[h] for h in sorted(groups)]
    point = float(stat(np.concatenate(g)))
    draws = stat(_resample(g, rng_for(label)))
    return [point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]


def ci_diff(gx: Dict[str, np.ndarray], gy: Dict[str, np.ndarray], label: str) -> List[float]:
    """[point, lo, hi] of mean(x) - mean(y), each resampled within house independently."""
    rng = rng_for(label)
    x = [gx[h] for h in sorted(gx)]
    y = [gy[h] for h in sorted(gy)]
    point = float(np.concatenate(x).mean() - np.concatenate(y).mean())
    draws = _resample(x, rng).mean(axis=1) - _resample(y, rng).mean(axis=1)
    return [point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]


def ci_agent_mean(per_agent: List[Dict[str, np.ndarray]], label: str) -> List[float]:
    """[point, lo, hi] of the average over agent types of each type's mean.

    Every agent type counts once, however many of its runs are kept.
    """
    rng = rng_for(label)
    point = float(np.mean([np.concatenate([g[h] for h in sorted(g)]).mean() for g in per_agent]))
    draws = np.mean([_resample([g[h] for h in sorted(g)], rng).mean(axis=1) for g in per_agent],
                    axis=0)
    return [point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]


def _poi(xs: List[np.ndarray], ys: List[np.ndarray]) -> np.ndarray:
    """Average over houses of P(a run of X beats a run of Y), ties counting half.

    Works on single samples (1-D per house) or on bootstrap draws (B x n per house).
    """
    ps = []
    for x, y in zip(xs, ys):
        diff = x[..., :, None] - y[..., None, :]
        ps.append((diff > 0).mean(axis=(-2, -1)) + 0.5 * (diff == 0).mean(axis=(-2, -1)))
    return np.mean(ps, axis=0)


def poi(gx: Dict[str, np.ndarray], gy: Dict[str, np.ndarray], label: str) -> List[float]:
    houses = sorted(set(gx) & set(gy))
    x, y = [gx[h] for h in houses], [gy[h] for h in houses]
    rng = rng_for(label)
    point = float(_poi(x, y))
    xs = [g[rng.integers(0, len(g), (B, len(g)))] for g in x]
    ys = [g[rng.integers(0, len(g), (B, len(g)))] for g in y]
    draws = _poi(xs, ys)
    return [point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))]


def n_runs(groups: Dict[str, np.ndarray]) -> int:
    return int(sum(len(v) for v in groups.values()))


# ------------------------------------------------------------------- analyses
def agents_in(d: pd.DataFrame) -> List[str]:
    present = set(d.baseline)
    unknown = present - set(ORDER)
    if unknown:
        raise SystemExit(f"agent(s) not in config.AGENT_ORDER: {sorted(unknown)}")
    return [a for a in ORDER if a in present]


def drop_record(d: pd.DataFrame, agent: str, level: str, label: str) -> Dict:
    """Drop in points (runs that learned house A, CI), relative drop, every-run drop."""
    g = drops(d, agent, level)
    rec = {"drop_points": [100 * v for v in ci(g, f"{label}|drop")],
           "relative_drop": float(np.mean(np.concatenate(list(
               drops(d, agent, level, relative=True).values())))),
           "runs": n_runs(g)}
    every = drops(d, agent, level, min_a=None)
    if n_runs(every) != n_runs(g):
        rec["drop_points_every_run"] = [100 * v for v in ci(every, f"{label}|drop_all")]
        rec["runs_every"] = n_runs(every)
    return rec


def ladder(set_name: str) -> Dict:
    d = load_set(set_name)
    agents = agents_in(d)
    out: Dict = {"set": set_name, "budget": budget_tag(set_name), "bootstrap_draws": B,
                 "seed": SEED, "min_house_A_success_for_drops": MIN_A, "agents": {}}
    for a in agents:
        rec = {}
        for r in LADDER:
            g = per_house(d, a, r)
            rec[r] = {"success": ci(g, f"{set_name}|success|{a}|{r}"),
                      "iqm": ci(g, f"{set_name}|iqm|{a}|{r}", stat=iqm),
                      "runs": n_runs(g)}
            if r != "A":
                rec[r].update(drop_record(d, a, r, f"{set_name}|{a}|{r}"))
        out["agents"][a] = rec
    out["gap_in_drop"], out["prob_improvement"] = {}, {}
    for r in SHIFTED:
        for i, x in enumerate(agents):
            for y in agents[i + 1:]:
                key = f"{x}>{y}@{r}"
                gap = ci_diff(drops(d, x, r), drops(d, y, r), f"{set_name}|gap|{key}")
                out["gap_in_drop"][key] = [100 * v for v in gap]
                out["prob_improvement"][key] = poi(per_house(d, x, r), per_house(d, y, r),
                                                   f"{set_name}|poi|{key}")
    if set_name == LADDER_300K:
        out["goal_control"] = goal_control()
    return out


def goal_control() -> Dict:
    """L2noT minus L2 (goal object's look unchanged minus changed), per agent.

    Same agent, same evaluation, from the tables `test_target_effect.py` tests
    (exact sign-flip there); this adds the interval. Four houses whose goal object
    was swapped, every run (no drop from house A is taken, so no floor applies).
    """
    import test_target_effect as tte
    data = tte.load("success_rate")
    out = {}
    for a in tte.AGENTS:
        g = {h: np.array([r[2] - r[3] for r in data[a][h]]) for h in tte.SWAPPABLE}
        out[a] = {"L2noT": float(np.mean([r[2] for h in tte.SWAPPABLE for r in data[a][h]])),
                  "L2": float(np.mean([r[3] for h in tte.SWAPPABLE for r in data[a][h]])),
                  "effect_points": [100 * v for v in ci(g, f"goal_control|{a}")],
                  "runs": n_runs(g)}
    return out


def reordered() -> Dict:
    d = load_set(REORDERED_LADDER_300K)
    agents = agents_in(d)
    out: Dict = {"set": REORDERED_LADDER_300K, "bootstrap_draws": B, "seed": SEED,
                 "min_house_A_success_for_drops": MIN_A,
                 "ladder": [list(x) for x in REORDERED_LADDER],
                 "alone": [list(x) for x in REORDERED_ALONE], "agents": {}}
    levels = [c for c, _n in REORDERED_LADDER] + [c for c, _n in REORDERED_ALONE
                                                  if c not in dict(REORDERED_LADDER)]
    for a in agents:
        rec = {}
        for lv in levels:
            g = per_house(d, a, lv)
            rec[lv] = {"success": ci(g, f"reordered|success|{a}|{lv}"), "runs": n_runs(g),
                       "per_house": {h: [float(v.mean()), float(v.std(ddof=1))]
                                     for h, v in g.items()}}
            if lv != "A":
                rec[lv].update(drop_record(d, a, lv, f"reordered|{a}|{lv}"))
        out["agents"][a] = rec
    out["mean_over_agents"] = {
        lv: [100 * v for v in ci_agent_mean([drops(d, a, lv) for a in agents],
                                            f"reordered|agentmean|{lv}")]
        for lv in levels if lv != "A"}
    return out


def single_change() -> Dict:
    d = load_set(SINGLE_CHANGE_300K)
    agents = agents_in(d)
    out: Dict = {"set": SINGLE_CHANGE_300K, "bootstrap_draws": B, "seed": SEED,
                 "min_house_A_success_for_drops": MIN_A,
                 "changes": [list(x) for x in SINGLE], "agents": {}}
    for a in agents:
        rec = {"A": {"success": ci(per_house(d, a, "A"), f"single|success|{a}|A")}}
        for code, _name in SINGLE:
            rec[code] = drop_record(d, a, code, f"single|{a}|{code}")
            rec[code]["success"] = ci(per_house(d, a, code), f"single|success|{a}|{code}")
        out["agents"][a] = rec
    out["mean_over_agents"] = {
        code: [100 * v for v in ci_agent_mean([drops(d, a, code) for a in agents],
                                              f"single|agentmean|{code}")]
        for code, _n in SINGLE}
    return out


# --------------------------------------------------------------------- render
def f2(v) -> str:
    return f"{v[0]:.2f} [{v[1]:.2f}, {v[2]:.2f}]"


def r0(x: float) -> str:
    """Rounded to a whole number; never prints '-0'."""
    t = f"{x:.0f}"
    return "0" if t == "-0" else t


def fp(v) -> str:
    """Points with CI, rounded."""
    return f"{r0(v[0])} [{r0(v[1])}, {r0(v[2])}]"


def drop_cell(rec: Dict) -> str:
    return f"{fp(rec['drop_points'])} ({r0(100 * rec['relative_drop'])}%)"


def every_run_rows(agents: Dict, levels: Sequence[str], lead: str = "") -> List[str]:
    """One extra row per agent that has runs below the house-A floor."""
    L = []
    for a, rec in agents.items():
        if any("drop_points_every_run" in rec[lv] for lv in levels):
            n_all = max(rec[lv].get("runs_every", rec[lv]["runs"]) for lv in levels)
            L.append(f"| {NAME[a]}, every run ({n_all}) | {lead}" + " | ".join(
                fp(rec[lv].get("drop_points_every_run", rec[lv]["drop_points"]))
                for lv in levels) + " |")
    return L


HEAD = ("Generated by `scripts/robust_stats.py` -- do not edit by hand. 95% stratified "
        "bootstrap CIs in square brackets ({b:,} draws; training seeds resampled within each "
        "house). Following Agarwal et al. (NeurIPS 2021).")
WHO = ("**Which runs.** Success rates use every run. Drops use runs that learned house A "
       f"(house-A success ≥ {MIN_A}): a run that never learned it has nothing to drop from, "
       "so its drop of about zero would read as perfect robustness. Only DreamerV3 has such "
       "runs; its every-run drop is shown on its own line.")
DROP_EXPLAINED = ("Drop = house-A success minus success in the changed house, in percentage "
                  "points, for the same trained agent. In round brackets after it: the drop as a "
                  "share of that agent's house-A success.")


def render_ladder(res: Dict) -> str:
    tag = res["budget"]
    ag = res["agents"]
    L = [f"# Original ladder with interval estimates ({tag} training steps)", "",
         HEAD.format(b=res["bootstrap_draws"]), "",
         "The ladder is CUMULATIVE: L1 changes the walls, floor and ceiling materials, the "
         "lighting and the sky; L2 also changes every object's look; L3 also adds clutter. "
         "Every house differs from house A only in appearance: same floor plan, objects and "
         "start poses.", "", WHO, "",
         "## 1. Success rate (every run)", "",
         "| agent | " + " | ".join(LADDER_NAME[r] for r in LADDER) + " |",
         "|---|" + "---|" * len(LADDER)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} | " + " | ".join(f2(rec[r]["success"]) for r in LADDER) + " |")
    L += ["", "## 2. Drop in success rate from house A (percentage points)", "",
          DROP_EXPLAINED, "",
          "| agent (runs) | " + " | ".join(LADDER_NAME[r] for r in SHIFTED) + " |",
          "|---|" + "---|" * len(SHIFTED)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} ({rec['L1']['runs']}) | "
                 + " | ".join(drop_cell(rec[r]) for r in SHIFTED) + " |")
    L += every_run_rows(ag, SHIFTED)
    L += ["", "## 3. Interquartile mean (IQM) success rate (every run)", "",
          "Mean of the middle 50% of runs; robust to runs that never learned house A.", "",
          "| agent | " + " | ".join(LADDER) + " |", "|---|" + "---|" * len(LADDER)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} | " + " | ".join(f2(rec[r]["iqm"]) for r in LADDER) + " |")
    if "goal_control" in res:
        L += ["", "## 4. Goal-object control: L2 with the goal object's look unchanged (L2noT) "
              "vs changed (L2)", "",
              "Same agent, same evaluation; the four houses whose goal object could be swapped "
              "(20 runs per agent). Effect = success with the goal's look unchanged minus success "
              "with it changed, in points. Exact tests, corrected for testing eight agent types: "
              "`results/tables/target_effect_tests.md`; the CIs here are not corrected.",
              "", "| agent | success, goal unchanged | success, goal changed | effect (points) |",
              "|---|---|---|---|"]
        for a in [x for x in ORDER if x in res["goal_control"]]:
            r = res["goal_control"][a]
            L.append(f"| {NAME[a]} | {r['L2noT']:.2f} | {r['L2']:.2f} | {fp(r['effect_points'])} |")
    agents = list(ag)
    L += ["", "## 5. Gap in drop between agents (percentage points)", "",
          "Drop of agent X minus drop of agent Y: how many points LESS agent Y gives up. "
          "A CI above 0 means Y is reliably more robust; below 0, X is.", "",
          "| X | Y | L1 | L2 | L3 |", "|---|---|---|---|---|"]
    for i, x in enumerate(agents):
        for y in agents[i + 1:]:
            L.append(f"| {NAME[x]} | {NAME[y]} | " + " | ".join(
                fp(res["gap_in_drop"][f"{x}>{y}@{r}"]) for r in SHIFTED) + " |")
    L += ["", "## 6. Probability of improvement (every run)", "",
          "P(X > Y): chance that a run of X succeeds more often than a run of Y in the same "
          "house, averaged over houses (0.5 = no difference). A CI above 0.5 means X is "
          "reliably ahead; below 0.5, Y is.", "",
          "| X | Y | L1 | L2 | L3 |", "|---|---|---|---|---|"]
    for i, x in enumerate(agents):
        for y in agents[i + 1:]:
            L.append(f"| {NAME[x]} | {NAME[y]} | " + " | ".join(
                f2(res["prob_improvement"][f"{x}>{y}@{r}"]) for r in SHIFTED) + " |")
    return "\n".join(L) + "\n"


RETRAIN_NOTE = ("For 7 of the 200 cells (6 DreamerV3, 1 TD-MPC2) the saved model is a retrain of "
                "the original run, because the original's model was lost; every number here "
                "compares an agent with itself.")


def render_reordered(res: Dict) -> str:
    ag = res["agents"]
    lad = [c for c, _n in REORDERED_LADDER]
    alone = [c for c, _n in REORDERED_ALONE]
    nm = dict(REORDERED_LADDER)
    an = dict(REORDERED_ALONE)
    mo = res["mean_over_agents"]
    L = ["# Reordered ladder with interval estimates (300k training steps)", "",
         HEAD.format(b=res["bootstrap_draws"]), "",
         "The same appearance changes as the original ladder, stacked from least to most "
         "damaging. The ladder is CUMULATIVE: each rung keeps every change below it and adds "
         "one more. R1 is the clutter-only house; R4 holds every change and is the same house "
         "file as the original L3. Section 3 instead applies each rung's change to house A on "
         "its own (not cumulative).", "",
         "One evaluation pass: every agent measured in all eight houses the same day. "
         + RETRAIN_NOTE, "", WHO, "",
         "## 1. Success rate along the reordered ladder (every run)", "",
         "| agent | " + " | ".join(nm[c] for c in lad) + " |", "|---|" + "---|" * len(lad)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} | " + " | ".join(f2(rec[c]["success"]) for c in lad) + " |")
    L += ["", "## 2. Drop in success rate from house A along the reordered ladder (points)", "",
          DROP_EXPLAINED, "",
          "| agent (runs) | " + " | ".join(nm[c] for c in lad[1:]) + " |",
          "|---|" + "---|" * (len(lad) - 1)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} ({rec[lad[1]]['runs']}) | "
                 + " | ".join(drop_cell(rec[c]) for c in lad[1:]) + " |")
    L += every_run_rows(ag, lad[1:])
    L.append(f"| **mean over the {len(ag)} agent types** | "
             + " | ".join(fp(mo[c]) for c in lad[1:]) + " |")
    L += ["", "## 3. Each rung's change on its own (not cumulative): drop from house A (points)", "",
          "| agent (runs) | " + " | ".join(an[c] for c in alone) + " |",
          "|---|" + "---|" * len(alone)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} ({rec[alone[0]]['runs']}) | "
                 + " | ".join(drop_cell(rec[c]) for c in alone) + " |")
    L += every_run_rows(ag, alone)
    L.append(f"| **mean over the {len(ag)} agent types** | "
             + " | ".join(fp(mo[c]) for c in alone) + " |")
    L += ["", "## 4. Success rate per house, mean ± s.d. over the 5 training seeds (every run)", ""]
    houses = sorted(next(iter(ag.values()))["A"]["per_house"])
    for h in houses:
        L += [f"**{h}**", "", "| agent | " + " | ".join(nm[c] for c in lad) + " |",
              "|---|" + "---|" * len(lad)]
        for a, rec in ag.items():
            L.append(f"| {NAME[a]} | " + " | ".join(
                "{:.2f} ± {:.2f}".format(*rec[c]["per_house"][h]) for c in lad) + " |")
        L.append("")
    return "\n".join(L) + "\n"


def render_single(res: Dict) -> str:
    ag = res["agents"]
    codes = [c for c, _n in SINGLE]
    nm = dict(SINGLE)
    mo = res["mean_over_agents"]
    L = ["# One change at a time: the ablation table (300k training steps)", "",
         HEAD.format(b=res["bootstrap_draws"]), "",
         "Each house is house A with exactly ONE thing changed, copied byte for byte from the "
         "change the original ladder made. The first three together make up L1; the next three "
         "are L2's object changes (\"all object looks\" is the two before it combined); clutter "
         "is L3's. One evaluation pass: every agent measured in every house the same day. "
         + RETRAIN_NOTE, "", WHO, "",
         "## Drop in success rate from house A (percentage points)", "", DROP_EXPLAINED, "",
         "| agent (runs) | house-A success | " + " | ".join(nm[c] for c in codes) + " |",
         "|---|---|" + "---|" * len(codes)]
    for a, rec in ag.items():
        L.append(f"| {NAME[a]} ({rec[codes[0]]['runs']}) | {rec['A']['success'][0]:.2f} | "
                 + " | ".join(drop_cell(rec[c]) for c in codes) + " |")
    L += every_run_rows(ag, codes, lead="| ")
    L.append(f"| **mean over the {len(ag)} agent types** | | "
             + " | ".join(fp(mo[c]) for c in codes) + " |")
    order = sorted(codes, key=lambda c: mo[c][0])
    L += ["", "## Ranking: which single change does the damage", "",
          "Mean over the agent types (each type counted once), smallest to largest.", "",
          "| change on its own | drop (points) | least / most affected agent (points) |",
          "|---|---|---|"]
    for c in order:
        vals = {a: ag[a][c]["drop_points"][0] for a in ag}
        lo, hi = min(vals, key=vals.get), max(vals, key=vals.get)
        L.append(f"| {nm[c]} | {fp(mo[c])} | {NAME[lo]} {r0(vals[lo])} / "
                 f"{NAME[hi]} {r0(vals[hi])} |")
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------- main
def write(name: str, res: Dict, text: str) -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    (TABLES_DIR / f"{name}.json").write_text(json.dumps(res, indent=1) + "\n")
    (TABLES_DIR / f"{name}.md").write_text(text)
    print(f"  wrote results/tables/{name}.md")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--set", default=None,
                    help="one ladder set only (e.g. ladder_150k); default = all three 300k sets")
    a = ap.parse_args()
    if a.set:
        res = ladder(a.set)
        write(f"grid_ci_{res['budget']}", res, render_ladder(res))
        return
    res = ladder(LADDER_300K)
    write(f"grid_ci_{res['budget']}", res, render_ladder(res))
    res = reordered()
    write("reordered_ladder_ci_300k", res, render_reordered(res))
    res = single_change()
    write("single_change_ci_300k", res, render_single(res))


if __name__ == "__main__":
    main()
