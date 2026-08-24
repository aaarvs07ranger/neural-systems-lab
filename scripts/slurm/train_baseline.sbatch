#!/bin/bash
# Full single-seed training + zero-shot transfer eval for one baseline.
#
#   sbatch scripts/slurm/train_baseline.sbatch dreamerv3
#   sbatch scripts/slurm/train_baseline.sbatch ppo
#   NSL_EXTRA_ARGS="--train-ratio 512" sbatch scripts/slurm/train_baseline.sbatch dreamerv3
#
# Auto-resume: checkpointing is preemption-safe. If the job dies or is
# preempted (`ckpt` partition), --requeue relaunches it and training resumes
# from results/checkpoints/<baseline>/latest.pt + the on-disk replay buffer.
#
#SBATCH --job-name=nsl-train
#SBATCH --account=rao            # verified via `hyakalloc` 2026-07-30
#SBATCH --partition=gpu-rtx6k    # Rao group allocation: 4x RTX 6000; `ckpt` = preemptible spare capacity
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8        # the Unity sim is CPU-bound; don't starve it
#SBATCH --mem=64G
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH --requeue
#SBATCH --output=slurm-%x-%j.out

set -euo pipefail
BASELINE="${1:-dreamerv3}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering   # headless Vulkan (auto-detected anyway)

# Run outputs (checkpoints, replay buffers, logs, tables, plots) go to a RUN
# ROOT that defaults to /gscratch/scrubbed/$USER/nsl-runs. Reason: on
# 2026-08-23 the shared /gscratch/rao fileset hit 100% (4.0T, ~6G free) —
# group-wide, not our data — and a job died with "Disk quota exceeded" while
# saving its model. /gscratch/scrubbed has ~9T free. NOTE: scrubbed files are
# auto-deleted after ~21 days, so rsync tables back into the repo promptly.
# Override with `NSL_RUN_ROOT=$PWD sbatch ...` to write next to the repo.
RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
mkdir -p "${RUN_ROOT}"
export NSL_RESULTS_DIR="${RUN_ROOT}/results_main_${BASELINE}"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] job ${SLURM_JOB_ID} on $(hostname): baseline=${BASELINE} extra='${NSL_EXTRA_ARGS:-}'"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader || true

# shellcheck disable=SC2086
python main.py --baseline "${BASELINE}" ${NSL_EXTRA_ARGS:-}
