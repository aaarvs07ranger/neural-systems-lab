#!/bin/bash
# Record paired A/B rollout visuals ON THE CLUSTER, under the same renderer the
# policy trained with (CloudRendering/Vulkan). This matters: replaying a
# klone-trained checkpoint on macOS (windowed build) does NOT reproduce its
# numbers -- PPO seed0 scored A 0.00 locally vs A 0.92 on klone -- so any
# rollout figure recorded locally is qualitatively suggestive but numerically
# wrong. Always record where the model was trained.
#
#   sbatch scripts/slurm/record_rollout.sbatch ppo results_seed0 10006,10020
#
# Args: <baseline> <source results dir, relative to submit dir> <eval seeds>
# Writes GIFs + filmstrips into <source results dir>/{videos,plots}/.
#
#SBATCH --job-name=nsl-rollout
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
BASELINE="${1:-ppo}"
SRC_DIR="${2:-results_seed0}"
SEEDS="${3:-10006,10020}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
cd "${SLURM_SUBMIT_DIR}"
export NSL_RESULTS_DIR="${SLURM_SUBMIT_DIR}/${SRC_DIR}"

echo "[slurm] recording ${BASELINE} rollouts from ${NSL_RESULTS_DIR}, eval seeds ${SEEDS}"
python scripts/record_rollout.py --baseline "${BASELINE}" --seeds "${SEEDS}"
echo "[slurm] done — filmstrips in ${NSL_RESULTS_DIR}/plots, GIFs in ${NSL_RESULTS_DIR}/videos"
