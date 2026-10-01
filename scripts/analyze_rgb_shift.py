"""How much did each changed house's IMAGES change, and does that predict the drop?

Vishwas, 2026-09-29: quantify the image change with the per-channel (red,
green, blue) pixel distributions at each level, and relate it to the drop in
success. RL researchers already know that visual shift hurts; the question is
whether the amount of shift explains the size of the drop.

IMAGE CHANGE (`scripts/measure_rgb_shift.py`, no agent involved). At the 25
pinned evaluation start views, every pixel of every view goes into one
256-bin histogram per colour channel, for house A and for the changed house.
The distance is Wasserstein-1 (earth mover's distance) between the two
histograms, in grey levels on the 0-255 scale: how far, on average, the pixel
values had to move to turn one distribution into the other. One number per
channel per changed house. Also reported: the mean per-pixel difference, which
compares the same pixel in both images (W1 ignores where a pixel is).

DROP. House-A success minus success in the changed house, in percentage points,
same trained agent, from the evaluation pass that measured that house: the
single-change pass for the twelve houses it holds (each change alone, plus L1,
L2noT, L2, L3), the reordered-ladder pass for the three only it holds (R2, R3,
lighting & sky). Runs that learned house A (house-A success >= 0.5); a house's
drop is the mean over its runs.

UNIT. One changed house: 69 of them (5 pairs x 14 variants; pair2 has no
goal-only house because its goal object cannot be swapped). Every agent in a
house sees the same images, so the image change is one measurement per house
variant, whichever agent is being scored.

TESTS. Spearman rank correlation between image change and drop.
  pooled       across all 69: mixes "this house is hard" with "this change is big".
  within house the rank correlation inside each house (13-14 variants), averaged
               over the 5 houses. p from a permutation test that shuffles the
               drops among the variants WITHIN each house (100,000 draws, two-
               sided). This asks the dose-response question with each house's
               difficulty held fixed. The variants in a house are nested (L1
               contains F_mat), so this is descriptive evidence of an ordering,
               not 69 independent experiments.

    python scripts/analyze_rgb_shift.py            # -> results/tables/rgb_shift_analysis.md (+ .json)
    python scripts/analyze_rgb_shift.py --selftest
"""
from __future__ import annotations

import argparse
import json
import sys
import zlib
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import robust_stats as rs  # noqa: E402
from config import (  # noqa: E402
    AGENT_NAME, AGENT_ORDER, REORDERED_LADDER_300K, SINGLE_CHANGE_300K, TABLES_DIR,
)

DRAWS = 100_000
SEED = 20260930
HOUSES = ["pair0", "pair1", "pair2", "pair3", "pair4"]
# Every changed house, with a plain name and the kind of change it is.
# kind: "repaint" = includes the wall/floor/ceiling change; "goal" = the goal
# object's look changes and the room is NOT repainted; "other" = neither.
VARIANTS: List[Tuple[str, str, str]] = [
    ("F_clut", "clutter", "other"),
    ("F_light", "lighting", "other"),
    ("F_sky", "sky", "other"),
    ("F_lightsky", "lighting & sky", "other"),
    ("F_obj", "object looks, goal unchanged", "other"),
    ("R2", "R2: clutter + lighting & sky", "other"),
    ("F_tgt", "goal object's look only", "goal"),
    ("F_objall", "all object looks", "goal"),
    ("R3", "R3: + object looks", "goal"),
    ("F_mat", "walls, floor & ceiling", "repaint"),
    ("L1", "L1: walls/floor/ceiling + light + sky", "repaint"),
    ("L2noT", "L2noT: L1 + object looks, goal unchanged", "repaint"),
    ("L2", "L2: L1 + all object looks", "repaint"),
    ("L3", "L3 = R4: every change", "repaint"),
]
FROM_REORDERED = {"R2", "R3", "F_lightsky"}
PREDICTORS = [("w1_mean", "W1, mean of R, G, B"), ("w1_r", "W1, red"), ("w1_g", "W1, green"),
              ("w1_b", "W1, blue"), ("mean_abs_diff", "mean per-pixel difference")]
KIND_NAME = {"repaint": "includes walls/floor/ceiling",
             "goal": "goal object's look changed, no repaint",
             "other": "other changes, no repaint"}


# ----------------------------------------------------------------------- data
def load_shift() -> Dict[Tuple[str, str], Dict[str, float]]:
    rows = json.loads((ROOT / "results" / "tables" / "rgb_shift.json").read_text())
    out = {(r["pair"], r["level"]): {k: float(r[k]) for k, _n in PREDICTORS} for r in rows}
    want = {(h, v) for h in HOUSES for v, _n, _k in VARIANTS if not (h == "pair2" and v == "F_tgt")}
    missing = sorted(want - set(out))
    if missing:
        raise ValueError(f"rgb_shift.json is missing {missing}")
    return out


def load_drops() -> Dict[str, Dict[Tuple[str, str], float]]:
    """agent -> (house, variant) -> mean drop in success (fraction), runs that learned A."""
    single = rs.load_set(SINGLE_CHANGE_300K)
    reord = rs.load_set(REORDERED_LADDER_300K)
    out: Dict[str, Dict[Tuple[str, str], float]] = {}
    agents = [a for a in AGENT_ORDER if a in set(single.baseline)]
    for a in agents:
        out[a] = {}
        for v, _n, _k in VARIANTS:
            src = reord if v in FROM_REORDERED else single
            for h, vals in rs.drops(src, a, v).items():
                out[a][(h, v)] = float(vals.mean())
    return out


# ------------------------------------------------------------------ statistics
def ranks(x: np.ndarray) -> np.ndarray:
    """Average ranks (ties share the mean of their positions)."""
    order = np.argsort(x, kind="mergesort")
    r = np.empty(len(x))
    xs = x[order]
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and xs[j + 1] == xs[i]:
            j += 1
        r[order[i:j + 1]] = 0.5 * (i + j) + 1
        i = j + 1
    return r


def spearman(x: np.ndarray, y: np.ndarray) -> float:
    rx, ry = ranks(x) - (len(x) + 1) / 2, ranks(y) - (len(y) + 1) / 2
    den = np.sqrt((rx @ rx) * (ry @ ry))
    return float(rx @ ry / den) if den else 0.0


def within_house(xs: Dict[str, np.ndarray], ys: Dict[str, np.ndarray], label: str,
                 draws: int = DRAWS) -> Tuple[float, float]:
    """Mean over houses of the within-house Spearman rho, and its permutation p.

    Shuffling y within a house permutes its ranks, which leaves each house's rank
    norms unchanged, so every draw's rho is one dot product per house.
    """
    rng = np.random.default_rng([SEED, zlib.crc32(label.encode())])
    obs, null = [], np.zeros(draws)
    for h in sorted(xs):
        rx = ranks(xs[h]) - (len(xs[h]) + 1) / 2
        ry = ranks(ys[h]) - (len(ys[h]) + 1) / 2
        den = np.sqrt((rx @ rx) * (ry @ ry))
        obs.append(float(rx @ ry / den) if den else 0.0)
        perm = ry[np.argsort(rng.random((draws, len(ry))), axis=1)]
        null += (perm @ rx) / den if den else 0.0
    null /= len(xs)
    rho = float(np.mean(obs))
    p = (int(np.count_nonzero(np.abs(null) >= abs(rho) - 1e-12)) + 1) / (draws + 1)
    return rho, p


# ----------------------------------------------------------------------- run
def analyse() -> Dict:
    shift = load_shift()
    drops = load_drops()
    agents = list(drops)
    keys = [(h, v) for h in HOUSES for v, _n, _k in VARIANTS if (h, v) in shift]
    for a in agents:
        lack = [k for k in keys if k not in drops[a]]
        if lack:
            raise ValueError(f"{a}: no drop for {lack}")
    mean_drop = {k: float(np.mean([drops[a][k] for a in agents])) for k in keys}
    series = {**{a: drops[a] for a in agents}, "all": mean_drop}
    res: Dict = {"agents": agents, "points": len(keys), "draws": DRAWS, "seed": SEED,
                 "pooled": {}, "within": {}, "per_point": []}
    for k in keys:
        res["per_point"].append({"pair": k[0], "level": k[1], **shift[k],
                                 "drop_points": {a: 100 * drops[a][k] for a in agents},
                                 "drop_points_mean": 100 * mean_drop[k]})
    for pred, _name in PREDICTORS:
        x_all = np.array([shift[k][pred] for k in keys])
        for s, ser in series.items():
            y_all = np.array([ser[k] for k in keys])
            res["pooled"][f"{pred}|{s}"] = spearman(x_all, y_all)
            xs = {h: np.array([shift[k][pred] for k in keys if k[0] == h]) for h in HOUSES}
            ys = {h: np.array([ser[k] for k in keys if k[0] == h]) for h in HOUSES}
            res["within"][f"{pred}|{s}"] = within_house(xs, ys, f"{pred}|{s}")
    # Dose or switch? The repaint houses have both the largest image change and
    # the largest drops, so a high correlation could be nothing more than "repaint
    # or not". Repeat inside each kind: does MORE change bring MORE damage among
    # the changes that leave the walls alone, and among those that repaint them?
    kind = {v: k for v, _n, k in VARIANTS}
    res["by_kind"] = {}
    for group, members in (("no_repaint", {"other", "goal"}), ("repaint", {"repaint"})):
        sub = [k for k in keys if kind[k[1]] in members]
        for pred in ("w1_mean", "mean_abs_diff"):
            for s, ser in series.items():
                xs = {h: np.array([shift[k][pred] for k in sub if k[0] == h]) for h in HOUSES}
                ys = {h: np.array([ser[k] for k in sub if k[0] == h]) for h in HOUSES}
                res["by_kind"][f"{group}|{pred}|{s}"] = within_house(xs, ys, f"{group}|{pred}|{s}")
    return res


def r0(x: float) -> str:
    t = f"{x:.0f}"
    return "0" if t == "-0" else t


def fmt_p(p: float) -> str:
    return "<0.0001" if p < 1e-4 else f"{p:.4f}" if p < 0.001 else f"{p:.3f}"


def render(res: Dict) -> str:
    agents = res["agents"]
    pts = {(r["pair"], r["level"]): r for r in res["per_point"]}
    names = {v: n for v, n, _k in VARIANTS}
    L = ["# Colour shift (R, G, B) vs drop in success (300k training steps)", "",
         "Generated by `scripts/analyze_rgb_shift.py` -- do not edit by hand.", "",
         "**Image change** = Wasserstein-1 distance between house A's and the changed house's "
         "histogram of one colour channel, over every pixel of the 25 fixed evaluation start "
         "views, in grey levels (0-255): how far pixel values had to move on average. No agent "
         "involved. **Drop** = house-A success minus success in the changed house, in percentage "
         "points, same agent, runs that learned house A. One point = one changed house: "
         f"{res['points']} of them (5 house pairs × 14 variants; pair2 has no goal-only house).",
         "",
         "## 1. How much each change moves the colour distributions", "",
         "W1 averaged over R, G and B, per house pair (grey levels), with the drop in success "
         f"averaged over the {len(agents)} agent types beside it.", "",
         "| change | " + " | ".join(f"{h} W1" for h in HOUSES) + " | mean drop, all agent types (points) |",
         "|---|" + "---|" * len(HOUSES) + "---|"]
    for v, n, _k in VARIANTS:
        cells = [f"{pts[(h, v)]['w1_mean']:.1f}" if (h, v) in pts else "—" for h in HOUSES]
        md = np.mean([pts[(h, v)]["drop_points_mean"] for h in HOUSES if (h, v) in pts])
        L.append(f"| {n} | " + " | ".join(cells) + f" | {md:.0f} |")
    L += ["", "Per channel, averaged over the five houses (grey levels):", "",
          "| change | red | green | blue |", "|---|---|---|---|"]
    for v, n, _k in VARIANTS:
        hs = [h for h in HOUSES if (h, v) in pts]
        L.append(f"| {n} | " + " | ".join(
            f"{np.mean([pts[(h, v)][c] for h in hs]):.1f}" for c in ("w1_r", "w1_g", "w1_b")) + " |")

    L += ["", "## 2. Does a bigger colour shift bring a bigger drop?", "",
          "Spearman rank correlation between image change and drop. **Within house** = computed "
          "inside each house, then averaged over the 5 houses, so a hard house cannot pass for a "
          f"big change; p from shuffling drops among variants within each house ({res['draws']:,} "
          "draws). **Pooled** = across all points at once (descriptive only).", "",
          "### Within house (rank correlation; p)", "",
          "| image change | " + " | ".join(AGENT_NAME[a] for a in agents) + " | all agent types |",
          "|---|" + "---|" * (len(agents) + 1)]
    for pred, pname in PREDICTORS:
        cells = []
        for s in agents + ["all"]:
            rho, p = res["within"][f"{pred}|{s}"]
            cells.append(f"{rho:+.2f} ({fmt_p(p)})")
        L.append(f"| {pname} | " + " | ".join(cells) + " |")
    L += ["", "### Pooled across all points (rank correlation)", "",
          "| image change | " + " | ".join(AGENT_NAME[a] for a in agents) + " | all agent types |",
          "|---|" + "---|" * (len(agents) + 1)]
    for pred, pname in PREDICTORS:
        L.append(f"| {pname} | " + " | ".join(
            f"{res['pooled'][f'{pred}|{s}']:+.2f}" for s in agents + ["all"]) + " |")

    L += ["", "### Dose or switch? The same within-house test inside each kind of change", "",
          "The repaint houses have both the largest image change and the largest drops, so the "
          "correlations above could mean no more than \"repainted or not\". Here the test is "
          "repeated among the changes that leave the walls, floor and ceiling alone (9 per house, "
          "8 in pair2) and among the five that repaint them.", "",
          "| kind of change | image change | " + " | ".join(AGENT_NAME[a] for a in agents)
          + " | all agent types |", "|---|---|" + "---|" * (len(agents) + 1)]
    for group, gname in (("no_repaint", "walls/floor/ceiling unchanged"),
                         ("repaint", "walls/floor/ceiling repainted")):
        for pred, pname in (("w1_mean", "W1, mean of R, G, B"),
                            ("mean_abs_diff", "mean per-pixel difference")):
            cells = []
            for s in agents + ["all"]:
                rho, p = res["by_kind"][f"{group}|{pred}|{s}"]
                cells.append(f"{rho:+.2f} ({fmt_p(p)})")
            L.append(f"| {gname} | {pname} | " + " | ".join(cells) + " |")

    L += ["", "## 3. Where the amount of change fails as an explanation", "",
          "The goal object's look on its own barely moves the colour distributions, yet for some "
          "agents it costs more than lighting or sky changes that move them several times as far "
          "(compare the first rows), and clutter moves them about as little and costs nothing. "
          "Mean over the four houses that have a goal-only house (pair2 does not):", "",
          "| change | W1, mean of R, G, B | " + " | ".join(AGENT_NAME[a] for a in agents) + " |",
          "|---|---|" + "---|" * len(agents)]
    for v in ("F_tgt", "F_light", "F_lightsky", "F_sky", "F_clut", "F_mat"):
        hs = [h for h in HOUSES if (h, v) in pts and (h, "F_tgt") in pts]
        L.append(f"| {names[v]} | {np.mean([pts[(h, v)]['w1_mean'] for h in hs]):.1f} | " + " | ".join(
            r0(np.mean([pts[(h, v)]['drop_points'][a] for h in hs])) for a in agents) + " |")
    L += ["", "Drops in percentage points. Houses: pair0, pair1, pair3, pair4."]
    return "\n".join(L) + "\n"


def selftest() -> None:
    x = np.arange(10.0)
    assert abs(spearman(x, x * 3 + 1) - 1) < 1e-12
    assert abs(spearman(x, -x) + 1) < 1e-12
    assert np.allclose(ranks(np.array([3.0, 1.0, 3.0, 2.0])), [3.5, 1.0, 3.5, 2.0])
    # A perfect ordering in every house must be rare under shuffling; noise must not be.
    xs = {h: np.arange(12.0) for h in "abcde"}
    rho, p = within_house(xs, {h: v * 2 for h, v in xs.items()}, "selftest1", draws=20_000)
    assert abs(rho - 1) < 1e-12 and p < 0.001, (rho, p)
    rng = np.random.default_rng(3)
    rho, p = within_house(xs, {h: rng.normal(size=12) for h in xs}, "selftest2", draws=20_000)
    assert p > 0.01, (rho, p)
    # Cross-check against scipy where available.
    try:
        from scipy.stats import spearmanr
        for _ in range(20):
            a, b = rng.normal(size=9), rng.normal(size=9)
            assert abs(spearman(a, b) - spearmanr(a, b)[0]) < 1e-12
        print("spearman matches scipy")
    except ImportError:
        print("scipy not installed; skipped the scipy cross-check")
    print("selftest passed")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return
    selftest()
    res = analyse()
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    (TABLES_DIR / "rgb_shift_analysis.json").write_text(json.dumps(res, indent=1) + "\n")
    out = TABLES_DIR / "rgb_shift_analysis.md"
    out.write_text(render(res))
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
