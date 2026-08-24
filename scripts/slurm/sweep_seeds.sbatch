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
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%A_%a.out

set -euo pipefail
BASELINE="${1:-dreamerv3}"
SEED="${SLURM_ARRAY_TASK_ID}"
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"

source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
# Run outputs (checkpoints, replay buffers, logs, tables, plots) go to a RUN
# ROOT that defaults to /gscratch/scrubbed/$USER/nsl-runs. Reason: on
# 2026-08-23 the shared /gscratch/rao fileset hit 100% (4.0T, ~6G free) —
# group-wide, not our data — and a job died with "Disk quota exceeded" while
# saving its model. /gscratch/scrubbed has ~9T free. NOTE: scrubbed files are
# auto-deleted after ~21 days, so rsync tables back into the repo promptly.
# Override with `NSL_RUN_ROOT=$PWD sbatch ...` to write next to the repo.
RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
mkdir -p "${RUN_ROOT}"
# Preflight: the shared /gscratch/rao fileset has been running at 100% since
# 2026-08-23. When it fills, writes fail mid-run and the crash is nearly
# invisible (Python emits "--- Logging error ---", the slurm .out truncates,
# and the job dies minutes later with a bare exit 1). Surface it up front.
RAO_FREE_KB=$(df -Pk "/gscratch/rao/${USER}" | awk 'NR==2 {print $4}')
echo "[slurm] /gscratch/rao free: $((RAO_FREE_KB / 1024)) MiB; run root: ${RUN_ROOT}"
if [ "${RAO_FREE_KB}" -lt 5242880 ]; then
    echo "[slurm] WARNING: <5 GiB free on /gscratch/rao — AI2-THOR writes into" \
         "~/.ai2thor (symlinked there) and can die mid-run. Free space or" \
         "relocate ~/.ai2thor before trusting long runs."
fi
export NSL_RESULTS_DIR="${RUN_ROOT}/results_seed${SEED}"

cd "${SLURM_SUBMIT_DIR}"
echo "[slurm] array task ${SLURM_ARRAY_JOB_ID}_${SEED} on $(hostname):" \
     "baseline=${BASELINE} seed=${SEED} results=${NSL_RESULTS_DIR}"

# shellcheck disable=SC2086
python main.py --baseline "${BASELINE}" --seed "${SEED}" ${NSL_EXTRA_ARGS:-}
