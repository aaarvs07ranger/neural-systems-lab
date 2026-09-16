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
        from transformers import AutoConfig, AutoImageProcessor, AutoModel

        if dtype not in ("fp16", "fp32"):
            raise ValueError(f"dtype={dtype!r} (expected 'fp16' or 'fp32')")
        self._torch = torch
        self._dtype = torch.float16 if dtype == "fp16" else torch.float32
        self._device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))

        cfg = AutoConfig.from_pretrained(model_id)
        # Trap 1: no masking. Pretraining masked 75% of patches; an agent must see
        # the whole frame, and a random mask would make evaluation irreproducible.
        if getattr(cfg, "mask_ratio", None):
            logger.info("%s: mask_ratio %.2f -> 0.0 (the agent sees the whole frame)",
                        model_id, cfg.mask_ratio)
            cfg.mask_ratio = 0.0
        self._model = AutoModel.from_pretrained(model_id, config=cfg, torch_dtype=self._dtype)
        self._model.eval().to(self._device)
        for p in self._model.parameters():
            p.requires_grad_(False)
        self._has_cls = getattr(cfg, "model_type", "") == "vit_mae"

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

    def _encode(self, frame: np.ndarray) -> np.ndarray:
        torch = self._torch
        with torch.no_grad():
            x = torch.from_numpy(np.ascontiguousarray(frame)).to(self._device)
            x = x.permute(2, 0, 1).unsqueeze(0).to(self._dtype).div(255.0)
            x = torch.nn.functional.interpolate(x, size=(self._size, self._size),
                                                mode="bilinear", align_corners=False)
            x = (x - self._mean) / self._std
            tokens = self._model(pixel_values=x).last_hidden_state
            if self._has_cls:                      # trap 2: patch tokens only
                tokens = tokens[:, 1:, :]
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
