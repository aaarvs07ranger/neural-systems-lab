"""Zero-shot transfer evaluation: trained policy, variant A vs variant B.

Loads the trained model (no weight updates of any kind) and evaluates it with a
deterministic policy on the training house and on every rung of the severity
ladder:

  A   variant A (the training visuals)           — in-domain reference
  L1  materials + lighting + skybox              — mild appearance shift
  L2  L1 + object-appearance swaps               — same objectType, new asset
  L3  L2 + distractor clutter                    — irrelevant objects added

using the SAME episode seed sequence on all of them. The rungs are cumulative
and the geometry never changes, so seeded resets produce paired start poses and
any metric gap is attributable to appearance alone. Those gaps are the
empirical signature of the visual-binding problem we are quantifying.

Walking the whole ladder inside ONE evaluation is what keeps the grid at 100
training runs instead of 300: the agent only ever trains in house A, so a single
trained model serves every rung.

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
import time
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Same guard as main.py: a --smoke eval must never overwrite the real
# results/tables in place. Must precede the config import.
if "--smoke" in sys.argv and "NSL_RESULTS_DIR" not in os.environ:
    _smoke_results = Path(__file__).resolve().parents[1] / (
        "results_smoke_local_" + time.strftime("%Y%m%d_%H%M%S")
    )
    os.environ["NSL_RESULTS_DIR"] = str(_smoke_results)
    print(f"[smoke] results redirected to {_smoke_results} (gitignored)")

from config import (  # noqa: E402
    EVAL_LEVELS,
    PLOTS_DIR,
    TABLES_DIR,
    PPOConfig,
    SmokePPOConfig,
    ensure_dirs,
    get_device,
    resolve_pair,
)
from envs.procthor_env import ObjectNavConfig, make_objectnav_env  # noqa: E402
from envs.task_setup import build_env_config  # noqa: E402
from scripts.train_ppo import final_model_path  # noqa: E402

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
    summaries: Dict[str, Dict[str, float]], out_path: Path, baseline: str,
    pair_id: str = "",
) -> None:
    """Severity ladder: one bar per rung for success & SPL, plus ep-length."""
    import matplotlib

    matplotlib.use("Agg")  # headless rendering
    import matplotlib.pyplot as plt
    import numpy as np

    levels = [lvl for lvl in ("A", "L1", "L2", "L3") if lvl in summaries]
    # Ordered light -> dark so the figure reads as increasing severity even in
    # grayscale; A keeps the reference blue it has had since the first result.
    colors = {"A": COLOR_TRAIN, "L1": "#6fd3ab", "L2": COLOR_TRANSFER,
              "L3": "#0f7a55"}

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(9.4, 3.9), width_ratios=[2, 1], facecolor=COLOR_SURFACE
    )
    for ax in (ax1, ax2):
        ax.set_facecolor(COLOR_SURFACE)
        ax.grid(axis="y", color=COLOR_GRID, linewidth=0.8, zorder=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(COLOR_BASELINE)
        ax.tick_params(colors=COLOR_MUTED, labelcolor=COLOR_INK, length=0)

    metrics = [("success_rate", "Success rate"), ("spl", "SPL")]
    x = np.arange(len(metrics))
    width = min(0.28, 0.8 / max(len(levels), 1))
    offset0 = -width * (len(levels) - 1) / 2
    for i, lvl in enumerate(levels):
        vals = [summaries[lvl][m] for m, _ in metrics]
        bars = ax1.bar(x + offset0 + i * width, vals, width * 0.92,
                       color=colors.get(lvl, COLOR_TRANSFER),
                       label=LEVEL_LABELS.get(lvl, lvl), zorder=3)
        # Direct value labels (relief rule: the aqua series is sub-3:1 on this
        # surface, so numbers wear ink rather than relying on the fill).
        ax1.bar_label(bars, fmt="%.2f", color=COLOR_INK, fontsize=8, padding=2)
    ax1.set_xticks(x, [label for _, label in metrics])
    ax1.set_ylim(0, 1.08)
    title = f"{baseline.upper()}: zero-shot transfer across the severity ladder"
    ax1.set_title(title + (f"  ({pair_id})" if pair_id else ""),
                  color=COLOR_INK, fontsize=11, loc="left")
    ax1.legend(frameon=False, fontsize=8, labelcolor=COLOR_INK,
               loc="upper right", ncol=1)

    lens = [summaries[lvl]["mean_episode_length"] for lvl in levels]
    b3 = ax2.bar(np.arange(len(levels)), lens, 0.55,
                 color=[colors.get(lvl, COLOR_TRANSFER) for lvl in levels],
                 zorder=3)
    ax2.set_xticks(np.arange(len(levels)), levels)
    ax2.set_title("Mean episode length", color=COLOR_INK, fontsize=11, loc="left")
    ax2.bar_label(b3, fmt="%.0f", color=COLOR_INK, fontsize=9, padding=2)

    fig.tight_layout()
    fig.savefig(out_path, dpi=200, facecolor=COLOR_SURFACE)
    plt.close(fig)
    logger.info("wrote %s", out_path)


def load_frozen_model(baseline: str, cfg: Any) -> Any:
    """Load the trained model for `baseline` (weights frozen, ready to predict)."""
    if baseline in ("ppo", "ppo_aug"):
        from stable_baselines3 import PPO

        # Eval envs are built raw in evaluate_on_house — train-time
        # augmentation (ppo_aug) is never applied here by construction.
        model_zip = final_model_path(baseline).with_suffix(".zip")
        if not model_zip.exists():
            raise FileNotFoundError(
                f"{model_zip} not found — run `python main.py --baseline "
                f"{baseline} --stage train` first."
            )
        return PPO.load(str(final_model_path(baseline)), device=get_device())
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
    if baseline == "tdmpc2":
        from models.td_mpc2.adapter import (
            FINAL_MODEL_PATH as TDM_FINAL_MODEL_PATH,
            TDMPC2Adapter,
        )

        if not TDM_FINAL_MODEL_PATH.exists():
            raise FileNotFoundError(
                f"{TDM_FINAL_MODEL_PATH} not found — run "
                "`python main.py --baseline tdmpc2 --stage train` first."
            )
        adapter = TDMPC2Adapter(cfg)
        adapter.load(TDM_FINAL_MODEL_PATH)
        return adapter
    raise NotImplementedError(f"no frozen-model loader for baseline '{baseline}'")


# Human-readable label per rung, used in tables and the figure legend.
LEVEL_LABELS = {
    "A": "A (train visuals)",
    "L1": "B_L1 (materials + lighting)",
    "L2": "B_L2 (+ object appearance)",
    "L3": "B_L3 (+ distractors)",
}


def run_transfer_eval(
    cfg: Any,
    baseline: str = "ppo",
    pair_id: Optional[str] = None,
    levels: Optional[Tuple[str, ...]] = None,
) -> Dict[str, Any]:
    """Evaluate the saved model on house A and every severity rung.

    ``cfg`` is the baseline's config dataclass (PPOConfig, DreamerV3Config,
    ...); only the shared protocol fields are used here: ``eval_episodes``,
    ``eval_seed_base``, ``max_episode_steps``. Writes tables + plot.

    Rungs that have no house on disk are skipped with a warning rather than
    failing, so a pair that only has L1 generated still evaluates.
    """
    import pandas as pd

    ensure_dirs()
    pair = resolve_pair(pair_id, levels)
    model = load_frozen_model(baseline, cfg)
    env_cfg = build_env_config(cfg, pair, split="eval")

    # Sequential evaluation (one Unity process at a time keeps memory sane).
    # Every rung reuses the same seed sequence, so episode i is the same start
    # pose everywhere and the comparison stays paired.
    frames, summaries = [], {}
    for level, house_path in pair.eval_houses:
        if not house_path.exists():
            logger.warning("skipping %s — %s not found", level, house_path)
            continue
        df = evaluate_on_house(
            model, house_path, env_cfg, cfg.eval_episodes,
            cfg.eval_seed_base, name=LEVEL_LABELS.get(level, level),
        )
        df.insert(0, "level", level)
        frames.append(df)
        summaries[level] = summarize(df)

    if "A" not in summaries:
        raise FileNotFoundError(
            f"house A not found for pair '{pair.pair_id or 'legacy'}' — "
            "nothing to compare against."
        )

    episodes = pd.concat(frames, ignore_index=True)
    episodes.to_csv(TABLES_DIR / f"{baseline}_transfer_episodes.csv", index=False)

    # Every rung is scored against A, the in-domain reference.
    base = summaries["A"]
    rows, result_levels = [], {}
    for level, s in summaries.items():
        drop_abs = base["success_rate"] - s["success_rate"]
        spl_drop_abs = base["spl"] - s["spl"]
        rows.append({
            "level": level,
            "variant": LEVEL_LABELS.get(level, level),
            **s,
            "success_drop_abs": drop_abs,
            "success_drop_rel": (drop_abs / base["success_rate"]
                                 if base["success_rate"] > 0 else float("nan")),
            "spl_drop_abs": spl_drop_abs,
            "spl_drop_rel": (spl_drop_abs / base["spl"]
                             if base["spl"] > 0 else float("nan")),
        })
        result_levels[level] = rows[-1]

    summary = pd.DataFrame(rows)
    summary_path = TABLES_DIR / f"{baseline}_transfer_summary"
    summary.to_csv(summary_path.with_suffix(".csv"), index=False)

    md_lines = [
        f"# {baseline.upper()} zero-shot visual transfer"
        + (f" — {pair.pair_id}" if pair.pair_id else ""),
        "",
        summary.drop(columns=["level"]).to_markdown(index=False, floatfmt=".3f"),
        "",
    ]
    for level in [lvl for lvl in summaries if lvl != "A"]:
        r = result_levels[level]
        md_lines.append(
            f"- **{level}: success drop {r['success_drop_abs']:.3f} absolute"
            + (f", {r['success_drop_rel']:.1%} relative"
               if r["success_drop_rel"] == r["success_drop_rel"] else "")
            + f" · SPL drop {r['spl_drop_abs']:.3f} absolute**"
        )
    md_lines += [
        "",
        "_Same frozen policy, same episode seeds (paired starts), no fine-tuning._",
    ]
    summary_path.with_suffix(".md").write_text("\n".join(md_lines) + "\n")
    logger.info("wrote %s.{csv,md}", summary_path)

    plot_transfer(summaries, PLOTS_DIR / f"{baseline}_transfer.png", baseline,
                  pair.pair_id)

    # Backwards-compatible top-level keys: callers (main.py, older scripts) have
    # always read the A -> L1 numbers, which stay exactly where they were.
    headline = result_levels.get("L1", result_levels[
        next(iter(k for k in result_levels if k != "A"), "A")])
    result = {
        "pair_id": pair.pair_id,
        "levels": result_levels,
        "summary_a": base,
        "summary_b": {k: headline[k] for k in
                      ("success_rate", "spl", "mean_episode_length",
                       "mean_total_reward", "episodes")},
        "success_drop_abs": headline["success_drop_abs"],
        "success_drop_rel": headline["success_drop_rel"],
        "spl_drop_abs": headline["spl_drop_abs"],
    }
    logger.info("transfer result: %s", json.dumps(result, indent=2))
    return result


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", choices=("ppo", "ppo_aug", "dreamerv3", "tdmpc2"),
                        default="ppo")
    parser.add_argument("--episodes", type=int, default=None,
                        help="override number of eval episodes per variant")
    parser.add_argument("--pair", default=None,
                        help="house pair id (e.g. pair0); default = $NSL_PAIR, "
                             "else the legacy flat data/house_*.json layout")
    parser.add_argument("--levels", default=None,
                        help="comma-separated severity rungs to evaluate "
                             f"(default {','.join(EVAL_LEVELS)})")
    parser.add_argument("--smoke", action="store_true",
                        help="tiny run to verify pipeline mechanics")
    args = parser.parse_args()

    from config import (
        DreamerV3Config,
        PPOAugConfig,
        SmokeDreamerV3Config,
        SmokePPOAugConfig,
        SmokeTDMPC2Config,
        TDMPC2Config,
    )

    config_classes = {
        ("ppo", False): PPOConfig,
        ("ppo", True): SmokePPOConfig,
        ("ppo_aug", False): PPOAugConfig,
        ("ppo_aug", True): SmokePPOAugConfig,
        ("dreamerv3", False): DreamerV3Config,
        ("dreamerv3", True): SmokeDreamerV3Config,
        ("tdmpc2", False): TDMPC2Config,
        ("tdmpc2", True): SmokeTDMPC2Config,
    }
    cfg = config_classes[(args.baseline, args.smoke)]()
    if args.episodes is not None:
        cfg = type(cfg)(**{**cfg.__dict__, "eval_episodes": args.episodes})
    levels = (tuple(args.levels.split(",")) if args.levels else None)
    run_transfer_eval(cfg, baseline=args.baseline, pair_id=args.pair,
                      levels=levels)


if __name__ == "__main__":
    main()
