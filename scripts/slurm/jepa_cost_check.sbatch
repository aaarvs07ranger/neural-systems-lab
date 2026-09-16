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
# NOTE (2026-09-16): /gscratch/scrubbed refuses our writes -- a shared quota is
# exhausted group-wide (we hold 17 G of it, and df still shows 7 T free), so a
# job writing its log there dies before it starts. Logs go to the rao fileset,
# which accepts writes. Revert when scrubbed is usable again.
#SBATCH --output=/gscratch/rao/%u/nsl-logs/slurm-%x-%j.out
# Times a frozen pretrained encoder per environment step. Trains nothing, boots
# no simulator.
#
# Environment: the pinned `nsl` conda env plus a venv layered on top of it
# (`venvs/jepa`, created with --system-site-packages) that adds `transformers`
# and nothing else. The pinned env, which produced every committed result, is
# read-only here: a package added for this experiment cannot change it.
set -euo pipefail

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"
source "${GSCRATCH_ROOT}/venvs/jepa/bin/activate"

export PYTHONUNBUFFERED=1
# Encoders were downloaded on the login node; compute nodes may have no internet.
export HF_HOME="${GSCRATCH_ROOT}/models/hf"
export HF_HUB_OFFLINE=1
cd "${SLURM_SUBMIT_DIR}"

python scripts/jepa_cost_check.py --iters 100 "$@"
echo "[slurm] done"
