"""Significance tests for the single-change houses.

Every number comes from ONE evaluation pass (``results/factor_300000/``), in
which each trained agent was measured in all twelve houses. That matters: a
comparison between two rungs is a comparison of the SAME agent on the SAME day,
so it carries none of the pass-to-pass noise that forced an earlier pooled
L2noT table to be withdrawn.

THE TWO FAMILIES ARE FIXED HERE, BEFORE ANY NUMBER IS COMPUTED, and each is
Holm-corrected within itself.

FAMILY 1 -- which change hurts (within agent, paired, 3 questions x 6 agent
types = 18 tests). The unit is one trained agent; the statistic is the paired
difference in success between two houses that agent was measured in.
    Q1  repaint vs lighting      d = success(F_light) - success(F_mat)
    Q2  target vs other objects  d = success(F_obj)   - success(F_tgt)
    Q3  does clutter cost?       d = success(A)       - success(F_clut)
Q2 runs in the four houses whose target can be swapped (pair2 has no F_tgt
house), so n = 20; Q1 and Q3 use all 25.

FAMILY 2 -- who is robust to what (between agent, 2 changes x 3 comparisons =
6 tests). PPO's own CNN against each of the two frozen pretrained encoders and
against the decoder-free world model, on the two changes Family 1 identifies as
mattering. The statistic is the share of house-A success LOST, so agents of
different in-domain skill are comparable, and runs with house-A success below
0.5 are excluded (the rule fixed 2026-09-05).

TESTS
  within agent  : exact sign-flip over all 2^n patterns. Success moves in steps
                  of 1/25, so every possible sum is an integer multiple of 1/25
                  and the exact null distribution is computed by convolution --
                  no sampling, no approximation. Ties count AGAINST the finding.
  between agent : stratified permutation, labels shuffled WITHIN each house
                  (200k draws), which is what makes the large per-house spread
                  a nuisance rather than a confound.

    python scripts/test_single_change.py            # -> results/tables/single_change_tests.md
    python scripts/test_single_change.py --selftest
"""
from __future__ import annotations

import argparse
import csv
import glob
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from config import TABLES_DIR  # noqa: E402
from test_target_effect import holm, stratified_perm  # noqa: E402

GRID = "factor_300000"
AGENTS = ["ppo", "ppo_aug", "ppo_jepa", "ppo_mae", "ppo_dino", "tdmpc2", "dreamerv3"]
NICE = {"ppo": "PPO", "ppo_aug": "PPO + aug", "ppo_jepa": "PPO + JEPA",
        "ppo_mae": "PPO+MAE", "ppo_dino": "PPO+DINOv2", "tdmpc2": "TD-MPC2", "dreamerv3": "DreamerV3"}
SWAPPABLE = ["pair0", "pair1", "pair3", "pair4"]
CONTROL = "pair2"
MIN_A = 0.5
EPISODES = 25                      # success moves in steps of 1/25
TOL = 1e-9

# Family 1: (key, better-off house, worse-off house, houses, question)
WITHIN = [
    ("repaint_vs_light", "F_light", "F_mat", None,
     "Is repainting the walls and floor worse than changing the lighting?"),
    ("target_vs_others", "F_obj", "F_tgt", SWAPPABLE,
     "Is changing the target's look worse than changing every other object's?"),
    ("clutter_cost", "A", "F_clut", None,
     "Does adding clutter cost anything at all?"),
]
# Family 2: (change, agent a, agent b)
BETWEEN = [(rung, "ppo", b) for rung in ("F_mat", "F_tgt")
           for b in ("ppo_jepa", "ppo_mae", "tdmpc2")]


# ---------------------------------------------------------------------------- data
def load() -> Dict[Tuple[str, str, int, str], Tuple[float, float]]:
    """(agent, pair, seed, rung) -> (success, spl), from the one factor pass."""
    out: Dict[Tuple[str, str, int, str], Tuple[float, float]] = {}
    for f in sorted(glob.glob(str(ROOT / "results" / GRID / "*" / "*" / "*_transfer_summary.csv"))):
        p = Path(f)
        agent = p.parents[1].name
        pair, seed = p.parent.name.split("_seed")
        # csv.DictReader, not split(","): the variant column is a quoted
        # description that contains commas.
        with p.open(newline="") as fh:
            for row in csv.DictReader(fh):
                out[(agent, pair, int(seed), row["level"])] = (
                    float(row["success_rate"]), float(row["spl"]))
    if not out:
        raise SystemExit(f"no results under results/{GRID}/")
    return out


def cells(data, agent: str, houses) -> List[Tuple[str, int]]:
    seen = sorted({(p, s) for (a, p, s, _r) in data if a == agent
                   and (houses is None or p in houses)})
    return seen


# ---------------------------------------------------------------------------- exact test
def sign_flip_exact_counts(k: np.ndarray) -> float:
    """Exact two-sided sign-flip p-value for INTEGER-valued paired differences.

    Enumerating 2^25 sign patterns directly is 33M dot products; instead the
    null distribution of the signed sum is built by convolution, which is exact
    and instant. Zero differences are kept: they contribute no information but
    they do count in n, which is the conservative choice.
    """
    k = np.asarray(k, dtype=np.int64)
    span = int(np.abs(k).sum())
    if span == 0:
        return 1.0
    dist = np.zeros(2 * span + 1)
    dist[span] = 1.0                      # index = sum + span
    for v in k:
        v = int(abs(v))
        if v == 0:
            continue
        shifted = np.zeros_like(dist)
        if v:
            shifted[v:] += dist[:len(dist) - v] * 0.5
            shifted[:len(dist) - v] += dist[v:] * 0.5
        dist = shifted
    obs = int(abs(k.sum()))
    idx = np.arange(len(dist)) - span
    return float(dist[np.abs(idx) >= obs].sum())


def paired(data, agent: str, good: str, bad: str, houses, metric: int):
    """Per-agent paired differences success(good) - success(bad)."""
    rows = []
    for pair, seed in cells(data, agent, houses):
        a = data.get((agent, pair, seed, good))
        b = data.get((agent, pair, seed, bad))
        if a is None or b is None:
            continue
        rows.append((pair, a[metric], b[metric]))
    return rows


# ---------------------------------------------------------------------------- analysis
def analyse(data, metric: int) -> dict:
    res: dict = {"within": {}, "between": {}, "control": {}}

    pvals, keys = [], []
    for key, good, bad, houses, _q in WITHIN:
        for agent in AGENTS:
            rows = paired(data, agent, good, bad, houses, metric)
            d = np.array([g - b for _p, g, b in rows])
            if metric == 0:      # success: exact, on integer counts
                p = sign_flip_exact_counts(np.rint(d * EPISODES).astype(np.int64))
            else:                # SPL is continuous -> enumerate signs by sampling
                rng = np.random.default_rng(20260920)
                draws = 200_000
                signs = rng.choice([-1.0, 1.0], size=(draws, len(d)))
                p = (int(np.count_nonzero(np.abs(signs @ d) >= abs(d.sum()) - TOL)) + 1) / (draws + 1)
            res["within"][(key, agent)] = {
                "n": len(d), "mean_good": float(np.mean([g for _p, g, _b in rows])),
                "mean_bad": float(np.mean([b for _p, _g, b in rows])),
                "effect": float(d.mean()), "p_raw": p,
                "n_pos": int((d > 0).sum()), "n_neg": int((d < 0).sum()),
                "n_zero": int((d == 0).sum()),
            }
            pvals.append(p)
            keys.append((key, agent))
    for k, adj in zip(keys, holm(pvals)):
        res["within"][k]["p_holm"] = adj

    # Between agents: share of house-A success lost, per house, competent runs.
    def lost(agent: str, rung: str) -> Dict[str, np.ndarray]:
        by_house: Dict[str, List[float]] = {}
        for pair, seed in cells(data, agent, None):
            A = data.get((agent, pair, seed, "A"))
            B = data.get((agent, pair, seed, rung))
            if A is None or B is None or A[metric] < MIN_A:
                continue
            by_house.setdefault(pair, []).append((A[metric] - B[metric]) / A[metric])
        return {h: np.array(v) for h, v in by_house.items()}

    rng = np.random.default_rng(20260920)
    pvals, keys = [], []
    for rung, a, b in BETWEEN:
        da, db = lost(a, rung), lost(b, rung)
        houses = sorted(set(da) & set(db))
        da = {h: da[h] for h in houses}
        db = {h: db[h] for h in houses}
        obs, p = stratified_perm(da, db, 200_000, rng, TOL)
        res["between"][(rung, a, b)] = {
            "gap_pts": 100 * obs, "p_raw": p, "houses": len(houses),
            "na": sum(len(v) for v in da.values()), "nb": sum(len(v) for v in db.values()),
            "mean_a": 100 * float(np.mean(np.concatenate([da[h] for h in houses]))),
            "mean_b": 100 * float(np.mean(np.concatenate([db[h] for h in houses]))),
        }
        pvals.append(p)
        keys.append((rung, a, b))
    for k, adj in zip(keys, holm(pvals)):
        res["between"][k]["p_holm"] = adj

    # Negative control: pair2 has no target house, so its F_objall IS its F_obj
    # (nothing else can change). Any difference there is evaluation randomness.
    for agent in AGENTS:
        rows = paired(data, agent, "F_obj", "F_objall", [CONTROL], metric)
        d = np.array([g - b for _p, g, b in rows])
        p = (sign_flip_exact_counts(np.rint(d * EPISODES).astype(np.int64))
             if metric == 0 else float("nan"))
        res["control"][agent] = {"effect": float(d.mean()) if len(d) else 0.0,
                                 "n": len(d), "p_raw": p}
    return res


# ---------------------------------------------------------------------------- report
def fmt_p(p: float) -> str:
    if p != p:
        return "—"
    return "<0.0001" if p < 1e-4 else f"{p:.4f}" if p < 0.001 else f"{p:.3f}"


def render(rs: dict, rspl: dict) -> str:
    L = ["# Which single change hurts, and who survives it", "",
         "Generated by `scripts/test_single_change.py` — do not edit by hand. "
         f"All numbers from one evaluation pass (`results/{GRID}/`), 300k training steps, "
         "6 agent types × 5 house pairs × 5 training seeds.", "",
         "## Family 1 — which change hurts (same agent, same evaluation)", "",
         "One trained agent per row of the underlying data; the effect is the mean paired "
         "difference in success rate. Exact sign-flip test over every possible sign pattern; "
         "ties count against the finding. p Holm-corrected over the 18 tests in this family.", ""]
    for key, good, bad, houses, q in WITHIN:
        n_txt = "4 houses, n=20" if houses else "5 houses, n=25"
        L += [f"### {q}", "", f"`{good}` minus `{bad}` ({n_txt})", "",
              f"| agent | success in `{good}` | success in `{bad}` | difference | signs +/0/− | p | p (Holm) | SPL p (Holm) |",
              "|---|---|---|---|---|---|---|---|"]
        for agent in AGENTS:
            r = rs["within"][(key, agent)]
            s = rspl["within"][(key, agent)]
            L.append(f"| {NICE[agent]} | {r['mean_good']:.3f} | {r['mean_bad']:.3f} | "
                     f"{r['effect']:+.3f} | {r['n_pos']}/{r['n_zero']}/{r['n_neg']} | "
                     f"{fmt_p(r['p_raw'])} | **{fmt_p(r['p_holm'])}** | {fmt_p(s['p_holm'])} |")
        L.append("")

    L += ["## Family 2 — who is robust to what (between agents)", "",
          "Share of house-A success lost, runs with house-A success ≥ 0.5. "
          "Stratified permutation, labels shuffled within each house, 200k draws. "
          "A positive gap means the second agent loses LESS. p Holm-corrected over the 6 "
          "tests in this family.", "",
          "| change | agent A | agent B | A loses | B loses | gap (pts) | runs | p | p (Holm) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for rung, a, b in BETWEEN:
        r = rs["between"][(rung, a, b)]
        L.append(f"| `{rung}` | {NICE[a]} | {NICE[b]} | {r['mean_a']:.0f}% | {r['mean_b']:.0f}% | "
                 f"{r['mean_a'] - r['mean_b']:+.1f} | {r['na']}/{r['nb']} | "
                 f"{fmt_p(r['p_raw'])} | **{fmt_p(r['p_holm'])}** |")

    L += ["", "## Negative control", "",
          "pair2's target has no footprint-safe alternative, so its `F_obj` and `F_objall` "
          "are the SAME house. Any difference is evaluation randomness, and it bounds how "
          "much of an effect elsewhere could be noise.", "",
          "| agent | difference | n | p |", "|---|---|---|---|"]
    for agent in AGENTS:
        c = rs["control"][agent]
        L.append(f"| {NICE[agent]} | {c['effect']:+.3f} | {c['n']} | {fmt_p(c['p_raw'])} |")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------- self-test
def selftest() -> None:
    """The exact test must agree with brute-force enumeration, and must fail
    when it should. A check that cannot fail is not a check."""
    rng = np.random.default_rng(7)
    for _ in range(5):
        n = rng.integers(4, 13)
        k = rng.integers(-6, 7, size=n)
        # brute force over 2^n sign patterns
        total, obs, hits = 1 << n, abs(int(k.sum())), 0
        for m in range(total):
            signs = np.array([1 if (m >> i) & 1 == 0 else -1 for i in range(n)])
            hits += abs(int(signs @ k)) >= obs
        brute = hits / total
        got = sign_flip_exact_counts(k)
        assert abs(brute - got) < 1e-12, f"exact test wrong: {brute} vs {got}"
    # all-zero differences -> p = 1 exactly
    assert sign_flip_exact_counts(np.zeros(9, dtype=np.int64)) == 1.0
    # a strong one-sided effect must be significant
    assert sign_flip_exact_counts(np.full(12, 3, dtype=np.int64)) < 0.001
    # and a balanced one must not be
    assert sign_flip_exact_counts(np.array([3, -3, 3, -3, 3, -3], dtype=np.int64)) > 0.5
    print("selftest OK: exact test matches brute force on 5 random cases, "
          "and fires/stays silent where it must")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    selftest()
    data = load()
    rs, rspl = analyse(data, 0), analyse(data, 1)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    out = TABLES_DIR / "single_change_tests.md"
    out.write_text(render(rs, rspl))
    print(f"  wrote {out}")
    for key, _g, _b, _h, q in WITHIN:
        print(f"\n{q}")
        for agent in AGENTS:
            r = rs["within"][(key, agent)]
            print(f"   {NICE[agent]:12s} {r['effect']:+.3f}  Holm p={fmt_p(r['p_holm'])}")
    print("\nBetween agents (share of house-A success lost):")
    for rung, a, b in BETWEEN:
        r = rs["between"][(rung, a, b)]
        print(f"   {rung:7s} {NICE[a]} {r['mean_a']:.0f}% vs {NICE[b]} {r['mean_b']:.0f}%  "
              f"gap {r['mean_a'] - r['mean_b']:+.1f} pts  Holm p={fmt_p(r['p_holm'])}")


if __name__ == "__main__":
    main()
