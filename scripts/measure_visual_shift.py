"""How visually different is each shifted house from the one the agent trained in?

The severity ladder's damage varies enormously by house -- PPO's L1 drop ranges
8% (pair2) to 92% (pair3) -- and reported bare, that spread reads as a broken
benchmark. It is not broken: at 300k every house reaches 0.948-0.959 in-domain,
and all three baselines independently collapse in pair3 and survive pair2. The
spread is signal.

This script asks whether the signal has an obvious cause: L1 draws wall
materials, floor materials, lighting and skybox at RANDOM per house, and nobody
has measured how big those draws actually are. If pair3's draw is simply a much
larger visual change than pair2's, the spread becomes a DOSE-RESPONSE result --
damage scales with how much the appearance changed -- which is far stronger than
the table alone. If it does NOT correlate, that is also a finding, and a sharper
one: damage depends on WHAT changed rather than HOW MUCH, which points straight
at object-level binding.

Method: teleport to each of the 25 PINNED evaluation start poses -- the same
poses the transfer numbers were measured from -- and capture the agent's actual
observation in house A and in each rung. Compare them. No policy is involved and
no episode is run, so this needs no trained model and cannot be confounded by
behaviour.

Three distances, because they answer different questions:
  * mean_abs      average per-pixel difference. Sensitive to a global recolour.
  * frac_changed  fraction of pixels differing by more than a just-noticeable
                  amount. Sensitive to HOW MUCH of the view changed.
  * hist_l1       L1 distance between colour histograms. Ignores spatial layout,
                  so it isolates palette change from geometric change.

MUST run on the cluster under CloudRendering: the renderer determines the pixels,
and the macOS build produces different ones (the same PPO checkpoint scored 0.92
under CloudRendering and 0.00 locally).

    python scripts/measure_visual_shift.py                # every pair
    python scripts/measure_visual_shift.py --pair pair0
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np

from config import (  # noqa: E402
    EVAL_LEVELS, GenerationConfig, PPOConfig, TABLES_DIR, pair_dir, resolve_pair,
)
from envs.procthor_env import make_objectnav_env  # noqa: E402
from envs.task_setup import build_env_config  # noqa: E402

logger = logging.getLogger("measure_visual_shift")

# A per-channel difference below this is invisible in practice; counting every
# 1/255 flicker as "changed" would make frac_changed report ~1.0 everywhere.
JND = 12


def capture(house: Path, env_cfg: Any, seeds: List[int], name: str) -> np.ndarray:
    """The agent's observation at each pinned start pose. No stepping."""
    env = make_objectnav_env(house, env_cfg, name=name)
    try:
        frames = []
        for seed in seeds:
            obs, _ = env.reset(seed=seed)
            frames.append(np.asarray(obs, dtype=np.uint8))
        return np.stack(frames)
    finally:
        env.close()


def distances(a: np.ndarray, b: np.ndarray) -> Dict[str, float]:
    """Per-pose distances, averaged over poses."""
    af = a.astype(np.int16)
    bf = b.astype(np.int16)
    diff = np.abs(af - bf)
    mean_abs = float(diff.mean())
    frac_changed = float((diff.max(axis=-1) > JND).mean())

    # Colour histogram, 16 bins per channel, normalised per pose.
    def hist(x: np.ndarray) -> np.ndarray:
        out = []
        for pose in x:
            h = np.concatenate([
                np.histogram(pose[..., c], bins=16, range=(0, 256))[0]
                for c in range(3)
            ]).astype(np.float64)
            out.append(h / max(h.sum(), 1))
        return np.stack(out)

    hist_l1 = float(np.abs(hist(a) - hist(b)).sum(axis=1).mean())
    return {"mean_abs_diff": round(mean_abs, 3),
            "frac_pixels_changed": round(frac_changed, 4),
            "hist_l1": round(hist_l1, 4)}


def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s: %(message)s")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pair", default=None, help="only this pair")
    ap.add_argument("--episodes", type=int, default=25,
                    help="how many pinned eval poses to sample")
    args = ap.parse_args()

    cfg = PPOConfig()
    seeds = [cfg.eval_seed_base + i for i in range(args.episodes)]
    pairs = ([args.pair] if args.pair
             else [f"pair{i}" for i in range(GenerationConfig().n_pairs)])

    rows = []
    for pid in pairs:
        pair = resolve_pair(pid)
        if not pair.house_a.exists():
            logger.warning("[%s] no house A — skipping", pid)
            continue
        # The eval slice, so these are the SAME poses the transfer numbers used.
        env_cfg = build_env_config(cfg, pair, split="eval")
        logger.info("[%s] capturing house A at %d pinned poses", pid, len(seeds))
        ref = capture(pair.house_a, env_cfg, seeds, f"{pid}_A")
        for level, house in pair.eval_houses:
            if level == "A" or not house.exists():
                continue
            logger.info("[%s] capturing %s", pid, level)
            got = capture(house, env_cfg, seeds, f"{pid}_{level}")
            d = distances(ref, got)
            rows.append({"pair": pid, "level": level, **d})
            logger.info("[%s] %s: mean|diff|=%.1f  changed=%.1f%%  histL1=%.3f",
                        pid, level, d["mean_abs_diff"],
                        100 * d["frac_pixels_changed"], d["hist_l1"])

    if not rows:
        raise SystemExit("nothing captured")
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    out = TABLES_DIR / "visual_shift.json"
    out.write_text(json.dumps(rows, indent=2))
    print(f"\nwrote {out}  ({len(rows)} pair x rung measurements)")
    print(f"{'pair':<8}{'rung':<7}{'mean|diff|':>11}{'% changed':>11}{'hist L1':>9}")
    for r in rows:
        print(f"{r['pair']:<8}{r['level']:<7}{r['mean_abs_diff']:>11.1f}"
              f"{100*r['frac_pixels_changed']:>11.1f}{r['hist_l1']:>9.3f}")


if __name__ == "__main__":
    main()
