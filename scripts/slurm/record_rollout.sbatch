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
# usage: sbatch record_rollout.sbatch <baseline> <pair> <seeds> [run-dir]
#   sbatch scripts/slurm/record_rollout.sbatch ppo pair0 10006,10020
BASELINE="${1:-ppo}"
PAIR="${2:-pair0}"
SEEDS="${3:-10006,10020}"
# The grid writes each cell to grid/<baseline>/<pair>_seed<N>; seed 0 is the
# default source because a filmstrip only needs one trained agent, and PPO's
# predict(deterministic=True) makes it exactly reproducible.
SRC_DIR="${4:-grid/${BASELINE}/${PAIR}_seed0}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
cd "${SLURM_SUBMIT_DIR}"
# Checkpoints live on scrubbed (the grid's run root), not in the repo.
RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
export NSL_RESULTS_DIR="${RUN_ROOT}/${SRC_DIR}"
# The protocol the grid ran, so the recorded episodes ARE the ones the tables
# describe -- same held-out slice, same pinned start poses.
export NSL_POSE_HOLDOUT=1
export NSL_PAIR="${PAIR}"

if [ ! -d "${NSL_RESULTS_DIR}/checkpoints" ]; then
    echo "[slurm] no checkpoints under ${NSL_RESULTS_DIR} — pass the run dir as \$4"
    exit 1
fi

echo "[slurm] recording ${BASELINE} on ${PAIR} from ${NSL_RESULTS_DIR}, eval seeds ${SEEDS}"
python scripts/record_rollout.py --baseline "${BASELINE}" --pair "${PAIR}" \
    --seeds "${SEEDS}"

# Filmstrips are paper figures and belong in the repo; GIFs are large and stay
# on scrubbed (they are gitignored anyway).
DEST="${SLURM_SUBMIT_DIR}/results/plots"
mkdir -p "${DEST}"
cp -f "${NSL_RESULTS_DIR}/plots/"*rollout*.png "${DEST}/" 2>/dev/null || true
echo "[slurm] filmstrips copied to ${DEST}"
echo "[slurm] done — filmstrips in ${NSL_RESULTS_DIR}/plots, GIFs in ${NSL_RESULTS_DIR}/videos"
