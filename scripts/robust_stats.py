"""Interval estimates for the ladder, following Agarwal et al. (NeurIPS 2021).

Why this exists. The earlier tables reported point estimates and "share of
house-A success lost" with Holm-corrected p-values. Two problems, both raised
2026-09-29: Vishwas found "success lost" confusing, and the paper he pointed us
to (Agarwal et al., "Deep RL at the Edge of the Statistical Precipice") argues
that with a handful of runs one should report INTERVAL estimates and effect
sizes rather than significant/not-significant verdicts. So this reports, per
agent and rung:

  * success rate                   mean over runs, 95% CI
  * drop in success rate           house A minus the rung, in percentage points
                                   (absolute -- no denominator), 95% CI
  * IQM success rate               interquartile mean (mean of the middle 50% of
                                   runs): robust to the runs that never learned
  * P(X > Y)                       probability that a run of agent X succeeds more
                                   often than a run of agent Y in the same house

Wording rule for everything downstream: success RATES and DROPS in success rate.
Never "loss", never "share of success lost" as the headline; a relative figure,
if shown at all, goes in brackets.

CIs are 95% percentile STRATIFIED bootstrap intervals: the 5 training seeds are
resampled with replacement within each of the 5 houses, the statistic is
recomputed over the 25 resampled runs, 10,000 times. Stratifying by house is
what Agarwal et al. recommend for few runs over several tasks -- our houses are
their tasks -- and it keeps the between-house spread out of the resampling.
Every run is used; there is no competency filter here, because no ratio is
formed.

    python scripts/robust_stats.py                       # 300k grid
    python scripts/robust_stats.py --grid grid           # 150k
    -> results/tables/grid_ci_<budget>.md and .json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import make_tables as mt  # noqa: E402

B = 10_000
SEED = 20260929
NAME = {"ppo": "PPO", "ppo_aug": "PPO+Aug", "ppo_jepa": "PPO+I-JEPA",
        "ppo_mae": "PPO+MAE", "ppo_dino": "PPO+DINOv2", "dreamerv3": "DreamerV3",
        "tdmpc2": "TD-MPC2", "tdmpc2_dino": "TD-MPC2+DINOv2"}
ORDER = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "ppo_dino", "dreamerv3", "tdmpc2",
         "tdmpc2_dino"]


def iqm(x: np.ndarray) -> float:
    """Interquartile mean: mean of the middle 50% of values (25% trimmed mean)."""
    x = np.sort(np.asarray(x, dtype=float))
    n = len(x)
    lo, hi = int(np.floor(0.25 * n)), int(np.ceil(0.75 * n))
    return float(x[lo:hi].mean())


def by_house(values: Dict[str, np.ndarray]) -> List[np.ndarray]:
    return [values[h] for h in sorted(values)]


def stratified_ci(groups: List[np.ndarray], stat: Callable[[np.ndarray], float],
                  rng: np.random.Generator) -> tuple:
    """Point estimate and 95% percentile CI, resampling runs within each group."""
    point = stat(np.concatenate(groups))
    draws = np.empty(B)
    for i in range(B):
        draws[i] = stat(np.concatenate([g[rng.integers(0, len(g), len(g))] for g in groups]))
    return point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))


def prob_improvement(x_groups: List[np.ndarray], y_groups: List[np.ndarray]) -> float:
    """Average over houses of P(a run of X beats a run of Y), ties counting half."""
    ps = []
    for x, y in zip(x_groups, y_groups):
        diff = x[:, None] - y[None, :]
        ps.append(float((diff > 0).mean() + 0.5 * (diff == 0).mean()))
    return float(np.mean(ps))


def poi_ci(x_groups, y_groups, rng) -> tuple:
    point = prob_improvement(x_groups, y_groups)
    draws = np.empty(B)
    for i in range(B):
        xs = [g[rng.integers(0, len(g), len(g))] for g in x_groups]
        ys = [g[rng.integers(0, len(g), len(g))] for g in y_groups]
        draws[i] = prob_improvement(xs, ys)
    return point, float(np.percentile(draws, 2.5)), float(np.percentile(draws, 97.5))


def run(grid: str) -> Dict:
    rng = np.random.default_rng(SEED)
    d = mt.load(grid)
    tag = mt.budget_tag(grid)
    agents = [a for a in ORDER if a in set(d.baseline)]
    rungs = mt.RUNGS
    per = {}   # agent -> rung -> house -> array of per-run success
    for a in agents:
        per[a] = {}
        for r in rungs:
            s = d[(d.baseline == a) & (d.rung == r)]
            per[a][r] = {h: s[s.pair == h].sort_values("seed").success.to_numpy()
                         for h in sorted(s.pair.unique())}
    out: Dict = {"grid": grid, "budget": tag, "bootstrap_draws": B, "seed": SEED,
                 "agents": {}}
    for a in agents:
        rec = {}
        for r in rungs:
            g = by_house(per[a][r])
            m, lo, hi = stratified_ci(g, np.mean, rng)
            q, qlo, qhi = stratified_ci(g, iqm, rng)
            rec[r] = {"success": [m, lo, hi], "iqm": [q, qlo, qhi]}
            if r != "A":
                # Per-run drop, paired within the run (same agent in A and the rung).
                gd = [per[a]["A"][h] - per[a][r][h] for h in sorted(per[a][r])]
                dm, dlo, dhi = stratified_ci(gd, np.mean, rng)
                rec[r]["drop_points"] = [100 * dm, 100 * dlo, 100 * dhi]
        out["agents"][a] = rec
    # Probability of improvement at every shifted rung, each pair of agents.
    poi = {}
    for r in ("L1", "L2", "L3"):
        for i, x in enumerate(agents):
            for y in agents[i + 1:]:
                poi[f"{x}>{y}@{r}"] = poi_ci(by_house(per[x][r]), by_house(per[y][r]), rng)
    out["prob_improvement"] = poi
    return out


def render(res: Dict) -> str:
    tag = res["budget"]
    f2 = lambda v: f"{v[0]:.2f} [{v[1]:.2f}, {v[2]:.2f}]"
    fp = lambda v: f"{v[0]:.0f} [{v[1]:.0f}, {v[2]:.0f}]"
    L = [f"# Ladder with interval estimates ({tag} steps)", "",
         "Generated by `scripts/robust_stats.py` -- do not edit by hand. 95% stratified "
         f"bootstrap CIs ({res['bootstrap_draws']:,} draws; seeds resampled within each "
         "house), every run included. Following Agarwal et al. (NeurIPS 2021).", "",
         "## Success rate", "",
         "| agent | A | L1 | L2 | L3 |", "|---|---|---|---|---|"]
    for a, rec in res["agents"].items():
        L.append(f"| {NAME[a]} | " + " | ".join(f2(rec[r]["success"]) for r in mt.RUNGS) + " |")
    L += ["", "## Drop in success rate from house A (percentage points)", "",
          "Paired within each run: that run's house-A success minus its success at the rung.", "",
          "| agent | L1 | L2 | L3 |", "|---|---|---|---|"]
    for a, rec in res["agents"].items():
        L.append(f"| {NAME[a]} | " + " | ".join(fp(rec[r]["drop_points"]) for r in ("L1", "L2", "L3")) + " |")
    L += ["", "## Interquartile mean (IQM) success rate", "",
          "Mean of the middle 50% of runs; robust to runs that never learned house A.", "",
          "| agent | A | L1 | L2 | L3 |", "|---|---|---|---|---|"]
    for a, rec in res["agents"].items():
        L.append(f"| {NAME[a]} | " + " | ".join(f2(rec[r]["iqm"]) for r in mt.RUNGS) + " |")
    L += ["", "## Probability of improvement", "",
          "P(X > Y): chance that a run of X succeeds more often than a run of Y in the same "
          "house, averaged over houses (0.5 = no difference). CI excludes 0.5 => X reliably ahead.", "",
          "| X | Y | L1 | L2 | L3 |", "|---|---|---|---|---|"]
    agents = list(res["agents"])
    for i, x in enumerate(agents):
        for y in agents[i + 1:]:
            L.append(f"| {NAME[x]} | {NAME[y]} | " + " | ".join(
                f2(res["prob_improvement"][f"{x}>{y}@{r}"]) for r in ("L1", "L2", "L3")) + " |")
    return "\n".join(L) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--grid", default="grid_300000")
    a = ap.parse_args()
    res = run(a.grid)
    tables = ROOT / "results" / "tables"
    (tables / f"grid_ci_{res['budget']}.json").write_text(json.dumps(res, indent=1) + "\n")
    (tables / f"grid_ci_{res['budget']}.md").write_text(render(res))
    print(f"  wrote results/tables/grid_ci_{res['budget']}.md")


if __name__ == "__main__":
    main()
