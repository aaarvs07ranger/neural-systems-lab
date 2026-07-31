# Vendored TD-MPC2

- **Upstream:** <https://github.com/nicklashansen/tdmpc2> (MIT license)
- **Pinned commit:** `e9f59321933cbc8e11a002b842adc7d4ffae8ff1` (2026-07-13, "fix q ensemble weight init")
- **Vendored subset:** `tdmpc2.py` + `common/{__init__,buffer,init,layers,math,scale,seed,world_model}.py`.
  NOT vendored: `train.py`/`evaluate.py`/`common/parser.py` (hydra entrypoints — our adapter builds
  the config namespace directly), `common/logger.py` (wandb), `trainer/` (re-implemented in
  `../adapter.py` without the interleaved eval env / video / wandb), `envs/` (their benchmark
  suites; our env bridge is `../thor_env.py`).

## Why this commit needed patches

Upstream HEAD targets torch ≥ 2.5 + new tensordict APIs; this repo is pinned to torch 2.2.2
(the ai2thor/MPS-verified stack, see requirements.lock.txt). All patches below are
**mechanical compatibility/device changes — the algorithm (losses, planning, update math,
hyperparameter semantics) is untouched.**

## Patch list (exhaustive)

1. **Relative imports** (`tdmpc2.py`, `common/world_model.py`): `from common import ...` →
   `from .common import ...` / `from . import ...` so the vendor lives as a subpackage
   (same rule as the DreamerV3 vendor — never sys.path-hack).
2. **De-vectorized Q ensemble** (`common/layers.py: Ensemble`): upstream stacks member params
   with `tensordict.from_modules` and vmaps the forward; tensordict 0.3.x (the last line
   compatible with torch 2.2) lacks that API. Replaced with an `nn.ModuleList` loop whose
   outputs are stacked on dim 0 — identical math, identical shapes, ~num_q× slower Q forward.
   `detach_params=True` reproduces upstream's `_detach_Qs` (Q-values that backprop to inputs
   but not to Q params) via `torch.func.functional_call` on detached params.
3. **Target-Q machinery** (`common/world_model.py: init/soft_update_target_Q/to/Q`): upstream
   maintains `TensorDictParams` views; replaced with a frozen `deepcopy` of the ensemble +
   explicit per-parameter Polyak `lerp_`. `to()` no longer re-inits (would have clobbered
   targets mid-training with the new representation).
4. **Q-ensemble zero-init** (`common/world_model.py`): `self._Qs.params["2", "weight"]` →
   `[q[-1].weight for q in self._Qs]` (same tensors, de-vectorized addressing).
5. **`torch.nn.Buffer` → `register_buffer`** (`common/scale.py`, `tdmpc2.py: _prev_mean`):
   nn.Buffer is torch ≥ 2.5. Also drops the hardcoded `device='cuda:0'` there.
6. **Device plumbing:** `tdmpc2.py` and `common/buffer.py` hardcoded `cuda:0`; both now read
   `cfg.device` (cuda/mps/cpu). Buffer's CUDA-memory heuristic only runs on CUDA (CPU storage
   otherwise). Adam `capturable=True` (CUDA-graphs feature) only on CUDA.
7. **`torch.get_default_device()`** (torch ≥ 2.3) in `load()` → `map_location=self.device`;
   dropped the `api_model_conversion` call (converts *their* legacy checkpoints; ours are
   native to this API and would trip its asserts).
8. **`torch.compiler.cudagraph_mark_step_begin()`** guarded behind `cfg.compile` + hasattr.
9. **`pi()` info container**: `tensordict.TensorDict({...})` → plain `dict` (used only for
   key lookups; TensorDict import removed from world_model).

## Behavioral notes (documented, not patched)

- `ShiftAug` (random-shift image augmentation) sits inside the rgb encoder and is active at
  eval time too — upstream behavior, kept. Eval actions are therefore slightly stochastic
  even with `eval_mode=True`; the paired A/B protocol is unaffected (env seeds fix start
  poses), but episode-level A/B pairing is no longer bit-deterministic like PPO/Dreamer.
- Reward two-hot regression covers symlog(r) ∈ [-10, 10]; our max per-step reward (~10.2 on
  success) is clipped by ~0.1% after symlog — negligible.
- Episodes shorter than horizon+1 (=4) transitions cannot be sliced by the sampler
  (`strict_length=True`); the adapter skips adding them to the buffer (~trivial-spawn
  episodes only) and logs the count. They still count toward the env-step budget.
- **MPS is excluded for this baseline** (adapter forces CPU when MPS is the best
  device): on torch 2.2.2 the update graph intermittently emits inf/nan losses on
  MPS — an async-execution race, reproducible with seeds 0-3 on M4, *masked* by
  inserting per-op synchronization, and absent on CPU (bit-comparable losses) —
  i.e. a Metal runtime bug, not an algorithm/patch bug. Post-update
  `torch.mps.synchronize()` does NOT fix it. Revisit on newer torch on the M5 Max.
