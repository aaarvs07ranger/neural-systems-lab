"""Bridge between our gymnasium ProcTHOR env and DreamerV3's env interface.

The vendored NM512 training loop (``tools.simulate``) expects an *old-gym*
style environment:

* ``reset() -> obs_dict`` and ``step(action) -> (obs_dict, reward, done, info)``
  (no ``terminated``/``truncated`` split);
* dict observations carrying ``image`` plus the ``is_first`` / ``is_last`` /
  ``is_terminal`` flags DreamerV3 trains its continuation head on;
* one-hot float actions, delivered as a ``{"action": ..., "logprob": ...}``
  dict (upstream splits these responsibilities across its OneHotAction /
  SelectAction / TimeLimit / UUID wrappers — we fold all four into this one
  class instead of vendoring their ``gym``-dependent wrappers module);
* a fresh ``id`` per episode (the replay cache keys episodes by it).

Frames are downscaled from the THOR render resolution (128x128) to Dreamer's
native 64x64 so the world model matches the published architecture and stays
tractable on the M4's MPS backend.
"""
from __future__ import annotations

import datetime
import uuid
from typing import Any, Dict, Tuple

import numpy as np
from gymnasium import spaces

from envs.procthor_env import ProcTHORObjectNavEnv


class DreamerTHOREnv:
    """Old-gym dict-observation adapter around :class:`ProcTHORObjectNavEnv`."""

    def __init__(self, env: ProcTHORObjectNavEnv, image_size: int, seed: int) -> None:
        self._env = env
        self._size = int(image_size)
        # Seed the start-pose RNG on the FIRST reset only (mirrors the PPO
        # training protocol); subsequent episodes vary reproducibly from it.
        self._pending_seed: int | None = int(seed)
        self.id = self._new_id()

        img = spaces.Box(0, 255, (self._size, self._size, 3), dtype=np.uint8)
        self.observation_space = spaces.Dict(
            {
                "image": img,
                "is_first": spaces.Box(0, 1, (), dtype=bool),
                "is_last": spaces.Box(0, 1, (), dtype=bool),
                "is_terminal": spaces.Box(0, 1, (), dtype=bool),
            }
        )
        # One-hot action box, as produced by Dreamer's onehot actor head.
        n = int(env.action_space.n)
        self.action_space = spaces.Box(0.0, 1.0, (n,), dtype=np.float32)
        self.num_actions = n

    # ------------------------------------------------------------------
    @staticmethod
    def _new_id() -> str:
        timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        return f"{timestamp}-{uuid.uuid4().hex}"

    def _obs(self, frame: np.ndarray, is_first: bool, is_last: bool,
             is_terminal: bool) -> Dict[str, Any]:
        import cv2  # installed as an ai2thor dependency

        if frame.shape[0] != self._size or frame.shape[1] != self._size:
            frame = cv2.resize(
                frame, (self._size, self._size), interpolation=cv2.INTER_AREA
            )
        return {
            "image": np.ascontiguousarray(frame, dtype=np.uint8),
            "is_first": is_first,
            "is_last": is_last,
            "is_terminal": is_terminal,
        }

    # ------------------------------------------------------------------
    # Old-gym API consumed by vendored tools.simulate (via Damy)
    # ------------------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        self.id = self._new_id()  # new replay-cache key per episode
        frame, _ = self._env.reset(seed=self._pending_seed)
        self._pending_seed = None
        return self._obs(frame, is_first=True, is_last=False, is_terminal=False)

    def step(
        self, action: Any
    ) -> Tuple[Dict[str, Any], float, bool, Dict[str, Any]]:
        if isinstance(action, dict):  # {"action": onehot, "logprob": ...}
            action = action["action"]
        index = int(np.argmax(np.asarray(action)))
        frame, reward, terminated, truncated, info = self._env.step(index)
        done = terminated or truncated
        # Discount 0 only on TRUE termination; time-limit truncation must not
        # teach the continuation head that the state was absorbing.
        info = dict(info)
        info["discount"] = np.array(0.0 if terminated else 1.0, dtype=np.float32)
        obs = self._obs(frame, is_first=False, is_last=done, is_terminal=terminated)
        return obs, float(reward), done, info

    def close(self) -> None:
        self._env.close()
