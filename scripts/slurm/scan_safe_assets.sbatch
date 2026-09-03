#!/bin/bash
# Build the L2 footprint-safe asset whitelist for every pair (boots Unity).
# Run once after generating pairs, BEFORE regenerating L2/L3.
#
#   sbatch scripts/slurm/scan_safe_assets.sbatch
#
#SBATCH --job-name=nsl-scan
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=04:00:00
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%j.out

set -euo pipefail
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
cd "${SLURM_SUBMIT_DIR}"

echo "[slurm] scanning footprint-safe assets for every pair"
python envs/scan_safe_assets.py "$@"
echo "[slurm] scan complete; regenerate L2/L3 next"
