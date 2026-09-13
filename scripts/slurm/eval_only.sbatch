#!/bin/bash
# Re-evaluate ALREADY-TRAINED agents on the full rung set, including the new
# L2noT control. No training happens here.
#
#   sbatch scripts/slurm/eval_only.sbatch ppo 300000
#
# WHY A SEPARATE OUTPUT TREE. Evaluation always walks every rung in
# config.EVAL_LEVELS, so this produces fresh A/L1/L2/L3 numbers as well as the
# new L2noT one. Writing those back over the committed grid would overwrite
# prior results, which the project's rigor rules forbid. So results land in
#   $RUN_ROOT/evalonly_<steps>/<baseline>/<cell>/
# and the re-measured A/L1/L2/L3 become a FREE REPRODUCIBILITY CHECK instead: the
# same checkpoint on the same pinned start poses should reproduce the committed
# numbers exactly for PPO (deterministic) and closely for the others. If it does
# not, something is wrong and we want to hear about it.
#
# The checkpoint directory is SYMLINKED, not copied -- the models are 56-210 MB
# each and the grid tree is the only copy that should exist.
#
#SBATCH --job-name=nsl-evalonly
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --array=0-24%8
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=04:00:00
#SBATCH --requeue
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%A_%a.out

set -euo pipefail
BASELINE="${1:-ppo}"
STEPS="${2:-300000}"
N_SEEDS="${NSL_N_SEEDS:-5}"
TASK="${SLURM_ARRAY_TASK_ID}"
PAIR="pair$(( TASK / N_SEEDS ))"
SEED=$(( TASK % N_SEEDS ))
CELL="${PAIR}_seed${SEED}"

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_PAIR="${PAIR}"
export NSL_POSE_HOLDOUT=1          # identical protocol to the grid

RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
GRID_TAG="grid$([ "${STEPS}" = "150000" ] && echo "" || echo "_${STEPS}")"
SRC="${RUN_ROOT}/${GRID_TAG}/${BASELINE}/${CELL}"
export NSL_RESULTS_DIR="${RUN_ROOT}/evalonly_${STEPS}/${BASELINE}/${CELL}"

if [ ! -d "${SRC}/checkpoints" ]; then
    echo "[slurm] no trained checkpoint at ${SRC} — nothing to evaluate. Skipping."
    exit 0
fi
mkdir -p "${NSL_RESULTS_DIR}"
# Symlink rather than copy: the trained model has exactly one home.
ln -sfn "${SRC}/checkpoints" "${NSL_RESULTS_DIR}/checkpoints"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] eval-only ${BASELINE} ${CELL} at ${STEPS} steps, rungs from EVAL_LEVELS"
python main.py --baseline "${BASELINE}" --pair "${PAIR}" --seed "${SEED}" \
    --stage eval --total-steps "${STEPS}" ${NSL_EXTRA_ARGS:-}

DEST="${SLURM_SUBMIT_DIR}/results/evalonly_${STEPS}/${BASELINE}/${CELL}"
mkdir -p "${DEST}"
cp -f "${NSL_RESULTS_DIR}/tables/"* "${DEST}/" 2>/dev/null || true
echo "[slurm] tables copied to ${DEST}"
