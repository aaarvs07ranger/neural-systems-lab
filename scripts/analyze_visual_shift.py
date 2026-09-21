"""Does damage grow with how much the image changed?

Inputs
  results/tables/visual_shift.json  how different each shifted house LOOKS from house A,
                                    measured at the 25 pinned evaluation start poses
                                    (per house x rung; no agent involved)
  per-agent summary tables          how much each agent's success fell

The unit is the HOUSE. Every agent in a house sees the same images, so the
independent measurements of "how much the image changed" number exactly five.
Treating each agent as a separate data point would count the same image change
25 times and manufacture significance.

Q1 (main). Across the 5 houses, does a bigger L1 image change bring bigger L1
    damage? Damage = fraction of house-A success lost, (A - L1) / A, averaged over
    that house's agents. Runs with house-A success < 0.5 are left out of this ratio
    (a near-zero denominator makes it meaningless; the rule was fixed on
    2026-09-05, before any of this analysis). Agents: the committed 300k grid.
    Statistic: Spearman rank correlation. p: exact, over all 120 orderings of the
    5 houses. With 5 houses even a perfect rank match gives p = 2/120 = 0.017, so
    this test can only detect an almost perfect relationship; the table beside it
    is the real evidence.
    All three image distances from measure_visual_shift.py are reported, none
    singled out.

Q1b (secondary, a planned design axis). The same test against house size
    (reachable floor cells) -- the houses were chosen to span sizes.

Q2 (descriptive). Within each house, each rung adds one kind of change. How much
    image change does each step add, and how much success does it cost? Both
    rungs of every step come from the same agent's single evaluation pass.

    python scripts/analyze_visual_shift.py
    python scripts/analyze_visual_shift.py --selftest
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from test_target_effect import source_for  # noqa: E402  same-pass table per agent

AGENTS = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "ppo_dino", "tdmpc2", "dreamerv3"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO+aug", "ppo_jepa": "PPO+JEPA", "ppo_mae": "PPO+MAE", "ppo_dino": "PPO+DINOv2",
        "tdmpc2": "TD-MPC2", "dreamerv3": "DreamerV3"}
HOUSES = ["pair0", "pair1", "pair2", "pair3", "pair4"]
SEEDS = range(5)
MIN_A = 0.5
METRICS = {"mean_abs_diff": "mean pixel difference (0-255)",
           "frac_pixels_changed": "share of pixels visibly changed",
           "hist_l1": "colour-histogram distance"}
OUT = ROOT / "results" / "tables" / "visual_shift_analysis.md"


def _summary(path: Path) -> Dict[str, Dict[str, str]]:
    with open(path) as f:
        return {r["level"]: r for r in csv.DictReader(f)}


# ------------------------------------------------------------------ statistics
def ranks(x: np.ndarray) -> np.ndarray:
    """Average ranks (ties share the mean of their positions)."""
    order = np.argsort(x, kind="mergesort")
    r = np.empty(len(x))
    i = 0
    xs = x[order]
    while i < len(x):
        j = i
        while j + 1 < len(x) and xs[j + 1] == xs[i]:
            j += 1
        r[order[i:j + 1]] = 0.5 * (i + j) + 1
        i = j + 1
    return r


def spearman(x: np.ndarray, y: np.ndarray) -> float:
    rx, ry = ranks(x), ranks(y)
    rx, ry = rx - rx.mean(), ry - ry.mean()
    return float((rx @ ry) / np.sqrt((rx @ rx) * (ry @ ry)))


def spearman_exact(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """Two-sided exact p over every ordering of y against x."""
    rho = spearman(x, y)
    perms = list(itertools.permutations(range(len(y))))
    hits = sum(abs(spearman(x, y[list(p)])) >= abs(rho) - 1e-12 for p in perms)
    return rho, hits / len(perms)


# ------------------------------------------------------------------------ data
def l1_damage_by_house(tree: str) -> Dict[str, Dict[str, float]]:
    """agent -> house -> mean (A - L1)/A over runs with A >= MIN_A.

    tree='grid'   : committed 300k grid (the headline agents)
    tree='same'   : the table holding L2noT for the agent that exists now
    """
    out: Dict[str, Dict[str, float]] = {}
    for agent in AGENTS:
        out[agent] = {}
        for h in HOUSES:
            vals = []
            for s in SEEDS:
                cell = f"{h}_seed{s}"
                path = (ROOT / "results" / "grid_300000" / agent / cell /
                        f"{agent}_transfer_summary.csv") if tree == "grid" else source_for(agent, cell)
                R = _summary(path)
                A = float(R["A"]["success_rate"])
                if A >= MIN_A:
                    vals.append((A - float(R["L1"]["success_rate"])) / A)
            out[agent][h] = float(np.mean(vals)) if vals else float("nan")
    return out


def step_costs() -> Dict[str, Dict[str, Dict[str, float]]]:
    """agent -> house -> {step: mean success lost over that step}, same-pass tables."""
    steps = [("L1", "A"), ("L2noT", "L1"), ("L2", "L2noT"), ("L3", "L2")]
    out: Dict[str, Dict[str, Dict[str, float]]] = {}
    for agent in AGENTS:
        out[agent] = {}
        for h in HOUSES:
            rows = [_summary(source_for(agent, f"{h}_seed{s}")) for s in SEEDS]
            out[agent][h] = {f"{prev}->{cur}": float(np.mean(
                [float(R[prev]["success_rate"]) - float(R[cur]["success_rate"]) for R in rows]))
                for cur, prev in steps}
    return out


def load_shift() -> Dict[str, Dict[str, Dict[str, float]]]:
    rows = json.loads((ROOT / "results" / "tables" / "visual_shift.json").read_text())
    out: Dict[str, Dict[str, Dict[str, float]]] = {}
    for r in rows:
        out.setdefault(r["pair"], {})[r["level"]] = {m: float(r[m]) for m in METRICS}
    missing = [(h, l) for h in HOUSES for l in ("L1", "L2noT", "L2", "L3")
               if l not in out.get(h, {})]
    if missing:
        raise ValueError(f"visual_shift.json is missing {missing}")
    return out


def house_size(h: str) -> int:
    v = json.loads((ROOT / "data" / "pairs" / h / "verification.json").read_text())
    return int(v["reference"]["n_reachable"])


# ---------------------------------------------------------------------- report
def run() -> str:
    shift = load_shift()
    dmg = l1_damage_by_house("grid")
    dmg_same = l1_damage_by_house("same")
    sizes = {h: house_size(h) for h in HOUSES}
    pooled = {h: float(np.mean([dmg[a][h] for a in AGENTS])) for h in HOUSES}
    pooled_same = {h: float(np.mean([dmg_same[a][h] for a in AGENTS])) for h in HOUSES}

    L: List[str] = [
        "# Damage vs how much the image changed (300k grid)", "",
        "Generated by `scripts/analyze_visual_shift.py` -- do not edit by hand.", "",
        "Image change is measured at the 25 pinned start poses, house A vs the shifted house,",
        "with no agent involved. **The unit is the house: 5 independent measurements.**", "",
        "## Q1. Does a bigger L1 image change bring bigger L1 damage?", "",
        "Damage = share of house-A success lost at L1, averaged over the house's agents "
        f"(runs with house-A success < {MIN_A} left out of the ratio).", "",
        "| house | cells | mean pixel diff | pixels changed | histogram dist | "
        + " | ".join(NICE[a] for a in AGENTS) + " | all agents |",
        "|---" * (5 + len(AGENTS) + 1) + "|",
    ]
    for h in sorted(HOUSES, key=lambda k: shift[k]["L1"]["mean_abs_diff"]):
        s = shift[h]["L1"]
        L.append(f"| {h} | {sizes[h]} | {s['mean_abs_diff']:.1f} | {100*s['frac_pixels_changed']:.0f}% | "
                 f"{s['hist_l1']:.2f} | " + " | ".join(f"{100*dmg[a][h]:.0f}%" for a in AGENTS)
                 + f" | **{100*pooled[h]:.0f}%** |")
    L += ["", "(rows ordered by mean pixel difference)", "",
          "Rank correlation with damage (Spearman; exact p over all 120 orderings; "
          "smallest possible p = 0.017):", "",
          "| predictor | " + " | ".join(NICE[a] for a in AGENTS) + " | all agents | p (all agents) |",
          "|---" * (len(AGENTS) + 3) + "|"]
    predictors = [(METRICS[m], {h: shift[h]["L1"][m] for h in HOUSES}) for m in METRICS]
    predictors.append(("house size (floor cells)", {h: float(sizes[h]) for h in HOUSES}))
    results = {}
    for name, pred in predictors:
        x = np.array([pred[h] for h in HOUSES])
        per = [spearman(x, np.array([dmg[a][h] for h in HOUSES])) for a in AGENTS]
        rho, p = spearman_exact(x, np.array([pooled[h] for h in HOUSES]))
        rho_same, p_same = spearman_exact(x, np.array([pooled_same[h] for h in HOUSES]))
        results[name] = (rho, p, rho_same, p_same)
        L.append(f"| {name} | " + " | ".join(f"{r:+.2f}" for r in per)
                 + f" | **{rho:+.2f}** | {p:.3f} |")
    L += ["", "Check with the same-pass tables instead of the committed grid "
          "(differs only for the 7 retrained agents):", "",
          "| predictor | all agents rho | p |", "|---|---|---|"]
    for name, (_r, _p, rs, ps) in results.items():
        L.append(f"| {name} | {rs:+.2f} | {ps:.3f} |")

    # Q2
    costs = step_costs()
    L += ["", "## Q2. What does each rung add, in image change and in lost success?", "",
          "Image change added = increase in mean pixel difference from the previous rung. "
          "Success lost = drop in success rate over that step (same agent, same evaluation), "
          "averaged over the house's 5 agents.", ""]
    # A->L1 is Q1's question, answered there with the house-A < 0.5 rule; repeated
    # here as a raw difference it would let agents that never learned house A
    # "improve" under shift. Q2 starts from L1.
    step_names = [("L1->L2noT", "other objects' look", "L1", "L2noT"),
                  ("L2noT->L2", "target's look only", "L2noT", "L2"),
                  ("L2->L3", "clutter", "L2", "L3")]
    for key, label, prev, cur in step_names:
        L += [f"**{key} ({label})**", "",
              "| house | image change added | " + " | ".join(NICE[a] for a in AGENTS) + " |",
              "|---" * (len(AGENTS) + 2) + "|"]
        for h in HOUSES:
            now = shift[h][cur]["mean_abs_diff"]
            added = now - shift[h][prev]["mean_abs_diff"]
            L.append(f"| {h} | {added:+.1f} | " + " | ".join(
                f"{costs[a][h][key]:+.2f}" for a in AGENTS) + " |")
        L.append("")
    L.append("Positive success lost = the agent did worse after this step.")
    return "\n".join(L) + "\n"


def selftest() -> None:
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    rho, p = spearman_exact(x, x * 10)
    assert abs(rho - 1) < 1e-12 and abs(p - 2 / 120) < 1e-12, (rho, p)
    rho, p = spearman_exact(x, -x)
    assert abs(rho + 1) < 1e-12 and abs(p - 2 / 120) < 1e-12
    assert np.allclose(ranks(np.array([3.0, 1.0, 3.0, 2.0])), [3.5, 1.0, 3.5, 2.0])
    try:
        from scipy.stats import spearmanr
        rng = np.random.default_rng(1)
        for _ in range(50):
            a, b = rng.normal(size=5), rng.normal(size=5)
            assert abs(spearman(a, b) - spearmanr(a, b)[0]) < 1e-12
        print("spearman matches scipy")
    except ImportError:
        print("scipy not installed; skipped the scipy cross-check")
    print("selftest passed")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    text = run()
    OUT.write_text(text)
    print(text)


if __name__ == "__main__":
    main()
