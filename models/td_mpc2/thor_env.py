"""Old-gym tensor bridge: ProcTHOR ObjectNav -> vendored TD-MPC2 conventions.

Folds the roles of upstream's ``envs/dmcontrol.py:Pixels`` (64x64 rgb,
3-frame stack, CHW) and ``envs/wrappers/tensor.py:TensorWrapper`` (torch
tensors, old-gym ``(obs, reward, done, info)`` step API) into one class over
our gymnasium :class:`ProcTHORObjectNavEnv`.

Discrete-action relaxation
--------------------------
TD-MPC2 plans in a continuous action space. We expose the Discrete(5)
ObjectNav actions as ``Box(-1, 1, (5,))`` and execute ``argmax(action)``.
The MPPI planner and Gaussian policy prior operate on the relaxed 5-vector;
the argmax at the env boundary is the standard one-hot relaxation from the
plan in ``models/td_mpc2/README.md``. ``rand_act()`` samples uniformly in the
box, whose argmax is uniform over the 5 discrete actions.
"""
from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path
from typing import Optional

import numpy as np
import torch


def frame_to_chw(frame: np.ndarray, size: int) -> np.ndarray:
    """THOR HWC uint8 frame -> resized CHW uint8 (cv2 INTER_AREA, like Dreamer)."""
    import cv2

    if frame.shape[0] != size or frame.shape[1] != size:
        frame = cv2.resize(frame, (size, size), interpolation=cv2.INTER_AREA)
    return np.ascontiguousarray(frame.transpose(2, 0, 1))


class TDMPC2THOREnv:
    """Single-task, single-env bridge satisfying the vendored trainer contract."""

    def __init__(
        self,
        env,
        image_size: int = 64,
        frame_stack: int = 3,
        seed: int = 0,
        max_episode_steps: int = 200,
    ) -> None:
        self._env = env
        self._size = int(image_size)
        self._frames: deque = deque(maxlen=int(frame_stack))
        self._num_actions = int(env.action_space.n)
        self._seed: Optional[int] = seed  # consumed by the first reset only
        self._rng = np.random.default_rng(seed)
        self.max_episode_steps = int(max_episode_steps)

    @property
    def num_actions(self) -> int:
        return self._num_actions

    @property
    def obs_shape(self) -> tuple:
        return (self._frames.maxlen * 3, self._size, self._size)

    def rand_act(self) -> torch.Tensor:
        return torch.from_numpy(
            self._rng.uniform(-1.0, 1.0, self._num_actions).astype(np.float32)
        )

    def _stacked_obs(self) -> torch.Tensor:
        return torch.from_numpy(np.concatenate(self._frames))  # (stack*3, H, W) uint8

    def reset(self) -> torch.Tensor:
        obs, _ = self._env.reset(seed=self._seed)
        self._seed = None  # subsequent resets draw fresh start poses
        frame = frame_to_chw(obs, self._size)
        for _ in range(self._frames.maxlen):
            self._frames.append(frame)
        return self._stacked_obs()

    def step(self, action: torch.Tensor):
        discrete = int(torch.as_tensor(action).argmax().item())
        obs, reward, terminated, truncated, info = self._env.step(discrete)
        self._frames.append(frame_to_chw(obs, self._size))
        out = defaultdict(float, info)
        out["success"] = float(info.get("success", 0.0))
        # True MDP termination only (success); time-limit truncation must NOT
        # train the termination head or zero the bootstrap.
        out["terminated"] = torch.tensor(float(terminated))
        done = bool(terminated or truncated)
        return self._stacked_obs(), torch.tensor(float(reward), dtype=torch.float32), done, out

    def close(self) -> None:
        self._env.close()
