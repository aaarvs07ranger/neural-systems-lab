"""One change at a time — the figure.

(a) The ranking. Rows are the six single changes, ordered by how much damage
    they do; the x-axis is the share of house-A success lost. One dot per agent,
    a bar at the mean. The point of the panel is that the ordering is the same
    for every agent: one change out of six does nearly all the damage, and the
    two axes this benchmark was built around — object appearance and clutter —
    cost almost nothing on their own.

(b) Do the parts add up? Predicted (the single losses added together) against
    actual (the cumulative rung), one point per agent, with the identity line.
    Below it, damage saturates: the agent was already broken. Above it, the
    combination costs more than its pieces.

Form: a ranking of categories is a dot plot with the categories on the y-axis,
never a bar chart with rotated labels. Panel (b) is two quantities per unit, so
a scatter against an identity line.

Colour follows the same rule as every other figure: hue = architecture class
(model-free blue, frozen encoder orange, world model aqua), and identity is
never colour-alone — the legend names every agent, and in (b) each point is
labelled directly. In (a) the agents are deliberately NOT distinguished, because
the panel's claim is about what they share.

Numbers come from `scripts/summarize_single_change.py`, never retyped.

    python scripts/plot_single_change.py [--mode light|dark|both]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import summarize_single_change as ssc  # noqa: E402
from plot_ladder import INK, SERIES  # noqa: E402

RANKED = ssc.RANKED
LABEL = {"F_clut": "clutter added", "F_light": "lighting", "F_sky": "sky",
         "F_obj": "objects, not the target", "F_tgt": "the target only",
         "F_mat": "walls, floor, ceiling"}
WHOLE = "L3"          # the top rung: every single change, stacked


def plot(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, muted, gridc, basec = INK[mode]
    data = ssc.load()
    agents = [a for a in ssc.AGENTS if any(k[0] == a for k in data)]
    dmg = {a: {k: ssc.mean(v for _h, v in ssc.lost(data, a, k)) for k in RANKED}
           for a in agents}
    order = sorted(RANKED, key=lambda k: ssc.mean(dmg[a][k] for a in agents))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 4.6), facecolor=surface,
                                   gridspec_kw={"width_ratios": [1.45, 1]})
    for ax in (ax1, ax2):
        ax.set_facecolor(surface)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        for sp in ("left", "bottom"):
            ax.spines[sp].set_color(basec)
        ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=8.5)

    # ---- (a) the ranking ---------------------------------------------------
    ax1.grid(axis="x", color=gridc, linewidth=0.8, zorder=0)
    ys = np.arange(len(order))
    for y, key in zip(ys, order):
        vals = np.array([100 * dmg[a][key] for a in agents])
        ax1.scatter(vals, np.full_like(vals, y, dtype=float), s=46, color=basec,
                    edgecolor=surface, linewidth=1.4, zorder=3)
        ax1.plot([vals.mean()] * 2, [y - 0.26, y + 0.26], color=ink, linewidth=2.4,
                 solid_capstyle="round", zorder=4)
        ax1.annotate(f"{vals.mean():.0f}%", (vals.mean(), y + 0.36), color=ink,
                     fontsize=8.5, ha="center")
    ax1.axvline(0, color=muted, linewidth=1.0, zorder=1)
    ax1.set_yticks(ys, [LABEL[k] for k in order], fontsize=9)
    ax1.set_ylim(-0.7, len(order) - 0.2)
    ax1.set_xlabel("share of house-A success lost (%)", color=ink, fontsize=8.5)
    ax1.set_title("(a) Repainting the room is the change that matters\n"
                  "one dot per agent type, bar at the mean; every other change is nearly free",
                  color=ink, fontsize=9.5, loc="left")

    # ---- (b) parts against whole ------------------------------------------
    ax2.grid(color=gridc, linewidth=0.8, zorder=0)
    parts = dict(ssc.DECOMPOSE)[WHOLE]
    xs, ys2 = [], []
    for a in agents:
        # F_objall is in the decomposition but not in the ranking set, so the
        # prediction is computed from the data rather than from `dmg`.
        pred = 100 * sum(ssc.mean(v for _h, v in ssc.lost(data, a, p)) for p in parts)
        act = 100 * ssc.mean(v for _h, v in ssc.lost(data, a, WHOLE))
        light, dark, _dash, label = SERIES[a]
        colour = light if mode == "light" else dark
        ax2.scatter([pred], [act], s=70, color=colour, edgecolor=surface,
                    linewidth=1.6, zorder=3)
        ax2.annotate(label.replace(" (frozen)", ""), (pred, act), xytext=(7, -3),
                     textcoords="offset points", fontsize=8, color=ink)
        xs.append(pred)
        ys2.append(act)
    lim = max(max(xs), max(ys2)) * 1.18
    ax2.plot([0, lim], [0, lim], color=muted, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    ax2.annotate("parts add up exactly", (lim * 0.62, lim * 0.62), rotation=38,
                 color=muted, fontsize=8, ha="center", va="bottom")
    ax2.set_xlim(0, lim)
    ax2.set_ylim(0, lim)
    ax2.set_xlabel("the single changes, added together (%)", color=ink, fontsize=8.5)
    ax2.set_ylabel("measured when stacked (%)", color=ink, fontsize=8.5)
    ax2.set_title("(b) Below the line, damage saturates;\nabove it, the combination costs extra",
                  color=ink, fontsize=9.5, loc="left")
    # No legend: every point carries its own label, so a legend would repeat
    # seven names and cover the plotting area to say nothing new.

    fig.suptitle("Each change on its own (300k training steps; 7 agent types x 5 house pairs "
                 "x 5 seeds, runs with house-A success ≥ 0.5)",
                 color=ink, fontsize=10, x=0.008, ha="left", va="top", y=0.995)
    fig.tight_layout()
    fig.subplots_adjust(top=0.79)
    out = ROOT / "results" / "plots" / f"single_change_300k_{mode}.png"
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
