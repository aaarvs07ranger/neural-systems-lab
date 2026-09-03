#!/bin/bash
# Regenerate every house pair from the verified safe-asset whitelist, then run
# the C1-C3 gate. Chain it after the scan:
#
#   SCAN=$(sbatch --parsable scripts/slurm/scan_safe_assets.sbatch)
#   sbatch --dependency=afterok:$SCAN scripts/slurm/regen_and_verify.sbatch
#
#SBATCH --job-name=nsl-regen
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
# Protocol v2: evaluation starts from floor cells training never samples. The
# grid runs with this on for all four baselines, so the oracle distance table
# written below must be measured over the SAME held-out cells -- otherwise the
# env finds no matching seed, falls back to measuring per house, and the L2
# yardstick problem Option A fixed comes straight back.
export NSL_POSE_HOLDOUT=1
cd "${SLURM_SUBMIT_DIR}"

echo "[slurm] regenerating pairs using the footprint-safe whitelist"
python envs/generate_variants.py --pairs 5
# The pose/distance table is produced first, from house A alone, because the
# prune step needs the pinned start poses to test against: a distractor can
# leave the navmesh untouched and still block a cell the agent teleports into.
echo "[slurm] measuring oracle poses + distances in house A"
python envs/verify_pairs.py --oracle-only
echo "[slurm] pruning L3 distractors that block floor or a pinned start pose"
python envs/prune_l3.py
echo "[slurm] running the C1-C3 verification gate"
python envs/verify_pairs.py
