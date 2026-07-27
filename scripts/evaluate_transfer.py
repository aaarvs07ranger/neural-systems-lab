"""Zero-shot transfer evaluation: trained policy, variant A vs variant B.

Loads the trained model (no weight updates of any kind), evaluates it with a
deterministic policy on:

  1. variant A (the training visuals)  — in-domain reference
  2. variant B (re-skinned visuals)    — zero-shot transfer

using the SAME episode seed sequence on both variants. Because A and B share
identical geometry, seeded resets produce paired start poses, so any metric
gap is attributable to appearance alone. This gap is the empirical signature
of the visual-binding problem we are quantifying.

Outputs:
    results/tables/<baseline>_transfer_episodes.csv   per-episode metrics
    results/tables/<baseline>_transfer_summary.csv    aggregate + drop metrics
    results/tables/<baseline>_transfer_summary.md     the same, human-readable
    results/plots/<baseline>_transfer.png             bar chart of the drop

Usage:
    python scripts/evaluate_transfer.py [--baseline ppo|dreamerv3] [--episodes N] [--smoke]
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import (  # noqa: E402
    HOUSE_A_PATH,
    HOUSE_B_PATH,
    PLOTS_DIR,
    TABLES_DIR,
    PPOConfig,
    SmokePPOConfig,
    ensure_dirs,
    get_device,
)
from envs.procthor_env import ObjectNavConfig, make_objectnav_env  # noqa: E402
from scripts.train_ppo import FINAL_MODEL_PATH, build_env_config  # noqa: E402

logger = logging.getLogger("evaluate_transfer")

# Chart colors: validated categorical palette (dataviz light-mode slots 1-2).
# Aqua is sub-3:1 on the light surface, so bars carry direct value labels.
COLOR_TRAIN = "#2a78d6"      # variant A (train visuals)
COLOR_TRANSFER = "#1baf7a"   # variant B (zero-shot visuals)
COLOR_SURFACE = "#fcfcfb"
COLOR_INK = "#0b0b0b"
COLOR_MUTED = "#898781"
COLOR_GRID = "#e1e0d9"
COLOR_BASELINE = "#c3c2b7"


def evaluate_on_house(
    model: Any,
    house_path: Path,
    env_cfg: ObjectNavConfig,
    n_episodes: int,
    seed_base: int,
    name: str,
) -> "pd.DataFrame":
    """Roll out the frozen policy for n episodes; returns per-episode metrics."""
    import pandas as pd

    env = make_objectnav_env(house_path, env_cfg, name=name)
    records = []
    try:
        for ep in range(n_episodes):
            # Explicit per-episode seed => reproducible AND paired across variants.
            obs, _ = env.reset(seed=seed_base + ep)
            # Recurrent baselines (DreamerV3, TD-MPC2) carry latent state
            # across steps; it must be cleared at every episode boundary.
            if hasattr(model, "reset_episode"):
                model.reset_episode()
            done = False
            total_reward = 0.0
            info: Dict[str, Any] = {}
            while not done:
                action, _ = model.predict(obs, deterministic=True)
                obs, reward, terminated, truncated, info = env.step(int(action))
                total_reward += reward
                done = terminated or truncated
            records.append(
                {
                    "variant": name,
                    "episode": ep,
                    "seed": seed_base + ep,
                    "success": info.get("success", 0.0),
                    "spl": info.get("spl", 0.0),
                    "episode_length": info.get("episode_step", 0),
                    "path_length": info.get("path_length", 0.0),
                    "shortest_path_length": info.get("shortest_path_length", 0.0),
                    "total_reward": total_reward,
                }
            )
            logger.info(
                "[%s] ep %d/%d: success=%.0f spl=%.3f len=%d reward=%.2f",
                name, ep + 1, n_episodes, records[-1]["success"],
                records[-1]["spl"], records[-1]["episode_length"], total_reward,
            )
    finally:
        env.close()
    return pd.DataFrame.from_records(records)


def summarize(df: "pd.DataFrame") -> Dict[str, float]:
    return {
        "success_rate": float(df["success"].mean()),
        "spl": float(df["spl"].mean()),
        "mean_episode_length": float(df["episode_length"].mean()),
        "mean_total_reward": float(df["total_reward"].mean()),
        "episodes": int(len(df)),
    }


def plot_transfer(
    summary_a: Dict[str, float], summary_b: Dict[str, float], out_path: Path,
    baseline: str,
) -> None:
    """Grouped bars for success rate & SPL (shared 0-1 axis), ep-length panel."""
    import matplotlib

    matplotlib.use("Agg")  # headless rendering
    import matplotlib.pyplot as plt
    import numpy as np

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(8.6, 3.8), width_ratios=[2, 1], facecolor=COLOR_SURFACE
    )
    labels = ["Success rate", "SPL"]
    vals_a = [summary_a["success_rate"], summary_a["spl"]]
    vals_b = [summary_b["success_rate"], summary_b["spl"]]
    x = np.arange(len(labels))
    width = 0.32  # thin marks with a visible gap between the pair

    for ax in (ax1, ax2):
        ax.set_facecolor(COLOR_SURFACE)
        ax.grid(axis="y", color=COLOR_GRID, linewidth=0.8, zorder=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(COLOR_BASELINE)
        ax.tick_params(colors=COLOR_MUTED, labelcolor=COLOR_INK, length=0)

    b1 = ax1.bar(x - width / 2 - 0.01, vals_a, width, color=COLOR_TRAIN,
                 label="Train visuals (A)", zorder=3)
    b2 = ax1.bar(x + width / 2 + 0.01, vals_b, width, color=COLOR_TRANSFER,
                 label="Zero-shot visuals (B)", zorder=3)
    ax1.set_xticks(x, labels)
    ax1.set_ylim(0, 1.0)
    ax1.set_title(f"{baseline.upper()}: zero-shot visual transfer",
                  color=COLOR_INK, fontsize=11, loc="left")
    # Direct value labels (relief rule for the aqua series; text wears ink).
    for bars in (b1, b2):
        ax1.bar_label(bars, fmt="%.2f", color=COLOR_INK, fontsize=9, padding=2)
    ax1.legend(frameon=False, fontsize=9, labelcolor=COLOR_INK, loc="upper right")

    lens = [summary_a["mean_episode_length"], summary_b["mean_episode_length"]]
    b3 = ax2.bar([0, 1], lens, 0.5, color=[COLOR_TRAIN, COLOR_TRANSFER], zorder=3)
    ax2.set_xticks([0, 1], ["A", "B"])
    ax2.set_title("Mean episode length", color=COLOR_INK, fontsize=11, loc="left")
    ax2.bar_label(b3, fmt="%.0f", color=COLOR_INK, fontsize=9, padding=2)

    fig.tight_layout()
    fig.savefig(out_path, dpi=200, facecolor=COLOR_SURFACE)
    plt.close(fig)
    logger.info("wrote %s", out_path)


def load_frozen_model(baseline: str, cfg: Any) -> Any:
    """Load the trained model for `baseline` (weights frozen, ready to predict)."""
    if baseline == "ppo":
        from stable_baselines3 import PPO

        model_zip = FINAL_MODEL_PATH.with_suffix(".zip")
        if not model_zip.exists():
            raise FileNotFoundError(
                f"{model_zip} not found — run scripts/train_ppo.py first."
            )
        return PPO.load(str(FINAL_MODEL_PATH), device=get_device())
    if baseline == "dreamerv3":
        from models.dreamer_v3.adapter import (
            FINAL_MODEL_PATH as DV3_FINAL_MODEL_PATH,
            DreamerV3Adapter,
        )

        if not DV3_FINAL_MODEL_PATH.exists():
            raise FileNotFoundError(
                f"{DV3_FINAL_MODEL_PATH} not found — run "
                "`python main.py --baseline dreamerv3 --stage train` first."
            )
        adapter = DreamerV3Adapter(cfg)
        adapter.load(DV3_FINAL_MODEL_PATH)
        return adapter
    raise NotImplementedError(f"no frozen-model loader for baseline '{baseline}'")


def run_transfer_eval(cfg: Any, baseline: str = "ppo") -> Dict[str, Any]:
    """Full A/B evaluation of the saved model; writes tables + plot.

    ``cfg`` is the baseline's config dataclass (PPOConfig, DreamerV3Config,
    ...); only the shared protocol fields are used here: ``eval_episodes``,
    ``eval_seed_base``, ``max_episode_steps``.
    """
    import pandas as pd

    ensure_dirs()
    model = load_frozen_model(baseline, cfg)
    env_cfg = build_env_config(cfg)

    # Sequential evaluation (one Unity process at a time keeps memory sane).
    df_a = evaluate_on_house(
        model, HOUSE_A_PATH, env_cfg, cfg.eval_episodes,
        cfg.eval_seed_base, name="variant_a",
    )
    df_b = evaluate_on_house(
        model, HOUSE_B_PATH, env_cfg, cfg.eval_episodes,
        cfg.eval_seed_base, name="variant_b",
    )

    episodes = pd.concat([df_a, df_b], ignore_index=True)
    episodes.to_csv(TABLES_DIR / f"{baseline}_transfer_episodes.csv", index=False)

    summary_a, summary_b = summarize(df_a), summarize(df_b)
    drop_abs = summary_a["success_rate"] - summary_b["success_rate"]
    drop_rel = drop_abs / summary_a["success_rate"] if summary_a["success_rate"] > 0 else float("nan")
    spl_drop_abs = summary_a["spl"] - summary_b["spl"]

    summary = pd.DataFrame(
        [
            {"variant": "A (train visuals)", **summary_a},
            {"variant": "B (zero-shot visuals)", **summary_b},
        ]
    )
    summary_path = TABLES_DIR / f"{baseline}_transfer_summary"
    summary.to_csv(summary_path.with_suffix(".csv"), index=False)

    md_lines = [
        f"# {baseline.upper()} zero-shot visual transfer",
        "",
        summary.to_markdown(index=False, floatfmt=".3f"),
        "",
        f"- **Success-rate drop (A - B): {drop_abs:.3f} absolute"
        + (f", {drop_rel:.1%} relative**" if drop_rel == drop_rel else "**"),
        f"- **SPL drop (A - B): {spl_drop_abs:.3f} absolute**",
        "",
        "_Same frozen policy, same episode seeds (paired starts), no fine-tuning._",
    ]
    summary_path.with_suffix(".md").write_text("\n".join(md_lines) + "\n")
    logger.info("wrote %s.{csv,md}", summary_path)

    plot_transfer(summary_a, summary_b, PLOTS_DIR / f"{baseline}_transfer.png", baseline)

    result = {
        "summary_a": summary_a,
        "summary_b": summary_b,
        "success_drop_abs": drop_abs,
        "success_drop_rel": drop_rel,
        "spl_drop_abs": spl_drop_abs,
    }
    logger.info("transfer result: %s", json.dumps(result, indent=2))
    return result


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", choices=("ppo", "dreamerv3"), default="ppo")
    parser.add_argument("--episodes", type=int, default=None,
                        help="override number of eval episodes per variant")
    parser.add_argument("--smoke", action="store_true",
                        help="tiny run to verify pipeline mechanics")
    args = parser.parse_args()

    from config import DreamerV3Config, SmokeDreamerV3Config

    config_classes = {
        ("ppo", False): PPOConfig,
        ("ppo", True): SmokePPOConfig,
        ("dreamerv3", False): DreamerV3Config,
        ("dreamerv3", True): SmokeDreamerV3Config,
    }
    cfg = config_classes[(args.baseline, args.smoke)]()
    if args.episodes is not None:
        cfg = type(cfg)(**{**cfg.__dict__, "eval_episodes": args.episodes})
    run_transfer_eval(cfg, baseline=args.baseline)


if __name__ == "__main__":
    main()
