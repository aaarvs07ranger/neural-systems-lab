#!/bin/bash
# Runtime C1-C3 verification of every house pair (boots Unity, needs a GPU).
# This is the gate: do not launch a grid until it passes.
#
#   sbatch scripts/slurm/verify_pairs.sbatch
#   sbatch scripts/slurm/verify_pairs.sbatch pair0 L1,L2,L3
#
#SBATCH --job-name=nsl-verify
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=02:00:00
# NOTE: deliberately NOT --exclusive. The shared-node CloudRendering
# failures we hit came from several of OUR OWN tasks landing on one node;
# this is a single job, and --exclusive only made it queue behind a whole
# free node for no benefit.
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%j.out

set -euo pipefail
PAIR="${1:-}"
LEVELS="${2:-}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
cd "${SLURM_SUBMIT_DIR}"

ARGS=()
[ -n "${PAIR}" ]   && ARGS+=(--pair "${PAIR}")
[ -n "${LEVELS}" ] && ARGS+=(--levels "${LEVELS}")

echo "[slurm] verifying pairs ${PAIR:-<all>} levels ${LEVELS:-<all>}"
python envs/verify_pairs.py "${ARGS[@]}"
echo "[slurm] verification complete"
