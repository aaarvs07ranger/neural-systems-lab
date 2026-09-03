#!/bin/bash
# Plumbing check for the grid pipeline, on a tiny training budget (~30-40 min).
#
#   sbatch scripts/slurm/smoke_grid.sbatch
#
# This validates MECHANICS, not science. Everything it exercises landed on
# 2026-09-03 and has never run against real Unity: pair selection, the
# A -> L1 -> L2 -> L3 ladder walk, held-out start poses, and the shared task
# builder that all four baselines now go through.
#
# Two tiers, because the ladder loop and the pair loop are each ONE code path --
# running all 4 x 5 x 3 combinations would test the same lines sixty times. The
# EVAL side is not sampled that way: every cell runs all 25 episodes, because
# each pinned start pose is an independent thing that can be individually
# broken and only running them all can prove none is.
#
#   Tier 1  all four baselines on pair0, full ladder. Each baseline has its own
#           env bridge and the shared-builder change touched all of them, so
#           every baseline must run; one pair's ladder covers the ladder code.
#   Tier 2  ppo (the cheapest) on pairs 1-4. Confirms every pair resolves to its
#           own house, its oracle table matches, and the pose holdout works
#           across houses from 128 to 681 cells with three different targets.
#
# The single most important assertion is at the bottom: ZERO oracle-table
# fallbacks. When the env cannot match a start pose it silently measures its own
# distance, which reinstates exactly the L2 yardstick bug Option A fixed -- and
# it does so with every run reporting success.
#
#SBATCH --job-name=nsl-smokegrid
#SBATCH --account=rao
#SBATCH --partition=ckpt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gpus=1
#SBATCH --time=02:00:00
#SBATCH --output=/gscratch/scrubbed/%u/nsl-runs/slurm-%x-%j.out

set -euo pipefail
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh" 2>/dev/null \
    || source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "${GSCRATCH_ROOT}/conda-envs/nsl"

export PYTHONUNBUFFERED=1
export NSL_THOR_PLATFORM=cloudrendering
export NSL_POSE_HOLDOUT=1          # the protocol the grid runs

RUN_ROOT="${NSL_RUN_ROOT:-/gscratch/scrubbed/${USER}/nsl-runs}"
SMOKE_ROOT="${RUN_ROOT}/smoke_grid_${SLURM_JOB_ID}"
mkdir -p "${SMOKE_ROOT}"

RAO_FREE_KB=$(df -Pk "/gscratch/rao/${USER}" | awk 'NR==2 {print $4}')
echo "[slurm] /gscratch/rao free: $((RAO_FREE_KB / 1024)) MiB; smoke root: ${SMOKE_ROOT}"

cd "${SLURM_SUBMIT_DIR}"
python -c "import torch; assert torch.cuda.is_available(), 'no CUDA'; \
print('CUDA OK:', torch.cuda.get_device_name(0))"

run_cell () {                      # baseline, pair
    local baseline="$1" pair="$2"
    export NSL_RESULTS_DIR="${SMOKE_ROOT}/${baseline}_${pair}"
    echo "=== [smoke] ${baseline} on ${pair} ==="
    # --smoke shrinks the budget; --pair selects the cell. Train and eval are
    # separate stages so neither can trigger house generation.
    python main.py --smoke --baseline "${baseline}" --pair "${pair}" --stage train
    # ALL 25 eval episodes, not the smoke default of 3. The 3-episode smoke
    # passed on 2026-09-03 and the grid then failed on eval seed 10016 -- a
    # pinned start pose the smoke had never touched. The pinned poses are the
    # thing most likely to be individually broken, so every one of them must be
    # exercised. Costs a couple of minutes; the alternative cost three days.
    python main.py --smoke --baseline "${baseline}" --pair "${pair}" --stage eval \
        --episodes 25
}

# --- Tier 1: every baseline, full ladder ----------------------------------
for b in ppo ppo_aug dreamerv3 tdmpc2; do
    run_cell "${b}" pair0
done

# --- Tier 2: every pair, cheapest baseline --------------------------------
for p in pair1 pair2 pair3 pair4; do
    run_cell ppo "${p}"
done

# --- Assertions -----------------------------------------------------------
echo
echo "=== [smoke] checking results ==="
# errexit off for the whole assertion block: every check must report before the
# script exits, otherwise the first failure hides the rest and the next run
# rediscovers them one at a time.
set +e
fail=0

# 0. The expected number of cells must actually exist. Without this, every
#    check below passes vacuously when nothing ran -- silence is not success.
n_summaries=$(ls "${SMOKE_ROOT}"/*/tables/*_transfer_summary.csv 2>/dev/null | wc -l)
if [ "${n_summaries}" -ne 8 ]; then
    echo "  FAIL ${n_summaries} summaries found, expected 8 (4 baselines on" \
         "pair0 + ppo on pairs 1-4)"
    fail=1
else
    echo "  OK  8 summaries present"
fi

# 1. Every run must have walked all four houses, not just A and B.
for d in "${SMOKE_ROOT}"/*/tables/*_transfer_summary.csv; do
    [ -e "$d" ] || continue
    levels=$(python -c "
import pandas, sys
df = pandas.read_csv(sys.argv[1])
print(','.join(sorted(df['level'].astype(str))))" "$d")
    if [ "${levels}" != "A,L1,L2,L3" ]; then
        echo "  FAIL ${d}: rungs = ${levels} (expected A,L1,L2,L3)"
        fail=1
    fi
done

# 2. The oracle table must be USED, never silently fallen back from.
SMOKE_LOG="/gscratch/scrubbed/${USER}/nsl-runs/slurm-nsl-smokegrid-${SLURM_JOB_ID}.out"
if [ ! -r "${SMOKE_LOG}" ]; then
    # A missing log makes both log-based checks vacuous, so it is a failure in
    # its own right rather than a reason to skip them.
    echo "  FAIL cannot read ${SMOKE_LOG} — log-based checks could not run"
    fail=1
fi
fallbacks=$(grep -c "measuring instead" "${SMOKE_LOG}" 2>/dev/null || true)
fallbacks="${fallbacks:-0}"
if [ "${fallbacks}" -gt 0 ]; then
    echo "  FAIL ${fallbacks} oracle-table fallbacks -- start poses do not match" \
         "the table, so SPL denominators are being measured per house again."
    fail=1
else
    echo "  OK  no oracle-table fallbacks"
fi

# 3. Training and evaluation must draw from disjoint slices of the floor.
python - <<'PYEOF'
import re, sys, os
log = f"/gscratch/scrubbed/{os.environ['USER']}/nsl-runs/slurm-nsl-smokegrid-{os.environ['SLURM_JOB_ID']}.out"
if not os.path.exists(log):
    print(f"  FAIL log {log} missing -- pose-split check could not run")
    sys.exit(1)
pat = re.compile(r"sampling starts from the '(train|eval)' slice \((\d+) of (\d+) cells")
seen = {}
for line in open(log, errors="ignore"):
    m = pat.search(line)
    if m:
        seen.setdefault((m.group(1), m.group(3)), set()).add(m.group(2))
bad = False
if not seen:
    print("  FAIL no pose-split lines in the log -- the holdout never engaged, "
          "so training and evaluation shared the whole floor")
    bad = True
for (split, total), counts in sorted(seen.items()):
    print(f"  {split:5s} slice: {sorted(counts)} of {total} cells")
    if len(counts) != 1:
        print(f"  FAIL {split} slice size varied within a {total}-cell house")
        bad = True
for total in {t for _, t in seen}:
    tr = next(iter(seen.get(("train", total), {"0"})))
    ev = next(iter(seen.get(("eval", total), {"0"})))
    if int(tr) + int(ev) != int(total):
        print(f"  FAIL {total}-cell house: train {tr} + eval {ev} != {total}")
        bad = True
    else:
        print(f"  OK  {total}-cell house: train {tr} + eval {ev} = {total}, disjoint")
sys.exit(1 if bad else 0)
PYEOF
[ $? -eq 0 ] || fail=1
set -e

if [ "${fail}" -ne 0 ]; then
    echo "[slurm] SMOKE GRID FAILED -- do not launch the grid"
    exit 1
fi
echo "[slurm] SMOKE GRID PASSED (8 cells; results under ${SMOKE_ROOT})"
