"""Every statistical claim in the paper, computed from the committed CSVs.

Consolidates the tests that were run ad hoc while the grid filled up, so each
one is reproducible, versioned, and impossible to quote from memory.

THE TEST. Comparing two agents by pooling all 25 of each agent's runs would mix
an easy house with a hard one; house difficulty moves both agents together and
is not what we are testing. So the baseline label is shuffled WITHIN each house,
the statistic is the mean difference across houses, and the p-value is the
fraction of shuffles reaching the observed value. Five seeds per cell make an
exact enumeration per house cheap (252 assignments), but the across-house
statistic has 252^5 combinations, so it is sampled.

THE ROBUSTNESS CHECK. Every number is a drop relative to that run's own house-A
score, which is what makes cross-baseline comparison fair. A run whose house-A
score is low has a noisy denominator. `--min-competency` repeats the whole
analysis excluding those runs. It exists because DreamerV3 produced two runs at
house-A success 0.36 where its other eight were 0.92-1.00, and the threshold was
fixed BEFORE its transfer numbers were looked at, so the choice cannot be fitted
to the answer.

    python scripts/analyze_grid.py
    python scripts/analyze_grid.py --min-competency 0.5
"""
from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

RUNGS = ["L1", "L2", "L3"]
ORDER = ["ppo", "ppo_aug", "dreamerv3", "tdmpc2"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO+aug", "dreamerv3": "DreamerV3",
        "tdmpc2": "TD-MPC2"}


def load() -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob("results/grid/*/*/*_transfer_summary.csv")):
        p = Path(f)
        baseline, (pair, seed) = p.parents[1].name, p.parent.name.split("_seed")
        df = pd.read_csv(f).set_index("level")
        A, AS = df.loc["A", "success_rate"], df.loc["A", "spl"]
        for rung in RUNGS:
            if rung not in df.index or not A or not AS:
                continue
            rows.append(dict(baseline=baseline, pair=pair, seed=int(seed),
                             rung=rung, A_success=A,
                             drop=(A - df.loc[rung, "success_rate"]) / A,
                             spl_drop=(AS - df.loc[rung, "spl"]) / AS))
    return pd.DataFrame(rows)


def stratified_perm(d, a, b, rung, col, draws, rng):
    """Shuffle the baseline label within each house; statistic = mean gap."""
    sub = d[d.rung == rung]
    obs, pools = [], []
    for pair in sorted(sub.pair.unique()):
        xa = sub[(sub.pair == pair) & (sub.baseline == a)][col].values
        xb = sub[(sub.pair == pair) & (sub.baseline == b)][col].values
        if len(xa) < 2 or len(xb) < 2:
            continue                       # a house one agent has not finished
        obs.append(xa.mean() - xb.mean())
        pools.append((np.concatenate([xa, xb]), len(xa)))
    if not pools:
        return None
    observed = float(np.mean(obs))
    hits = 0
    for _ in range(draws):
        diffs = []
        for pool, k in pools:
            idx = rng.permutation(len(pool))
            diffs.append(pool[idx[:k]].mean() - pool[idx[k:]].mean())
        hits += abs(float(np.mean(diffs))) >= abs(observed) - 1e-12
    signs = "".join("+" if x > 0 else "-" for x in obs)
    return observed, (hits + 1) / (draws + 1), signs, len(pools)


def report(d: pd.DataFrame, draws: int, seed: int, title: str) -> None:
    rng = np.random.default_rng(seed)
    present = [b for b in ORDER if b in set(d.baseline)]
    print(f"\n{'='*78}\n{title}\n{'='*78}")
    n = d.groupby("baseline").apply(lambda g: g.pair.count() // len(RUNGS),
                                    include_groups=False)
    print("  cells per baseline:", {NICE[k]: int(v) for k, v in n.items()})
    print("\n  mean relative drop (pooled over houses and seeds)")
    pv = d.pivot_table(index="baseline", columns="rung", values="drop")
    print("    " + pv.reindex(present).round(3).to_string().replace("\n", "\n    "))

    print("\n  pairwise, stratified permutation over houses"
          "  (positive = the SECOND agent is more robust)")
    for i, a in enumerate(present):
        for b in present[i + 1:]:
            print(f"\n    --- {NICE[a]} vs {NICE[b]} ---")
            for col, label in (("drop", "success"), ("spl_drop", "SPL")):
                for rung in RUNGS:
                    r = stratified_perm(d, a, b, rung, col, draws, rng)
                    if r is None:
                        continue
                    o, p, signs, k = r
                    star = " ***" if p < 0.01 else (" **" if p < 0.05
                                                    else ("  *" if p < 0.10 else ""))
                    print(f"      {label:<7} {rung}: {o:+6.1%}  p={p:.4f}  "
                          f"houses {signs} (n={k}){star}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--draws", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=20260905)
    ap.add_argument("--min-competency", type=float, default=0.5,
                    help="house-A success floor for the robustness pass")
    args = ap.parse_args()

    d = load()
    if d.empty:
        raise SystemExit("no grid results under results/grid/")
    report(d, args.draws, args.seed, "ALL RUNS (headline)")

    weak = d[d.A_success < args.min_competency]
    if weak.empty:
        print(f"\n  robustness pass: no run has house-A success below "
              f"{args.min_competency}; headline stands unqualified.")
        return
    n_weak = weak.groupby("baseline").apply(lambda g: g.pair.count() // len(RUNGS),
                                            include_groups=False)
    print(f"\n  {int(n_weak.sum())} run(s) below house-A success "
          f"{args.min_competency}: {{{', '.join(f'{NICE[k]}: {int(v)}' for k, v in n_weak.items())}}}")
    report(d[d.A_success >= args.min_competency], args.draws, args.seed,
           f"ROBUSTNESS: excluding runs with house-A success < {args.min_competency}")
    print("\n  Compare the two blocks. Same conclusions => one line in the paper."
          "\n  Different => that difference IS the result and belongs in the main body.")


if __name__ == "__main__":
    main()
