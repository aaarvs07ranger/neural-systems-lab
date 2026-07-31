"""Central configuration for the NSL zero-shot visual-transfer baseline pipeline.

Every script in this repo (env generation, training, evaluation) pulls paths
and hyperparameters from this single module so experiments stay reproducible.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Paths (everything is relative to the project root, never the CWD)
# ---------------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parent
DATA_DIR: Path = PROJECT_ROOT / "data"
# NSL_RESULTS_DIR redirects the whole results tree (checkpoints, logs, tables,
# plots) — parallel slurm array tasks point it at per-seed dirs so their
# checkpoint/replay accounting never collides. data/ stays shared.
RESULTS_DIR: Path = Path(os.environ.get("NSL_RESULTS_DIR", str(PROJECT_ROOT / "results")))
LOGS_DIR: Path = RESULTS_DIR / "logs"
CHECKPOINTS_DIR: Path = RESULTS_DIR / "checkpoints"
TABLES_DIR: Path = RESULTS_DIR / "tables"
PLOTS_DIR: Path = RESULTS_DIR / "plots"

HOUSE_A_PATH: Path = DATA_DIR / "house_a.json"          # training visual variant
HOUSE_B_PATH: Path = DATA_DIR / "house_b.json"          # zero-shot transfer variant
TASK_CONFIG_PATH: Path = DATA_DIR / "task_config.json"  # target object, seeds, provenance


def ensure_dirs() -> None:
    """Create all output directories (idempotent)."""
    for d in (DATA_DIR, RESULTS_DIR, LOGS_DIR, CHECKPOINTS_DIR, TABLES_DIR, PLOTS_DIR):
        d.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Device selection (M4 MPS first, CPU fallback)
# ---------------------------------------------------------------------------
def get_device() -> str:
    """Return the best available device: 'cuda' (cluster) > 'mps' (M4) > 'cpu'.

    Import of torch is deferred so that scripts which never touch torch
    (e.g. envs/generate_variants.py) can import this module cheaply.
    """
    import torch  # local import by design

    if torch.cuda.is_available():
        return "cuda"
    return "mps" if torch.backends.mps.is_available() else "cpu"


# ---------------------------------------------------------------------------
# Environment-generation settings
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class GenerationConfig:
    """Settings for producing the paired visual variants (house A / house B)."""

    dataset: str = "procthor-10k"
    # Pinned dataset revision compatible with our pinned (pre-5.0) AI2-THOR
    # commit build; HEAD of procthor-10k requires ai2thor >= 5.0.
    dataset_revision: str = "ab3cacd0fc17754d4c080a3fd50b18395fae8647"
    split: str = "train"
    scan_limit: int = 500          # how many houses to scan for selection/material pools
    max_rooms: int = 2             # keep the house small so PPO can learn at modest budgets
    variant_seed: int = 1337       # RNG seed for the visual re-skin of variant B
    # Target types we accept, in preference order (must exist in the chosen house).
    preferred_targets: Tuple[str, ...] = (
        "Television", "Fridge", "Bed", "Sofa", "Toilet", "Microwave",
    )


# ---------------------------------------------------------------------------
# PPO baseline settings
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class PPOConfig:
    """Hyperparameters for the stable-baselines3 PPO baseline."""

    total_timesteps: int = 150_000
    n_steps: int = 1024            # rollout length per update (single env)
    batch_size: int = 128
    n_epochs: int = 4
    learning_rate: float = 2.5e-4
    gamma: float = 0.99
    gae_lambda: float = 0.95
    ent_coef: float = 0.01
    clip_range: float = 0.2
    seed: int = 0
    checkpoint_freq: int = 25_000  # env steps between checkpoints
    max_episode_steps: int = 200
    eval_episodes: int = 25
    eval_seed_base: int = 10_000   # eval episode seeds start here (disjoint from training)


# Tiny settings used by `--smoke` to verify the full pipeline mechanics quickly.
@dataclass(frozen=True)
class SmokePPOConfig(PPOConfig):
    total_timesteps: int = 512
    n_steps: int = 128
    batch_size: int = 64
    checkpoint_freq: int = 512
    max_episode_steps: int = 50
    eval_episodes: int = 3


# ---------------------------------------------------------------------------
# DreamerV3 baseline settings (vendored NM512/dreamerv3-torch, see
# models/dreamer_v3/). Budget & eval protocol match PPOConfig for a fair table.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class DreamerV3Config:
    """Hyperparameters for the DreamerV3 baseline (M4/MPS-sized)."""

    # Budget & protocol — keep identical to PPOConfig.
    total_timesteps: int = 150_000   # env steps INCLUDING prefill
    seed: int = 0
    max_episode_steps: int = 200
    eval_episodes: int = 25
    eval_seed_base: int = 10_000

    # Observation: Dreamer's published CNN operates at 64x64; THOR frames
    # (128x128) are downscaled in the adapter wrapper.
    image_size: int = 64

    # Replay / optimisation. train_ratio = replayed frames per env step;
    # upstream uses 512 on GPU clusters. 32 (~4.7k updates at 150k steps)
    # collapsed the actor (flat value head, zero actor grad — see CLAUDE.md
    # Session 4); 128 = one grad step per 8 env steps (~18.7k updates), the
    # largest ratio tolerable on M4 wall clock. Go to 512 on cluster GPUs.
    prefill: int = 2_500             # random-policy steps seeding the replay buffer
    batch_size: int = 16
    batch_length: int = 64
    train_ratio: int = 128
    pretrain: int = 100              # grad steps on the buffer before rollouts
    dataset_size: int = 1_000_000    # replay capacity in frames (disk-backed)

    # Model size — upstream defaults (the small DMC-scale world model).
    dyn_hidden: int = 512
    dyn_deter: int = 512
    units: int = 512
    cnn_depth: int = 32

    # Bookkeeping.
    log_every: int = 2_000           # env steps between TensorBoard writes
    save_every: int = 10_000         # env steps between latest.pt checkpoints


@dataclass(frozen=True)
class SmokeDreamerV3Config(DreamerV3Config):
    total_timesteps: int = 500
    prefill: int = 250
    batch_size: int = 8
    batch_length: int = 12
    train_ratio: int = 16
    pretrain: int = 5
    max_episode_steps: int = 50
    eval_episodes: int = 3
    log_every: int = 200
    save_every: int = 250


# ---------------------------------------------------------------------------
# TD-MPC2 baseline settings (vendored nicklashansen/tdmpc2, see
# models/td_mpc2/). Budget & eval protocol match PPOConfig for a fair table.
# All algorithm hyperparameters are upstream's published single-task defaults
# (config.yaml at the pinned commit); only budget/protocol fields are ours.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class TDMPC2Config:
    """Hyperparameters for the TD-MPC2 baseline (upstream default recipe)."""

    # Budget & protocol — keep identical to PPOConfig.
    total_timesteps: int = 150_000
    seed: int = 0
    max_episode_steps: int = 200
    eval_episodes: int = 25
    eval_seed_base: int = 10_000

    # Observation: upstream rgb recipe — 64x64, 3 stacked frames (9 channels).
    image_size: int = 64
    frame_stack: int = 3

    # Recipe: 1 grad update per env step after seed_steps random steps, plus a
    # seed_steps-sized pretrain burst (upstream online_trainer). seed_steps
    # None => upstream formula max(1000, 5 * episode_length).
    seed_steps: Optional[int] = None
    batch_size: int = 256
    buffer_size: int = 1_000_000     # min'd with total steps inside the buffer
    horizon: int = 3

    # Optimisation (upstream defaults).
    lr: float = 3e-4
    enc_lr_scale: float = 0.3
    grad_clip_norm: float = 20.0
    tau: float = 0.01
    rho: float = 0.5
    consistency_coef: float = 20.0
    reward_coef: float = 0.1
    value_coef: float = 0.1
    termination_coef: float = 1.0    # episodic task: success terminates
    entropy_coef: float = 1e-4
    discount_denom: float = 5.0
    discount_min: float = 0.95
    discount_max: float = 0.995

    # Planning (MPPI, upstream defaults).
    iterations: int = 6
    num_samples: int = 512
    num_elites: int = 64
    num_pi_trajs: int = 24
    min_std: float = 0.05
    max_std: float = 2.0
    temperature: float = 0.5

    # Heads / architecture.
    log_std_min: float = -10.0
    log_std_max: float = 2.0
    num_bins: int = 101
    vmin: float = -10.0
    vmax: float = 10.0
    model_size: int = 5              # upstream default single-task model (5M)
    num_channels: int = 32
    dropout: float = 0.01
    simnorm_dim: int = 8

    # Bookkeeping.
    log_every: int = 2_000           # env steps between metric log lines
    save_every: int = 10_000         # env steps between latest.pt checkpoints


@dataclass(frozen=True)
class SmokeTDMPC2Config(TDMPC2Config):
    total_timesteps: int = 600
    seed_steps: Optional[int] = 200
    batch_size: int = 16
    buffer_size: int = 10_000
    # model_size stays 5 (as the full run): the upstream rgb conv encoder
    # emits a fixed 512-dim feature, which only matches latent_dim=512 —
    # model_size 1 (latent 128) is structurally incompatible with rgb obs.
    iterations: int = 2
    num_samples: int = 64
    num_elites: int = 8
    num_pi_trajs: int = 4
    max_episode_steps: int = 50
    eval_episodes: int = 3
    log_every: int = 100
    save_every: int = 300
