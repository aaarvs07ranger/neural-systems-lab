"""Target-control figure: does changing ONLY the target's appearance hurt?

Form: the quantity is one signed difference per agent (success with the target
unchanged minus with it changed), and the question is whether those differences
sit above zero, house by house. So: a dot per trained agent, a short bar at the
house mean, and a strong zero line. Small multiples by agent type -- identity is
carried by the panel title, not by colour, so no categorical-palette limit applies.

Colour: the same two validated hues as the ladder figure, carrying the same
meaning (model-free blue, world model aqua). pair2 is drawn in neutral grey: its
two houses are the same file, so it is the negative control, not a data point.

Numbers come from `scripts/test_target_effect.py` (same agent, one evaluation;
exact sign-flip test, Holm-corrected), never retyped.

    python scripts/plot_target_effect.py [--mode light|dark|both]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np

import test_target_effect as tte
from plot_ladder import INK, SERIES

ORDER = ["ppo", "ppo_aug", "tdmpc2", "dreamerv3"]
HOUSES = tte.SWAPPABLE + [tte.CONTROL]
HOUSE_LABEL = {"pair0": "pair0\nFridge", "pair1": "pair1\nBed", "pair3": "pair3\nBed",
               "pair4": "pair4\nTV", "pair2": "pair2\ncontrol"}


def plot(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, muted, gridc, basec = INK[mode]
    data = tte.load("success_rate")
    _l, res = tte.analyse("success_rate", draws=200_000, seed=20260915)

    fig, axes = plt.subplots(1, len(ORDER), figsize=(12.5, 3.6), sharey=True, facecolor=surface)
    x = np.arange(len(HOUSES), dtype=float)
    x[-1] += 0.6                                    # gap before the control
    jitter = np.linspace(-0.16, 0.16, 5)
    for ax, agent in zip(axes, ORDER):
        light, dark, _dash, label = SERIES[agent]
        colour = light if mode == "light" else dark
        ax.set_facecolor(surface)
        ax.grid(axis="y", color=gridc, linewidth=0.8, zorder=0)
        for sp in ("top", "right", "left", "bottom"):
            ax.spines[sp].set_visible(False)
        ax.axhline(0, color=muted, linewidth=1.2, zorder=1)
        ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=8)
        for xi, h in zip(x, HOUSES):
            d = np.array([r[2] - r[3] for r in data[agent][h]])
            c = basec if h == tte.CONTROL else colour
            ax.scatter(xi + jitter, d, s=34, color=c, edgecolor=surface, linewidth=1.4, zorder=3)
            ax.plot([xi - 0.26, xi + 0.26], [d.mean()] * 2, color=ink, linewidth=2.0,
                    solid_capstyle="round", zorder=4)
        r = res["within"][agent]
        p = r["p_holm"]
        ax.set_title(f"{label}\nmean {r['effect']:+.2f}, p = {p:.3f}", color=ink, fontsize=9,
                     loc="left", pad=8)
        ax.set_xticks(x, [HOUSE_LABEL[h] for h in HOUSES], fontsize=7.5)
    axes[0].set_ylabel("success, target unchanged\nminus success, target changed", color=ink, fontsize=8.5)
    fig.suptitle("Does changing only the target's appearance hurt?  (300k training steps; "
                 "dot = one trained agent, bar = house mean; pair2's two houses are identical)\n"
                 "p: exact sign-flip test over the 20 agents in pair0/1/3/4, Holm-corrected over 4 agent types",
                 color=ink, fontsize=9.5, x=0.008, ha="left", va="top", y=0.99, linespacing=1.5)
    fig.tight_layout()
    fig.subplots_adjust(top=0.72)          # room for the two-line figure title
    out = ROOT / "results" / "plots" / f"target_effect_300k_{mode}.png"
    fig.savefig(out, dpi=220, facecolor=surface, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=("light", "dark", "both"), default="both")
    a = ap.parse_args()
    for m in (("light", "dark") if a.mode == "both" else (a.mode,)):
        print(f"  wrote {plot(m)}")


if __name__ == "__main__":
    main()
