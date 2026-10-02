"""Paper-sized versions of the result figures (CoRL text width, 5.5 in).

The figures in results/plots/ are built for screens: 16 in wide with titles
baked in. Shrunk to a 5.5 in column their text lands near 3 pt. These are the
same data and the same encodings, re-laid out for print: no embedded titles
(the caption carries them), 6-7 pt text, vector PDF.

    python scripts/plot_paper_figures.py      # -> paper_v2/figures/{ladder,reordered,single_change}.pdf

Encoding follows plot_ladder.py: hue = architecture class (model-free blue,
frozen pretrained encoder orange, world model aqua), dash = member within the
class, and every series is named in a legend, so identity never rests on colour.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import numpy as np  # noqa: E402

import plot_ladder as pl  # noqa: E402
import robust_stats as rs  # noqa: E402
import summarize_single_change as ssc  # noqa: E402
from config import AGENT_NAME, LADDER_300K, REORDERED_LADDER  # noqa: E402

OUT = ROOT / "paper_v2" / "figures"     # the first draft in paper/ is frozen
TEXTWIDTH = 5.5
LABEL = AGENT_NAME
INK, MUTED, GRID, BASE = "#0b0b0b", "#52514e", "#e1e0d9", "#c3c2b7"


def _style():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": "serif", "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "mathtext.fontset": "stix", "font.size": 7, "axes.titlesize": 7,
        "axes.labelsize": 7, "xtick.labelsize": 6.5, "ytick.labelsize": 6.5,
        "legend.fontsize": 6.5, "pdf.fonttype": 42, "ps.fonttype": 42,
    })
    return plt


def _clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(BASE)
        ax.spines[s].set_linewidth(0.6)
    ax.tick_params(colors=MUTED, labelcolor=INK, length=0, pad=2)


def ladder() -> Path:
    plt = _style()
    from matplotlib.lines import Line2D

    d = pl.load(LADDER_300K, all_agents=False)
    meta = pl.pair_meta()
    pairs = sorted(d.pair.unique(), key=lambda p: meta[p]["cells"])
    fig, axes = plt.subplots(2, 3, figsize=(TEXTWIDTH, 3.0), sharey=True)
    x = np.arange(len(pl.RUNGS))
    for ax, pid in zip(axes.flat, pairs):
        _clean(ax)
        ax.grid(axis="y", color=GRID, linewidth=0.5, zorder=0)
        for b, (colour, _cd, dash, _lab) in pl.SERIES.items():
            sub = d[(d.baseline == b) & (d.pair == pid)]
            if sub.empty:
                continue
            g = sub.groupby("rung")["success"].agg(["mean", "std"]).reindex(pl.RUNGS)
            ax.fill_between(x, (g["mean"] - g["std"]).clip(0, 1),
                            (g["mean"] + g["std"]).clip(0, 1),
                            color=colour, alpha=0.08, linewidth=0, zorder=2)
            ax.plot(x, g["mean"], color=colour, linewidth=1.1,
                    dashes=dash if dash else (None, None), marker="o", markersize=2.6,
                    markeredgecolor="white", markeredgewidth=0.5, zorder=3)
        m = meta[pid]
        title = f"{pid.replace('pair', 'P')}: {m['target']}, {m['cells']} cells"
        if not m["swappable"]:
            title += " (target not swapped)"
        ax.set_title(title, loc="left", pad=3, color=INK)
        ax.set_xticks(x, pl.RUNGS)
        ax.set_ylim(-0.03, 1.05)
        ax.set_yticks([0, 0.5, 1.0])
    for ax in axes[:, 0]:
        ax.set_ylabel("success rate")
    # Sixth cell carries the legend.
    leg_ax = axes.flat[-1]
    leg_ax.axis("off")
    handles = [Line2D([0], [0], color=c, linewidth=1.1, dashes=dash if dash else (None, None),
                      marker="o", markersize=2.6, markeredgecolor="white",
                      markeredgewidth=0.5, label=LABEL[b])
               for b, (c, _cd, dash, _l) in pl.SERIES.items()]
    leg_ax.legend(handles=handles, loc="center", frameon=False, handlelength=2.6,
                  labelspacing=0.45)
    fig.tight_layout(pad=0.3, h_pad=0.9, w_pad=0.6)
    out = OUT / "ladder.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=220)
    plt.close(fig)
    return out


def single_change() -> Path:
    plt = _style()
    data = ssc.load()
    agents = [a for a in ssc.AGENTS if any(k[0] == a for k in data)]
    dmg = {a: {k: ssc.mean(v for _h, v in ssc.drop(data, a, k)) for k in ssc.RANKED}
           for a in agents}
    order = sorted(ssc.RANKED, key=lambda k: ssc.mean(dmg[a][k] for a in agents))
    names = {"F_clut": "clutter", "F_light": "lighting", "F_obj": "objects (not goal)",
             "F_sky": "sky", "F_tgt": "goal object only", "F_mat": "walls/floor/ceiling"}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.05),
                                   gridspec_kw={"width_ratios": [1.35, 1]})
    for ax in (ax1, ax2):
        _clean(ax)

    ax1.grid(axis="x", color=GRID, linewidth=0.5, zorder=0)
    for y, key in enumerate(order):
        for a in agents:
            colour = pl.SERIES[a][0]
            ax1.scatter(100 * dmg[a][key], y, s=9, color=colour, edgecolor="white",
                        linewidth=0.4, zorder=3)
        mu = 100 * ssc.mean(dmg[a][key] for a in agents)
        ax1.plot([mu, mu], [y - 0.3, y + 0.3], color=INK, linewidth=1.3, zorder=4)
        ax1.annotate(f"{0 if abs(mu) < 0.5 else mu:.0f}", (mu, y + 0.32), ha="center", va="bottom", fontsize=6)
    ax1.axvline(0, color=MUTED, linewidth=0.5)
    ax1.set_yticks(range(len(order)), [names[k] for k in order])
    ax1.set_ylim(-0.6, len(order) - 0.15)
    ax1.set_xlabel("drop in success rate from house A (points)")
    ax1.set_title("(a) one change at a time", loc="left", pad=3)

    ax2.grid(color=GRID, linewidth=0.5, zorder=0)
    parts = dict(ssc.DECOMPOSE)["L3"]
    pts = []
    for a in agents:
        pred = 100 * sum(ssc.mean(v for _h, v in ssc.drop(data, a, p)) for p in parts)
        act = 100 * ssc.mean(v for _h, v in ssc.drop(data, a, "L3"))
        pts.append((a, pred, act))
        ax2.scatter(pred, act, s=14, color=pl.SERIES[a][0], edgecolor="white",
                    linewidth=0.4, zorder=3)
    # Hand-placed offsets (points) so the eight labels do not collide at 6 pt.
    off = {"ppo": (0, -9), "ppo_aug": (4, -3), "ppo_jepa": (-4, 3), "ppo_mae": (4, 1),
           "ppo_dino": (4, -3), "tdmpc2": (4, -1), "dreamerv3": (-4, 3),
           "tdmpc2_dino": (4, -4)}
    for a, pred, act in pts:
        dx, dy = off.get(a, (4, 0))
        ax2.annotate(LABEL[a], (pred, act), xytext=(dx, dy), textcoords="offset points",
                     fontsize=6, ha="right" if dx < 0 else ("center" if dx == 0 else "left"),
                     color=INK)
    ax2.plot([0, 110], [0, 110], color=MUTED, linewidth=0.7, linestyle=(0, (3, 2)), zorder=1)
    ax2.set_xlim(0, 110)
    ax2.set_ylim(0, 110)
    ax2.set_xticks([0, 25, 50, 75, 100])
    ax2.set_yticks([0, 25, 50, 75, 100])
    ax2.set_xlabel("single changes' drops, summed (points)")
    ax2.set_ylabel("drop measured at L3 (points)")
    ax2.set_title("(b) do the parts add up?", loc="left", pad=3)
    fig.tight_layout(pad=0.3, w_pad=1.2)
    out = OUT / "single_change.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=220)
    plt.close(fig)
    return out


def reordered() -> Path:
    """Pooled success along the reordered (cumulative) ladder, 95% CI bands."""
    plt = _style()
    res = rs.reordered()["agents"]
    codes = [c for c, _n in REORDERED_LADDER]
    ticks = ["A", "R1\nclutter", "R2\n+ light\n& sky", "R3\n+ object\nlooks",
             "R4\n+ walls,\nfloor, ceiling"]
    fig, ax = plt.subplots(figsize=(TEXTWIDTH * 0.72, 2.4))
    _clean(ax)
    ax.grid(axis="y", color=GRID, linewidth=0.5, zorder=0)
    x = np.arange(len(codes))
    for b, (colour, _cd, dash, _lab) in pl.SERIES.items():
        if b not in res:
            continue
        s = np.array([res[b][c]["success"] for c in codes])
        ax.fill_between(x, s[:, 1], s[:, 2], color=colour, alpha=0.09, linewidth=0, zorder=2)
        ax.plot(x, s[:, 0], color=colour, linewidth=1.1, dashes=dash if dash else (None, None),
                marker="o", markersize=2.6, markeredgecolor="white", markeredgewidth=0.5,
                zorder=3, label=LABEL[b])
    ax.set_xticks(x, ticks)
    ax.set_ylim(0, 1.03)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_ylabel("success rate")
    ax.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False, handlelength=2.6,
              labelspacing=0.4)
    fig.tight_layout(pad=0.3)
    out = OUT / "reordered.pdf"
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), dpi=220, bbox_inches="tight")
    plt.close(fig)
    return out


# Kind of change, for the colour-shift figures. Colour here marks the KIND of
# change, never the agent, so it stays clear of the agent palette; shape repeats it.
KIND_STYLE = {"repaint": ("s", INK, 10, "includes walls/floor/ceiling"),
              "goal": ("^", "#b03a2e", 13, "goal object's look changed, no repaint"),
              "other": ("o", "#a6a59c", 9, "other changes, no repaint")}
CHANNEL_RAMP = {"red": ("#f2a5a0", "#de5a52", "#a8221b"),
                "green": ("#9fd8ae", "#3fae63", "#1e6e38"),
                "blue": ("#a9c6f2", "#4f86dd", "#1d4fa0")}


def _rgb_results():
    import json
    import analyze_rgb_shift as ars
    res = json.loads((ROOT / "results" / "tables" / "rgb_shift_analysis.json").read_text())
    kind = {v: k for v, _n, k in ars.VARIANTS}
    return res, kind


def _shift_panel(ax, pts, kind, who):
    for k, (marker, colour, size, _lab) in KIND_STYLE.items():
        sel = [q for q in pts if kind[q["level"]] == k]
        ax.scatter([max(q["w1_mean"], 0.05) for q in sel],
                   [q["drop_points_mean"] if who == "all" else q["drop_points"][who] for q in sel],
                   marker=marker, s=size, color=colour, edgecolor="white", linewidth=0.3, zorder=3)
    ax.set_xscale("log")
    ax.set_xlim(0.04, 120)
    ax.axhline(0, color=MUTED, linewidth=0.5, zorder=1)
    ax.grid(color=GRID, linewidth=0.5, zorder=0)


def rgb() -> Path:
    """Body figure: colour shift against drop, all agents averaged, PPO, TD-MPC2+DINOv2."""
    plt = _style()
    from matplotlib.lines import Line2D
    res, kind = _rgb_results()
    pts = res["per_point"]
    panels = [("all", "(a) mean over the eight agents"), ("ppo", "(b) PPO"),
              ("tdmpc2_dino", "(c) TD-MPC2+DINOv2")]
    fig, axes = plt.subplots(1, 3, figsize=(TEXTWIDTH, 2.05), sharey=True)
    for ax, (who, title) in zip(axes, panels):
        _clean(ax)
        _shift_panel(ax, pts, kind, who)
        rho = res["within"][f"w1_mean|{who}"][0]
        ax.set_title(f"{title}\nwithin-house rank corr. {rho:+.2f}", loc="left", pad=3)
        ax.set_xlabel("colour shift, W1 (grey levels)")
    axes[0].set_ylabel("drop in success rate (points)")
    axes[0].set_ylim(-20, 95)
    handles = [Line2D([0], [0], linestyle="", marker=m, markersize=3.6, color=c, label=lab)
               for m, c, _s, lab in KIND_STYLE.values()]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False,
               bbox_to_anchor=(0.5, -0.02), handletextpad=0.3, columnspacing=1.2)
    fig.tight_layout(pad=0.3, w_pad=0.8, rect=(0, 0.08, 1, 1))
    out = OUT / "rgb_shift.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=220)
    plt.close(fig)
    return out


def rgb_by_agent() -> Path:
    """Appendix: the same scatter for every agent type."""
    plt = _style()
    res, kind = _rgb_results()
    pts = res["per_point"]
    agents = res["agents"]
    fig, axes = plt.subplots(2, 4, figsize=(TEXTWIDTH, 3.0), sharex=True, sharey=True)
    for ax, a in zip(axes.flat, agents):
        _clean(ax)
        _shift_panel(ax, pts, kind, a)
        rho = res["within"][f"w1_mean|{a}"][0]
        ax.set_title(f"{LABEL[a]}  ({rho:+.2f})", loc="left", pad=2)
    for ax in axes[:, 0]:
        ax.set_ylabel("drop (points)")
    for ax in axes[-1]:
        ax.set_xlabel("W1 (grey levels)")
    axes[0][0].set_ylim(-25, 100)
    fig.tight_layout(pad=0.3, h_pad=0.6, w_pad=0.4)
    out = OUT / "rgb_by_agent.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=220)
    plt.close(fig)
    return out


def rgb_distributions() -> Path:
    """Appendix: R, G, B histograms of house A and three reordered rungs, every house."""
    plt = _style()
    import json
    hist = np.load(ROOT / "results" / "tables" / "rgb_hist.npz")
    shift = {(r["pair"], r["level"]): r for r in
             json.loads((ROOT / "results" / "tables" / "rgb_shift.json").read_text())}
    meta = pl.pair_meta()
    pairs = sorted(meta, key=lambda q: meta[q]["cells"])
    fig, axes = plt.subplots(len(pairs), 3, figsize=(TEXTWIDTH, 5.4), sharex=True)
    grey = np.arange(256)
    kernel = np.ones(5) / 5
    rungs = ["R2", "R3", "L3"]
    for i, pid in enumerate(pairs):
        for j, (key, cname) in enumerate((("w1_r", "red"), ("w1_g", "green"), ("w1_b", "blue"))):
            ax = axes[i, j]
            _clean(ax)
            a = hist[f"{pid}/A"][j].astype(float)
            a = np.convolve(a / a.sum(), kernel, mode="same")
            ax.fill_between(grey, a, color=BASE, alpha=0.6, linewidth=0, zorder=1)
            peak = a.max()
            for lvl, colour in zip(rungs, CHANNEL_RAMP[cname]):
                h = hist[f"{pid}/{lvl}"][j].astype(float)
                h = np.convolve(h / h.sum(), kernel, mode="same")
                peak = max(peak, h.max())
                ax.plot(grey, h, color=colour, linewidth=0.8, zorder=2)
            ax.set_ylim(0, peak * 1.15)
            ax.set_yticks([])
            ax.text(0.98, 0.88, f"W1 = {shift[(pid, 'L3')][key]:.0f}", transform=ax.transAxes,
                    ha="right", va="top", fontsize=6)
            if i == 0:
                ax.set_title(f"{cname} channel", loc="left", pad=2)
            if j == 0:
                m = meta[pid]
                ax.set_ylabel(f"{pid.replace('pair', 'P')}\n{m['target']}", rotation=0,
                              ha="right", va="center", labelpad=6)
    for ax in axes[-1]:
        ax.set_xlabel("pixel value")
        ax.set_xlim(0, 255)
    fig.tight_layout(pad=0.3, h_pad=0.3, w_pad=0.6)
    out = OUT / "rgb_distributions.pdf"
    fig.savefig(out)
    fig.savefig(out.with_suffix(".png"), dpi=220)
    plt.close(fig)
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for fn in (ladder, reordered, single_change, rgb, rgb_by_agent, rgb_distributions):
        print(f"  wrote {fn()}")


if __name__ == "__main__":
    main()
