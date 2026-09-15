"""Damage vs how much the image changed -- two panels.

(a) One point per house: how much the L1 shift changed the start-view image (x)
    against the share of house-A success agents lost at L1 (y, all four agent
    types averaged; the vertical line spans the lowest to highest agent type).
    Five points, because the image change is one measurement per house.
(b) One point per house per rung step (L1->L2noT other objects, L2noT->L2 the
    target, L2->L3 clutter): image change that step added (x) against success lost
    over the step (y), for PPO and DreamerV3 -- the agent types at the two ends of
    the target test. Marker shape = which step. All four agent types are in
    results/tables/visual_shift_analysis.md.

Form: two quantities against each other per unit -> scatter. Colour in (b) is
the same validated model-free blue / world-model aqua as every other figure;
identity there is also carried by the legend and by direct labels on the points
that matter, never colour alone. Panel (a) is one series, so no legend.

Numbers come from `scripts/analyze_visual_shift.py`, never retyped.

    python scripts/plot_visual_shift.py [--mode light|dark|both]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np

import analyze_visual_shift as avs
from plot_ladder import INK, SERIES

STEPS = [("L1->L2noT", "L1", "L2noT", "other objects' look", "o"),
         ("L2noT->L2", "L2noT", "L2", "target's look only", "^"),
         ("L2->L3", "L2", "L3", "clutter added", "s")]
SHOWN = ["ppo", "dreamerv3"]


def plot(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    surface, ink, muted, gridc, basec = INK[mode]
    shift = avs.load_shift()
    dmg = avs.l1_damage_by_house("grid")
    costs = avs.step_costs()
    houses = avs.HOUSES
    x = np.array([shift[h]["L1"]["mean_abs_diff"] for h in houses])
    per_type = np.array([[dmg[a][h] for a in avs.AGENTS] for h in houses])
    y = per_type.mean(axis=1)
    rho, p = avs.spearman_exact(x, y)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.2), facecolor=surface,
                                   gridspec_kw={"width_ratios": [1, 1.15]})
    for ax in (ax1, ax2):
        ax.set_facecolor(surface)
        ax.grid(color=gridc, linewidth=0.8, zorder=0)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        for sp in ("left", "bottom"):
            ax.spines[sp].set_color(basec)
        ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=8)

    # (a)
    for xi, lo, hi in zip(x, per_type.min(axis=1), per_type.max(axis=1)):
        ax1.plot([xi, xi], [100 * lo, 100 * hi], color=basec, linewidth=2.0,
                 solid_capstyle="round", zorder=2)
    ax1.scatter(x, 100 * y, s=70, color=ink, edgecolor=surface, linewidth=2.0, zorder=3)
    for h, xi, yi in zip(houses, x, y):
        ax1.annotate(h, (xi, 100 * yi), xytext=(8, 4), textcoords="offset points",
                     fontsize=8.5, color=ink)
    ax1.set_xlabel("image change at L1  (mean pixel difference, 0–255)", color=ink, fontsize=8.5)
    ax1.set_ylabel("share of house-A success lost at L1 (%)", color=ink, fontsize=8.5)
    ax1.set_ylim(-5, 105)
    ax1.set_xlim(0, max(x) * 1.15)
    ax1.set_title(f"(a) More image change ≠ more damage\n"
                  f"rank correlation {rho:+.2f}, p = {p:.2f} (5 houses)",
                  color=ink, fontsize=9.5, loc="left")

    # (b)
    for agent in SHOWN:
        light, dark, _dash, label = SERIES[agent]
        colour = light if mode == "light" else dark
        for key, prev, cur, _name, marker in STEPS:
            xs = [shift[h][cur]["mean_abs_diff"] - shift[h][prev]["mean_abs_diff"] for h in houses]
            ys = [costs[agent][h][key] for h in houses]
            ax2.scatter(xs, ys, s=110 if marker == "^" else 64, marker=marker, color=colour, edgecolor=surface,
                        linewidth=1.6, zorder=3)
            if agent == "ppo" and key == "L2noT->L2":
                for h, xi, yi in zip(houses, xs, ys):
                    if yi > 0.2:
                        ax2.annotate(f"PPO, {h}: target swap", (xi, yi), xytext=(10, -2),
                                     textcoords="offset points", fontsize=8, color=ink)
    ax2.axhline(0, color=muted, linewidth=1.0, zorder=1)
    ax2.set_xlabel("image change added by the step  (mean pixel difference)", color=ink, fontsize=8.5)
    ax2.set_ylabel("success lost over the step", color=ink, fontsize=8.5)
    ax2.set_title("(b) A change of ~1 to the target alone costs PPO the most\n"
                  "each point = one house; mean over its 5 agents",
                  color=ink, fontsize=9.5, loc="left")
    handles = [Line2D([0], [0], linestyle="", marker="o", markersize=7,
                      color=(SERIES[a][0] if mode == "light" else SERIES[a][1]), label=SERIES[a][3])
               for a in SHOWN]
    handles += [Line2D([0], [0], linestyle="", marker=m, markersize=7, color=muted, label=n)
                for _k, _p, _c, n, m in STEPS]
    ax2.legend(handles=handles, frameon=False, fontsize=8, labelcolor=ink, loc="upper right")

    fig.suptitle("Damage tracks WHAT changes more than how much  (300k training steps; image change "
                 "measured from the 25 fixed start views, no agent involved)",
                 color=ink, fontsize=10, x=0.008, ha="left", va="top", y=0.99)
    fig.tight_layout()
    fig.subplots_adjust(top=0.8)
    out = ROOT / "results" / "plots" / f"visual_shift_300k_{mode}.png"
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
