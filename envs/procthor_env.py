"""Gymnasium-compatible ObjectNav environment for fixed ProcTHOR houses.

Wraps an AI2-THOR controller around a *fixed* ProcTHOR house specification
(a JSON dict) and exposes a standard :class:`gymnasium.Env` so the same task
can be driven by stable-baselines3 (PPO), DreamerV3, or TD-MPC2 adapters.

Key design decisions
--------------------
* The house is loaded ONCE when the Unity controller boots; per-episode resets
  only teleport the agent to a new start pose. The action set is
  navigation-only, so scene state cannot drift between episodes — this makes
  resets ~100x faster than a full ``controller.reset(scene=house)`` reload.
* Success (default): the agent is within ``success_distance`` meters
  (xz-plane Euclidean) of any instance of the target object type AND that
  instance is currently visible. Termination on success is automatic so the
  sparse task stays learnable at small step budgets (an explicit ``Done``
  action a la habitat ObjectNav is much harder; flip ``require_done`` later
  for the paper-grade protocol).
* SPL is computed per episode with AI2-THOR's shortest-path utilities and
  falls back to the straight-line start->target distance if navmesh
  pathfinding fails on a procedural house.
* Variants A and B share identical geometry, so their reachable-position sets
  match. Seeding eval resets with the same seed sequence on both variants
  yields PAIRED episode starts — a cleaner zero-shot transfer contrast.
"""
from __future__ import annotations

import json
import logging
import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import gymnasium as gym
import numpy as np
from gymnasium import spaces

logger = logging.getLogger(__name__)

Vec3 = Dict[str, float]


def _resolve_thor_platform() -> Optional[Any]:
    """Select the AI2-THOR rendering platform for this host.

    ``NSL_THOR_PLATFORM`` values:
      * ``cloudrendering`` — headless Vulkan Linux build (Hyak/slurm GPU nodes;
        no X server or window required).
      * ``default``        — ai2thor's native windowed build for the host OS.
      * ``auto`` (unset)   — ``cloudrendering`` on display-less Linux,
        ``default`` everywhere else (macOS keeps its Rosetta Unity window).
    """
    choice = os.environ.get("NSL_THOR_PLATFORM", "auto").strip().lower()
    if choice == "auto":
        headless_linux = sys.platform.startswith("linux") and not os.environ.get("DISPLAY")
        choice = "cloudrendering" if headless_linux else "default"
    if choice == "default":
        return None  # Controller(platform=None) picks the windowed build
    if choice == "cloudrendering":
        from ai2thor.platform import CloudRendering  # deferred: heavy import

        return CloudRendering
    raise ValueError(
        f"NSL_THOR_PLATFORM={choice!r} not recognized "
        "(expected 'auto', 'default', or 'cloudrendering')"
    )


def _xz_distance(a: Vec3, b: Vec3) -> float:
    """Euclidean distance in the floor plane (y ignored)."""
    return math.sqrt((a["x"] - b["x"]) ** 2 + (a["z"] - b["z"]) ** 2)


def load_house(path: Path) -> Dict[str, Any]:
    """Load a ProcTHOR house JSON produced by ``envs/generate_variants.py``."""
    with open(path, "r") as f:
        return json.load(f)


@dataclass(frozen=True)
class ObjectNavConfig:
    """All knobs for the ObjectNav task and the underlying THOR controller."""

    target_object_type: str = "Television"
    width: int = 128                 # render width  (also the observation width)
    height: int = 128                # render height (also the observation height)
    field_of_view: float = 90.0
    grid_size: float = 0.25          # meters per MoveAhead step
    rotate_step_degrees: float = 30.0
    look_step_degrees: float = 30.0
    visibility_distance: float = 1.5
    success_distance: float = 1.5
    require_visibility: bool = True  # target must be on-screen at success time
    max_steps: int = 200
    step_penalty: float = -0.01
    success_reward: float = 10.0
    distance_reward_scale: float = 1.0   # reward per meter of progress toward target
    actions: Tuple[str, ...] = (
        "MoveAhead", "RotateLeft", "RotateRight", "LookUp", "LookDown",
    )


class ProcTHORObjectNavEnv(gym.Env):
    """ObjectNav in a single fixed ProcTHOR house.

    Observations: RGB uint8 array of shape (height, width, 3).
    Actions: ``Discrete(len(config.actions))`` mapping onto THOR nav actions.
    """

    metadata = {"render_modes": ["rgb_array"]}

    def __init__(
        self,
        house: Dict[str, Any],
        config: ObjectNavConfig,
        name: str = "procthor-objectnav",
    ) -> None:
        super().__init__()
        self._house = house
        self._cfg = config
        self.name = name

        self.observation_space = spaces.Box(
            low=0, high=255, shape=(config.height, config.width, 3), dtype=np.uint8
        )
        self.action_space = spaces.Discrete(len(config.actions))

        # Unity controller is created lazily on first reset() so that merely
        # constructing the env (e.g. for space inspection) never boots Unity.
        self._controller: Optional[Any] = None
        self._reachable: Optional[List[Vec3]] = None

        # Per-episode state.
        self._steps: int = 0
        self._path_length: float = 0.0
        self._shortest_path: float = 0.0
        self._prev_dist: float = float("inf")
        self._last_pos: Vec3 = {"x": 0.0, "y": 0.0, "z": 0.0}
        self._last_frame: Optional[np.ndarray] = None

    # ------------------------------------------------------------------
    # Controller lifecycle
    # ------------------------------------------------------------------
    def _ensure_controller(self) -> None:
        """Boot the Unity controller with the fixed house (first call only)."""
        if self._controller is not None:
            return
        from ai2thor.controller import Controller  # deferred: heavy import

        platform = _resolve_thor_platform()
        platform_kwargs: Dict[str, Any] = {}
        if platform is not None:
            platform_kwargs["platform"] = platform
            # slurm's cgroup exposes only the allocated GPU(s); render on the
            # first one unless explicitly redirected.
            platform_kwargs["gpu_device"] = int(os.environ.get("NSL_THOR_GPU", "0"))
        logger.info(
            "[%s] booting AI2-THOR controller (first reset, platform=%s)...",
            self.name, platform.__name__ if platform is not None else "default",
        )
        self._controller = Controller(
            scene=self._house,
            **platform_kwargs,
            agentMode="default",
            gridSize=self._cfg.grid_size,
            # snapToGrid must be False for non-90-degree rotateStepDegrees;
            # this is also the standard ProcTHOR configuration.
            snapToGrid=False,
            rotateStepDegrees=self._cfg.rotate_step_degrees,
            visibilityDistance=self._cfg.visibility_distance,
            width=self._cfg.width,
            height=self._cfg.height,
            fieldOfView=self._cfg.field_of_view,
            renderDepthImage=False,
            renderInstanceSegmentation=False,
        )
        event = self._controller.step(action="GetReachablePositions")
        positions = event.metadata.get("actionReturn") or []
        if not positions:
            raise RuntimeError(
                f"[{self.name}] GetReachablePositions returned no positions — "
                "the house spec is likely malformed."
            )
        # Sort for a deterministic ordering independent of engine internals,
        # so seeded start-pose sampling pairs up across visual variants.
        self._reachable = sorted(positions, key=lambda p: (p["x"], p["z"]))
        logger.info(
            "[%s] controller ready: %d reachable positions, target=%s",
            self.name, len(self._reachable), self._cfg.target_object_type,
        )

    # ------------------------------------------------------------------
    # Observation extraction
    # ------------------------------------------------------------------
    def _frame_to_obs(self, event: Any) -> np.ndarray:
        """Return a contiguous uint8 (H, W, 3) observation.

        Two THOR-on-macOS quirks are handled here:
        * frames can be negative-stride views -> ascontiguousarray copy;
        * resizing the Unity window changes the render resolution mid-run
          -> ask THOR to restore it and rescale the offending frame so the
          observation contract is never violated.
        """
        frame = np.ascontiguousarray(event.frame, dtype=np.uint8)
        expected = (self._cfg.height, self._cfg.width)
        if frame.shape[:2] != expected:
            logger.warning(
                "[%s] frame is %s, expected %s (Unity window was resized?) — "
                "restoring resolution", self.name, frame.shape[:2], expected,
            )
            import cv2  # installed as an ai2thor dependency

            try:
                assert self._controller is not None
                self._controller.step(
                    action="ChangeResolution",
                    x=self._cfg.width,
                    y=self._cfg.height,
                )
            except Exception as exc:  # keep serving valid obs even if this fails
                logger.warning("[%s] ChangeResolution failed: %s", self.name, exc)
            frame = np.ascontiguousarray(
                cv2.resize(
                    frame,
                    (self._cfg.width, self._cfg.height),
                    interpolation=cv2.INTER_AREA,
                ),
                dtype=np.uint8,
            )
        return frame

    # ------------------------------------------------------------------
    # Target bookkeeping
    # ------------------------------------------------------------------
    def _target_state(self, metadata: Dict[str, Any]) -> Tuple[float, bool]:
        """Return (distance to closest target instance, success predicate).

        Success requires proximity and — if configured — that a sufficiently
        close instance is visible on screen.
        """
        agent_pos: Vec3 = metadata["agent"]["position"]
        min_dist = float("inf")
        success = False
        for obj in metadata["objects"]:
            if obj["objectType"] != self._cfg.target_object_type:
                continue
            d = _xz_distance(agent_pos, obj["position"])
            min_dist = min(min_dist, d)
            if d <= self._cfg.success_distance:
                if obj["visible"] or not self._cfg.require_visibility:
                    success = True
        if math.isinf(min_dist):
            raise RuntimeError(
                f"[{self.name}] no instance of target type "
                f"'{self._cfg.target_object_type}' exists in this house."
            )
        return min_dist, success

    def _shortest_path_length(self, start: Vec3) -> float:
        """Geodesic start->target length for SPL (straight-line fallback)."""
        assert self._controller is not None
        try:
            from ai2thor.util.metrics import (  # deferred: optional dependency path
                get_shortest_path_to_object_type,
                path_distance,
            )

            path = get_shortest_path_to_object_type(
                self._controller, self._cfg.target_object_type, initial_position=start
            )
            return float(path_distance(path))
        except Exception as exc:  # pathfinding can fail on procedural navmeshes
            logger.debug("[%s] shortest-path fallback (%s)", self.name, exc)
            metadata = self._controller.last_event.metadata
            dists = [
                _xz_distance(start, o["position"])
                for o in metadata["objects"]
                if o["objectType"] == self._cfg.target_object_type
            ]
            return float(min(dists)) if dists else 0.0

    # ------------------------------------------------------------------
    # gymnasium API
    # ------------------------------------------------------------------
    def reset(
        self, *, seed: Optional[int] = None, options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self._ensure_controller()
        assert self._controller is not None and self._reachable is not None

        # Sample a start pose from the (deterministically ordered) reachable
        # set. With an explicit seed this is fully reproducible AND paired
        # across visual variants (identical geometry => identical set).
        n_rot = max(1, int(round(360.0 / self._cfg.rotate_step_degrees)))
        event = None
        for _ in range(10):  # rare: a sampled cell can be transiently blocked
            idx = int(self.np_random.integers(len(self._reachable)))
            yaw = float(self.np_random.integers(n_rot)) * self._cfg.rotate_step_degrees
            event = self._controller.step(
                action="Teleport",
                position=self._reachable[idx],
                rotation={"x": 0.0, "y": yaw, "z": 0.0},
                horizon=0.0,
                standing=True,
            )
            if event.metadata["lastActionSuccess"]:
                break
        assert event is not None
        if not event.metadata["lastActionSuccess"]:
            raise RuntimeError(f"[{self.name}] could not teleport to any start pose.")

        metadata = event.metadata
        start_pos: Vec3 = metadata["agent"]["position"]
        self._steps = 0
        self._path_length = 0.0
        self._last_pos = start_pos
        self._prev_dist, _ = self._target_state(metadata)
        self._shortest_path = self._shortest_path_length(start_pos)
        self._last_frame = self._frame_to_obs(event)

        info: Dict[str, Any] = {
            "start_position": start_pos,
            "shortest_path_length": self._shortest_path,
            "distance_to_target": self._prev_dist,
        }
        return self._last_frame, info

    def step(
        self, action: int
    ) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        assert self._controller is not None, "call reset() before step()"
        name = self._cfg.actions[int(action)]
        kwargs: Dict[str, Any] = {}
        if name == "MoveAhead":
            kwargs["moveMagnitude"] = self._cfg.grid_size
        elif name in ("RotateLeft", "RotateRight"):
            kwargs["degrees"] = self._cfg.rotate_step_degrees
        elif name in ("LookUp", "LookDown"):
            kwargs["degrees"] = self._cfg.look_step_degrees

        event = self._controller.step(action=name, **kwargs)
        metadata = event.metadata
        # Failed actions (collisions, look limits) are legal no-ops in THOR.

        pos: Vec3 = metadata["agent"]["position"]
        self._path_length += _xz_distance(self._last_pos, pos)
        self._last_pos = pos

        dist, success = self._target_state(metadata)
        # Dense shaping: reward progress toward the target, small time penalty.
        reward = self._cfg.step_penalty + self._cfg.distance_reward_scale * (
            self._prev_dist - dist
        )
        self._prev_dist = dist
        if success:
            reward += self._cfg.success_reward

        self._steps += 1
        terminated = bool(success)
        truncated = (not terminated) and self._steps >= self._cfg.max_steps
        self._last_frame = self._frame_to_obs(event)

        info: Dict[str, Any] = {"distance_to_target": dist, "episode_step": self._steps}
        if terminated or truncated:
            # Episode metrics consumed by Monitor/eval (must exist at done).
            spl = 0.0
            if success:
                denom = max(self._shortest_path, self._path_length, 1e-6)
                spl = float(self._shortest_path) / denom if self._shortest_path > 0 else 1.0
            info.update(
                success=float(success),
                spl=float(np.clip(spl, 0.0, 1.0)),
                path_length=self._path_length,
                shortest_path_length=self._shortest_path,
            )
        return self._last_frame, float(reward), terminated, truncated, info

    def render(self) -> Optional[np.ndarray]:
        return self._last_frame

    def close(self) -> None:
        if self._controller is not None:
            self._controller.stop()
            self._controller = None


def make_objectnav_env(
    house_path: Path, config: ObjectNavConfig, name: str
) -> ProcTHORObjectNavEnv:
    """Factory: build the env for one saved house variant."""
    return ProcTHORObjectNavEnv(house=load_house(house_path), config=config, name=name)
