#!/bin/bash
# DIAGNOSTIC ONLY -- these runs never enter the paper.
#
# 9 of DreamerV3's 25 grid cells finished with house-A success below 0.5, while
# PPO reached ~0.9 and TD-MPC2 ~1.0 on the same houses. None show the July
# collapse signature (value_std and actor_grad_norm are healthy in all nine), so
# the question is whether 150k env steps is simply too few for DreamerV3 in the
# larger houses, or whether this is seed instability that more steps will not
# cure.
#
# This re-runs exactly those 9 cells at DOUBLE the budget and changes nothing
# else. If most recover, a full parity re-run of all four baselines at 300k is
# justified (~3 days). If they do not, more compute is wasted and the grid is
# reported as it stands with the pre-committed robustness pass.
#
# Results land in a SEPARATE tree so they can never be mistaken for grid cells:
#   $RUN_ROOT/diag300k/dreamerv3/<pair>_seed<N>
# A 300k DreamerV3 is not comparable to a 150k PPO -- that is the whole point of
# budget parity -- so these numbers answer one question and are then discarded.
#
#   sbatch scripts/slurm/diag_dreamer_budget.sbatch
#
#SBATCH --job-name=nsl-diag300k
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --array=0-8
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH --requeue
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%A_%a.out

set -euo pipefail

# The nine cells with house-A success < 0.5, as "<pair> <seed>".
CELLS=(
  "pair1 0"   # A 0.36
  "pair1 1"   # A 0.36
  "pair2 0"   # A 0.20
  "pair2 3"   # A 0.48
  "pair3 0"   # A 0.44
  "pair3 1"   # A 0.20
  "pair3 2"   # A 0.36
  "pair4 2"   # A 0.32
  "pair4 3"   # A 0.00
)
read -r PAIR SEED <<< "${CELLS[$SLURM_ARRAY_TASK_ID]}"
STEPS=300000

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_PAIR="${PAIR}"
export NSL_POSE_HOLDOUT=1          # identical protocol to the grid

RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
export NSL_RESULTS_DIR="${RUN_ROOT}/diag300k/dreamerv3/${PAIR}_seed${SEED}"
mkdir -p "${NSL_RESULTS_DIR}"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] DIAGNOSTIC ${PAIR} seed ${SEED} at ${STEPS} steps (grid used 150000)"

python main.py --baseline dreamerv3 --pair "${PAIR}" --seed "${SEED}" \
    --stage train --train-ratio 512 --total-steps "${STEPS}"
python main.py --baseline dreamerv3 --pair "${PAIR}" --seed "${SEED}" \
    --stage eval --train-ratio 512 --total-steps "${STEPS}"

A=$(awk -F, '$1=="A"{print $3}' "${NSL_RESULTS_DIR}/tables/dreamerv3_transfer_summary.csv" 2>/dev/null)
echo "[slurm] ${PAIR}_seed${SEED}: house-A success at 300k = ${A:-?}  (was <0.5 at 150k)"

# Diagnostic runs keep nothing but their tables.
rm -rf "${NSL_RESULTS_DIR}/logs/dreamerv3" 2>/dev/null || true
find "${NSL_RESULTS_DIR}/checkpoints" -name 'latest.pt' -delete 2>/dev/null || true
