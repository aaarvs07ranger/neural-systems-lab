"""Contract tests for the DreamerV3 + frozen-encoder agent (``dreamerv3_dino``).

The real encoder (DINOv2-giant) and the simulator live on the cluster, so these
tests drive the DreamerV3 bridge and adapter with a fake environment that already
emits feature vectors -- which is exactly what the frozen-encoder wrapper hands
the bridge. What must hold:

  1. The bridge reads the observation kind off the env's own observation space,
     puts a feature vector under ``feature`` (float32, untouched) and has no
     ``image`` key; the pixel path is unchanged.
  2. The feature config routes ``feature`` to the MLP encoder and decoder and
     builds no CNN; the pixel config is upstream's default, as before.
  3. The DINOv2 config differs from DreamerV3's only in its name and encoder.
  4. Vendored patch #5: the image rescale still happens when there is an image,
     and an observation without one no longer raises.
  5. A feature-input DreamerV3 trains end to end through the real adapter
     (replay, updates, checkpoints), saves, and is loaded back by the adapter,
     which reads the feature width off the checkpoint, then acts.
  6. The two DreamerV3 agents write to different directories.

Run: python tests/test_dreamerv3_dino.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

# Before anything imports config: every path this file creates (checkpoints,
# replay, logs) lands in a throwaway directory, never in the repo's results/.
_TMP = tempfile.mkdtemp(prefix="nsl_test_dv3dino_")
os.environ["NSL_RESULTS_DIR"] = _TMP

import gymnasium as gym  # noqa: E402
import numpy as np  # noqa: E402

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
        terminated = int(action) == 0 and self._t > 3
        truncated = self._t >= 8
        return obs, float(terminated), terminated, truncated and not terminated, {"success": float(terminated)}

    def close(self):
        pass


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


def _onehot(i: int) -> np.ndarray:
    a = np.zeros(5, np.float32)
    a[i] = 1.0
    return a


def test_bridge_routes_features_to_feature_key():
    from models.dreamer_v3.thor_env import DreamerTHOREnv
    env = DreamerTHOREnv(_FakeFeatureEnv(), image_size=64, seed=0)
    assert env.obs_kind == "feature" and env.obs_size == FEAT
    assert set(env.observation_space.spaces) == {"feature", "is_first", "is_last", "is_terminal"}
    obs = env.reset()
    assert "image" not in obs and obs["is_first"] and not obs["is_last"]
    assert obs["feature"].shape == (FEAT,) and obs["feature"].dtype == np.float32
    obs2, _r, _done, info = env.step({"action": _onehot(2), "logprob": 0.0})
    assert obs2["feature"].shape == (FEAT,) and not np.array_equal(obs["feature"], obs2["feature"])
    assert not obs2["is_first"] and "discount" in info


def test_image_path_unchanged():
    from models.dreamer_v3.thor_env import DreamerTHOREnv
    env = DreamerTHOREnv(_FakeImageEnv(), image_size=64, seed=0)
    assert env.obs_kind == "image"
    assert set(env.observation_space.spaces) == {"image", "is_first", "is_last", "is_terminal"}
    obs = env.reset()
    assert "feature" not in obs
    assert obs["image"].shape == (64, 64, 3) and obs["image"].dtype == np.uint8


def test_feature_config_routes_feature_to_the_mlp():
    from config import DreamerV3DinoConfig
    from models.dreamer_v3.adapter import _make_dreamer_config
    img = _make_dreamer_config(DreamerV3DinoConfig(), 5, "image")
    feat = _make_dreamer_config(DreamerV3DinoConfig(), 5, "feature")
    for part in ("encoder", "decoder"):
        assert img.__dict__[part]["cnn_keys"] == "image" and img.__dict__[part]["mlp_keys"] == "$^"
        assert feat.__dict__[part]["mlp_keys"] == "^feature$" and feat.__dict__[part]["cnn_keys"] == "$^"
        # Nothing else about the encoder/decoder changes.
        rest = {k: v for k, v in img.__dict__[part].items() if k not in ("mlp_keys", "cnn_keys")}
        assert rest == {k: v for k, v in feat.__dict__[part].items() if k not in ("mlp_keys", "cnn_keys")}
    others = {k for k in img.__dict__ if k not in ("encoder", "decoder")}
    assert all(img.__dict__[k] == feat.__dict__[k] for k in others)
    try:
        _make_dreamer_config(DreamerV3DinoConfig(), 5, "pixels")
    except ValueError:
        pass
    else:
        raise AssertionError("an unknown observation kind must raise")


def test_dino_config_differs_from_dreamerv3_only_in_identity_and_encoder():
    from config import (DreamerV3Config, DreamerV3DinoConfig, SmokeDreamerV3Config,
                        SmokeDreamerV3DinoConfig)
    for base, dino in ((DreamerV3Config(), DreamerV3DinoConfig()),
                       (SmokeDreamerV3Config(), SmokeDreamerV3DinoConfig())):
        b, d = base.__dict__, dino.__dict__
        diff = {k for k in b if b[k] != d[k]}
        assert diff == {"baseline_name", "frozen_encoder"}, diff


def test_agents_write_to_separate_directories():
    from models.dreamer_v3 import adapter as ad
    a, b = ad.run_paths("dreamerv3"), ad.run_paths("dreamerv3_dino")
    assert all(x != y for x, y in zip(a, b)), (a, b)
    # The original agent's paths are exactly the ones every existing run used.
    assert (ad.DV3_CKPT_DIR, ad.DV3_LOG_DIR, ad.FINAL_MODEL_PATH) == a[:3]
    assert ad.FINAL_MODEL_PATH.name == "dreamer_final.pt"


def test_vendor_patch_keeps_the_image_rescale():
    import torch

    from models.dreamer_v3.vendor.models import WorldModel
    fake = SimpleNamespace(_config=SimpleNamespace(device="cpu", discount=0.997))
    flags = {"is_first": np.zeros((1, 2)), "is_terminal": np.zeros((1, 2))}
    out = WorldModel.preprocess(fake, {"image": np.full((1, 2, 4, 4, 3), 255.0), **flags})
    assert torch.allclose(out["image"], torch.ones_like(out["image"]))
    feat = np.arange(6, dtype=np.float32).reshape(1, 2, 3)
    out = WorldModel.preprocess(fake, {"feature": feat, **flags})   # used to raise KeyError
    assert "image" not in out and torch.equal(out["feature"], torch.tensor(feat))


def test_feature_agent_trains_saves_reloads_and_acts():
    from config import SmokeDreamerV3DinoConfig
    from envs import frozen_encoder
    from models.dreamer_v3 import adapter as ad

    from models.dreamer_v3.vendor import networks

    cfg = SmokeDreamerV3DinoConfig()
    saved = (ad.make_objectnav_env, frozen_encoder.wrap_if_frozen_encoder, ad.get_device,
             networks.MLP.__init__.__defaults__)
    # The fake env already emits features, so the encoder wrapper must not load
    # DINOv2 here; CPU keeps the test deterministic on any machine.
    ad.make_objectnav_env = lambda *a, **k: _FakeFeatureEnv()
    frozen_encoder.wrap_if_frozen_encoder = lambda env, c: (env, "MlpPolicy")
    ad.get_device = lambda: "cpu"
    # The vendored MLP builds a small std tensor on device="cuda" whenever the
    # caller passes no device, which MultiEncoder/MultiDecoder never do. Only the
    # "normal_std_fixed" output reads it, and neither the feature encoder nor
    # the symlog_mse feature decoder uses that output, so on the cluster (always
    # a GPU) it is created and never touched. This machine has no CUDA.
    networks.MLP.__init__.__defaults__ = tuple(
        "cpu" if d == "cuda" else d for d in saved[3])
    try:
        final = ad.DreamerV3Adapter(cfg).train(Path("unused.json"), cfg.total_timesteps, seed=0)
        assert final == ad.run_paths("dreamerv3_dino")[2] and final.exists(), final
        assert any(ad.run_paths("dreamerv3_dino")[1].joinpath("train_eps").glob("*.npz"))

        import torch
        sd = torch.load(final, map_location="cpu")["agent_state_dict"]
        assert not any("encoder._cnn" in k or "decoder._cnn" in k for k in sd), "a CNN was built"
        first = next(v for k, v in sd.items() if k.endswith(ad._MLP_IN_SUFFIX))
        assert first.shape[1] == FEAT, first.shape

        agent = ad.DreamerV3Adapter(cfg)
        agent.load(final)
        assert agent._obs_kind == "feature"
        rng = np.random.default_rng(1)
        for _ in range(3):
            action, _state = agent.predict(rng.standard_normal(FEAT).astype(np.float32))
            assert isinstance(action, int) and 0 <= action < 5
        agent.reset_episode()
        assert agent._is_first
    finally:
        (ad.make_objectnav_env, frozen_encoder.wrap_if_frozen_encoder, ad.get_device,
         networks.MLP.__init__.__defaults__) = saved


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
