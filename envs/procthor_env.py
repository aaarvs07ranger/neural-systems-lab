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
import random
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
    # T2 (sequential ObjectNav): visit these object types IN ORDER. Empty means
    # the single-goal task T1, i.e. just ``target_object_type`` -- so T1 is a
    # one-element special case of T2 and shares every line of code below.
    # ``max_steps`` is the budget PER LEG, so a 3-leg episode gets 600 steps and
    # the per-leg budget stays constant across tasks.
    target_sequence: Tuple[str, ...] = ()
    # Path to a precomputed oracle-distance table measured in house A (written
    # by envs/verify_pairs.py). When set, an episode started with an explicit
    # seed present in the table uses A's distances instead of measuring its own.
    #
    # Why: the walk to a target ends at the target's SURFACE. Swapping in a
    # different-shaped asset of the same type moves that surface, so the
    # measured distance shifts by up to ~1.3 m even though the floor and the
    # object's position are unchanged. Since SPL divides by this distance, the
    # two variants would otherwise be scored with different yardsticks. One
    # yardstick, taken from A, keeps A and B directly comparable; the residual
    # bias is identical for every baseline, so cross-baseline claims are
    # unaffected. Raw per-seed deltas are recorded in verification.json.
    oracle_path_table: Optional[str] = None
    # Protocol v2: hold a slice of the floor out of training so evaluation
    # starts from places the agent has never stood.
    #
    # "" keeps the original protocol (every reachable cell available to both).
    # "train" samples only from the training slice, "eval" only from the
    # held-out slice. The split is over POSITIONS, not (position, yaw) pairs, so
    # a held-out start is somewhere the agent never visited at all rather than
    # somewhere it visited facing a different way.
    #
    # The partition is drawn from a FIXED seed, never the training seed, so it
    # is identical across every baseline, every training seed, and every rung of
    # the ladder -- C1 guarantees A and B share a reachable set, and the sorted
    # order makes the draw reproducible on top of it.
    pose_split: str = ""
    eval_pose_fraction: float = 0.2
    pose_split_seed: int = 20260903


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

        # One canonical list of goals. T1 is len == 1.
        self._sequence: Tuple[str, ...] = tuple(
            config.target_sequence or (config.target_object_type,)
        )
        self._max_steps: int = config.max_steps * len(self._sequence)

        self.observation_space = spaces.Box(
            low=0, high=255, shape=(config.height, config.width, 3), dtype=np.uint8
        )
        self.action_space = spaces.Discrete(len(config.actions))

        # Unity controller is created lazily on first reset() so that merely
        # constructing the env (e.g. for space inspection) never boots Unity.
        self._controller: Optional[Any] = None
        self._reachable: Optional[List[Vec3]] = None
        self._pose_pool: Optional[List[Vec3]] = None

        # Per-episode state.
        self._steps: int = 0
        self._path_length: float = 0.0
        self._shortest_path: float = 0.0
        self._prev_dist: float = float("inf")
        self._last_pos: Vec3 = {"x": 0.0, "y": 0.0, "z": 0.0}
        self._last_frame: Optional[np.ndarray] = None
        # Sequential-task state (unused when len(self._sequence) == 1).
        self._leg: int = 0
        self._leg_steps: List[int] = []
        self._leg_paths: List[float] = []
        self._oracle_legs: List[float] = []
        self._oracle_table: Optional[Dict[str, Any]] = None
        self._oracle_source: str = "measured"

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
        self._pose_pool = self._split_poses(self._reachable)
        logger.info(
            "[%s] controller ready: %d reachable positions, target=%s",
            self.name, len(self._reachable), self._cfg.target_object_type,
        )
        if self._cfg.pose_split:
            logger.info(
                "[%s] protocol v2: sampling starts from the '%s' slice "
                "(%d of %d cells, split seed %d)",
                self.name, self._cfg.pose_split, len(self._pose_pool),
                len(self._reachable), self._cfg.pose_split_seed,
            )

    def _split_poses(self, reachable: List[Vec3]) -> List[Vec3]:
        """Partition the floor into train and held-out eval slices.

        Returns the slice this env may start episodes from. An empty
        ``pose_split`` returns everything, which is the original protocol.
        """
        split = self._cfg.pose_split
        if not split:
            return list(reachable)
        if split not in ("train", "eval"):
            raise ValueError(
                f"pose_split must be '', 'train' or 'eval'; got {split!r}"
            )
        # A dedicated RNG, seeded by a constant: the partition must not move
        # when the training seed changes, or seeds would not be comparable.
        order = list(range(len(reachable)))
        random.Random(self._cfg.pose_split_seed).shuffle(order)
        n_eval = max(1, int(round(len(reachable) * self._cfg.eval_pose_fraction)))
        if len(reachable) - n_eval < 1:
            raise ValueError(
                f"[{self.name}] eval_pose_fraction={self._cfg.eval_pose_fraction} "
                f"leaves no training poses in a {len(reachable)}-cell house."
            )
        chosen = order[:n_eval] if split == "eval" else order[n_eval:]
        return [reachable[i] for i in sorted(chosen)]

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
    def _target_state(
        self, metadata: Dict[str, Any], target_type: Optional[str] = None
    ) -> Tuple[float, bool]:
        """Return (distance to closest target instance, success predicate).

        Success requires proximity and — if configured — that a sufficiently
        close instance is visible on screen.
        """
        target_type = target_type or self._sequence[self._leg]
        agent_pos: Vec3 = metadata["agent"]["position"]
        min_dist = float("inf")
        success = False
        for obj in metadata["objects"]:
            if obj["objectType"] != target_type:
                continue
            d = _xz_distance(agent_pos, obj["position"])
            min_dist = min(min_dist, d)
            if d <= self._cfg.success_distance:
                if obj["visible"] or not self._cfg.require_visibility:
                    success = True
        if math.isinf(min_dist):
            raise RuntimeError(
                f"[{self.name}] no instance of target type "
                f"'{target_type}' exists in this house."
            )
        return min_dist, success

    def _shortest_path_length(
        self, start: Vec3, target_type: Optional[str] = None
    ) -> float:
        """Geodesic start->target length for SPL (straight-line fallback)."""
        target_type = target_type or self._sequence[0]
        assert self._controller is not None
        try:
            from ai2thor.util.metrics import (  # deferred: optional dependency path
                get_shortest_path_to_object_type,
                path_distance,
            )

            path = get_shortest_path_to_object_type(
                self._controller, target_type, initial_position=start
            )
            self._last_path_end = dict(path[-1]) if path else dict(start)
            return float(path_distance(path))
        except Exception as exc:  # pathfinding can fail on procedural navmeshes
            logger.debug("[%s] shortest-path fallback (%s)", self.name, exc)
            metadata = self._controller.last_event.metadata
            candidates = [o for o in metadata["objects"]
                          if o["objectType"] == target_type]
            if not candidates:
                self._last_path_end = dict(start)
                return 0.0
            nearest = min(candidates,
                          key=lambda o: _xz_distance(start, o["position"]))
            self._last_path_end = dict(nearest["position"])
            return float(_xz_distance(start, nearest["position"]))

    def _load_oracle_table(self) -> Dict[str, Any]:
        """Read the house-A distance table once, if one was configured."""
        if self._oracle_table is None:
            path = getattr(self._cfg, "oracle_path_table", None)
            if path and Path(path).exists():
                self._oracle_table = json.loads(Path(path).read_text()).get("seeds", {})
                logger.info("[%s] using oracle distances measured in house A (%s)",
                            self.name, path)
            else:
                self._oracle_table = {}
        return self._oracle_table

    def _oracle_for_seed(self, seed: Optional[int], start: Vec3) -> Optional[List[float]]:
        """A's distances for this episode, if available and the start matches."""
        if seed is None:
            return None
        entry = self._load_oracle_table().get(str(seed))
        if not entry:
            return None
        stored = entry.get("start_position", {})
        if any(abs(stored.get(k, 0.0) - start.get(k, 0.0)) > 1e-3 for k in ("x", "z")):
            logger.warning("[%s] seed %s start pose differs from the oracle table "
                           "- measuring instead", self.name, seed)
            return None
        return [float(x) for x in entry["legs"]]

    def _oracle_chain(self, start: Vec3) -> List[float]:
        """Per-leg geodesic lengths for the shortest route visiting the whole
        itinerary in order: start -> T1 -> T2 -> ...

        This is the SPL denominator. It depends only on the start pose and the
        itinerary, never on what the agent actually does, which is what keeps
        it a fair yardstick and keeps it identical between variant A and B
        (guaranteed by the C2 check in envs/verify_pairs.py).
        """
        legs: List[float] = []
        cursor = dict(start)
        for target_type in self._sequence:
            self._last_path_end = dict(cursor)
            legs.append(self._shortest_path_length(cursor, target_type))
            cursor = dict(getattr(self, "_last_path_end", cursor))
        return legs

    # ------------------------------------------------------------------
    # gymnasium API
    # ------------------------------------------------------------------
    def reset(
        self, *, seed: Optional[int] = None, options: Optional[Dict[str, Any]] = None
    ) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        self._ensure_controller()
        assert self._controller is not None and self._pose_pool is not None

        # Sample a start pose from the (deterministically ordered) reachable
        # set. With an explicit seed this is fully reproducible AND paired
        # across visual variants (identical geometry => identical set).
        n_rot = max(1, int(round(360.0 / self._cfg.rotate_step_degrees)))
        event = None
        for _ in range(10):  # rare: a sampled cell can be transiently blocked
            idx = int(self.np_random.integers(len(self._pose_pool)))
            yaw = float(self.np_random.integers(n_rot)) * self._cfg.rotate_step_degrees
            event = self._controller.step(
                action="Teleport",
                position=self._pose_pool[idx],
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
        self._leg = 0
        self._leg_steps = []
        self._leg_paths = []
        self._prev_dist, _ = self._target_state(metadata)
        cached = self._oracle_for_seed(seed, start_pos)
        if cached is not None:
            self._oracle_legs, self._oracle_source = cached, "house_a_table"
        else:
            self._oracle_legs, self._oracle_source = self._oracle_chain(start_pos), "measured"
        self._shortest_path = float(sum(self._oracle_legs))
        self._last_frame = self._frame_to_obs(event)

        info: Dict[str, Any] = {
            "start_position": start_pos,
            "shortest_path_length": self._shortest_path,
            "distance_to_target": self._prev_dist,
            "n_legs": len(self._sequence),
            "current_target": self._sequence[0],
            "oracle_source": self._oracle_source,
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

        dist, leg_done = self._target_state(metadata)
        # Dense shaping: reward progress toward the CURRENT target, small time
        # penalty. Identical to the single-goal case when there is one leg.
        reward = self._cfg.step_penalty + self._cfg.distance_reward_scale * (
            self._prev_dist - dist
        )
        self._prev_dist = dist
        self._steps += 1
        if leg_done:
            reward += self._cfg.success_reward
            self._leg_steps.append(self._steps - sum(self._leg_steps))
            self._leg_paths.append(self._path_length - sum(self._leg_paths))
            self._leg += 1
            if self._leg < len(self._sequence):
                # Re-anchor the shaping on the NEXT target before the next step
                # computes its delta. Without this the agent would eat one large
                # negative reward at the exact moment it succeeded.
                self._prev_dist, _ = self._target_state(metadata)

        success = self._leg >= len(self._sequence)
        terminated = bool(success)
        truncated = (not terminated) and self._steps >= self._max_steps
        self._last_frame = self._frame_to_obs(event)

        info: Dict[str, Any] = {
            "distance_to_target": dist,
            "episode_step": self._steps,
            "legs_completed": self._leg,
            "current_target": (self._sequence[self._leg]
                               if self._leg < len(self._sequence) else None),
        }
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
                # Partial credit: how far through the itinerary it got. Always
                # 0.0 or 1.0 for the single-goal task, so T1 tables are
                # unaffected.
                progress=float(self._leg) / float(len(self._sequence)),
                legs_completed=self._leg,
                n_legs=len(self._sequence),
                leg_steps=list(self._leg_steps),
                leg_path_lengths=[round(x, 4) for x in self._leg_paths],
                oracle_leg_lengths=[round(x, 4) for x in self._oracle_legs],
                oracle_source=self._oracle_source,
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
