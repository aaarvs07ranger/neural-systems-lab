"""Severity-ladder figure: how each agent degrades as the visual shift worsens.

Form: the rungs are an ORDERED, CUMULATIVE sequence (A -> L1 -> L2 -> L3), and
the question is change across that sequence, so this is a line chart, not bars.
Small multiples by house pair, because the per-house spread is itself a result --
PPO's L1 drop ranges 8% to 92% across houses, and a pooled line would describe
no house.

Colour: four agents cannot be four hues. The documented categorical palette
clears the all-pairs colour-blindness floors at three slots, and zero of the 70
four-slot subsets pass in both light and dark (checked, not assumed). So the
encoding is COMPOSITE, which is also what the science wants: hue carries the
paper's actual axis -- model-free (blue) vs world model (aqua) -- and dash
separates the two members within each group. Identity is therefore never
colour-alone: hue + dash + a direct label.

    python scripts/plot_ladder.py [--metric success|spl] [--mode light|dark]
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
import pandas as pd

from config import GenerationConfig, pair_dir

RUNGS = ["A", "L1", "L2", "L3"]
RUNG_LABEL = {"A": "A\ntrain", "L1": "L1\n+materials\n+lighting",
              "L2": "L2\n+object\nappearance", "L3": "L3\n+clutter"}

# Documented categorical palette, slots 1 (blue) and 3 (aqua). Validated
# all-pairs in both modes: worst CVD dE 23.1 light / 19.6 dark against a target
# of 8; normal-vision 24.0 / 20.9 against a floor of 15. Aqua is 2.74:1 on the
# light surface, under 3:1, so the relief rule applies and every series carries
# a direct label.
SERIES = {
    # baseline:      (light,     dark,      dashes,      label)
    "ppo":       ("#2a78d6", "#3987e5", (),          "PPO"),
    "ppo_aug":   ("#2a78d6", "#3987e5", (5, 2),      "PPO + augmentation"),
    "dreamerv3": ("#1baf7a", "#199e70", (),          "DreamerV3"),
    "tdmpc2":    ("#1baf7a", "#199e70", (5, 2),      "TD-MPC2"),
}
INK = {"light": ("#fcfcfb", "#0b0b0b", "#52514e", "#e1e0d9", "#c3c2b7"),
       "dark":  ("#1a1a19", "#ffffff", "#c3c2b7", "#3a3a38", "#52514e")}


def load() -> pd.DataFrame:
    rows = []
    for f in sorted(glob.glob("results/grid/*/*/*_transfer_summary.csv")):
        p = Path(f)
        baseline = p.parents[1].name
        pair, seed = p.parent.name.split("_seed")
        df = pd.read_csv(f).set_index("level")
        for rung in RUNGS:
            if rung not in df.index:
                continue
            rows.append(dict(baseline=baseline, pair=pair, seed=int(seed), rung=rung,
                             success=df.loc[rung, "success_rate"],
                             spl=df.loc[rung, "spl"]))
    return pd.DataFrame(rows)


def pair_meta() -> dict:
    """Cells and target-swappability per pair -- both are annotations on the figure."""
    meta = {}
    for i in range(GenerationConfig().n_pairs):
        pid = f"pair{i}"
        try:
            v = json.loads((pair_dir(pid) / "verification.json").read_text())
            s = json.loads((pair_dir(pid) / "safe_assets.json").read_text())
            t = json.loads((pair_dir(pid) / "task_config.json").read_text())
            meta[pid] = dict(cells=v["reference"]["n_reachable"],
                             swappable=bool(s.get("target_swappable")),
                             target=t["target_object_type"])
        except FileNotFoundError:
            continue
    return meta


def plot(metric: str = "success", mode: str = "light") -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    surface, ink, muted, grid, baseline_c = INK[mode]
    d = load()
    if d.empty:
        raise SystemExit("no grid results under results/grid/ yet")
    meta = pair_meta()
    # Panels ordered by house size: the L1 damage tracks it loosely, and the
    # one non-swappable pair then stands out on its own merits rather than
    # because it was placed first.
    pairs = sorted(d.pair.unique(), key=lambda p: meta.get(p, {}).get("cells", 0))

    fig, axes = plt.subplots(1, len(pairs), figsize=(3.0 * len(pairs) + 1.6, 3.9),
                             sharey=True, facecolor=surface)
    axes = np.atleast_1d(axes)
    x = np.arange(len(RUNGS))

    for ax, pid in zip(axes, pairs):
        ax.set_facecolor(surface)
        ax.grid(axis="y", color=grid, linewidth=0.8, zorder=0)
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(baseline_c)
        ax.tick_params(colors=muted, labelcolor=ink, length=0, labelsize=8)

        for b, (cl, cd, dash, _lab) in SERIES.items():
            sub = d[(d.baseline == b) & (d.pair == pid)]
            if sub.empty:
                continue
            g = sub.groupby("rung")[metric].agg(["mean", "std", "count"]).reindex(RUNGS)
            colour = cl if mode == "light" else cd
            ok = g["mean"].notna()
            # +/-1 std over seeds, as a band rather than caps: four overlapping
            # series make error bars a thicket.
            ax.fill_between(x[ok], (g["mean"] - g["std"].fillna(0))[ok],
                            (g["mean"] + g["std"].fillna(0))[ok],
                            color=colour, alpha=0.13, linewidth=0, zorder=2)
            ax.plot(x[ok], g["mean"][ok], color=colour, linewidth=2.0,
                    dashes=dash if dash else (None, None), marker="o",
                    markersize=5, markeredgecolor=surface, markeredgewidth=1.2,
                    zorder=3, solid_capstyle="round")

        m = meta.get(pid, {})
        title = f"{pid} · {m.get('target','?')} · {m.get('cells','?')} cells"
        ax.set_title(title, color=ink, fontsize=9, loc="left", pad=14)
        if not m.get("swappable", True):
            # The natural control: this pair's target has no footprint-safe
            # alternative asset, so its L2 changes everything EXCEPT the target.
            ax.text(0, 1.015, "target NOT swapped at L2", transform=ax.transAxes,
                    fontsize=8, color=colour_accent(mode), fontweight="bold")
        ax.set_xticks(x, [RUNG_LABEL[r] for r in RUNGS], fontsize=7.5)
        ax.set_ylim(-0.03, 1.06)

    axes[0].set_ylabel("Success rate" if metric == "success" else "SPL",
                       color=ink, fontsize=9)

    # Direct labels on the right-hand panel. Mandatory, not decorative: the
    # light-mode aqua sits at 2.74:1 on this surface, under the 3:1 line, so the
    # relief rule requires identity to be readable without relying on the fill.
    # Labels are nudged apart when lines converge, which they do at the bottom
    # of the collapsed panels.
    last, pid = axes[-1], pairs[-1]
    ends = []
    for b, (cl, cd, dash, lab) in SERIES.items():
        sub = d[(d.baseline == b) & (d.pair == pid)]
        if sub.empty:
            continue
        g = sub.groupby("rung")[metric].mean().reindex(RUNGS)
        if pd.isna(g.iloc[-1]):
            continue
        ends.append([float(g.iloc[-1]), lab, cl if mode == "light" else cd])
    ends.sort()
    MIN_GAP = 0.075                       # in axis units, ~ the label height
    for i in range(1, len(ends)):
        if ends[i][0] - ends[i - 1][0] < MIN_GAP:
            ends[i][0] = ends[i - 1][0] + MIN_GAP
    for y, lab, colour in ends:
        last.annotate(lab, xy=(len(RUNGS) - 1, y), xytext=(11, 0),
                      textcoords="offset points", va="center", fontsize=8,
                      color=ink, annotation_clip=False)
        last.plot([len(RUNGS) - 1 + 0.14], [y], marker="s", markersize=4,
                  color=colour, clip_on=False, zorder=4)

    # Legend: always present for >=2 series, and every series is also direct-
    # labelled below, so identity never rests on colour alone (the light-mode
    # aqua is under 3:1 on this surface -- the relief rule).
    handles = [Line2D([0], [0], color=(c if mode == "light" else cd), linewidth=2.0,
                      dashes=dash if dash else (None, None), marker="o", markersize=5,
                      markeredgecolor=surface, label=lab)
               for _b, (c, cd, dash, lab) in SERIES.items()]
    fig.legend(handles=handles, frameon=False, fontsize=8.5, labelcolor=ink,
               loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.035))

    fig.suptitle("Zero-shot transfer across the severity ladder"
                 f"   ({'success rate' if metric=='success' else 'SPL'}, mean ±1 s.d. over 5 seeds)",
                 color=ink, fontsize=11, x=0.008, ha="left", y=1.0)
    # Right margin reserved for the direct labels, which sit outside the axes.
    fig.tight_layout(rect=(0, 0.06, 0.9, 0.97))

    out = Path("results/plots") / f"ladder_{metric}_{mode}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=220, facecolor=surface, bbox_inches="tight")
    plt.close(fig)
    return out


def colour_accent(mode: str) -> str:
    # Status-ish emphasis for the annotation; kept out of the categorical slots.
    return "#e34948" if mode == "light" else "#e66767"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metric", choices=("success", "spl"), default="success")
    ap.add_argument("--mode", choices=("light", "dark", "both"), default="both")
    a = ap.parse_args()
    modes = ("light", "dark") if a.mode == "both" else (a.mode,)
    metrics = ("success", "spl") if a.metric == "success" else (a.metric,)
    for m in modes:
        for k in metrics:
            print(f"  wrote {plot(k, m)}")


if __name__ == "__main__":
    main()
