#!/bin/bash
#SBATCH --job-name=nsl-jepa-cost
#SBATCH --account=rao
#SBATCH --partition=gpu-rtx6k
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --gpus=1
#SBATCH --mem=32G
#SBATCH --time=00:30:00
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%j.out
# Times a frozen pretrained encoder per environment step. Trains nothing, boots
# no simulator. Runs in the CLONED env (nsl-jepa): the pinned `nsl` env that
# produced every committed result is never touched.
set -euo pipefail

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl-jepa"

export PYTHONUNBUFFERED=1
# Encoders were downloaded on the login node; compute nodes may have no internet.
export HF_HOME="${GSCRATCH_ROOT}/models/hf"
export HF_HUB_OFFLINE=1
cd "${SLURM_SUBMIT_DIR}"

python scripts/jepa_cost_check.py --iters 100 "$@"
echo "[slurm] done"
