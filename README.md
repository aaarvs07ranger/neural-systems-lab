# NSL Zero-Shot Visual Transfer Baselines (ProcTHOR)

Empirical baseline pipeline for quantifying the **visual-binding problem**:
how much do standard RL / world-model agents (PPO, DreamerV3, TD-MPC2) degrade
when transferred zero-shot between two ProcTHOR houses that are **structurally
identical** (same floorplan, object layout, task graph) but **visually
disparate** (different wall/floor/ceiling materials, lighting color and
intensity, skybox)?

Neural Systems Lab, UW — baseline track for the masking + CSCG architecture project.

## Requirements

- Apple Silicon Mac (developed on M4, 32 GB) with **Rosetta 2**
  (AI2-THOR's macOS Unity build is x86_64: `softwareupdate --install-rosetta --agree-to-license`)
- ~5 GB free disk (conda env + ProcTHOR-10k dataset + Unity build)
- Network access on first run (PyPI, `ai2thor-pypi.allenai.org`, dataset download)

## One-command setup (M4 / Apple Silicon)

```bash
bash setup.sh
```

This installs Miniforge if needed, creates the conda env **`nsl`
(Python 3.9)**, installs the pinned arm64 stack (`torch 2.2.2` with MPS,
`stable-baselines3 2.3.2`, `gymnasium 0.29.1`, `prior`), installs **AI2-THOR
from AllenAI's private index at the ProcTHOR-pinned commit**
(`0+391b3fae...`), verifies MPS is active, and writes `requirements.lock.txt`.

Python 3.9 is deliberate: it is the version the ProcTHOR-era tooling
(`procthor`, `prior`, the pinned AI2-THOR build) was built and tested against,
and every pinned package above ships py3.9 arm64 wheels.

## Run the experiment

```bash
conda activate nsl

# fast end-to-end mechanics check (~minutes; tiny step counts)
python main.py --smoke

# full PPO transfer experiment (env generation -> train on A -> zero-shot eval on B)
python main.py

# PPO + train-time photometric augmentation (the "why not just augment?" baseline;
# identical recipe/budget to ppo — only the training observations are jittered)
python main.py --baseline ppo_aug

# full DreamerV3 transfer experiment (same protocol, vendored NM512 world model)
python main.py --baseline dreamerv3
tensorboard --logdir results/logs/dreamerv3   # live training curves

# individual stages
python main.py --stage generate          # build the two visual variants only
python main.py --stage train             # train the selected baseline on variant A
python main.py --stage eval              # frozen-policy eval on A and B
python main.py --total-steps 300000      # override the training budget
```

First `train`/`eval` run downloads the AI2-THOR Unity build (~0.5 GB) and
opens a small Unity window — this is normal on macOS (no headless mode).

## Experimental protocol

1. **`envs/generate_variants.py`** picks a small (≤2-room) ProcTHOR-10k house
   containing a preferred ObjectNav target (Television/Fridge/Bed/...).
   Variant **A** is the house verbatim; variant **B** rewrites *only*
   appearance fields — wall/floor/ceiling materials (remapped to materials
   harvested from other ProcTHOR houses, so all names are valid), warm-tinted
   dimmed lighting, swapped skybox. A structural-identity assertion verifies
   geometry/objects/doors/windows are byte-identical.
2. **Task**: ObjectNav to a fixed target type. RGB-only 128×128 egocentric
   observations, discrete actions (MoveAhead 0.25 m, Rotate±30°, Look±30°).
   Success = within 1.5 m of a visible target instance. Dense progress
   shaping + step penalty during training; success/SPL/episode-length logged.
3. **Training**: on variant A only (`device=mps`), identical 150k-env-step
   budget per baseline — PPO (SB3 CnnPolicy, 128×128 obs) and DreamerV3
   (vendored NM512 PyTorch implementation, native 64×64 obs).
4. **Zero-shot transfer**: the frozen policy is evaluated on A and B with the
   *same episode seeds* — identical geometry means paired start poses — so the
   metric gap isolates appearance. **No weight updates, no fine-tuning.**
5. **Outputs**: per-episode CSVs, aggregate summary (CSV + Markdown), and a
   bar chart of the A→B drop in `results/`.

## Project layout

```
config.py                     # single source of truth: paths + hyperparameters
setup.sh                      # one-command environment setup (M4/MPS)
main.py                       # pipeline: generate -> train -> transfer eval
envs/
  procthor_env.py             # gymnasium ObjectNav env over a fixed ProcTHOR house
  generate_variants.py        # paired visual variants A/B + structural identity check
  augmentation.py             # photometric jitter wrapper (ppo_aug, TRAIN PATH ONLY)
models/
  common.py                   # BaselineAdapter protocol shared by all baselines
  dreamer_v3/                 # DreamerV3: vendored NM512 impl + adapter + THOR bridge
  td_mpc2/                    # TD-MPC2: vendored nicklashansen impl + adapter
scripts/
  train_ppo.py                # PPO / ppo_aug training on variant A
  evaluate_transfer.py        # frozen-policy A vs B eval, tables + plot
  tracker.py                  # experiment tracker: backfill/ingest-sweep/add/render
  plot_baselines.py           # headline figure across all baselines (per-seed dots)
  record_rollout.py           # paired A/B rollout GIF + filmstrip from a checkpoint
  visualize_variants.py       # A vs B screenshots from identical poses
  visualize_augmentation.py   # what ppo_aug sees: jitter draws vs the real A->B shift
  slurm/                      # Hyak (klone) job templates + workflow README
tests/                        # contract tests (run directly; the pinned env has no pytest)
data/                         # house_a/house_b JSON, task config, variant diff summary
results/                      # checkpoints/, logs/, tables/, plots/, sweeps/, tracker/
```

## Evaluation platform rule (important)

**A trained policy may only be evaluated under the renderer it trained with.**
Cluster runs use headless CloudRendering (Vulkan); macOS uses the windowed
build. Replaying a klone-trained PPO checkpoint locally scored 0.00 success on
variant A where the same checkpoint scores 0.92 on the cluster — the graphics
backend alone is a large enough appearance shift to break an appearance-bound
policy. Record rollout figures on the cluster
(`sbatch scripts/slurm/record_rollout.sbatch ppo results_seed0 10006,10020`);
use the laptop for smoke tests and code, never for reported numbers.

## MPS / performance notes

- `PYTORCH_ENABLE_MPS_FALLBACK=1` is set automatically (a few SB3 ops lack
  Metal kernels; they fall back to CPU transparently).
- The simulator (Unity, CPU-bound, under Rosetta) is the throughput
  bottleneck, not the policy net — expect ~10–30 env steps/s at 128×128.
- Keep the laptop plugged in for full training runs; ~150k steps ≈ several hours.

## Troubleshooting

- **`ai2thor` install fails**: check `https://ai2thor-pypi.allenai.org` is
  reachable; as a fallback `pip install ai2thor==5.0.0` (public PyPI) also
  supports ProcTHOR house specs.
- **Unity window never appears / times out**: first run downloads ~0.5 GB to
  `~/.ai2thor`; re-run once it completes. Grant the app screen permissions if
  macOS prompts.
- **`prior` dataset download fails**: requires git + network; re-run
  `python main.py --stage generate`.
