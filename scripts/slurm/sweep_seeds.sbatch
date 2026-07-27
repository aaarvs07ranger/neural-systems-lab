#!/bin/bash
# Seed sweep: one array task per training seed, run in parallel.
#
#   sbatch scripts/slurm/sweep_seeds.sbatch dreamerv3
#   sbatch --array=0-9 scripts/slurm/sweep_seeds.sbatch ppo   # more seeds
#
# Each task trains with seed = SLURM_ARRAY_TASK_ID and writes its ENTIRE
# results tree (checkpoints, replay, logs, tables, plots) to an isolated
# results_seed<N>/ dir via NSL_RESULTS_DIR, so parallel tasks never collide.
# data/ (houses, task config) is shared read-only. Eval episode seeds stay at
# eval_seed_base (10000+) in every task — the paired A/B protocol is fixed.
#
#SBATCH --job-name=nsl-sweep
#SBATCH --account=rao            # verify with `hyakalloc`
#SBATCH --partition=ckpt         # sweeps are wide: preemptible spare capacity + requeue
#SBATCH --array=0-4
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gpus=1
#SBATCH --time=24:00:00
#SBATCH --requeue
#SBATCH --output=slurm-%x-%A_%a.out

set -euo pipefail
BASELINE="${1:-dreamerv3}"
SEED="${SLURM_ARRAY_TASK_ID}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_RESULTS_DIR="${SLURM_SUBMIT_DIR}/results_seed${SEED}"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] array task ${SLURM_ARRAY_JOB_ID}_${SEED} on $(hostname):" \
     "baseline=${BASELINE} seed=${SEED} results=${NSL_RESULTS_DIR}"

# shellcheck disable=SC2086
python main.py --baseline "${BASELINE}" --seed "${SEED}" ${NSL_EXTRA_ARGS:-}
