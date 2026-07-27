# Hyak (klone) workflow

One-time setup, then everything runs as slurm jobs. Local M4 laptops stay on
dev + smoke duty; the cluster does the multi-hour training.

## One-time setup

```bash
ssh <netid>@klone.hyak.uw.edu
hyakalloc                      # note the Rao group's account + GPU partitions
mkdir -p /gscratch/rao/$USER   # group scratch — NEVER /gscratch/cse (UW-IT rule)
cd /gscratch/rao/$USER
git clone https://github.com/aaarvs07ranger/neural-systems-lab.git nsl
cd nsl
bash setup_hyak.sh             # conda env + CUDA torch + CloudRendering build
```

Then edit `#SBATCH --account=` / `--partition=` in the three `.sbatch` files to
match what `hyakalloc` reported, and validate the whole stack on a GPU node:

```bash
sbatch scripts/slurm/smoke.sbatch      # ~15-30 min; must PASS before full runs
```

## Launching experiments

```bash
# DreamerV3 at the upstream compute recipe (the run the M4 could not afford):
NSL_EXTRA_ARGS="--train-ratio 512" sbatch scripts/slurm/train_baseline.sbatch dreamerv3

# PPO full run:
sbatch scripts/slurm/train_baseline.sbatch ppo

# 5-seed parallel sweeps (isolated results_seed<N>/ trees, preemptible ckpt partition):
NSL_EXTRA_ARGS="--train-ratio 512" sbatch scripts/slurm/sweep_seeds.sbatch dreamerv3
sbatch scripts/slurm/sweep_seeds.sbatch ppo
```

Monitoring:

```bash
squeue -u $USER                 # queue state
tail -f slurm-nsl-train-*.out   # live training log
sacct -j <jobid> --format=JobID,State,Elapsed,MaxRSS   # after completion
scancel <jobid>                 # kill
```

## Auto-resume / preemption

Checkpointing is preemption-safe by design: `latest.pt` (Dreamer) and periodic
`.zip` checkpoints (PPO) are written throughout, and a requeued job re-runs the
same `python main.py ...` command, which resumes from what is on disk. The
`ckpt` partition trades preemption risk for much wider capacity — use it for
sweeps, and the group partition for single must-finish runs.

## Getting results back

Summary tables and plots under `results/tables` + `results/plots` are
git-tracked: commit and push them from klone, then pull on the laptop.
Per-seed sweep trees (`results_seed*/`) and checkpoints are gitignored — rsync
what you need (one authenticated ControlMaster connection covers this):

```bash
rsync -av klone:/gscratch/rao/$USER/nsl/results_seed*/tables/ ./results/sweeps/
```

## Known tuning headroom (not yet enabled)

`compile=True` and mixed precision in the vendored DreamerV3 config were
forced off for MPS (torch 2.2 has no inductor-MPS). On CUDA they should work
and give a further speedup — flip them only after a smoke run confirms
numerics, and note it in CLAUDE.md.
