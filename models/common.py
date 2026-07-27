"""Shared interface every baseline must satisfy for the transfer pipeline.

PPO fulfils this contract via scripts/train_ppo.py + SB3's own model class;
DreamerV3 via models/dreamer_v3/adapter.py. The TD-MPC2 adapter (next
milestone) should implement the same protocol so main.py can drive all
three baselines uniformly and the eval/reporting code is reused unchanged.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Protocol, Tuple


class BaselineAdapter(Protocol):
    """Contract for a trainable baseline in the A->B transfer experiment."""

    name: str

    def train(self, house_a_path: Path, total_timesteps: int, seed: int) -> Path:
        """Train on visual variant A; return path to the saved final model."""
        ...

    def load(self, model_path: Path) -> None:
        """Load a trained model for evaluation (weights frozen)."""
        ...

    def predict(
        self, observation, deterministic: bool = True
    ) -> Tuple[int, Optional[object]]:
        """Discrete action for an RGB observation, as an SB3-style
        ``(action, state)`` tuple so the eval loop can unpack uniformly."""
        ...

    def reset_episode(self) -> None:
        """Clear any recurrent/latent state at an episode boundary.

        The eval loop calls this via ``hasattr`` after every ``env.reset()``;
        stateless baselines (e.g. plain SB3 PPO models) simply lack it."""
        ...
