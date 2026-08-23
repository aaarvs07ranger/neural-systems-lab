"""Photometric augmentation wrapper for the PPO+augmentation baseline.

:class:`PhotometricJitter` applies the standard color-jitter recipe
(brightness, contrast, saturation, hue — the 0.4/0.4/0.4/0.1 strengths
popularized by SimCLR/RAD-style pixel-RL augmentation) to the uint8 RGB
observations of :class:`envs.procthor_env.ProcTHORObjectNavEnv`.

Protocol-critical design rules
------------------------------
* TRAIN PATH ONLY. ``scripts/train_ppo.py`` wraps the training env when
  ``cfg.augment`` is set; ``scripts/evaluate_transfer.py`` builds its eval
  envs directly and never wraps them — the paired A/B transfer protocol
  always sees raw frames, so ppo_aug numbers stay comparable with every
  other baseline.
* Jitter parameters are resampled once per EPISODE by default (domain-
  randomization convention: the world keeps one consistent re-tinted look
  within an episode, simulating training across many visual variants —
  the closest analogue of the A->B appearance shift). ``resample="step"``
  switches to independent per-frame jitter (RAD-style) if wanted later.
* Determinism: the wrapper owns a private ``np.random.Generator`` seeded
  from the training seed. It never touches the env's start-pose RNG, so
  start-pose sequences are identical between ppo and ppo_aug runs at the
  same seed.
* Op order is fixed (saturation -> contrast -> brightness -> hue); each op
  matches the torchvision ColorJitter definition.
"""
from __future__ import annotations

from typing import Optional, Tuple

import gymnasium as gym
import numpy as np

# Rec. 601 luma weights (same convention as torchvision's rgb_to_grayscale).
_LUMA = np.array([0.299, 0.587, 0.114], dtype=np.float32)


class PhotometricJitter(gym.ObservationWrapper):
    """Brightness/contrast/saturation/hue jitter on uint8 (H, W, 3) obs."""

    def __init__(
        self,
        env: gym.Env,
        brightness: float = 0.4,
        contrast: float = 0.4,
        saturation: float = 0.4,
        hue_degrees: float = 36.0,
        resample: str = "episode",
        seed: int = 0,
    ) -> None:
        super().__init__(env)
        if resample not in ("episode", "step"):
            raise ValueError(f"resample={resample!r} (expected 'episode' or 'step')")
        self._strength: Tuple[float, float, float, float] = (
            float(brightness), float(contrast), float(saturation), float(hue_degrees),
        )
        self._resample = resample
        # Fixed offset decorrelates this stream from any other consumer of the
        # training seed without hurting reproducibility.
        self._rng = np.random.default_rng(int(seed) + 0x5EED)
        self._params: Tuple[float, float, float, float] = self._draw()

    # ------------------------------------------------------------------
    def _draw(self) -> Tuple[float, float, float, float]:
        b, c, s, h = self._strength
        return (
            float(self._rng.uniform(1.0 - b, 1.0 + b)),   # brightness factor
            float(self._rng.uniform(1.0 - c, 1.0 + c)),   # contrast factor
            float(self._rng.uniform(1.0 - s, 1.0 + s)),   # saturation factor
            float(self._rng.uniform(-h, h)),              # hue shift, degrees
        )

    # ------------------------------------------------------------------
    def reset(self, *, seed: Optional[int] = None, options=None):
        if self._resample == "episode":
            self._params = self._draw()
        return super().reset(seed=seed, options=options)

    def observation(self, observation: np.ndarray) -> np.ndarray:
        if self._resample == "step":
            self._params = self._draw()
        b, c, s, hue = self._params

        x = observation.astype(np.float32)
        gray = x @ _LUMA                                   # (H, W) luma image
        # saturation: blend with per-pixel grayscale
        x = x * s + gray[..., None] * (1.0 - s)
        # contrast: blend with the scalar mean of the grayscale image
        x = x * c + float(gray.mean()) * (1.0 - c)
        # brightness: scale
        x = x * b
        out = np.clip(x, 0.0, 255.0).astype(np.uint8)

        if abs(hue) > 1e-6:
            import cv2  # installed as an ai2thor dependency

            # HSV_FULL maps hue onto [0, 255], so uint8 addition wraps the hue
            # circle exactly (no 179-bucket truncation as with plain HSV).
            hsv = cv2.cvtColor(out, cv2.COLOR_RGB2HSV_FULL)
            shift = np.uint8(int(round(hue / 360.0 * 256.0)) % 256)
            hsv[..., 0] = hsv[..., 0] + shift              # uint8 wraparound is intended
            out = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB_FULL)
        return np.ascontiguousarray(out)
