"""The R, G and B pixel distributions of every house, and how far each one moves.

Vishwas (2026-09-29): show how much the image changes at each level as three
distributions -- one each for R, G and B -- and relate that shift to how much
success drops. `measure_visual_shift.py` only kept three summary numbers for the
original ladder; this keeps the full distributions, for EVERY house the benchmark
defines (original ladder, reordered ladder, each rung alone, every single
factor), so there are ~15 comparisons per house instead of 4.

What is captured: the agent's own 128x128 observation at each of the 25 PINNED
evaluation start poses -- the exact views the success numbers were measured
from. No policy and no episode is involved, so nothing here depends on behaviour.

What is written:

  results/tables/rgb_hist.npz     per (pair, house, channel): a 256-bin histogram
                                  of pixel values pooled over the 25 views
  results/tables/rgb_shift.json   per (pair, house) vs house A:
      w1_r / w1_g / w1_b   Wasserstein-1 (earth mover's) distance between the
                           house's and house A's distribution of that channel, in
                           grey levels: "how far the red distribution moved"
      w1_mean              the mean of the three
      mean_abs_diff        average per-pixel difference, same pose (spatial)
  <run root>/rgb_frames/<pair>.npz  the frames themselves (uint8), kept OUT of
                           the repo, for measuring how far each agent's own
                           representation moves (a separate step)

The two kinds of distance answer different questions and both are kept: the
Wasserstein distances ignore WHERE pixels are (a colour-palette shift), the
per-pixel difference does not.

MUST run under CloudRendering on the cluster: the renderer determines the pixels.

    python scripts/measure_rgb_shift.py                 # every pair
    python scripts/measure_rgb_shift.py --pair pair0
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np

from config import (  # noqa: E402
    GenerationConfig, PPOConfig, TABLES_DIR, pair_house_path, resolve_pair,
)
from envs.procthor_env import make_objectnav_env  # noqa: E402
from envs.task_setup import build_env_config  # noqa: E402

logger = logging.getLogger("measure_rgb_shift")

# Every evaluation house, in reading order. Missing ones (pair2 has no F_tgt)
# are skipped, not faked.
HOUSES = ["L1", "L2noT", "L2", "L3",                       # original ladder
          "R2", "R3",                                      # reordered ladder (R1 = F_clut, R4 = L3)
          "F_clut", "F_lightsky", "F_objall", "F_mat",     # each rung alone
          "F_light", "F_sky", "F_obj", "F_tgt"]            # single factors
CHANNELS = ("r", "g", "b")


def capture(house: Path, env_cfg: Any, seeds: List[int], name: str) -> np.ndarray:
    """The agent's observation at each pinned start pose. No stepping."""
    env = make_objectnav_env(house, env_cfg, name=name)
    try:
        return np.stack([np.asarray(env.reset(seed=s)[0], dtype=np.uint8) for s in seeds])
    finally:
        env.close()


def channel_hists(frames: np.ndarray) -> np.ndarray:
    """(3, 256) pixel-value counts, pooled over every view and pixel."""
    return np.stack([np.bincount(frames[..., c].ravel(), minlength=256)
                     for c in range(3)]).astype(np.int64)


def wasserstein1(h_a: np.ndarray, h_b: np.ndarray) -> float:
    """W1 between two 1-D histograms on the integer grid 0..255, in grey levels.

    For distributions on a line, W1 is the area between their cumulative
    distribution functions -- exact, no approximation.
    """
    ca = np.cumsum(h_a / h_a.sum())
    cb = np.cumsum(h_b / h_b.sum())
    return float(np.abs(ca - cb).sum())


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pair", default=None)
    ap.add_argument("--episodes", type=int, default=25)
    args = ap.parse_args()

    cfg = PPOConfig()
    seeds = [cfg.eval_seed_base + i for i in range(args.episodes)]
    pairs = [args.pair] if args.pair else [f"pair{i}" for i in range(GenerationConfig().n_pairs)]
    frame_dir = Path(os.environ.get("NSL_FRAME_DIR", "rgb_frames"))
    frame_dir.mkdir(parents=True, exist_ok=True)

    hists: Dict[str, np.ndarray] = {}
    rows: List[Dict[str, Any]] = []
    for pid in pairs:
        pair = resolve_pair(pid)
        env_cfg = build_env_config(cfg, pair, split="eval")   # the pinned eval poses
        frames = {"A": capture(pair.house_a, env_cfg, seeds, f"{pid}_A")}
        for level in HOUSES:
            path = pair_house_path(pid, level)
            if not path.exists():
                logger.info("[%s] %s: no such house, skipped", pid, level)
                continue
            frames[level] = capture(path, env_cfg, seeds, f"{pid}_{level}")
        np.savez_compressed(frame_dir / f"{pid}.npz", **frames)

        ref = channel_hists(frames["A"])
        hists[f"{pid}/A"] = ref
        for level, f in frames.items():
            if level == "A":
                continue
            h = channel_hists(f)
            hists[f"{pid}/{level}"] = h
            w = [wasserstein1(ref[c], h[c]) for c in range(3)]
            row = {"pair": pid, "level": level,
                   **{f"w1_{ch}": round(w[c], 3) for c, ch in enumerate(CHANNELS)},
                   "w1_mean": round(float(np.mean(w)), 3),
                   "mean_abs_diff": round(float(np.abs(
                       f.astype(np.int16) - frames["A"].astype(np.int16)).mean()), 3)}
            rows.append(row)
            logger.info("[%s] %-10s W1 r/g/b = %5.1f %5.1f %5.1f   |diff| = %5.1f",
                        pid, level, *w, row["mean_abs_diff"])

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(TABLES_DIR / "rgb_hist.npz", **hists)
    (TABLES_DIR / "rgb_shift.json").write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {TABLES_DIR / 'rgb_shift.json'} ({len(rows)} house comparisons), "
          f"{TABLES_DIR / 'rgb_hist.npz'}, frames in {frame_dir}")


if __name__ == "__main__":
    main()
