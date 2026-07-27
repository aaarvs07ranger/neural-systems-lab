"""Render side-by-side screenshots of visual variants A and B.

Captures frames from IDENTICAL agent poses in both houses (possible because
the geometry matches exactly), producing the qualitative companion to the
quantitative transfer tables — and a ready-made paper figure.

Output: results/plots/variant_comparison.png

Usage:
    python scripts/visualize_variants.py
"""
from __future__ import annotations

import logging
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import HOUSE_A_PATH, HOUSE_B_PATH, PLOTS_DIR, ensure_dirs  # noqa: E402
from envs.procthor_env import load_house  # noqa: E402

logger = logging.getLogger("visualize_variants")

# Render size for the figure (larger than the 128px training observations).
WIDTH, HEIGHT = 560, 420
TARGET_TYPE = "Fridge"

Vec3 = Dict[str, float]


def _yaw_towards(src: Vec3, dst: Vec3) -> float:
    """THOR yaw (deg, 0 = +z, clockwise) pointing from src to dst."""
    return math.degrees(math.atan2(dst["x"] - src["x"], dst["z"] - src["z"]))


def capture_poses(house_path: Path) -> List[np.ndarray]:
    """Boot the house, capture frames from two deterministic poses."""
    from ai2thor.controller import Controller

    controller = Controller(
        scene=load_house(house_path),
        agentMode="default",
        snapToGrid=False,
        width=WIDTH,
        height=HEIGHT,
        fieldOfView=90,
    )
    try:
        event = controller.step(action="GetReachablePositions")
        reachable = sorted(
            event.metadata["actionReturn"], key=lambda p: (p["x"], p["z"])
        )
        objects = controller.last_event.metadata["objects"]
        fridge = next(o for o in objects if o["objectType"] == TARGET_TYPE)

        # Pose 1: from ~1/4 through the room, looking at the fridge (target view).
        # Pose 2: from ~3/4 through the room, looking back across it (room view).
        picks: List[Tuple[Vec3, Vec3]] = [
            (reachable[len(reachable) // 4], fridge["position"]),
            (reachable[(3 * len(reachable)) // 4],
             reachable[len(reachable) // 8]),
        ]
        frames: List[np.ndarray] = []
        for pos, look_at in picks:
            controller.step(
                action="Teleport",
                position=pos,
                rotation={"x": 0.0, "y": _yaw_towards(pos, look_at), "z": 0.0},
                horizon=0.0,
                standing=True,
            )
            frames.append(
                np.ascontiguousarray(controller.last_event.frame, dtype=np.uint8)
            )
        return frames
    finally:
        controller.stop()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    ensure_dirs()

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    logger.info("capturing variant A frames...")
    frames_a = capture_poses(HOUSE_A_PATH)
    logger.info("capturing variant B frames...")
    frames_b = capture_poses(HOUSE_B_PATH)

    fig, axes = plt.subplots(2, 2, figsize=(10, 7.6), facecolor="#fcfcfb")
    col_titles = ("Variant A — train visuals", "Variant B — zero-shot visuals")
    row_labels = ("View toward target (Fridge)", "Room overview")
    for row in range(2):
        for col, frames in enumerate((frames_a, frames_b)):
            ax: Any = axes[row][col]
            ax.imshow(frames[row])
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_visible(False)
            if row == 0:
                ax.set_title(col_titles[col], fontsize=12, color="#0b0b0b", pad=8)
            if col == 0:
                ax.set_ylabel(row_labels[row], fontsize=10, color="#52514e")
    fig.suptitle(
        "Identical structure, identical camera poses — appearance only differs",
        fontsize=11, color="#52514e", y=0.02, va="bottom",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    out = PLOTS_DIR / "variant_comparison.png"
    fig.savefig(out, dpi=150, facecolor="#fcfcfb")
    logger.info("wrote %s", out)


if __name__ == "__main__":
    main()
