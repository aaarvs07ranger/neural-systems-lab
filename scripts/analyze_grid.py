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

Each comparison draws from its own random stream, seeded from the pair's names,
so adding an agent never changes another comparison's p-value.

These are the declared SIGNIFICANCE TESTS, on the relative drop they were
specified with (drop / house-A success). The paper leads with interval
estimates on drops in points instead (`scripts/robust_stats.py`, following
Agarwal et al. 2021); this file is the appendix record.

    python scripts/analyze_grid.py                 # 300k -> results/tables/grid_stats_300k.md
    python scripts/analyze_grid.py --grid ladder_150k   # 150k -> results/tables/grid_stats_150k.md

L2noT is not tested here: its within-agent test is scripts/test_target_effect.py.
"""
from __future__ import annotations

import argparse
import glob
import sys
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

from config import AGENT_NAME, AGENT_ORDER

RUNGS = ["L1", "L2", "L3"]
ORDER = list(AGENT_ORDER)
NICE = AGENT_NAME
# Agents present when each declared family was fixed. A family is NEVER grown by
# adding an agent later: that is exactly what the correction is meant to stop.
DINO_FAMILY_AGENTS = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "dreamerv3", "tdmpc2"]


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


def pair_rng(seed: int, a: str, b: str, rung: str, col: str) -> np.random.Generator:
    """One reproducible stream per comparison (crc32 is stable across runs)."""
    return np.random.default_rng([seed, zlib.crc32(f"{a}|{b}|{rung}|{col}".encode())])


def stratified_perm(d, a, b, rung, col, draws, seed):
    """Shuffle the baseline label within each house; statistic = mean gap."""
    rng = pair_rng(seed, a, b, rung, col)
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
    # All draws at once: one independent random ordering of each house's runs
    # per draw (argsort of uniforms is a uniform random permutation).
    diffs = np.zeros(draws)
    for pool, k in pools:
        perm = pool[np.argsort(rng.random((draws, len(pool))), axis=1)]
        diffs += perm[:, :k].mean(axis=1) - perm[:, k:].mean(axis=1)
    diffs /= len(pools)
    hits = int(np.count_nonzero(np.abs(diffs) >= abs(observed) - 1e-12))
    signs = "".join("+" if x > 0 else "-" for x in obs)
    return observed, (hits + 1) / (draws + 1), signs, len(pools)


def report(d: pd.DataFrame, draws: int, seed: int, title: str) -> None:
    present = [b for b in ORDER if b in set(d.baseline)]
    unknown = set(d.baseline) - set(ORDER)
    if unknown:
        raise SystemExit(f"agent(s) not in config.AGENT_ORDER: {sorted(unknown)}")
    print(f"\n{'='*78}\n{title}\n{'='*78}")
    n = d.groupby("baseline").apply(lambda g: g.pair.count() // len(RUNGS),
                                    include_groups=False)
    print("  cells per baseline:", {NICE[k]: int(v) for k, v in n.items()})
    print("\n  mean relative drop in success rate (drop / house-A success; pooled over houses and seeds)")
    pv = d.pivot_table(index="baseline", columns="rung", values="drop")
    print("    " + pv.reindex(present).round(3).to_string().replace("\n", "\n    "))

    print("\n  pairwise, stratified permutation over houses"
          "  (gap in relative drop; positive = the SECOND agent drops less)")
    headline = []                          # success at L2: the pre-specified family
    for i, a in enumerate(present):
        for b in present[i + 1:]:
            print(f"\n    --- {NICE[a]} vs {NICE[b]} ---")
            for col, label in (("drop", "success"), ("spl_drop", "SPL")):
                for rung in RUNGS:
                    r = stratified_perm(d, a, b, rung, col, draws, seed)
                    if r is None:
                        continue
                    o, p, signs, k = r
                    if col == "drop" and rung == "L2":
                        headline.append((a, b, o, p))
                    star = " ***" if p < 0.01 else (" **" if p < 0.05
                                                    else ("  *" if p < 0.10 else ""))
                    print(f"      {label:<7} {rung}: {o:+6.1%}  p={p:.4f}  "
                          f"houses {signs} (n={k}){star}")

    def report_family(title: str, provenance: str, rows) -> None:
        """Holm-correct WITHIN a declared family and print it with its provenance.

        Which comparisons belong together is a decision, not a fact, and it
        changes the answer: the same PPO+aug vs TD-MPC2 gap was significant
        under six comparisons and not under fifteen. So every family is printed
        with the date it was fixed and whether any of its numbers had been seen
        first. Nothing here is chosen after the fact for being favourable; the
        conservative all-pairs family is always reported alongside.
        """
        rows = [r for r in rows if r is not None]
        if not rows:
            return
        ps = [r[3] for r in rows]
        order = np.argsort(ps)
        adj, run = [0.0] * len(ps), 0.0
        for rank, idx in enumerate(order):
            run = max(run, min(1.0, (len(ps) - rank) * ps[idx]))
            adj[idx] = run
        print(f"\n  {title}  ({len(ps)} comparisons, Holm-corrected within this family)")
        print(f"    provenance: {provenance}")
        for (a, b, o, p), pa in zip(rows, adj):
            print(f"    {NICE[a]:>14} vs {NICE[b]:<14} {o:+6.1%}  p={p:.4f}  Holm p={pa:.4f}"
                  f"{'  significant' if pa < 0.05 else ''}")

    report_family(
        "ALL-PAIRS FAMILY — success at L2",
        "every pair of agents present, corrected together. The conservative "
        "reading, and the one to quote if only one family is reported.",
        headline)

    # The four agents the benchmark was designed around, whose comparisons were
    # fixed before any pretrained-encoder agent existed.
    ORIGINAL = ["ppo", "ppo_aug", "dreamerv3", "tdmpc2"]
    orig = [h for h in headline if h[0] in ORIGINAL and h[1] in ORIGINAL]
    report_family(
        "ORIGINAL-FOUR FAMILY — success at L2",
        "fixed 2026-09-05, before ppo_jepa, ppo_mae or ppo_dino existed; "
        "reported because adding agents later must not retroactively weaken a "
        "test that was specified first.",
        orig)

    # Does the strongest available frozen encoder help? One agent against each
    # of the others, at the rung where every agent breaks.
    dino = []
    for a in DINO_FAMILY_AGENTS:
        if a not in present:
            continue
        r = stratified_perm(d, a, "ppo_dino", "L1", "drop", draws, seed)
        if r is not None:
            dino.append((a, "ppo_dino", r[0], r[1]))
    report_family(
        "DINOv2 FAMILY — success at L1",
        "fixed 2026-09-21, after DINOv2's mean damage had been seen but before "
        "any p-value was computed. Stated rather than hidden. Its six members are "
        "the agents that existed then; TD-MPC2+DINOv2 has its own family below.",
        dino)

    # Does a world model that plans gain from the same frozen encoder? The
    # eighth agent against each of the other seven, at the same rung.
    if "tdmpc2_dino" in present:
        tdd = []
        for a in present:
            if a == "tdmpc2_dino":
                continue
            r = stratified_perm(d, a, "tdmpc2_dino", "L1", "drop", draws, seed)
            if r is not None:
                tdd.append((a, "tdmpc2_dino", r[0], r[1]))
        report_family(
            "TD-MPC2+DINOv2 FAMILY — success at L1",
            "fixed 2026-09-30, after TD-MPC2+DINOv2's ladder means and interval "
            "estimates had been seen but before any p-value was computed. Stated "
            "rather than hidden.",
            tdd)


def main() -> None:
    import contextlib, io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _main()
    text = buf.getvalue()
    print(text)
    grid = next((sys.argv[i + 1] for i, x in enumerate(sys.argv[:-1]) if x == "--grid"), "ladder_300k")
    from config import budget_tag
    tag = budget_tag(grid)
    out = Path("results/tables") / f"grid_stats_{tag}.md"
    out.write_text(f"# Grid statistics ({tag} steps)\n\nGenerated by `scripts/analyze_grid.py`"
                   " -- do not edit by hand. Statistic: mean gap in the RELATIVE drop in success"
                   " rate (or SPL) between two agent types, i.e. drop / house-A success, averaged"
                   " over houses; positive = the SECOND agent drops less. Labels shuffled within"
                   " each house. These are the declared significance tests (appendix); the paper"
                   " leads with drops in percentage points and their 95% CIs in"
                   " `grid_ci_<budget>.md`.\n\n```\n" + text + "```\n")
    print(f"  wrote {out}")


def _main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--draws", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=20260905)
    ap.add_argument("--grid", default="ladder_300k")
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
