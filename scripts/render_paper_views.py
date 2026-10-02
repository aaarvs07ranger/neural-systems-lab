"""Paper figure: one camera view, rendered in the training house and every changed house.

Every house in a pair has identical geometry, so the same pose can be rendered in
all of them and any pixel difference is the appearance change alone. This is an
ILLUSTRATION, never a measurement: it may be rendered locally (macOS windowed
build) at a higher resolution than the 128x128 the agents see, which is fine for
showing what changed and useless for anything an agent is scored on (renderer
rule, CLAUDE.md 4s).

Two steps, because a good view has to be chosen by eye:

    # 1. contact sheet of candidate poses in house A
    python scripts/render_paper_views.py --pair pair1 --candidates
    # 2. render the chosen candidate in every house of the pair
    python scripts/render_paper_views.py --pair pair1 --pick 3

Output: paper_v2/figures/views_<pair>.png (and _candidates.png for step 1). The
paper's figure: --pair pair1 --pick 2 --look-at 2.2,0.6 (the first draft, frozen
in paper/, used the same pose with the original ladder).
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from config import pair_dir, pair_house_path  # noqa: E402
from envs.procthor_env import load_house  # noqa: E402

WIDTH, HEIGHT = 480, 360
OUT_DIR = ROOT / "paper_v2" / "figures"     # the first draft in paper/ is frozen

# (house key, panel label). Top row: the reordered ladder, cumulative, least to
# most damaging. Bottom row: each rung's change applied to house A on its own,
# under the rung that adds it (clutter alone IS R1), and the goal object alone.
TOP = [("A", "A (training)"), ("F_clut", "R1: clutter"), ("R2", "R2: + lighting, sky"),
       ("R3", "R3: + object looks"), ("L3", "R4: + walls, floor, ceiling")]
BOTTOM = [("F_tgt", "goal object only"), ("F_clut", "clutter only (= R1)"),
          ("F_lightsky", "lighting, sky only"), ("F_objall", "object looks only"),
          ("F_mat", "walls, floor, ceiling only")]

Vec3 = Dict[str, float]


def _yaw_towards(src: Vec3, dst: Vec3) -> float:
    return math.degrees(math.atan2(dst["x"] - src["x"], dst["z"] - src["z"]))


def _controller(house: dict):
    from ai2thor.controller import Controller
    return Controller(scene=house, agentMode="default", snapToGrid=False,
                      width=WIDTH, height=HEIGHT, fieldOfView=90)


def candidate_poses(controller, target_type: str, n: int = 8,
                    look_at: Vec3 = None) -> List[Tuple[Vec3, float]]:
    """Reachable positions 1.5-4.5 m from the target (or `look_at`), facing it,
    spread by distance."""
    ev = controller.step(action="GetReachablePositions")
    reachable = ev.metadata["actionReturn"]
    if look_at is None:
        target = next(o for o in controller.last_event.metadata["objects"]
                      if o["objectType"] == target_type)
        tp = target["position"]
    else:
        tp = look_at
    cands = []
    for p in reachable:
        d = math.hypot(p["x"] - tp["x"], p["z"] - tp["z"])
        if 1.5 <= d <= 4.5:
            cands.append((d, p))
    cands.sort(key=lambda t: (t[0], t[1]["x"], t[1]["z"]))
    if not cands:
        raise SystemExit("no reachable position 1.5-4.5 m from the target")
    idx = np.linspace(0, len(cands) - 1, n).round().astype(int)
    return [(cands[i][1], _yaw_towards(cands[i][1], tp)) for i in idx]


def render(controller, pose: Tuple[Vec3, float], horizon: float) -> np.ndarray:
    pos, yaw = pose
    ev = controller.step(action="Teleport", position=pos,
                         rotation={"x": 0.0, "y": yaw, "z": 0.0},
                         horizon=horizon, standing=True)
    if not ev.metadata["lastActionSuccess"]:
        raise RuntimeError(f"teleport failed: {ev.metadata['errorMessage']}")
    return np.ascontiguousarray(ev.frame, dtype=np.uint8)


def _target_type(pair: str) -> str:
    import json
    return json.loads((pair_dir(pair) / "task_config.json").read_text())["target_object_type"]


def main() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pair", default="pair1")
    ap.add_argument("--candidates", action="store_true")
    ap.add_argument("--pick", type=int, default=0)
    ap.add_argument("--horizon", type=float, default=15.0)
    ap.add_argument("--look-at", default="", help="x,z to face instead of the target")
    a = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = _target_type(a.pair)

    ctl = _controller(load_house(pair_house_path(a.pair, "A")))
    try:
        look = None
        if a.look_at:
            x, z = (float(v) for v in a.look_at.split(","))
            look = {"x": x, "y": 0.0, "z": z}
        poses = candidate_poses(ctl, target, look_at=look)
        if a.candidates:
            frames = [render(ctl, p, a.horizon) for p in poses]
            fig, axes = plt.subplots(2, 4, figsize=(12, 4.8))
            for i, (ax, f) in enumerate(zip(axes.flat, frames)):
                ax.imshow(f)
                ax.set_title(f"candidate {i}", fontsize=9)
                ax.axis("off")
            out = OUT_DIR / f"views_{a.pair}_candidates.png"
            fig.tight_layout()
            fig.savefig(out, dpi=110)
            print(f"  wrote {out}")
            return
        pose = poses[a.pick]
        frames = {}
        for key, _lab in TOP + BOTTOM:
            if key in frames:
                continue
            ctl.reset(scene=load_house(pair_house_path(a.pair, key)))
            frames[key] = render(ctl, pose, a.horizon)
    finally:
        ctl.stop()

    # Full-resolution frames too, for inspecting a panel closely.
    from PIL import Image
    frame_dir = OUT_DIR / f"views_{a.pair}"
    frame_dir.mkdir(exist_ok=True)
    for key, f in frames.items():
        Image.fromarray(f).save(frame_dir / f"{key}.png")

    # Same type as the other paper figures; TrueType (42), never Type 3.
    plt.rcParams.update({"font.family": "serif",
                         "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
                         "pdf.fonttype": 42, "ps.fonttype": 42})
    # 5.5 in = the CoRL text width; two rows of five 4:3 panels.
    fig, axes = plt.subplots(2, len(TOP), figsize=(5.5, 2.05))
    for row, spec in enumerate((TOP, BOTTOM)):
        for ax, (key, lab) in zip(axes[row], spec):
            ax.imshow(frames[key])
            ax.set_xticks([])
            ax.set_yticks([])
            for s in ax.spines.values():
                s.set_linewidth(0.4)
            ax.set_title(lab, fontsize=5.8, pad=2)
    axes[0][0].set_ylabel("cumulative", fontsize=6.2)
    axes[1][0].set_ylabel("one change\non house A", fontsize=6.2)
    fig.subplots_adjust(left=0.045, right=0.997, top=0.92, bottom=0.01,
                        wspace=0.04, hspace=0.22)
    out = OUT_DIR / f"views_{a.pair}.pdf"
    fig.savefig(out, dpi=300)
    fig.savefig(out.with_suffix(".png"), dpi=200)
    print(f"  wrote {out}")


if __name__ == "__main__":
    main()
