"""Record a frozen policy acting in variant A and variant B, side by side.

This is the qualitative counterpart to the transfer tables: the same trained
agent, the same start pose (paired eval seed), one run in the appearance it
trained on and one in the shifted appearance. When the binding problem bites,
you can watch it — a direct walk to the Fridge on A, aimless circling on B.

Frames are the agent's ACTUAL observations (128x128 uint8), not a beauty
render, so what you see is what the policy saw.

Outputs (per episode seed):
    results/videos/<baseline>_seed<N>_AB.gif      animated, gitignored
    results/plots/<baseline>_rollout_seed<N>.png  filmstrip, paper-ready

Usage:
    python scripts/record_rollout.py --baseline ppo --episodes 2
    python scripts/record_rollout.py --baseline ppo_aug --seeds 10002,10007
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    HOUSE_A_PATH, HOUSE_B_PATH, PLOTS_DIR, RESULTS_DIR, ensure_dirs,
)
from envs.procthor_env import make_objectnav_env  # noqa: E402
from main import CONFIG_CLASSES  # noqa: E402
from scripts.evaluate_transfer import load_frozen_model  # noqa: E402
from scripts.train_ppo import build_env_config  # noqa: E402

logger = logging.getLogger("record_rollout")

VIDEOS_DIR = RESULTS_DIR / "videos"
UPSCALE = 2          # 128 -> 256 px per panel (nearest, keeps pixels honest)
BAR_H = 26           # caption strip height
FILMSTRIP_N = 6      # frames per row in the paper figure

Episode = Dict[str, Any]


def rollout(
    model: Any, house_path: Path, env_cfg: Any, seeds: List[int], name: str,
) -> List[Episode]:
    """Replay `seeds` on one house, keeping every observation frame."""
    env = make_objectnav_env(house_path, env_cfg, name=name)
    episodes: List[Episode] = []
    try:
        for seed in seeds:
            obs, _ = env.reset(seed=seed)
            if hasattr(model, "reset_episode"):
                model.reset_episode()   # recurrent baselines: clear latent state
            frames = [np.asarray(obs, dtype=np.uint8)]
            done = False
            info: Dict[str, Any] = {}
            while not done:
                action, _ = model.predict(obs, deterministic=True)
                obs, _reward, terminated, truncated, info = env.step(int(action))
                frames.append(np.asarray(obs, dtype=np.uint8))
                done = terminated or truncated
            episodes.append({
                "seed": seed,
                "frames": frames,
                "success": float(info.get("success", 0.0)),
                "spl": float(info.get("spl", 0.0)),
                "length": int(info.get("episode_step", len(frames) - 1)),
            })
            logger.info("[%s] seed %d: success=%.0f spl=%.3f len=%d",
                        name, seed, episodes[-1]["success"],
                        episodes[-1]["spl"], episodes[-1]["length"])
    finally:
        env.close()
    return episodes


def _panel(frame: np.ndarray, caption: str, ok: bool) -> "Any":
    """One upscaled frame with a colored caption bar (green ok / red failed)."""
    from PIL import Image, ImageDraw

    img = Image.fromarray(frame).resize(
        (frame.shape[1] * UPSCALE, frame.shape[0] * UPSCALE), Image.NEAREST
    )
    canvas = Image.new("RGB", (img.width, img.height + BAR_H), "#101010")
    canvas.paste(img, (0, BAR_H))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, 0, canvas.width, BAR_H], fill="#1baf7a" if ok else "#c2413a")
    draw.text((6, 7), caption, fill="#ffffff")
    return canvas


def _caption(label: str, ep: Episode, i: int) -> str:
    """Frame caption; once an episode has ended its last frame is held, so say so."""
    if i >= len(ep["frames"]) - 1:
        verdict = "reached target" if ep["success"] > 0 else "TIMEOUT, never found it"
        return f"{label}  done t={ep['length']} — {verdict}"
    return f"{label}  t={i}"


def compose(ep_a: Episode, ep_b: Episode) -> Tuple[List[Any], List[Any]]:
    """Side-by-side A|B frames; the shorter episode freezes on its last frame."""
    from PIL import Image

    n = max(len(ep_a["frames"]), len(ep_b["frames"]))
    pairs: List[Any] = []
    for i in range(n):
        fa = ep_a["frames"][min(i, len(ep_a["frames"]) - 1)]
        fb = ep_b["frames"][min(i, len(ep_b["frames"]) - 1)]
        pa = _panel(fa, _caption("A train", ep_a, i), ep_a["success"] > 0)
        pb = _panel(fb, _caption("B shifted", ep_b, i), ep_b["success"] > 0)
        combo = Image.new("RGB", (pa.width + pb.width + 4, pa.height), "#101010")
        combo.paste(pa, (0, 0))
        combo.paste(pb, (pa.width + 4, 0))
        pairs.append(combo)
    # Hold the final frame so the outcome is readable before the loop restarts.
    return pairs + [pairs[-1]] * 12, pairs


def write_filmstrip(pairs: List[Any], out: Path, title: str) -> None:
    from PIL import Image, ImageDraw

    idx = np.linspace(0, len(pairs) - 1, FILMSTRIP_N).round().astype(int)
    tiles = [pairs[i] for i in idx]
    w, h = tiles[0].size
    cols, rows = 2, (FILMSTRIP_N + 1) // 2
    sheet = Image.new("RGB", (cols * w + 8, rows * h + 8 + 22), "#fcfcfb")
    ImageDraw.Draw(sheet).text((6, 6), title, fill="#0b0b0b")
    for k, tile in enumerate(tiles):
        r, c = divmod(k, cols)
        sheet.paste(tile, (c * (w + 8), 22 + r * (h + 8)))
    sheet.save(out)
    logger.info("wrote %s", out)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", choices=tuple(sorted({b for b, _ in CONFIG_CLASSES})),
                        default="ppo")
    parser.add_argument("--episodes", type=int, default=2,
                        help="how many eval seeds to record (from eval_seed_base)")
    parser.add_argument("--seeds", type=str, default=None,
                        help="explicit comma-separated eval seeds, e.g. 10002,10007")
    parser.add_argument("--fps", type=int, default=6)
    args = parser.parse_args()

    ensure_dirs()
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

    cfg = CONFIG_CLASSES[(args.baseline, False)]()
    seeds = ([int(s) for s in args.seeds.split(",")] if args.seeds
             else [cfg.eval_seed_base + i for i in range(args.episodes)])
    env_cfg = build_env_config(cfg)
    model = load_frozen_model(args.baseline, cfg)

    logger.info("recording variant A (%d episodes)...", len(seeds))
    eps_a = rollout(model, HOUSE_A_PATH, env_cfg, seeds, "variant_a")
    logger.info("recording variant B (same seeds)...")
    eps_b = rollout(model, HOUSE_B_PATH, env_cfg, seeds, "variant_b")

    for ep_a, ep_b in zip(eps_a, eps_b):
        seed = ep_a["seed"]
        gif_frames, pairs = compose(ep_a, ep_b)
        gif = VIDEOS_DIR / f"{args.baseline}_seed{seed}_AB.gif"
        gif_frames[0].save(gif, save_all=True, append_images=gif_frames[1:],
                           duration=int(1000 / args.fps), loop=0)
        logger.info("wrote %s (%d frames)", gif, len(gif_frames))
        title = (f"{args.baseline} | eval seed {seed} | "
                 f"A: success={ep_a['success']:.0f} spl={ep_a['spl']:.2f} "
                 f"len={ep_a['length']}   vs   "
                 f"B: success={ep_b['success']:.0f} spl={ep_b['spl']:.2f} "
                 f"len={ep_b['length']}")
        write_filmstrip(pairs, PLOTS_DIR / f"{args.baseline}_rollout_seed{seed}.png",
                        title)


if __name__ == "__main__":
    main()
