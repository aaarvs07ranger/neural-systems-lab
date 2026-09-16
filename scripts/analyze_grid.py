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

    python scripts/analyze_grid.py                 # 300k -> results/tables/grid_stats_300k.md
    python scripts/analyze_grid.py --grid grid     # 150k -> results/tables/grid_stats_150k.md

L2noT is not tested here: its within-agent test is scripts/test_target_effect.py.
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
ORDER = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "dreamerv3", "tdmpc2"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO+aug", "ppo_jepa": "PPO+JEPA",
        "ppo_mae": "PPO+MAE", "dreamerv3": "DreamerV3", "tdmpc2": "TD-MPC2"}


def load(grid: str) -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob(f"results/{grid}/*/*/*_transfer_summary.csv")):
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
    headline = []                          # success at L2: the pre-specified family
    for i, a in enumerate(present):
        for b in present[i + 1:]:
            print(f"\n    --- {NICE[a]} vs {NICE[b]} ---")
            for col, label in (("drop", "success"), ("spl_drop", "SPL")):
                for rung in RUNGS:
                    r = stratified_perm(d, a, b, rung, col, draws, rng)
                    if r is None:
                        continue
                    o, p, signs, k = r
                    if col == "drop" and rung == "L2":
                        headline.append((a, b, o, p))
                    star = " ***" if p < 0.01 else (" **" if p < 0.05
                                                    else ("  *" if p < 0.10 else ""))
                    print(f"      {label:<7} {rung}: {o:+6.1%}  p={p:.4f}  "
                          f"houses {signs} (n={k}){star}")

    if headline:
        ps = [h[3] for h in headline]
        order = np.argsort(ps)
        adj, run = [0.0] * len(ps), 0.0
        for rank, idx in enumerate(order):
            run = max(run, min(1.0, (len(ps) - rank) * ps[idx]))
            adj[idx] = run
        print("\n  HEADLINE FAMILY — success at L2, Holm-corrected over the "
              f"{len(ps)} pairwise comparisons")
        for (a, b, o, p), pa in zip(headline, adj):
            print(f"    {NICE[a]:>9} vs {NICE[b]:<9} {o:+6.1%}  p={p:.4f}  Holm p={pa:.4f}"
                  f"{'  significant' if pa < 0.05 else ''}")


def main() -> None:
    import contextlib, io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _main()
    text = buf.getvalue()
    print(text)
    grid = next((sys.argv[i + 1] for i, x in enumerate(sys.argv[:-1]) if x == "--grid"), "grid_300000")
    tag = "150k" if grid == "grid" else f"{int(grid.split('_')[1]) // 1000}k"
    out = Path("results/tables") / f"grid_stats_{tag}.md"
    out.write_text(f"# Grid statistics ({tag} steps)\n\nGenerated by `scripts/analyze_grid.py`"
                   " -- do not edit by hand. Statistic: mean gap in relative success/SPL drop"
                   " between two agent types, averaged over houses; positive = the SECOND agent"
                   " loses less. Labels shuffled within each house.\n\n```\n" + text + "```\n")
    print(f"  wrote {out}")


def _main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--draws", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=20260905)
    ap.add_argument("--grid", default="grid_300000")
    ap.add_argument("--min-competency", type=float, default=0.5,
                    help="house-A success floor for the robustness pass")
    args = ap.parse_args()

    d = load(args.grid)
    if d.empty:
        raise SystemExit(f"no grid results under results/{args.grid}/")
    report(d, args.draws, args.seed, "ALL RUNS (DreamerV3 relative drops here are distorted by runs that never learned house A)")

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
           f"RUNS WITH HOUSE-A SUCCESS >= {args.min_competency} (the set used for comparisons between agents)")
    print("\n  Compare the two blocks. Same conclusions => one line in the paper."
          "\n  Different => that difference IS the result and belongs in the main body.")


if __name__ == "__main__":
    main()
