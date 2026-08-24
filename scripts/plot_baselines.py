"""Headline figure: zero-shot visual transfer across all baselines.

Reads the committed per-seed sweep tables under ``results/sweeps/`` and renders
one three-panel comparison (one bar group per baseline) (success rate, SPL, episode length): paired A/B mean
bars per baseline with per-seed dots and ±1 std whiskers, plus the relative-drop
annotation that carries the paper's headline. Palette and styling match
``scripts/evaluate_transfer.py`` (validated: A blue / B green pass CVD checks;
the green is sub-3:1 on this surface, so bars carry direct value labels).

Usage:
    python scripts/plot_baselines.py
Output:
    results/plots/baseline_transfer.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import PROJECT_ROOT  # noqa: E402

# Same palette as evaluate_transfer.py (dataviz-validated for CVD on this surface).
COLOR_TRAIN = "#2a78d6"      # variant A (train visuals)
COLOR_TRANSFER = "#1baf7a"   # variant B (zero-shot visuals)
COLOR_SURFACE = "#fcfcfb"
COLOR_INK = "#0b0b0b"
COLOR_MUTED = "#898781"
COLOR_GRID = "#e1e0d9"
COLOR_BASELINE = "#c3c2b7"

# Order = the paper's argument: model-free, model-free + the obvious fix,
# then the two world models.
SWEEPS = {
    "PPO": PROJECT_ROOT / "results/sweeps/ppo",
    "PPO + aug": PROJECT_ROOT / "results/sweeps/ppo_aug",
    "DreamerV3-512": PROJECT_ROOT / "results/sweeps/dreamerv3_512",
    "TD-MPC2": PROJECT_ROOT / "results/sweeps/tdmpc2",
}
FILE_PREFIX = {"PPO": "ppo", "PPO + aug": "ppo_aug",
               "DreamerV3-512": "dreamerv3", "TD-MPC2": "tdmpc2"}
METRICS = [
    ("success_rate", "Success rate", "%.2f", (0.0, 1.12)),
    ("spl", "SPL", "%.2f", (0.0, 1.12)),
    ("mean_episode_length", "Mean episode length", "%.0f", None),
]


def load_seeds(baseline: str) -> dict:
    """Return {variant: {metric: np.array of per-seed values}}."""
    out = {"A": {m: [] for m, *_ in METRICS}, "B": {m: [] for m, *_ in METRICS}}
    for seed_dir in sorted(SWEEPS[baseline].glob("seed*")):
        df = pd.read_csv(seed_dir / f"{FILE_PREFIX[baseline]}_transfer_summary.csv")
        for _, row in df.iterrows():
            variant = "A" if row["variant"].startswith("A") else "B"
            for metric, *_ in METRICS:
                out[variant][metric].append(float(row[metric]))
    return {v: {m: np.asarray(xs) for m, xs in d.items()} for v, d in out.items()}


def main() -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    data = {b: load_seeds(b) for b in SWEEPS}
    baselines = list(SWEEPS)
    x = np.arange(len(baselines))
    width = 0.30
    rng = np.random.default_rng(0)  # deterministic dot jitter

    fig, axes = plt.subplots(1, 3, figsize=(14.4, 4.6), facecolor=COLOR_SURFACE)
    for ax, (metric, title, fmt, ylim) in zip(axes, METRICS):
        ax.set_facecolor(COLOR_SURFACE)
        ax.grid(axis="y", color=COLOR_GRID, linewidth=0.8, zorder=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(COLOR_BASELINE)
        ax.tick_params(colors=COLOR_MUTED, labelcolor=COLOR_INK, length=0)

        # Fix headroom per panel so labels above whiskers/dots never clip.
        panel_max = max(
            float(np.max(data[b][v][metric])) for b in baselines for v in ("A", "B")
        )
        top = ylim[1] if ylim else panel_max * 1.18
        for off, variant, color, label in (
            (-width / 2 - 0.015, "A", COLOR_TRAIN, "Train visuals (A)"),
            (+width / 2 + 0.015, "B", COLOR_TRANSFER, "Zero-shot visuals (B)"),
        ):
            means = np.array([data[b][variant][metric].mean() for b in baselines])
            stds = np.array([data[b][variant][metric].std(ddof=1) for b in baselines])
            ax.bar(x + off, means, width, color=color, zorder=3,
                   label=label if metric == "success_rate" else None)
            ax.errorbar(x + off, means, yerr=stds, fmt="none", zorder=4,
                        ecolor=COLOR_INK, elinewidth=0.9, capsize=2.5, capthick=0.9)
            # Per-seed dots with a surface ring so overlaps stay separable.
            for i, b in enumerate(baselines):
                vals = data[b][variant][metric]
                jitter = rng.uniform(-0.045, 0.045, len(vals))
                ax.scatter(np.full(len(vals), x[i] + off) + jitter, vals, s=21,
                           color=color, edgecolor=COLOR_SURFACE, linewidth=1.1,
                           zorder=5)
            # Direct value labels ABOVE whisker + dot extent (relief rule for
            # the sub-3:1 green; also avoids label/whisker collisions).
            for i, b in enumerate(baselines):
                vals = data[b][variant][metric]
                y = max(means[i] + stds[i], float(np.max(vals))) + 0.025 * top
                ax.annotate(fmt % means[i], (x[i] + off, y), ha="center",
                            fontsize=8.5, color=COLOR_INK, zorder=6)

        # Headline annotation: mean relative drop A->B per baseline.
        for i, b in enumerate(baselines):
            a, bb = data[b]["A"][metric], data[b]["B"][metric]
            drops = (a - bb) / np.where(a > 0, a, np.nan)
            sign = "−" if np.nanmean(drops) >= 0 else "+"
            ax.annotate(f"{sign}{abs(np.nanmean(drops)):.0%} rel",
                        (x[i], 0), xytext=(0, -30), textcoords="offset points",
                        ha="center", fontsize=8, color=COLOR_MUTED)

        ax.set_xticks(x, baselines, fontsize=8.5)
        ax.set_ylim(0, top)
        ax.set_title(title, color=COLOR_INK, fontsize=11, loc="left")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, fontsize=9, labelcolor=COLOR_INK,
               loc="upper right", bbox_to_anchor=(0.995, 0.985), ncols=2)
    fig.suptitle(
        "Zero-shot visual transfer — four baselines at published recipes,\n"
        "5 training seeds each (dots = seeds, whiskers = ±1 std)",
        color=COLOR_INK, fontsize=12, x=0.01, ha="left",
    )
    fig.tight_layout(rect=(0, 0.02, 1, 0.90))
    out = PROJECT_ROOT / "results/plots/baseline_transfer.png"
    fig.savefig(out, dpi=200, facecolor=COLOR_SURFACE, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
