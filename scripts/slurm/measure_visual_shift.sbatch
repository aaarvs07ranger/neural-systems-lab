#!/bin/bash
# Measure how visually different each shifted house is from house A.
#
#   sbatch scripts/slurm/measure_visual_shift.sbatch
#
# No training, no policy, no episodes -- it teleports to the 25 pinned
# evaluation start poses and captures the agent's observation in each house.
# Minutes, one GPU, one Unity process at a time.
#
# MUST run here rather than locally: the renderer determines the pixels, and
# these numbers are meant to be compared against transfer results that were
# measured under CloudRendering.
#
#SBATCH --job-name=nsl-vshift
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%j.out

set -euo pipefail
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_POSE_HOLDOUT=1          # the same held-out slice the numbers came from
# Write into the repo: the output is one small JSON that the paper cites.
export NSL_RESULTS_DIR="${SLURM_SUBMIT_DIR}/results"

cd "${SLURM_SUBMIT_DIR}"
python scripts/measure_visual_shift.py
echo "[slurm] wrote results/tables/visual_shift.json"
