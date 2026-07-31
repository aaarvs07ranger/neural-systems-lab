#!/bin/bash
# GPU-node validation of the whole pipeline: CloudRendering boot, CUDA torch,
# tiny train + paired A/B eval for all implemented baselines (~15-30 min).
# Run this once after setup_hyak.sh, before any full submission.
#
#   sbatch scripts/slurm/smoke.sbatch
#
# Writes to a throwaway results_smoke_<jobid>/ dir — real results are never
# touched. Delete the dir after inspecting the output.
#
#SBATCH --job-name=nsl-smoke
#SBATCH --account=rao            # verified via `hyakalloc` 2026-07-30
#SBATCH --partition=gpu-rtx6k    # Rao group allocation: 4x RTX 6000, 20 CPUs, 188G
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH --output=slurm-%x-%j.out

set -euo pipefail
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_RESULTS_DIR="${SLURM_SUBMIT_DIR}/results_smoke_${SLURM_JOB_ID}"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] smoke on $(hostname); vulkan: $(ldconfig -p | grep -c libvulkan || true) libs"
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader || true
python -c "import torch; assert torch.cuda.is_available(), 'no CUDA'; print('CUDA OK:', torch.cuda.get_device_name(0))"

python main.py --smoke --baseline ppo
python main.py --smoke --baseline dreamerv3
python main.py --smoke --baseline tdmpc2
echo "[slurm] smoke PASSED for ppo + dreamerv3 + tdmpc2 (results in ${NSL_RESULTS_DIR})"
