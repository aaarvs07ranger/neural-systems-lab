#!/bin/bash
# Evaluate ALREADY-TRAINED agents in the single-change houses. No training.
#
#   sbatch scripts/slurm/factor_eval.sbatch ppo
#   sbatch scripts/slurm/factor_eval.sbatch dreamerv3 300000
#
# WHAT THIS ADDS. The severity ladder is cumulative -- L2 changes object
# appearances on top of L1's repaint, L3 adds clutter on top of both -- so it
# cannot say what each rung costs on its own. These houses run the rungs
# INDEPENDENTLY: F_objall is L2's change without the repaint, F_clut is L3's
# change alone, and L1 alone is the frozen b_L1 (it is the bottom rung). F_obj /
# F_tgt split L2's change by whether the target itself changed, and F_mat /
# F_light / F_sky split L1's. The agent only ever TRAINS in house A, so none of
# this needs retraining -- just more houses to evaluate the checkpoints in.
#
# L1 and L2 ARE RE-MEASURED IN THE SAME PASS, deliberately. The question the
# factors exist to answer is "do the parts add up to the whole", and world-model
# evaluation is stochastic enough that a factor measured today must not be
# compared against a whole measured last week. A and L1/L2 also re-measure
# numbers we already hold, which is a free reproducibility check.
#
# SEPARATE OUTPUT TREE (results/factor_<steps>/) so no committed result is ever
# overwritten -- the same rule eval_only.sbatch follows.
#
# CHECKPOINTS ARE SYMLINKED, never copied, and searched across every root that
# holds models: the purge-safe copy on rao first, then the JEPA/MAE run root,
# then the original grid tree on scrubbed.
#
#SBATCH --job-name=nsl-factor
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --array=0-24%8
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=08:00:00
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

# pair2's target has no footprint-safe alternative, so it has no "target only"
# house. A missing rung is skipped with a warning, not a crash.
LEVELS="${NSL_LEVELS:-F_objall,F_clut,F_obj,F_tgt,F_mat,F_light,F_sky,L1,L2}"

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"
if [[ "${BASELINE}" == "ppo_jepa" || "${BASELINE}" == "ppo_mae" ]]; then
    # Frozen encoders need `transformers`, which is not in the pinned env.
    source "${GSCRATCH_ROOT}/venvs/jepa/bin/activate"
    export HF_HOME="${GSCRATCH_ROOT}/models/hf"
    export HF_HUB_OFFLINE=1
fi

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_PAIR="${PAIR}"
export NSL_POSE_HOLDOUT=1          # identical protocol to the grid

GRID_TAG="grid$([ "${STEPS}" = "150000" ] && echo "" || echo "_${STEPS}")"
MODEL_ROOTS="${NSL_MODEL_ROOTS:-${GSCRATCH_ROOT}/nsl-models:${GSCRATCH_ROOT}/nsl-runs:/gscratch/scrubbed/${USER}/nsl-runs}"
SRC=""
IFS=':' read -ra ROOTS <<< "${MODEL_ROOTS}"
for root in "${ROOTS[@]}"; do
    cand="${root}/${GRID_TAG}/${BASELINE}/${CELL}"
    if [ -d "${cand}/checkpoints" ]; then SRC="${cand}"; break; fi
done
if [ -z "${SRC}" ]; then
    echo "[slurm] FAILED: no trained checkpoint for ${BASELINE} ${CELL} in ${MODEL_ROOTS}"
    exit 1        # loud: a silent skip would leave a hole nothing reports
fi
echo "[slurm] using checkpoint ${SRC}"

RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
# Overridable so a mechanics check can never land where a real result lives.
TAG="${NSL_FACTOR_TAG:-factor_${STEPS}}"
export NSL_RESULTS_DIR="${RUN_ROOT}/${TAG}/${BASELINE}/${CELL}"
mkdir -p "${NSL_RESULTS_DIR}"
ln -sfn "${SRC}/checkpoints" "${NSL_RESULTS_DIR}/checkpoints"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] factor eval ${BASELINE} ${CELL} at ${STEPS} steps, rungs ${LEVELS}"
python scripts/evaluate_transfer.py --baseline "${BASELINE}" --pair "${PAIR}" \
    --levels "${LEVELS}" ${NSL_EXTRA_ARGS:-}

DEST="${SLURM_SUBMIT_DIR}/results/${TAG}/${BASELINE}/${CELL}"
mkdir -p "${DEST}"
cp -f "${NSL_RESULTS_DIR}/tables/"* "${DEST}/" 2>/dev/null || true
echo "[slurm] tables copied to ${DEST}"
