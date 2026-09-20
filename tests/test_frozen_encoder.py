"""Contract tests for the frozen-encoder observation wrapper.

The real encoders are 600M-parameter ViTs that live on the cluster, so these
tests stand in a fake `transformers` module and check the wiring the agent
depends on -- in particular the two traps documented in
`envs/frozen_encoder.py`:

  1. ViT-MAE masks 75% of the image by default. Unfixed, the agent would see a
     quarter of the scene and evaluation would be random.
  2. ViT-MAE prepends a CLS token and I-JEPA does not, so pooling must take
     patch tokens only or the two encoders average different things.

Run: python tests/test_frozen_encoder.py
"""
from __future__ import annotations

import sys
import types
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

HIDDEN = 8
N_PATCHES = 4


class _Cfg:
    def __init__(self, model_type: str, mask_ratio: float = 0.0,
                 n_registers: int = 0) -> None:
        self.model_type = model_type
        self.mask_ratio = mask_ratio
        # 16px image / patch 8 => 2x2 = 4 patches, matching N_PATCHES. The
        # wrapper counts patches to work out how many non-image tokens sit in
        # front of them, so this has to be self-consistent.
        self.patch_size = 8
        self.num_register_tokens = n_registers


class _Out:
    def __init__(self, tensor: torch.Tensor) -> None:
        self.last_hidden_state = tensor


class _FakeModel(torch.nn.Module):
    """Returns one token per patch (plus a CLS token when the model has one).

    Token k is filled with the mean pixel of the input times (k + 1), so the
    output depends on the input and the CLS token is distinguishable.
    """

    def __init__(self, cfg: _Cfg) -> None:
        super().__init__()
        self.cfg = cfg
        self.seen_mask_ratio = cfg.mask_ratio
        self.dummy = torch.nn.Parameter(torch.zeros(1))
        self.calls = 0

    def forward(self, pixel_values: torch.Tensor):  # noqa: D401
        self.calls += 1
        prefix = (1 if self.cfg.model_type in ("vit_mae", "dinov2") else 0)
        prefix += int(self.cfg.num_register_tokens)
        n = N_PATCHES + prefix
        base = pixel_values.mean()
        toks = torch.stack([base * (k + 1) for k in range(n)]).view(1, n, 1)
        for k in range(prefix):
            toks[0, k] = 999.0        # CLS + registers: must not be pooled
        return _Out(toks.expand(1, n, HIDDEN).to(pixel_values.dtype))


def _install_fake_transformers(model_type: str, mask_ratio: float,
                               n_registers: int = 0,
                               crop_16_from_32: bool = False) -> _FakeModel:
    cfg = _Cfg(model_type, mask_ratio, n_registers)
    holder = {}

    class AutoConfig:
        @staticmethod
        def from_pretrained(_id):
            return cfg

    class AutoModel:
        @staticmethod
        def from_pretrained(_id, config=None, torch_dtype=None):
            m = _FakeModel(config)
            m.to(torch_dtype or torch.float32)
            holder["model"] = m
            return m

    class AutoImageProcessor:
        @staticmethod
        def from_pretrained(_id):
            proc = types.SimpleNamespace()
            proc.image_mean = (0.5, 0.5, 0.5)
            proc.image_std = (0.5, 0.5, 0.5)
            proc.size = {"height": 16, "width": 16}
            if crop_16_from_32:
                # DINOv2's shape: resize the short edge to one size, then
                # centre-crop to a smaller one. What the model sees is the CROP.
                proc.size = {"shortest_edge": 32}
                proc.crop_size = {"height": 16, "width": 16}
                proc.do_center_crop = True
            return proc

    mod = types.ModuleType("transformers")
    mod.AutoConfig, mod.AutoModel, mod.AutoImageProcessor = AutoConfig, AutoModel, AutoImageProcessor
    sys.modules["transformers"] = mod
    return holder


class _StubEnv:
    """Minimal gym-like env emitting uint8 frames."""

    def __init__(self) -> None:
        import gymnasium as gym
        self.observation_space = gym.spaces.Box(0, 255, shape=(12, 12, 3), dtype=np.uint8)
        self.action_space = gym.spaces.Discrete(5)
        self.metadata, self.render_mode, self.spec = {}, None, None
        self.unwrapped = self

    def _frame(self, val: int) -> np.ndarray:
        return np.full((12, 12, 3), val, dtype=np.uint8)

    def reset(self, **_kw):
        return self._frame(100), {}

    def step(self, _a):
        return self._frame(150), 0.0, False, False, {}


def _wrapper(model_type="ijepa", mask_ratio=0.0, dtype="fp32", n_registers=0,
             crop_16_from_32=False):
    holder = _install_fake_transformers(model_type, mask_ratio, n_registers,
                                        crop_16_from_32)
    from envs.frozen_encoder import FrozenVisionEncoder
    return FrozenVisionEncoder(_StubEnv(), "fake/model", device="cpu", dtype=dtype), holder


def test_mae_masking_is_switched_off() -> None:
    """Trap 1: pretraining hides 75% of patches; the agent must see all of them."""
    _w, holder = _wrapper(model_type="vit_mae", mask_ratio=0.75)
    assert holder["model"].cfg.mask_ratio == 0.0, holder["model"].cfg.mask_ratio


def test_cls_token_is_excluded_for_mae() -> None:
    """Trap 2: MAE has a CLS token, I-JEPA has none; pool patch tokens only."""
    w, _h = _wrapper(model_type="vit_mae")
    feat = w.observation(np.full((12, 12, 3), 100, dtype=np.uint8))
    assert feat.max() < 100, f"CLS token (999) leaked into the feature: {feat.max()}"


def test_observation_is_a_float_vector_matching_the_space() -> None:
    w, _h = _wrapper()
    feat = w.observation(np.full((12, 12, 3), 100, dtype=np.uint8))
    assert feat.dtype == np.float32, feat.dtype
    assert feat.shape == w.observation_space.shape == (HIDDEN,), (feat.shape, w.observation_space.shape)
    assert w.observation_space.dtype == np.float32


def test_same_frame_gives_the_same_feature() -> None:
    """Evaluation is deterministic only if encoding is."""
    w, _h = _wrapper()
    frame = np.full((12, 12, 3), 123, dtype=np.uint8)
    assert np.array_equal(w.observation(frame), w.observation(frame))


def test_different_frames_give_different_features() -> None:
    w, _h = _wrapper()
    a = w.observation(np.full((12, 12, 3), 10, dtype=np.uint8))
    b = w.observation(np.full((12, 12, 3), 200, dtype=np.uint8))
    assert not np.allclose(a, b)


def test_encoder_runs_once_per_observation() -> None:
    """One forward pass per env step — the reason it wraps the env, not the policy."""
    w, holder = _wrapper()
    before = holder["model"].calls
    w.observation(np.full((12, 12, 3), 77, dtype=np.uint8))
    assert holder["model"].calls == before + 1, holder["model"].calls - before


def test_encoder_parameters_are_frozen() -> None:
    w, holder = _wrapper()
    assert all(not p.requires_grad for p in holder["model"].parameters())
    assert not holder["model"].training


def test_helper_is_a_no_op_without_an_encoder() -> None:
    """Every other baseline must be untouched by this code path."""
    from envs.frozen_encoder import wrap_if_frozen_encoder

    class _Cfg:
        frozen_encoder = ""

    env = _StubEnv()
    out, policy = wrap_if_frozen_encoder(env, _Cfg())
    assert out is env and policy == "CnnPolicy", (out, policy)


def test_helper_wraps_and_switches_policy_when_an_encoder_is_named() -> None:
    _install_fake_transformers("ijepa", 0.0)
    from envs.frozen_encoder import FrozenVisionEncoder, wrap_if_frozen_encoder

    class _Cfg:
        frozen_encoder = "fake/model"
        encoder_dtype = "fp32"

    out, policy = wrap_if_frozen_encoder(_StubEnv(), _Cfg())
    assert isinstance(out, FrozenVisionEncoder) and policy == "MlpPolicy", (out, policy)


def test_rejects_unknown_dtype() -> None:
    try:
        _wrapper(dtype="fp8")
    except ValueError:
        return
    raise AssertionError("expected ValueError for an unsupported dtype")


def test_centre_crop_size_wins_over_resize_size() -> None:
    """DINOv2 resizes the short edge to 256 and then crops to 224, so 224 is
    what the model sees -- and it is also what I-JEPA and MAE see, which is what
    keeps the three encoders comparable. Reading the resize size would feed it a
    resolution it was never trained at."""
    w, _h = _wrapper(model_type="dinov2", crop_16_from_32=True)
    assert w._size == 16, f"used the resize size, not the crop: {w._size}"
    # ...and it still pools the right tokens at that size.
    feat = w.observation(np.full((16, 16, 3), 40, dtype=np.uint8))
    assert feat.max() < 900


def test_class_and_register_tokens_are_all_excluded() -> None:
    """DINOv3 prepends a class token AND four registers -- bookkeeping slots,
    not picture. The wrapper works out how many to drop by counting the patches
    the image must produce, so it needs no per-model table."""
    w, _h = _wrapper(model_type="dinov2", n_registers=4)
    feat = w.observation(np.full((16, 16, 3), 40, dtype=np.uint8))
    assert feat.max() < 900, f"a prefix token (999) leaked into the feature: {feat.max()}"


def test_miscounted_tokens_raise_rather_than_pool_the_wrong_set() -> None:
    """Negative control: if the token count cannot be explained by the patch
    grid, pooling silently over the wrong set is the failure we cannot detect
    downstream, so it must raise instead."""
    try:
        # 1 class token + 9 registers is more prefix than any real encoder has,
        # so the count cannot be explained by the patch grid. The wrapper probes
        # its feature width when it is built, so this raises there.
        _wrapper(model_type="dinov2", n_registers=9)
    except RuntimeError as exc:
        assert "tokens" in str(exc), exc
    else:
        raise AssertionError("a token count it cannot explain must raise")


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
            print(f"FAIL  {name}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    raise SystemExit(1 if failed else 0)
