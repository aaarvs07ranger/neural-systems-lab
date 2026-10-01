"""Colour distributions (R, G, B) of every house, and colour shift against drop.

Two figures, both from committed tables, never retyped:

  rgb_distributions_300k_<mode>.png
      One row per house pair, one column per colour channel. Each panel is the
      histogram of that channel over every pixel of the 25 fixed evaluation start
      views: house A filled in grey, and three rungs of the reordered ladder drawn
      on top in a light-to-dark ramp of the channel's own colour -- R2 (lighting &
      sky), R3 (+ object looks), R4 (+ walls, floor & ceiling = every change). R1
      (clutter) is left out: it is indistinguishable from house A at these views.
      The number in each panel is the Wasserstein-1 shift of the darkest line, in
      grey levels.

  rgb_shift_vs_drop_300k_<mode>.png
      (a)-(c) For each channel: that channel's shift (x, log scale) against the drop
      in success averaged over the agent types (y), one point per changed house.
      Shape and shade mark the kind of change: repainted walls/floor/ceiling,
      the goal object's look changed without a repaint, or anything else.
      (d)-(k) The same against the mean of R, G and B, one panel per agent type.
      Each panel prints the within-house rank correlation and its p (from
      `analyze_rgb_shift.py`).

Form: a distribution is drawn as a histogram line over a filled reference, so
the shift reads as one curve moving off another. Shift against drop is two
quantities per unit -> scatter. The channel ramps are the one place colour
carries data identity directly (red channel = red), and the column title says
it too; the kinds of change carry both a marker shape and a shade, never colour
alone.

    python scripts/plot_rgb_shift.py [--mode light|dark|both]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import analyze_rgb_shift as ars  # noqa: E402
from config import AGENT_NAME  # noqa: E402
from plot_ladder import INK, pair_meta  # noqa: E402

CHANNELS = [("w1_r", "red"), ("w1_g", "green"), ("w1_b", "blue")]
# Light-to-dark ramps per channel (R2, R3, R4), light and dark mode.
RAMP = {
    "light": {"red": ("#f2a5a0", "#de5a52", "#a8221b"),
              "green": ("#9fd8ae", "#3fae63", "#1e6e38"),
              "blue": ("#a9c6f2", "#4f86dd", "#1d4fa0")},
    "dark": {"red": ("#7a2e2a", "#d0524a", "#ff9a92"),
             "green": ("#245c35", "#3fae63", "#93e3a9"),
             "blue": ("#26457a", "#4f86dd", "#a3c3ff")},
}
RUNGS = [("R2", "R2: + lighting & sky"), ("R3", "R3: + object looks"),
         ("L3", "R4: + walls, floor & ceiling")]
KIND_STYLE = {  # kind: (marker, light shade, dark shade, size)
    "repaint": ("s", "#0b0b0b", "#ffffff", 34),
    "goal": ("^", "#eb6834", "#d95926", 46),
    "other": ("o", "#a6a59c", "#77766e", 30),
}
FLOOR = 0.05      # W1 below this is drawn at the floor of the log axis


def _style(ax, surface, ink, muted, gridc, basec):
    ax.set_facecolor(surface)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(basec)
    ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=7.5)


def distributions(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    surface, ink, muted, gridc, basec = INK[mode]
    hist = np.load(ROOT / "results" / "tables" / "rgb_hist.npz")
    shift = {(r["pair"], r["level"]): r for r in
             json.loads((ROOT / "results" / "tables" / "rgb_shift.json").read_text())}
    meta = pair_meta()
    pairs = sorted(meta, key=lambda p: meta[p]["cells"])
    fig, axes = plt.subplots(len(pairs), 3, figsize=(11.0, 2.0 * len(pairs) + 0.9),
                             sharex=True, facecolor=surface)
    grey = np.arange(256)
    kernel = np.ones(5) / 5                       # light smoothing, display only
    for i, pid in enumerate(pairs):
        for j, (key, cname) in enumerate(CHANNELS):
            ax = axes[i, j]
            _style(ax, surface, ink, muted, gridc, basec)
            a = hist[f"{pid}/A"][j].astype(float)
            a = np.convolve(a / a.sum(), kernel, mode="same")
            ax.fill_between(grey, a, color=basec, alpha=0.55, linewidth=0, zorder=1)
            peak = a.max()
            for (lvl, _lab), colour in zip(RUNGS, RAMP[mode][cname]):
                h = hist[f"{pid}/{lvl}"][j].astype(float)
                h = np.convolve(h / h.sum(), kernel, mode="same")
                peak = max(peak, h.max())
                ax.plot(grey, h, color=colour, linewidth=1.3, zorder=2)
            ax.set_ylim(0, peak * 1.12)
            ax.set_yticks([])
            w1 = shift[(pid, "L3")][key]
            ax.text(0.98, 0.9, f"W1 at R4 = {w1:.0f}", transform=ax.transAxes, ha="right",
                    va="top", fontsize=7.5, color=ink)
            if i == 0:
                ax.set_title(f"{cname} channel", color=ink, fontsize=9, loc="left")
            if j == 0:
                m = meta[pid]
                ax.set_ylabel(f"{pid}\n{m['target']}, {m['cells']} cells", color=ink,
                              fontsize=8, rotation=0, ha="right", va="center", labelpad=8)
        for ax in axes[-1]:
            ax.set_xlabel("pixel value (0-255)", color=ink, fontsize=8)
            ax.set_xlim(0, 255)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    handles = [Patch(color=basec, alpha=0.55, label="house A (training)")]
    for (lvl, lab), shade in zip(RUNGS, ("#c9c8c0", "#7d7c75", "#2b2b29") if mode == "light"
                                 else ("#5a5953", "#a6a59c", "#ecebe4")):
        handles.append(Line2D([0], [0], color=shade, linewidth=1.6, label=lab))
    fig.legend(handles=handles, frameon=False, fontsize=8, labelcolor=ink, ncol=4,
               loc="lower center", bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("How each house's colours shift along the reordered ladder  (every pixel of "
                 "the 25 fixed start views; lines darken as more changes are stacked; legend "
                 "shades stand for each channel's own ramp)", color=ink, fontsize=9.5,
                 x=0.008, ha="left", va="top", y=0.995)
    fig.tight_layout(rect=(0, 0.035, 1, 0.97))
    out = ROOT / "results" / "plots" / f"rgb_distributions_300k_{mode}.png"
    fig.savefig(out, dpi=220, facecolor=surface, bbox_inches="tight")
    plt.close(fig)
    return out


def shift_vs_drop(mode: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    surface, ink, muted, gridc, basec = INK[mode]
    res = json.loads((ROOT / "results" / "tables" / "rgb_shift_analysis.json").read_text())
    pts = res["per_point"]
    agents = res["agents"]
    kind = {v: k for v, _n, k in ars.VARIANTS}

    fig = plt.figure(figsize=(13.0, 9.6), facecolor=surface)
    gs = fig.add_gridspec(3, 4, height_ratios=[1.15, 1, 1], hspace=0.62, wspace=0.28)
    top = [fig.add_subplot(gs[0, c]) for c in range(3)]
    legend_ax = fig.add_subplot(gs[0, 3])
    legend_ax.axis("off")
    small = [fig.add_subplot(gs[1 + i // 4, i % 4]) for i in range(len(agents))]

    def scatter(ax, xs, ys, kinds):
        for k, (marker, cl, cd, size) in KIND_STYLE.items():
            sel = [i for i, kk in enumerate(kinds) if kk == k]
            ax.scatter([max(xs[i], FLOOR) for i in sel], [ys[i] for i in sel], marker=marker,
                       s=size, color=cl if mode == "light" else cd, edgecolor=surface,
                       linewidth=0.8, zorder=3)
        ax.set_xscale("log")
        ax.set_xlim(FLOOR * 0.8, 120)
        ax.axhline(0, color=muted, linewidth=0.9, zorder=1)
        ax.grid(color=gridc, linewidth=0.7, zorder=0)

    kinds = [kind[p["level"]] for p in pts]
    letters = "abcdefghijk"
    for j, ((key, cname), ax) in enumerate(zip(CHANNELS, top)):
        _style(ax, surface, ink, muted, gridc, basec)
        scatter(ax, [p[key] for p in pts], [p["drop_points_mean"] for p in pts], kinds)
        rho, pv = res["within"][f"{key}|all"]
        ax.set_title(f"({letters[j]}) {cname} channel\nrank corr. {rho:+.2f} "
                     f"(p {ars.fmt_p(pv)})", color=ink, fontsize=8.5, loc="left")
        ax.set_xlabel(f"{cname} shift, W1 (grey levels, log scale)", color=ink, fontsize=8)
    top[0].set_ylabel("drop in success rate (points)\nmean over agent types", color=ink,
                      fontsize=8)
    for i, (a, ax) in enumerate(zip(agents, small)):
        _style(ax, surface, ink, muted, gridc, basec)
        scatter(ax, [p["w1_mean"] for p in pts], [p["drop_points"][a] for p in pts], kinds)
        rho, pv = res["within"][f"w1_mean|{a}"]
        ax.set_title(f"({letters[3 + i]}) {AGENT_NAME[a]}\nrank corr. {rho:+.2f} "
                     f"(p {ars.fmt_p(pv)})", color=ink, fontsize=8.5, loc="left")
        ax.set_ylim(-25, 100)
        if i % 4 == 0:
            ax.set_ylabel("drop (points)", color=ink, fontsize=8)
        if i >= 4:
            ax.set_xlabel("W1, mean of R, G, B (log)", color=ink, fontsize=8)
    handles = [Line2D([0], [0], linestyle="", marker=m, markersize=7,
                      color=cl if mode == "light" else cd, label=ars.KIND_NAME[k])
               for k, (m, cl, cd, _s) in KIND_STYLE.items()]
    leg = legend_ax.legend(handles=handles, frameon=False, fontsize=8.5, labelcolor=ink,
                           loc="center left", title="one point = one changed house",
                           title_fontsize=8.5)
    leg.get_title().set_color(ink)
    legend_ax.text(0.0, 0.08, f"shifts below {FLOOR} drawn at {FLOOR}\n(clutter is nearly "
                   "invisible from the start views)", transform=legend_ax.transAxes,
                   fontsize=7.5, color=muted)
    fig.suptitle("Colour shift against drop in success  (300k training steps; 69 changed houses; "
                 "image change measured with no agent involved; drops from runs that learned "
                 "house A)\n(a)-(c): drop averaged over all agent types.  rank corr. = Spearman "
                 "correlation computed within each house, averaged over the 5 houses; p from "
                 "shuffling within houses", color=ink, fontsize=10, x=0.008, ha="left", va="top",
                 y=0.995, linespacing=1.5)
    out = ROOT / "results" / "plots" / f"rgb_shift_vs_drop_300k_{mode}.png"
    fig.savefig(out, dpi=220, facecolor=surface, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", choices=("light", "dark", "both"), default="both")
    a = ap.parse_args()
    for m in (("light", "dark") if a.mode == "both" else (a.mode,)):
        print(f"  wrote {distributions(m)}")
        print(f"  wrote {shift_vs_drop(m)}")


if __name__ == "__main__":
    main()
