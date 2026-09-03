#!/bin/bash
# The Phase-1 grid: one array task per (house pair x training seed).
#
#   sbatch scripts/slurm/sweep_grid.sbatch ppo
#   sbatch --array=0-24%4 scripts/slurm/sweep_grid.sbatch dreamerv3   # tighter cap
#
# 25 tasks = 5 pairs x 5 seeds. Run this once per baseline and the grid is
# 4 x 25 = 100 training runs.
#
# NOT x severity level: the agent only ever TRAINS in house A, and the rung
# changes which house is EVALUATED. One trained model walks A -> L1 -> L2 -> L3
# inside its own eval, so levels cost eval episodes, not training runs. Arraying
# over levels too would triple the compute for identical results.
#
# Task id decodes as:   pair = id / n_seeds,   seed = id % n_seeds
# so tasks 0-4 are pair0 seeds 0-4, tasks 5-9 are pair1 seeds 0-4, and so on.
#
#SBATCH --job-name=nsl-grid
#SBATCH --account=rao
#SBATCH --partition=ckpt          # wide sweep: preemptible spare capacity + requeue
#SBATCH --array=0-24%10
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH --requeue
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%A_%a.out

set -euo pipefail
BASELINE="${1:-ppo}"
N_SEEDS="${NSL_N_SEEDS:-5}"
TASK="${SLURM_ARRAY_TASK_ID}"
PAIR_IDX=$(( TASK / N_SEEDS ))
SEED=$(( TASK % N_SEEDS ))
PAIR="pair${PAIR_IDX}"
CELL="${PAIR}_seed${SEED}"

GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_PAIR="${PAIR}"
# Protocol v2 for every cell of the grid. A protocol change applied to some
# baselines and not others would make the columns incomparable, which is exactly
# why the pose holdout waited for the grid instead of shipping with ppo_aug.
export NSL_POSE_HOLDOUT=1

# Bulky run output (checkpoints, replay buffers, logs) goes to scrubbed: the
# shared /gscratch/rao fileset hit 100% on 2026-08-23 group-wide, and a job died
# with "Disk quota exceeded" mid-save. Scrubbed has ~9T but auto-purges after
# ~21 days, which is why tables are copied into the repo below as each cell
# lands rather than in one sweep at the end.
RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
export NSL_RESULTS_DIR="${RUN_ROOT}/grid/${BASELINE}/${CELL}"
mkdir -p "${NSL_RESULTS_DIR}"

RAO_FREE_KB=$(df -Pk "/gscratch/rao/${USER}" | awk 'NR==2 {print $4}')
echo "[slurm] /gscratch/rao free: $((RAO_FREE_KB / 1024)) MiB"
if [ "${RAO_FREE_KB}" -lt 5242880 ]; then
    echo "[slurm] WARNING: <5 GiB free on /gscratch/rao — AI2-THOR writes into" \
         "~/.ai2thor (symlinked there) and can die mid-run."
fi

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] ${SLURM_ARRAY_JOB_ID}_${TASK} on $(hostname):" \
     "baseline=${BASELINE} pair=${PAIR} seed=${SEED} results=${NSL_RESULTS_DIR}"

# Train and eval are named explicitly rather than using --stage all, which also
# runs generation. Ten concurrent tasks regenerating the shared data/ tree would
# race each other and could rewrite the verified houses mid-grid. Generation is
# a one-off cluster-wide step (regen_and_verify.sbatch), never a per-run one.
# shellcheck disable=SC2086
python main.py --baseline "${BASELINE}" --pair "${PAIR}" --seed "${SEED}" \
    --stage train ${NSL_EXTRA_ARGS:-}
# shellcheck disable=SC2086
python main.py --baseline "${BASELINE}" --pair "${PAIR}" --seed "${SEED}" \
    --stage eval ${NSL_EXTRA_ARGS:-}

# --- land the results, then shrink the footprint --------------------------
# Tables and plots are kilobytes and are the actual deliverable, so they are
# copied into the repo immediately: scrubbed purges after ~21 days and a grid
# this size will straddle that window.
DEST="${SLURM_SUBMIT_DIR}/results/grid/${BASELINE}/${CELL}"
mkdir -p "${DEST}"
cp -f "${NSL_RESULTS_DIR}/tables/"* "${DEST}/" 2>/dev/null || true
cp -f "${NSL_RESULTS_DIR}/plots/"*  "${DEST}/" 2>/dev/null || true
echo "[slurm] tables copied to ${DEST}"

# Vishwas's disk mandate (2026-09-01): keep a minimal steady-state footprint
# rather than asking for a big allocation. Replay buffers dominate -- roughly
# 6 GB per world-model run -- and are worthless once the tables are written,
# since a rerun regenerates them from the seed. The final model is KEPT: rollout
# figures need it, and re-training to recover one costs hours.
if [ -d "${DEST}" ] && [ -n "$(ls -A "${DEST}" 2>/dev/null)" ]; then
    rm -rf "${NSL_RESULTS_DIR}/logs/tdmpc2" "${NSL_RESULTS_DIR}/logs/dreamerv3"
    find "${NSL_RESULTS_DIR}/checkpoints" -name '*_steps.zip' -delete 2>/dev/null || true
    find "${NSL_RESULTS_DIR}/checkpoints" -name 'latest.pt' -delete 2>/dev/null || true
    echo "[slurm] cleaned replay buffers and intermediate checkpoints for ${CELL}"
else
    echo "[slurm] WARNING: no tables landed in ${DEST} — keeping everything" \
         "so the run can be diagnosed."
fi

echo "[slurm] cell ${BASELINE}/${CELL} DONE"
