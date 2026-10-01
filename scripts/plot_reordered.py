"""Reordered ladder figures: the same changes, stacked from least to most damaging.

Vishwas (2026-09-29) found the original L1/L2/L3 order confusing and asked for a
ladder that gets progressively worse. The reordered ladder stacks the same
appearance changes in the order the single-change pass ranked them: clutter,
then lighting & sky, then object looks, then walls, floor & ceiling. It is
CUMULATIVE (each rung keeps every change below it); R4 is the same house file as
the original L3.

  reordered_ladder_300k_<mode>.png
      Pooled over the five houses: success rate (every run) along A -> R1 -> R2
      -> R3 -> R4, one line per agent type, with its 95% CI band (stratified
      bootstrap, `robust_stats.py`). Direct labels at the right end.
  reordered_ladder_by_house_300k_success_<mode>.png
      One panel per house, mean ± 1 s.d. over the five training seeds, drawn by
      the same code as the original ladder figure (`plot_ladder.plot`).

Encoding as everywhere else: hue = how the agent decides (model-free blue,
model-free on a frozen encoder orange, world model aqua), dash pattern = which
member of the group (dots = frozen DINOv2 in both groups that have one).

    python scripts/plot_reordered.py [--mode light|dark|both]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import plot_ladder as pl  # noqa: E402
import robust_stats as rs  # noqa: E402
from config import REORDERED_LADDER, REORDERED_LADDER_300K  # noqa: E402

CODES = [c for c, _n in REORDERED_LADDER]
TICK = {"A": "A\ntrain", "F_clut": "R1\nclutter", "R2": "R2\n+ lighting\n& sky",
        "R3": "R3\n+ object\nlooks", "L3": "R4\n+ walls, floor\n& ceiling"}


def pooled(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, muted, gridc, basec = pl.INK[mode]
    res = rs.reordered()
    ag = res["agents"]
    x = np.arange(len(CODES))
    fig, ax = plt.subplots(figsize=(9.4, 4.6), facecolor=surface)
    ax.set_facecolor(surface)
    ax.grid(axis="y", color=gridc, linewidth=0.8, zorder=0)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.spines["bottom"].set_color(basec)
    ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=8.5)
    ends = []
    for a, rec in ag.items():
        cl, cd, dash, lab = pl.SERIES[a]
        colour = cl if mode == "light" else cd
        m = np.array([rec[c]["success"][0] for c in CODES])
        lo = np.array([rec[c]["success"][1] for c in CODES])
        hi = np.array([rec[c]["success"][2] for c in CODES])
        ax.fill_between(x, lo, hi, color=colour, alpha=0.10, linewidth=0, zorder=2)
        ax.plot(x, m, color=colour, linewidth=2.0, dashes=dash if dash else (None, None),
                marker="o", markersize=5, markeredgecolor=surface, markeredgewidth=1.2,
                zorder=3, solid_capstyle="round")
        ends.append([float(m[-1]), lab, colour])
    # Direct labels, nudged apart where the lines converge.
    ends.sort()
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < 0.052:
            ends[i][0] = ends[i - 1][0] + 0.052
    for y, lab, colour in ends:
        ax.annotate(lab, xy=(len(CODES) - 1, y), xytext=(12, 0), textcoords="offset points",
                    va="center", fontsize=8, color=ink, annotation_clip=False)
        ax.plot([len(CODES) - 1 + 0.07], [y], marker="s", markersize=4, color=colour,
                clip_on=False, zorder=4)
    ax.set_xticks(x, [TICK[c] for c in CODES], fontsize=8)
    ax.set_ylim(0, 1.04)
    ax.set_ylabel("success rate", color=ink, fontsize=9)
    n_dream = ag["dreamerv3"]["A"]["runs"] if "dreamerv3" in ag else 25
    fig.suptitle("The reordered ladder: the same changes, stacked from least to most damaging\n"
                 "Success rate pooled over 5 houses × 5 seeds (every run, "
                 f"{n_dream} per agent type), shaded band = 95% CI; cumulative: each rung keeps "
                 "the changes before it", color=ink, fontsize=10, x=0.008, ha="left", va="top",
                 y=0.995, linespacing=1.5)
    fig.subplots_adjust(left=0.08, right=0.79, top=0.86, bottom=0.17)
    out = ROOT / "results" / "plots" / f"reordered_ladder_300k_{mode}.png"
    fig.savefig(out, dpi=220, facecolor=surface, bbox_inches="tight")
    plt.close(fig)
    return out


SHORT = {"A": "A", "F_clut": "R1", "R2": "R2", "R3": "R3", "L3": "R4"}


def by_house(mode: str) -> Path:
    return pl.plot("success", mode, REORDERED_LADDER_300K, all_agents=False, rungs=CODES,
                   rung_label=SHORT, out_name="reordered_ladder_by_house_300k_success",
                   title="The reordered ladder, house by house (300k training steps; cumulative). "
                         "R1 clutter · R2 + lighting & sky · R3 + object looks · "
                         "R4 + walls, floor & ceiling")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=("light", "dark", "both"), default="both")
    a = ap.parse_args()
    for m in (("light", "dark") if a.mode == "both" else (a.mode,)):
        print(f"  wrote {pooled(m)}")
        print(f"  wrote {by_house(m)}")


if __name__ == "__main__":
    main()
