"""Contract tests for the ppo_aug photometric augmentation.

These pin the protocol-critical properties of :mod:`envs.augmentation`:
identity at neutral parameters, per-episode (not per-step) resampling,
seed determinism, the uint8/shape contract, and that the jitter actually
changes the image enough to matter. Run with::

    python -m pytest tests/test_augmentation.py -q
"""
from __future__ import annotations

import sys
from pathlib import Path

import gymnasium as gym
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from envs.augmentation import PhotometricJitter, apply_jitter  # noqa: E402

H = W = 32


def _frame(seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(H, W, 3), dtype=np.uint8)


class _StubEnv(gym.Env):
    """Minimal env emitting a fixed frame — no THOR/Unity needed."""

    def __init__(self) -> None:
        self.observation_space = gym.spaces.Box(0, 255, (H, W, 3), np.uint8)
        self.action_space = gym.spaces.Discrete(5)
        self._frame = _frame()

    def reset(self, *, seed=None, options=None):
        return self._frame, {}

    def step(self, action):
        return self._frame, 0.0, False, False, {}


def test_neutral_params_are_identity() -> None:
    f = _frame()
    assert np.array_equal(apply_jitter(f, 1.0, 1.0, 1.0, 0.0), f)


def test_dtype_and_shape_contract() -> None:
    out = apply_jitter(_frame(), 1.3, 0.7, 1.2, 20.0)
    assert out.dtype == np.uint8 and out.shape == (H, W, 3)
    assert out.flags["C_CONTIGUOUS"]  # torch conversion requires this


def test_jitter_visibly_changes_pixels() -> None:
    """Guards against a silently no-op augmentation (the worst failure mode:
    a 'ppo_aug' run that is secretly just ppo)."""
    env = PhotometricJitter(_StubEnv(), seed=0)
    raw, _ = _StubEnv().reset()
    obs, _ = env.reset()
    assert np.abs(obs.astype(int) - raw.astype(int)).mean() > 5.0


def test_params_resample_per_episode_not_per_step() -> None:
    env = PhotometricJitter(_StubEnv(), seed=0, resample="episode")
    env.reset()
    a = env.step(0)[0]
    b = env.step(0)[0]
    assert np.array_equal(a, b), "params must be fixed within an episode"
    env.reset()
    c = env.step(0)[0]
    assert not np.array_equal(a, c), "params must be redrawn on reset"


def test_step_mode_resamples_every_frame() -> None:
    env = PhotometricJitter(_StubEnv(), seed=0, resample="step")
    env.reset()
    assert not np.array_equal(env.step(0)[0], env.step(0)[0])


def test_same_seed_same_stream() -> None:
    outs = []
    for _ in range(2):
        env = PhotometricJitter(_StubEnv(), seed=7)
        env.reset()
        outs.append(env.step(0)[0])
    assert np.array_equal(*outs)


def test_different_seeds_differ() -> None:
    frames = []
    for seed in (0, 1):
        env = PhotometricJitter(_StubEnv(), seed=seed)
        env.reset()
        frames.append(env.step(0)[0])
    assert not np.array_equal(*frames)


def test_rejects_bad_resample_mode() -> None:
    try:
        PhotometricJitter(_StubEnv(), resample="sometimes")
    except ValueError:
        return
    raise AssertionError("expected ValueError for invalid resample mode")


if __name__ == "__main__":
    # Dependency-free runner: the pinned `nsl` env has no pytest, and adding
    # one for eight assertions is not worth perturbing the lockfiles.
    fns = [(n, f) for n, f in sorted(globals().items())
           if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in fns:
        try:
            fn()
            print(f"PASS  {name}")
        except Exception as exc:  # noqa: BLE001 — test runner reports everything
            failed += 1
            print(f"FAIL  {name}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    raise SystemExit(1 if failed else 0)
