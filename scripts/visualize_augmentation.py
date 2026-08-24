"""Render what the `ppo_aug` agent actually sees during training.

Produces the qualitative companion to the ppo_aug transfer numbers, and the
figure that makes the augmentation argument legible in the paper:

    row 1 : variant A (raw, what plain PPO trains on) + variant B
            (the zero-shot test appearance, never seen during training)
    row 2 : six random photometric-jitter draws of the SAME variant-A pose —
            the appearance distribution ppo_aug is trained over

The visual question a reader should be able to answer from this figure:
does the jitter distribution actually cover the A->B shift, or is it a
different family of appearance change? (Ours is photometric; the A->B shift
is materials + lighting + skybox, so coverage is partial by construction —
that is exactly why augmentation is a baseline and not the solution.)

Output: results/plots/augmentation_examples.png

Usage:
    python scripts/visualize_augmentation.py
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any, List

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    HOUSE_A_PATH, HOUSE_B_PATH, PLOTS_DIR, PPOAugConfig, ensure_dirs,
)
from envs.augmentation import apply_jitter  # noqa: E402
from scripts.visualize_variants import capture_poses  # noqa: E402

logger = logging.getLogger("visualize_augmentation")

N_SAMPLES = 6      # jitter draws to show
POSE_INDEX = 0     # 0 = view toward the Fridge target, 1 = room overview


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    ensure_dirs()

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    cfg = PPOAugConfig()
    logger.info("capturing variant A pose...")
    frame_a = capture_poses(HOUSE_A_PATH)[POSE_INDEX]
    logger.info("capturing variant B pose (same camera)...")
    frame_b = capture_poses(HOUSE_B_PATH)[POSE_INDEX]

    # Same distribution the training wrapper draws from (config strengths),
    # a fixed seed so the figure is reproducible.
    rng = np.random.default_rng(0)
    samples: List[np.ndarray] = []
    labels: List[str] = []
    for _ in range(N_SAMPLES):
        b = rng.uniform(1 - cfg.aug_brightness, 1 + cfg.aug_brightness)
        c = rng.uniform(1 - cfg.aug_contrast, 1 + cfg.aug_contrast)
        s = rng.uniform(1 - cfg.aug_saturation, 1 + cfg.aug_saturation)
        h = rng.uniform(-cfg.aug_hue_degrees, cfg.aug_hue_degrees)
        samples.append(apply_jitter(frame_a, b, c, s, h))
        labels.append(f"b{b:.2f} c{c:.2f} s{s:.2f} h{h:+.0f}°")

    fig = plt.figure(figsize=(12, 6.0), facecolor="#fcfcfb")
    gs = fig.add_gridspec(2, 6, height_ratios=(2.6, 1.0), hspace=0.02, wspace=0.06,
                      left=0.045, right=0.99, top=0.90, bottom=0.04)

    def _clean(ax: Any) -> None:
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

    ax_a = fig.add_subplot(gs[0, 0:3])
    ax_a.imshow(frame_a)
    ax_a.set_title("Variant A — training appearance (raw)", fontsize=12, pad=8)
    _clean(ax_a)

    ax_b = fig.add_subplot(gs[0, 3:6])
    ax_b.imshow(frame_b)
    ax_b.set_title("Variant B — zero-shot test appearance (never seen)",
                   fontsize=12, pad=8)
    _clean(ax_b)

    for i, (img, label) in enumerate(zip(samples, labels)):
        ax = fig.add_subplot(gs[1, i])
        ax.imshow(img)
        ax.set_xlabel(label, fontsize=7, color="#52514e", labelpad=4)
        _clean(ax)
        if i == 0:
            ax.set_ylabel("ppo_aug\ntraining draws", fontsize=9, color="#52514e")

    fig.suptitle(
        "What `ppo_aug` trains on: one photometric jitter draw per episode "
        f"(brightness/contrast/saturation ±{cfg.aug_brightness:.0%}, "
        f"hue ±{cfg.aug_hue_degrees:.0f}°) — eval always uses raw frames",
        fontsize=11, color="#0b0b0b", y=0.975,
    )
    out = PLOTS_DIR / "augmentation_examples.png"
    fig.savefig(out, dpi=150, facecolor="#fcfcfb")
    logger.info("wrote %s", out)


if __name__ == "__main__":
    main()
