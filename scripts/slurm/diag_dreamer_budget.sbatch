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
# This re-runs FIVE of those cells at DOUBLE the budget and changes nothing else.
# At ~14k steps/hour measured, 300k steps is ~20 h per cell; all five run
# concurrently, so ~20 h total. If 4 of 5 recover, a full parity re-run of all
# four baselines at 300k is justified (~3 days). If they do not, more compute is
# wasted and the grid is reported as it stands with the pre-committed robustness
# pass, disclosing DreamerV3 as the least reliable of the four in-domain.
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
#SBATCH --array=0-4
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gpus=1
#SBATCH --time=30:00:00
#SBATCH --requeue
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%A_%a.out

set -euo pipefail

# FIVE of the nine weak cells, one from each affected house plus the two
# extremes, so the sample spans the range rather than clustering in one house:
#
#   pair4 3  house-A 0.00  the worst case -- if anything recovers, this should
#   pair2 0  house-A 0.20  small house, so not explainable by house size
#   pair3 1  house-A 0.20  largest affected house
#   pair1 0  house-A 0.36  mid
#   pair2 3  house-A 0.48  just under the threshold -- the easiest to recover
#
# Five rather than nine because the run before this died on "Disk quota
# exceeded" with nine concurrent replay buffers, on a /gscratch that is 98% full
# group-wide and outside our control. Five halves the peak footprint at the same
# wall clock, since all five run concurrently.
CELLS=(
  "pair4 3"   # A 0.00
  "pair2 0"   # A 0.20
  "pair3 1"   # A 0.20
  "pair1 0"   # A 0.36
  "pair2 3"   # A 0.48
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

# The previous attempt died 4 h in with "Disk quota exceeded" while writing
# replay episodes: /gscratch is 98% full group-wide. Surface that up front
# rather than discovering it after a night of compute.
FREE_GB=$(df -BG --output=avail /gscratch/scrubbed 2>/dev/null | tail -1 | tr -dc "0-9")
echo "[slurm] /gscratch/scrubbed free: ${FREE_GB:-?} GiB (this cell needs ~12 GiB of replay)"
if [ -n "${FREE_GB}" ] && [ "${FREE_GB}" -lt 200 ]; then
    echo "[slurm] ABORT: under 200 GiB free; five concurrent replay buffers will not fit."
    exit 1
fi

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
