"""Frozen pretrained vision encoder as the agent's observation.

The JEPA/MAE agents are ordinary PPO with the trained CNN replaced by a frozen
ViT: image -> encoder -> feature vector -> small MLP head. Only the head learns.

Where this sits, and why
------------------------
The encoder is an OBSERVATION WRAPPER on the environment, not part of the
policy. Frozen weights mean a frame's feature never changes, so it should be
computed exactly once per environment step; inside an SB3 policy, PPO's
``n_epochs`` x minibatch passes would re-encode every stored frame and multiply
the cost several-fold.

Consequence, and the difference from `envs.augmentation`: photometric jitter is a
TRAINING-ONLY wrapper (eval must see raw frames). This wrapper IS the
observation, so it applies identically on the training and evaluation paths --
the agent has no other way to see.

Two traps this file exists to avoid
-----------------------------------
1. **ViT-MAE masks 75% of the image by default.** `transformers.ViTMAEModel`
   carries `mask_ratio=0.75` from pretraining and drops that fraction of patches
   at random on every forward pass. Left alone it would (a) hide most of the
   scene from the agent and (b) make the observation random, breaking the
   deterministic evaluation protocol. `mask_ratio` is forced to 0.0 here, and a
   contract test asserts the same frame twice gives the identical feature.
2. **CLS token.** ViT-MAE prepends one; I-JEPA has none. Pooling blindly over
   `last_hidden_state` would average a different token set for the two encoders.
   Patch tokens only, for both.

Normalisation uses each model's own published mean/std (from its preprocessor
config), applied as tensor maths on the GPU -- not the HF image processor, which
runs PIL per frame on the CPU and would dominate the per-step cost.
"""
from __future__ import annotations

import logging
from typing import Any, Optional, Tuple

import gymnasium as gym
import numpy as np

logger = logging.getLogger("frozen_encoder")

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)


def load_encoder(model_id: str, dtype: str = "fp16", attn: str = "", device: Optional[str] = None):
    """Load a frozen encoder the ONE way the agent uses it.

    Anything that touches these encoders -- the agent, the cost check, any later
    analysis -- must come through here, or it measures a different model than the
    one that runs. That is not hypothetical: the first cost check loaded ViT-MAE
    directly and timed it with 75% of the image masked (fast, and wrong), while
    its precision comparison unknowingly compared two DIFFERENT random maskings
    and reported the difference as a precision effect.

    Returns (model, config, torch_dtype).
    """
    import torch
    from transformers import AutoConfig, AutoModel

    if dtype not in ("fp16", "fp32"):
        raise ValueError(f"dtype={dtype!r} (expected 'fp16' or 'fp32')")
    torch_dtype = torch.float16 if dtype == "fp16" else torch.float32
    cfg = AutoConfig.from_pretrained(model_id)
    if getattr(cfg, "mask_ratio", None):
        logger.info("%s: mask_ratio %.2f -> 0.0 (the agent sees the whole frame)",
                    model_id, cfg.mask_ratio)
        cfg.mask_ratio = 0.0
    kw = {"attn_implementation": attn} if attn else {}
    model = AutoModel.from_pretrained(model_id, config=cfg, torch_dtype=torch_dtype, **kw)
    model.eval()
    if device is not None:
        model.to(device)
    for p in model.parameters():
        p.requires_grad_(False)
    return model, cfg, torch_dtype


class FrozenVisionEncoder(gym.ObservationWrapper):
    """uint8 (H, W, 3) frames -> float32 feature vector from a frozen ViT."""

    def __init__(
        self,
        env: gym.Env,
        model_id: str,
        device: Optional[str] = None,
        dtype: str = "fp16",
        image_size: Optional[int] = None,
    ) -> None:
        super().__init__(env)
        import torch
        from transformers import AutoImageProcessor

        self._torch = torch
        self._device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        # Trap 1 (no masking) lives in load_encoder, so every caller gets it.
        self._model, cfg, self._dtype = load_encoder(
            model_id, dtype=dtype, device=str(self._device))
        self._cfg = cfg
        self._patch = int(getattr(cfg, "patch_size", 0) or 0)

        proc = AutoImageProcessor.from_pretrained(model_id)
        mean = tuple(getattr(proc, "image_mean", IMAGENET_MEAN))
        std = tuple(getattr(proc, "image_std", IMAGENET_STD))
        size = getattr(proc, "size", {}) or {}
        self._size = int(image_size or size.get("height") or size.get("shortest_edge") or 224)
        self._mean = torch.tensor(mean, device=self._device).view(1, 3, 1, 1).to(self._dtype)
        self._std = torch.tensor(std, device=self._device).view(1, 3, 1, 1).to(self._dtype)

        dim = int(self._probe_dim())
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, shape=(dim,), dtype=np.float32)
        logger.info("frozen encoder %s on %s (%s): %dx%d -> %d-d feature, %.0fM params (never trained)",
                    model_id, self._device, dtype, self._size, self._size, dim,
                    sum(p.numel() for p in self._model.parameters()) / 1e6)

    # -- encoding -----------------------------------------------------------
    def _probe_dim(self) -> int:
        h, w = self.env.observation_space.shape[:2]
        return self._encode(np.zeros((h, w, 3), dtype=np.uint8)).shape[0]

    def _n_prefix_tokens(self, n_tokens: int) -> int:
        """How many non-patch tokens the encoder puts in front of the patches.

        (image_size / patch_size)^2 patches must be there; anything extra is a
        class token and/or register tokens, which are bookkeeping slots and not
        part of the picture. Raises rather than guessing: a silent miscount
        would average the wrong token set and nothing downstream would notice.
        """
        if not self._patch:
            return 0
        patches = (self._size // self._patch) ** 2
        prefix = n_tokens - patches
        if prefix < 0 or prefix > 8:
            raise RuntimeError(
                f"{n_tokens} tokens but {patches} patches expected "
                f"({self._size}px / patch {self._patch}) — cannot tell which "
                "tokens are the image")
        return prefix

    def _encode(self, frame: np.ndarray) -> np.ndarray:
        torch = self._torch
        with torch.no_grad():
            x = torch.from_numpy(np.ascontiguousarray(frame)).to(self._device)
            x = x.permute(2, 0, 1).unsqueeze(0).to(self._dtype).div(255.0)
            x = torch.nn.functional.interpolate(x, size=(self._size, self._size),
                                                mode="bilinear", align_corners=False)
            x = (x - self._mean) / self._std
            tokens = self._model(pixel_values=x).last_hidden_state
            # Trap 2, generalised: pool PATCH tokens only. Rather than keep a
            # list of which encoder prepends what (MAE a class token, I-JEPA
            # nothing, DINOv2 a class token, DINOv3 a class token plus four
            # registers), count the patches the image must produce and drop
            # whatever sits in front of them. Correct by construction for any
            # encoder, including ones not written yet.
            tokens = tokens[:, self._n_prefix_tokens(tokens.shape[1]):, :]
            feat = tokens.mean(dim=1)
        return feat.float().squeeze(0).cpu().numpy()

    def observation(self, observation: np.ndarray) -> np.ndarray:
        return self._encode(observation)


def wrap_if_frozen_encoder(env: gym.Env, cfg: Any) -> Tuple[gym.Env, str]:
    """Wrap `env` when `cfg` names a frozen encoder; returns (env, SB3 policy name).

    One helper used by BOTH the training and evaluation paths, so the two can
    never disagree about what the agent sees.
    """
    model_id = getattr(cfg, "frozen_encoder", "")
    if not model_id:
        return env, "CnnPolicy"
    return (FrozenVisionEncoder(env, model_id,
                                dtype=getattr(cfg, "encoder_dtype", "fp16")),
            "MlpPolicy")
