"""Does changing ONLY the target's appearance hurt an agent? (L2noT vs L2)

For every trained agent, the two rungs differ in exactly one thing: whether the
target object's appearance was swapped. Both numbers come from the SAME agent in
the SAME evaluation pass, so the comparison is always an agent against itself.

Unit of analysis: one trained agent. Per agent, d = success(L2noT) - success(L2),
i.e. how much better it does when the target still looks like it did in training.

Tests (all fixed before looking at the numbers):

1. Target effect per agent type -- exact sign-flip test.
   If the target's look did not matter, L2noT and L2 would be interchangeable
   labels, so each agent's d is equally likely to be + or -. We enumerate EVERY
   one of the 2^20 sign patterns for the 20 agents in the four houses where the
   target was swapped (pair0, pair1, pair3, pair4). p = share of patterns whose
   mean is at least as far from zero as the real one (two-sided). Exact, no
   random sampling. Holm-corrected across the 6 agent types.

2. Is the effect bigger for one agent type than another -- stratified
   permutation. Within each house, shuffle which agent type each d belongs to;
   statistic = difference in mean d. 200,000 draws, fixed seed. Holm-corrected
   across the 15 pairs of agent types. (A significant effect in one type and a
   non-significant one in another is NOT by itself evidence they differ; this
   test is.)

3. Negative control -- pair2. Its target cannot be swapped, so its L2noT and L2
   are the same house file. The same sign-flip test must find nothing.

p-values count ties AGAINST the finding (a pattern exactly as extreme as the real one
counts as extreme), the standard conservative choice. No confidence interval is
reported: success moves in steps of 1/25, so the test's p jumps at tied values and
no interval can agree with it exactly; the per-agent signs and per-house effects
show the spread instead.

Success is the primary metric. SPL is run through the same tests as a check.

    python scripts/test_target_effect.py            # writes results/tables/target_effect_tests.md
    python scripts/test_target_effect.py --selftest # checks the test machinery on known answers
"""
from __future__ import annotations

import argparse
import csv
import itertools
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "ppo_dino", "tdmpc2", "dreamerv3"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO+aug", "ppo_jepa": "PPO+JEPA", "ppo_mae": "PPO+MAE", "ppo_dino": "PPO+DINOv2",
        "tdmpc2": "TD-MPC2", "dreamerv3": "DreamerV3"}
SWAPPABLE = ["pair0", "pair1", "pair3", "pair4"]
CONTROL = "pair2"
SEEDS = range(5)
EPISODES = 25
OUT = ROOT / "results" / "tables" / "target_effect_tests.md"


# ----------------------------------------------------------------------------- data
def _summary(path: Path) -> Dict[str, Dict[str, str]]:
    with open(path) as f:
        return {r["level"]: r for r in csv.DictReader(f)}


def source_for(agent: str, cell: str) -> Path:
    """The one table holding BOTH L2noT and L2 for the agent that exists now.

    rerun_300000  : cells retrained because the saved model was gone
    evalonly_300000: original checkpoints re-evaluated with the L2noT rung
    grid_300000   : cells whose first (and only) run already included L2noT
    """
    name = f"{agent}_transfer_summary.csv"
    for tree in ("rerun_300000", "evalonly_300000", "grid_300000"):
        p = ROOT / "results" / tree / agent / cell / name
        if p.exists() and "L2noT" in _summary(p):
            return p
    raise FileNotFoundError(f"no table with L2noT for {agent}/{cell}")


def load(metric: str) -> Dict[str, Dict[str, List[Tuple[str, float, float, float]]]]:
    """agent -> house -> [(cell, A, L2noT, L2)] for metric 'success_rate' or 'spl'."""
    data: Dict[str, Dict[str, List[Tuple[str, float, float, float]]]] = {}
    for agent in AGENTS:
        data[agent] = {}
        for house in SWAPPABLE + [CONTROL]:
            rows = []
            for s in SEEDS:
                cell = f"{house}_seed{s}"
                R = _summary(source_for(agent, cell))
                for lvl in ("A", "L2noT", "L2"):
                    if int(R[lvl]["episodes"]) != EPISODES:
                        raise ValueError(f"{agent}/{cell}/{lvl}: {R[lvl]['episodes']} episodes")
                rows.append((cell, float(R["A"][metric]), float(R["L2noT"][metric]),
                             float(R["L2"][metric])))
            data[agent][house] = rows
    return data


# ------------------------------------------------------------------------ statistics
def sign_flip_exact(d: np.ndarray, tol: float) -> float:
    """Two-sided exact sign-flip p-value over all 2^n sign patterns."""
    n = len(d)
    obs = abs(d.sum())
    hits = 0
    total = 1 << n
    chunk = 1 << 16
    bits = np.arange(n, dtype=np.uint32)
    for start in range(0, total, chunk):
        idx = np.arange(start, min(start + chunk, total), dtype=np.uint32)
        signs = 1.0 - 2.0 * ((idx[:, None] >> bits) & 1).astype(np.float64)
        hits += int(np.count_nonzero(np.abs(signs @ d) >= obs - tol))
    return hits / total


def stratified_perm(da: Dict[str, np.ndarray], db: Dict[str, np.ndarray],
                    draws: int, rng: np.random.Generator, tol: float) -> Tuple[float, float]:
    """Shuffle agent-type labels within each house; statistic = mean(d_a) - mean(d_b)."""
    houses = sorted(da)
    obs = np.mean(np.concatenate([da[h] for h in houses])) - \
        np.mean(np.concatenate([db[h] for h in houses]))
    pools = [(np.concatenate([da[h], db[h]]), len(da[h])) for h in houses]
    na = sum(k for _p, k in pools)
    nb = sum(len(p) - k for p, k in pools)
    sa = np.zeros(draws)
    sb = np.zeros(draws)
    for pool, k in pools:
        # one independent random ordering of this house's agents per draw
        order = np.argsort(rng.random((draws, len(pool))), axis=1)
        perm = pool[order]
        sa += perm[:, :k].sum(axis=1)
        sb += perm[:, k:].sum(axis=1)
    hits = int(np.count_nonzero(np.abs(sa / na - sb / nb) >= abs(obs) - tol))
    return float(obs), (hits + 1) / (draws + 1)


def holm(pvals: List[float]) -> List[float]:
    order = np.argsort(pvals)
    m = len(pvals)
    adj = [0.0] * m
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (m - rank) * pvals[i]))
        adj[i] = running
    return adj


# ---------------------------------------------------------------------------- report
def analyse(metric: str, draws: int, seed: int) -> Tuple[List[str], dict]:
    data = load(metric)
    tol = 1e-9
    rng = np.random.default_rng(seed)
    lines: List[str] = []
    res: dict = {"within": {}, "between": {}, "control": {}}

    # 1. within agent type
    raw = []
    for agent in AGENTS:
        by_house = {h: np.array([r[2] - r[3] for r in data[agent][h]]) for h in SWAPPABLE}
        d = np.concatenate([by_house[h] for h in SWAPPABLE])
        if metric == "success_rate":   # counts of 25 episodes: exact integers
            k = d * EPISODES
            if not np.allclose(k, np.round(k), atol=1e-6):
                raise ValueError(f"{agent}: success is not a multiple of 1/{EPISODES}")
            p = sign_flip_exact(np.round(k), tol=0.5)
        else:
            p = sign_flip_exact(d, tol=tol)
        if abs(p - sign_flip_exact(d, tol=tol)) > 1e-12:
            raise AssertionError(f"{agent}: integer and float sign-flip p disagree")
        l2n = np.mean([r[2] for h in SWAPPABLE for r in data[agent][h]])
        l2 = np.mean([r[3] for h in SWAPPABLE for r in data[agent][h]])
        res["within"][agent] = dict(n=len(d), L2noT=l2n, L2=l2, effect=float(d.mean()),
                                    p=p, pos=int((d > tol).sum()), neg=int((d < -tol).sum()),
                                    zero=int((np.abs(d) <= tol).sum()),
                                    houses={h: float(by_house[h].mean()) for h in SWAPPABLE})
        raw.append(p)
    for agent, padj in zip(AGENTS, holm(raw)):
        res["within"][agent]["p_holm"] = padj

    # 2. between agent types
    raw_b, keys = [], []
    for a, b in itertools.combinations(AGENTS, 2):
        da = {h: np.array([r[2] - r[3] for r in data[a][h]]) for h in SWAPPABLE}
        db = {h: np.array([r[2] - r[3] for r in data[b][h]]) for h in SWAPPABLE}
        diff, p = stratified_perm(da, db, draws, rng, tol)
        res["between"][(a, b)] = dict(diff=diff, p=p)
        raw_b.append(p)
        keys.append((a, b))
    for key, padj in zip(keys, holm(raw_b)):
        res["between"][key]["p_holm"] = padj

    # 3. negative control
    for agent in AGENTS:
        d = np.array([r[2] - r[3] for r in data[agent][CONTROL]])
        if metric == "success_rate":
            p = sign_flip_exact(np.round(d * EPISODES), tol=0.5)
        else:
            p = sign_flip_exact(d, tol=tol)
        res["control"][agent] = dict(effect=float(d.mean()), p=p, max_abs=float(np.abs(d).max()))
    return lines, res


def fmt_p(p: float) -> str:
    return "<0.0001" if p < 1e-4 else f"{p:.4f}"


def render(res_s: dict, res_spl: dict, draws: int, seed: int) -> str:
    w = res_s["within"]
    out = [
        "# Target-appearance test: L2noT vs L2 (300k grid)",
        "",
        "Generated by `scripts/test_target_effect.py` -- do not edit by hand.",
        "",
        "**Question.** Does an agent do worse when ONLY the target object's appearance changes?",
        "L2noT and L2 differ in nothing else. Each agent is compared with itself, in one evaluation.",
        "",
        "**Effect** = success at L2noT minus success at L2, averaged over the 20 agents of each type",
        "in the four houses where the target was swapped (pair0, pair1, pair3, pair4). Positive = the",
        "agent does better when the target still looks like it did in training.",
        "",
        "## 1. Is there a target effect? (exact sign-flip test, all 2^20 patterns)",
        "",
        f"| agent | L2noT success | L2 success | effect | agents better / worse / same | p | p (Holm, {len(AGENTS)} tests) |",
        "|---|---|---|---|---|---|---|",
    ]
    for a in AGENTS:
        r = w[a]
        out.append(f"| {NICE[a]} | {r['L2noT']:.3f} | {r['L2']:.3f} | {r['effect']:+.3f} | "
                   f"{r['pos']} / {r['neg']} / {r['zero']} | "
                   f"{fmt_p(r['p'])} | {fmt_p(r['p_holm'])} |")
    out += ["", "Per house (mean effect, 5 agents each; too few for a test on their own -- "
            "the smallest possible two-sided p with 5 agents is 0.0625):", "",
            "| agent | " + " | ".join(SWAPPABLE) + " |", "|---" * (len(SWAPPABLE) + 1) + "|"]
    for a in AGENTS:
        out.append(f"| {NICE[a]} | " + " | ".join(f"{w[a]['houses'][h]:+.3f}" for h in SWAPPABLE) + " |")
    out += ["", "## 2. Is the target effect bigger for one agent type than another?",
            f"(stratified permutation within house, {draws:,} draws)", "",
            f"| comparison | difference in effect | p | p (Holm, {len(res_s['between'])} tests) |", "|---|---|---|---|"]
    for (a, b), r in res_s["between"].items():
        out.append(f"| {NICE[a]} minus {NICE[b]} | {r['diff']:+.3f} | {fmt_p(r['p'])} | {fmt_p(r['p_holm'])} |")
    out += ["", "## 3. Negative control: pair2 (L2noT and L2 are the same house file)", "",
            "| agent | effect | largest single-agent difference | p |", "|---|---|---|---|"]
    for a in AGENTS:
        r = res_s["control"][a]
        out.append(f"| {NICE[a]} | {r['effect']:+.3f} | {r['max_abs']:.2f} | {fmt_p(r['p'])} |")
    out += ["", "## 4. Same tests on SPL (check)", "",
            "| agent | effect | agents better / worse / same | p | p (Holm) |", "|---|---|---|---|---|"]
    for a in AGENTS:
        r = res_spl["within"][a]
        out.append(f"| {NICE[a]} | {r['effect']:+.3f} | {r['pos']} / {r['neg']} / {r['zero']} | "
                   f"{fmt_p(r['p'])} | {fmt_p(r['p_holm'])} |")
    out += ["", "| comparison (SPL) | difference | p (Holm) |", "|---|---|---|"]
    for (a, b), r in res_spl["between"].items():
        out.append(f"| {NICE[a]} minus {NICE[b]} | {r['diff']:+.3f} | {fmt_p(r['p_holm'])} |")
    counts = {}
    for a in AGENTS:
        c = {}
        for h in SWAPPABLE + [CONTROL]:
            for sd in SEEDS:
                tree = source_for(a, f"{h}_seed{sd}").parts[-4]
                c[tree] = c.get(tree, 0) + 1
        counts[a] = ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
    out += ["", "Where each agent type's 25 numbers came from: " +
            "; ".join(f"{NICE[a]}: {counts[a]}" for a in AGENTS) + "."]
    out += ["", f"Settings: permutation draws {draws:,}, random seed {seed}. "
            "Sources per agent: rerun_300000 if retrained, else evalonly_300000, else grid_300000."]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- selftest
def selftest() -> None:
    rng = np.random.default_rng(0)
    # all zero -> nothing is ever smaller than zero -> p = 1
    assert sign_flip_exact(np.zeros(10), tol=0.5) == 1.0
    # all equal and positive -> only the all-+ and all-- patterns reach it
    assert abs(sign_flip_exact(np.ones(12), tol=0.5) - 2 / 2 ** 12) < 1e-15
    # matches brute force on a small random integer vector
    d = rng.integers(-5, 6, 8).astype(float)
    brute = np.mean([abs(sum(s * x for s, x in zip(signs, d))) >= abs(d.sum()) - 0.5
                     for signs in itertools.product([1, -1], repeat=8)])
    assert abs(sign_flip_exact(d, tol=0.5) - brute) < 1e-15
    # identical groups -> no difference; clearly separated groups -> small p
    same = {h: np.array([1.0, 2.0, 3.0]) for h in "ab"}
    diff, p = stratified_perm(same, same, 2000, rng, 1e-9)
    assert diff == 0.0 and p == 1.0
    hi = {h: np.full(5, 10.0) for h in "abcd"}
    lo = {h: np.zeros(5) for h in "abcd"}
    _, p = stratified_perm(hi, lo, 5000, rng, 1e-9)
    assert p < 0.001, p
    # Holm: known example
    assert np.allclose(holm([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])
    print("selftest passed")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--draws", type=int, default=200_000)
    ap.add_argument("--seed", type=int, default=20260915)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    _l, res_s = analyse("success_rate", args.draws, args.seed)
    _l, res_spl = analyse("spl", args.draws, args.seed)
    OUT.write_text(render(res_s, res_spl, args.draws, args.seed))
    print(OUT.read_text())


if __name__ == "__main__":
    sys.exit(main())
