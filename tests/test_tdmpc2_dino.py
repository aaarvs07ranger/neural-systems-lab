"""Contract tests for the TD-MPC2 + frozen-encoder agent (``tdmpc2_dino``).

The real encoder (DINOv2-giant) and the simulator live on the cluster, so these
tests drive the TD-MPC2 bridge and adapter with a fake environment that already
emits feature vectors -- which is exactly what the frozen-encoder wrapper hands
the bridge. What must hold:

  1. The bridge detects vector observations from the env's own observation
     space, passes them through as float32 and does NOT stack them (the same
     single-frame feature PPO+DINOv2 sees).
  2. The rgb path is untouched (the original ``tdmpc2`` agent must not change).
  3. A state-observation TD-MPC2 can be built, act, update, save, and be loaded
     back by the adapter, which reads the feature width off the checkpoint.
  4. The two TD-MPC2 agents write to different directories.

Run: python tests/test_tdmpc2_dino.py
"""
from __future__ import annotations

import sys
import tempfile
from dataclasses import replace
from pathlib import Path

import gymnasium as gym
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

FEAT = 24


class _FakeFeatureEnv(gym.Env):
    """Stands in for ObjectNav wrapped by FrozenVisionEncoder."""

    def __init__(self, dim: int = FEAT) -> None:
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, shape=(dim,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(5)
        self._t = 0
        self._rng = np.random.default_rng(0)

    def reset(self, seed=None, options=None):
        self._t = 0
        return self._rng.standard_normal(self.observation_space.shape).astype(np.float32), {}

    def step(self, action):
        self._t += 1
        obs = self._rng.standard_normal(self.observation_space.shape).astype(np.float32)
        done = self._t >= 8
        return obs, float(action == 0), False, done, {"success": 0.0}


class _FakeImageEnv(_FakeFeatureEnv):
    def __init__(self) -> None:
        super().__init__()
        self.observation_space = gym.spaces.Box(0, 255, shape=(128, 128, 3), dtype=np.uint8)

    def reset(self, seed=None, options=None):
        self._t = 0
        return np.zeros((128, 128, 3), np.uint8), {}

    def step(self, action):
        self._t += 1
        return np.zeros((128, 128, 3), np.uint8), 0.0, False, self._t >= 8, {"success": 0.0}


def test_bridge_passes_features_through_unstacked():
    from models.td_mpc2.thor_env import TDMPC2THOREnv
    env = TDMPC2THOREnv(_FakeFeatureEnv(), frame_stack=3)
    assert env.obs_type == "state"
    assert env.obs_shape == (FEAT,)
    obs = env.reset()
    assert obs.shape == (FEAT,) and obs.dtype == torch.float32, (obs.shape, obs.dtype)
    obs2, _r, _d, info = env.step(env.rand_act())
    assert obs2.shape == (FEAT,) and not torch.equal(obs, obs2)
    assert "terminated" in info


def test_rgb_path_unchanged():
    from models.td_mpc2.thor_env import TDMPC2THOREnv
    env = TDMPC2THOREnv(_FakeImageEnv(), image_size=64, frame_stack=3)
    assert env.obs_type == "rgb"
    assert env.obs_shape == (9, 64, 64)
    obs = env.reset()
    assert obs.shape == (9, 64, 64) and obs.dtype == torch.uint8


def test_config_state_requires_dimension():
    from config import SmokeTDMPC2DinoConfig
    from models.td_mpc2.adapter import _make_tdmpc2_config
    try:
        _make_tdmpc2_config(SmokeTDMPC2DinoConfig(), 5, "state", 0)
    except ValueError:
        pass
    else:
        raise AssertionError("state obs without a feature width must raise")
    cfg = _make_tdmpc2_config(SmokeTDMPC2DinoConfig(), 5, "state", FEAT)
    assert cfg.obs == "state" and cfg.obs_shape == {"state": (FEAT,)}


def test_agents_write_to_separate_directories():
    from models.td_mpc2.adapter import run_paths
    a, b = run_paths("tdmpc2"), run_paths("tdmpc2_dino")
    assert all(x != y for x, y in zip(a, b)), (a, b)
    assert a[2].name == "tdmpc2_final.pt"   # original agent's file name unchanged


def test_dino_config_differs_from_tdmpc2_only_in_identity_and_encoder():
    from config import TDMPC2Config, TDMPC2DinoConfig
    base, dino = TDMPC2Config().__dict__, TDMPC2DinoConfig().__dict__
    diff = {k for k in base if base[k] != dino[k]}
    assert diff == {"baseline_name", "frozen_encoder"}, diff


def test_state_agent_acts_updates_saves_and_reloads():
    from tensordict.tensordict import TensorDict

    from config import SmokeTDMPC2DinoConfig
    from models.td_mpc2.adapter import TDMPC2Adapter, _make_tdmpc2_config
    from models.td_mpc2.thor_env import TDMPC2THOREnv
    from models.td_mpc2.vendor.common.buffer import Buffer
    from models.td_mpc2.vendor.tdmpc2 import TDMPC2

    tcfg = replace(SmokeTDMPC2DinoConfig(), batch_size=4, buffer_size=200)
    env = TDMPC2THOREnv(_FakeFeatureEnv(), frame_stack=3)
    cfg = _make_tdmpc2_config(tcfg, 5, "state", FEAT)
    cfg.device = "cpu"
    agent, buffer = TDMPC2(cfg), Buffer(cfg)

    def td(obs, action=None, reward=None, term=None):
        return TensorDict(dict(
            obs=obs.unsqueeze(0),
            action=(action if action is not None else torch.full((5,), float("nan"))).unsqueeze(0),
            reward=(reward if reward is not None else torch.tensor(float("nan"))).unsqueeze(0),
            terminated=(term if term is not None else torch.tensor(float("nan"))).unsqueeze(0),
        ), batch_size=(1,))

    for _ in range(3):
        obs = env.reset()
        tds, done = [td(obs)], False
        while not done:
            a = agent.act(obs, t0=len(tds) == 1)
            obs, r, done, info = env.step(a)
            tds.append(td(obs, a, r, info["terminated"]))
        buffer.add(torch.cat(tds))
    metrics = agent.update(buffer)
    assert all(np.isfinite(float(v)) for v in metrics.values()), metrics

    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "tdmpc2_dino_final.pt"
        agent.save(path)
        adapter = TDMPC2Adapter(tcfg)
        import models.td_mpc2.adapter as ad
        orig = ad._tdmpc2_device
        ad._tdmpc2_device = lambda: "cpu"
        try:
            adapter.load(path)
        finally:
            ad._tdmpc2_device = orig
        assert adapter._obs_type == "state"
        action, _ = adapter.predict(np.zeros(FEAT, np.float32))
        assert 0 <= action < 5


if __name__ == "__main__":
    fns = [(n, f) for n, f in sorted(globals().items())
           if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in fns:
        try:
            fn()
            print(f"PASS  {name}")
        except Exception as exc:  # noqa: BLE001 — the runner reports everything
            failed += 1
            print(f"FAIL  {name}: {type(exc).__name__}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    raise SystemExit(1 if failed else 0)
