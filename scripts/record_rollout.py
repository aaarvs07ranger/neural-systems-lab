"""Record one frozen policy walking the whole severity ladder, from one start.

The qualitative counterpart to the transfer tables: the same trained agent, the
same PINNED start pose, replayed in house A and in every rung of the shift. When
the binding problem bites you can watch it happen -- a direct walk to the Fridge
on A, aimless circling once the Fridge is a different Fridge.

Frames are the agent's ACTUAL observations (128x128 uint8), not a beauty render,
so what you see is what the policy saw.

TWO RULES, both learned the hard way:
  * Record on the CLUSTER, under the renderer the policy trained with. The same
    PPO checkpoint scored 0.92 on CloudRendering and 0.00 on the macOS build.
    Locally-recorded strips are qualitatively suggestive and numerically false.
  * Use PPO for anything that must be reproducible. TD-MPC2 keeps upstream
    random-shift augmentation active at evaluation, so one of its episodes
    replayed twice gave 65 steps and then a timeout.

Outputs (per episode seed):
    results/videos/<baseline>_<pair>_seed<N>_ladder.gif   animated, gitignored
    results/plots/<baseline>_<pair>_rollout_seed<N>.png   filmstrip, paper-ready

Usage:
    python scripts/record_rollout.py --baseline ppo --pair pair0 --episodes 2
    python scripts/record_rollout.py --baseline ppo --pair pair2 --seeds 10006
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
    PLOTS_DIR, RESULTS_DIR, ensure_dirs, resolve_pair,
)
from envs.procthor_env import make_objectnav_env  # noqa: E402
from main import CONFIG_CLASSES  # noqa: E402
from scripts.evaluate_transfer import load_frozen_model  # noqa: E402
from envs.task_setup import build_env_config  # noqa: E402

logger = logging.getLogger("record_rollout")

VIDEOS_DIR = RESULTS_DIR / "videos"
UPSCALE = 2          # 128 -> 256 px per panel (nearest, keeps pixels honest)
BAR_H = 26           # caption strip height
FILMSTRIP_N = 6      # time samples across the strip

# Row labels, short enough to sit in a 26px caption bar.
RUNG_CAPTION = {"A": "A  train visuals", "L1": "L1  +materials/lighting",
                "L2": "L2  +object appearance", "L3": "L3  +clutter"}

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
        verdict = "REACHED TARGET" if ep["success"] > 0 else "TIMEOUT, never found it"
        return f"{label}  done t={ep['length']}: {verdict}"
    return f"{label}  t={i}"


def compose_ladder(rungs: List[Tuple[str, Episode]]) -> Tuple[List[Any], List[Any]]:
    """One frame per timestep: every rung stacked vertically, same instant.

    Episodes that end early hold their final frame, so the reader sees the
    outcome of each rung side by side rather than panels vanishing at different
    times. Stacking (rather than the old A-beside-B) is what makes the ladder
    legible: one column of the same room, four appearances, one shared start.
    """
    from PIL import Image

    n = max(len(ep["frames"]) for _l, ep in rungs)
    stacked: List[Any] = []
    for i in range(n):
        panels = []
        for label, ep in rungs:
            f = ep["frames"][min(i, len(ep["frames"]) - 1)]
            panels.append(_panel(f, _caption(RUNG_CAPTION.get(label, label), ep, i),
                                 ep["success"] > 0))
        w = max(p.width for p in panels)
        h = sum(p.height for p in panels) + 3 * (len(panels) - 1)
        col = Image.new("RGB", (w, h), "#101010")
        y = 0
        for pan in panels:
            col.paste(pan, (0, y))
            y += pan.height + 3
        stacked.append(col)
    # Hold the final frame so the outcome is readable before the loop restarts.
    return stacked + [stacked[-1]] * 12, stacked


def write_ladder_filmstrip(stacked: List[Any], out: Path, title: str,
                           lengths: List[int]) -> None:
    """Rows = severity rungs, columns = time. The paper figure.

    Time samples are spaced over the LONGEST episode, so a rung that finished at
    t=12 shows its held final frame in later columns while a rung still
    wandering at t=180 shows where it is -- which is the comparison the figure
    exists to make.
    """
    from PIL import Image, ImageDraw

    idx = np.linspace(0, len(stacked) - 1, FILMSTRIP_N).round().astype(int)
    tiles = [stacked[i] for i in idx]
    w, h = tiles[0].size
    pad, top = 8, 26
    sheet = Image.new("RGB", (FILMSTRIP_N * w + pad * (FILMSTRIP_N + 1),
                              h + top + pad * 2), "#fcfcfb")
    d = ImageDraw.Draw(sheet)
    d.text((pad, 7), title, fill="#0b0b0b")
    for k, tile in enumerate(tiles):
        x = pad + k * (w + pad)
        sheet.paste(tile, (x, top + pad))
        d.text((x + 2, top + pad - 12), f"t = {idx[k]}", fill="#52514e")
    sheet.save(out)
    logger.info("wrote %s", out)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", choices=tuple(sorted({b for b, _ in CONFIG_CLASSES})),
                        default="ppo")
    parser.add_argument("--pair", default=None,
                        help="house pair id (e.g. pair0); default $NSL_PAIR, else "
                             "the legacy flat layout (A and L1 only)")
    parser.add_argument("--episodes", type=int, default=2,
                        help="how many eval seeds to record (from eval_seed_base)")
    parser.add_argument("--seeds", type=str, default=None,
                        help="explicit comma-separated eval seeds, e.g. 10006,10020")
    parser.add_argument("--fps", type=int, default=6)
    args = parser.parse_args()

    ensure_dirs()
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

    cfg = CONFIG_CLASSES[(args.baseline, False)]()
    pair = resolve_pair(args.pair)
    seeds = ([int(s) for s in args.seeds.split(",")] if args.seeds
             else [cfg.eval_seed_base + i for i in range(args.episodes)])
    # The eval slice, so the start poses are the pinned ones the tables used --
    # a filmstrip from a different pose is not the episode the numbers describe.
    env_cfg = build_env_config(cfg, pair, split="eval")
    model = load_frozen_model(args.baseline, cfg)

    # Every rung, same seeds, same pinned starts. One house at a time keeps a
    # single Unity process alive rather than four.
    by_rung: List[Tuple[str, List[Episode]]] = []
    for level, house in pair.eval_houses:
        if not house.exists():
            logger.warning("skipping %s (%s not found)", level, house)
            continue
        logger.info("recording %s (%d episodes)...", level, len(seeds))
        by_rung.append((level, rollout(model, house, env_cfg, seeds, level)))

    if not by_rung:
        raise SystemExit("no houses to record")

    tag = f"{args.baseline}_{pair.pair_id or 'legacy'}"
    for k, seed in enumerate(seeds):
        rungs = [(level, eps[k]) for level, eps in by_rung]
        gif_frames, stacked = compose_ladder(rungs)
        gif = VIDEOS_DIR / f"{tag}_seed{seed}_ladder.gif"
        gif_frames[0].save(gif, save_all=True, append_images=gif_frames[1:],
                           duration=int(1000 / args.fps), loop=0)
        logger.info("wrote %s (%d frames)", gif, len(gif_frames))

        outcome = "   ".join(
            f"{lvl}: {'reached' if ep['success'] > 0 else 'TIMEOUT'} "
            f"len={ep['length']} spl={ep['spl']:.2f}" for lvl, ep in rungs)
        title = f"{args.baseline}  |  {pair.pair_id or 'legacy'}  |  eval seed {seed}  |  {outcome}"
        write_ladder_filmstrip(
            stacked, PLOTS_DIR / f"{tag}_rollout_seed{seed}.png", title,
            [ep["length"] for _l, ep in rungs])


if __name__ == "__main__":
    main()
