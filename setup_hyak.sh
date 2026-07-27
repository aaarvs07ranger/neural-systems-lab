#!/usr/bin/env bash
# One-command environment setup for the NSL zero-shot baseline project —
# Hyak (klone) twin of setup.sh. Target: Linux x86_64 + CUDA GPU nodes.
#
#   bash setup_hyak.sh          # run once on a klone login node
#
# Differences from the macOS setup:
#   * torch 2.2.2 from PyPI ships CUDA 12.1 Linux wheels — the same pin as
#     the Mac becomes GPU-enabled with no extra index and no module loads
#     (the wheel bundles the CUDA runtime; nodes only need the driver).
#   * AI2-THOR renders through the headless CloudRendering (Vulkan) Linux
#     build — no window, no X server. envs/procthor_env.py auto-selects it
#     on display-less Linux (override with NSL_THOR_PLATFORM).
#   * Everything heavy (conda + envs, pip cache, Unity builds, ProcTHOR-10k
#     dataset) lives under /gscratch — klone home dirs have a ~10 GB quota.
#     Per UW-IT: use the Rao group dir, NEVER /gscratch/cse.
# Idempotent: safe to re-run at any time.
set -euo pipefail

ENV_NAME="nsl"
PY_VERSION="3.9"
# AI2-THOR commit build required by ProcTHOR-10k (from the private index).
AI2THOR_COMMIT="391b3fae4d4cc026f1522e5acf60953560235971"
AI2THOR_INDEX="https://ai2thor-pypi.allenai.org"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Rao-group scratch space (override with NSL_GSCRATCH if the group dir differs).
GSCRATCH_ROOT="${NSL_GSCRATCH:-/gscratch/rao/${USER}}"
ENV_PREFIX="${GSCRATCH_ROOT}/conda-envs/${ENV_NAME}"

log()  { printf '\033[1;34m[setup-hyak]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[setup-hyak:warn]\033[0m %s\n' "$*"; }

# ---------------------------------------------------------------------------
# 0. Platform checks + gscratch layout
# ---------------------------------------------------------------------------
if [[ "$(uname -s)" != "Linux" || "$(uname -m)" != "x86_64" ]]; then
    warn "expected Linux x86_64 (klone); continuing, but pins target that."
fi
case "$(hostname)" in
    klone*|n[0-9]*|g[0-9]*) : ;;
    *) warn "hostname '$(hostname)' does not look like a Hyak node." ;;
esac
if [[ ! -d "$(dirname "${GSCRATCH_ROOT}")" ]]; then
    warn "$(dirname "${GSCRATCH_ROOT}") not found — check \`groups\` includes"
    warn "u_hyak_rao, or point NSL_GSCRATCH at your group's gscratch dir."
    exit 1
fi
mkdir -p "${GSCRATCH_ROOT}"
log "gscratch root: ${GSCRATCH_ROOT}"

# Keep the big caches off the home quota.
export PIP_CACHE_DIR="${GSCRATCH_ROOT}/.cache/pip"
mkdir -p "${PIP_CACHE_DIR}"
# AI2-THOR hardcodes ~/.ai2thor for Unity builds (~1 GB); prior puts the
# ProcTHOR-10k dataset in ~/.prior. Symlink both into gscratch once.
for d in .ai2thor .prior; do
    if [[ ! -e "${HOME}/${d}" ]]; then
        mkdir -p "${GSCRATCH_ROOT}/${d}"
        ln -s "${GSCRATCH_ROOT}/${d}" "${HOME}/${d}"
        log "symlinked ~/${d} -> ${GSCRATCH_ROOT}/${d}"
    fi
done

# ---------------------------------------------------------------------------
# 1. Conda (install Miniforge into gscratch if absent)
# ---------------------------------------------------------------------------
if ! command -v conda >/dev/null 2>&1; then
    log "conda not found — installing Miniforge (Linux x86_64) into gscratch..."
    curl -fsSL -o "${GSCRATCH_ROOT}/miniforge.sh" \
        "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"
    bash "${GSCRATCH_ROOT}/miniforge.sh" -b -p "${GSCRATCH_ROOT}/miniforge3"
    rm -f "${GSCRATCH_ROOT}/miniforge.sh"
    # shellcheck disable=SC1091
    source "${GSCRATCH_ROOT}/miniforge3/etc/profile.d/conda.sh"
    conda init bash
    log "Miniforge installed at ${GSCRATCH_ROOT}/miniforge3."
else
    log "conda found: $(conda --version)"
fi

# Register the gscratch env dir so `conda activate nsl` works by name.
if ! conda config --show envs_dirs 2>/dev/null | grep -q "${GSCRATCH_ROOT}/conda-envs"; then
    conda config --append envs_dirs "${GSCRATCH_ROOT}/conda-envs"
fi

# ---------------------------------------------------------------------------
# 2. Environment (Python 3.9 — matches procthor/prior-era tooling)
# ---------------------------------------------------------------------------
if [[ -d "${ENV_PREFIX}" ]]; then
    log "conda env at ${ENV_PREFIX} already exists — reusing."
else
    log "creating conda env '${ENV_NAME}' (python ${PY_VERSION}) in gscratch..."
    conda create -y -p "${ENV_PREFIX}" "python=${PY_VERSION}"
fi

RUN=(conda run -p "${ENV_PREFIX}" --no-capture-output)

# `prior` (ProcTHOR-10k dataset loader) shells out to wget and git-lfs.
# No root on klone — install missing tools into the conda env instead.
for tool in wget git-lfs; do
    if ! command -v "${tool}" >/dev/null 2>&1 \
        && ! "${RUN[@]}" command -v "${tool}" >/dev/null 2>&1; then
        log "installing ${tool} into the env (required by prior)..."
        conda install -y -p "${ENV_PREFIX}" -c conda-forge "${tool}"
    fi
done
"${RUN[@]}" git lfs install >/dev/null 2>&1 || true

# ---------------------------------------------------------------------------
# 3. Python dependencies (same pins as macOS; Linux resolves CUDA torch)
# ---------------------------------------------------------------------------
log "upgrading pip..."
"${RUN[@]}" python -m pip install --quiet --upgrade pip

log "installing pinned requirements (torch/CUDA, SB3, gymnasium, prior, ...)..."
"${RUN[@]}" python -m pip install -r "${PROJECT_ROOT}/requirements.txt"

log "installing AI2-THOR ${AI2THOR_COMMIT:0:8} from ${AI2THOR_INDEX}..."
# numpy/opencv are re-stated here: ai2thor's unbounded opencv-python dep
# otherwise resolves to opencv 5.x, which force-upgrades numpy to 2.x and
# breaks torch 2.2.2 (compiled against numpy 1.x). Same trap as macOS.
"${RUN[@]}" python -m pip install \
    --extra-index-url "${AI2THOR_INDEX}" \
    "ai2thor==0+${AI2THOR_COMMIT}" \
    "numpy==1.26.4" \
    "opencv-python==4.10.0.84"

log "installing procthor (optional, best-effort)..."
"${RUN[@]}" python -m pip install procthor \
    || "${RUN[@]}" python -m pip install "procthor @ git+https://github.com/allenai/procthor.git" \
    || warn "procthor install failed — not required for the baseline pipeline."

# ---------------------------------------------------------------------------
# 4. CloudRendering prerequisites
# ---------------------------------------------------------------------------
# The Vulkan loader + NVIDIA ICD live on GPU compute nodes; login nodes may
# lack them. A miss here is only fatal if it also happens on a GPU node.
if ldconfig -p 2>/dev/null | grep -q libvulkan; then
    log "libvulkan present on this node."
else
    warn "libvulkan not found on this node — fine on a login node; verify on"
    warn "a GPU node (smoke.sbatch) before launching full runs."
fi

log "pre-downloading the AI2-THOR CloudRendering Unity build (~1 GB, best-effort)..."
"${RUN[@]}" python - <<'PY' || warn "pre-download failed — first slurm job will fetch it instead."
from ai2thor.controller import Controller
from ai2thor.platform import CloudRendering

Controller(platform=CloudRendering, download_only=True)
print("  CloudRendering build present under ~/.ai2thor (-> gscratch)")
PY

# ---------------------------------------------------------------------------
# 5. Verification (login nodes have no GPU — only assert CUDA if one exists)
# ---------------------------------------------------------------------------
log "verifying installation..."
"${RUN[@]}" python - <<'PY'
import platform
import shutil

import ai2thor
import gymnasium
import numpy
import prior  # noqa: F401
import stable_baselines3 as sb3
import torch

print(f"  python            {platform.python_version()}")
print(f"  numpy             {numpy.__version__}")
print(f"  torch             {torch.__version__}")
print(f"  CUDA available    {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  GPU               {torch.cuda.get_device_name(0)}")
print(f"  gymnasium         {gymnasium.__version__}")
print(f"  stable-baselines3 {sb3.__version__}")
print(f"  ai2thor           {ai2thor.__version__}")
if shutil.which("nvidia-smi") and not torch.cuda.is_available():
    raise AssertionError("node has a GPU but torch cannot see it — check the install")
if not torch.cuda.is_available():
    print("  (no GPU on this node — normal for a login node; re-verify via smoke.sbatch)")
PY

# ---------------------------------------------------------------------------
# 6. Lock file (Linux/CUDA resolution, kept separate from the macOS lock)
# ---------------------------------------------------------------------------
"${RUN[@]}" python -m pip freeze > "${PROJECT_ROOT}/requirements.lock.hyak.txt"
log "wrote requirements.lock.hyak.txt"

log "done. Activate with:  conda activate ${ENV_NAME}   (or: conda activate ${ENV_PREFIX})"
log "next: check your allocation with \`hyakalloc\`, set account/partition in"
log "scripts/slurm/*.sbatch, then validate on a GPU node:"
log "  sbatch scripts/slurm/smoke.sbatch"
