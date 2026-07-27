#!/usr/bin/env bash
# One-command environment setup for the NSL zero-shot baseline project.
# Target: Apple Silicon (M-series) macOS with MPS acceleration.
#
#   bash setup.sh
#
# Creates/updates the conda env `nsl` (Python 3.9), installs the pinned
# arm64 stack, installs AI2-THOR from AllenAI's private index at the
# ProcTHOR-pinned commit, verifies imports + MPS, and writes a lock file.
# Idempotent: safe to re-run at any time.
set -euo pipefail

ENV_NAME="nsl"
PY_VERSION="3.9"
# AI2-THOR commit build required by ProcTHOR-10k (from the private index).
AI2THOR_COMMIT="391b3fae4d4cc026f1522e5acf60953560235971"
AI2THOR_INDEX="https://ai2thor-pypi.allenai.org"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log()  { printf '\033[1;34m[setup]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[setup:warn]\033[0m %s\n' "$*"; }

# ---------------------------------------------------------------------------
# 0. Platform checks
# ---------------------------------------------------------------------------
if [[ "$(uname -s)" != "Darwin" || "$(uname -m)" != "arm64" ]]; then
    warn "expected Apple Silicon macOS; continuing, but pins target arm64."
fi
# AI2-THOR's macOS Unity build is x86_64 and runs under Rosetta 2.
if ! /usr/bin/pgrep -q oahd; then
    warn "Rosetta 2 not detected — AI2-THOR's Unity build needs it. Install with:"
    warn "  softwareupdate --install-rosetta --agree-to-license"
fi

# `prior` (ProcTHOR-10k dataset loader) shells out to wget and git-lfs;
# macOS ships neither. Install via Homebrew when available.
for tool in wget git-lfs; do
    if ! command -v "${tool}" >/dev/null 2>&1; then
        if command -v brew >/dev/null 2>&1; then
            log "installing ${tool} via Homebrew (required by prior)..."
            brew install --quiet "${tool}"
        else
            warn "${tool} not found and Homebrew unavailable — dataset download will fail."
        fi
    fi
done
command -v git-lfs >/dev/null 2>&1 && git lfs install >/dev/null 2>&1 || true

# ---------------------------------------------------------------------------
# 1. Conda (install Miniforge if absent)
# ---------------------------------------------------------------------------
if ! command -v conda >/dev/null 2>&1; then
    log "conda not found — installing Miniforge (arm64)..."
    curl -fsSL -o /tmp/miniforge.sh \
        "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh"
    bash /tmp/miniforge.sh -b -p "${HOME}/miniforge3"
    # shellcheck disable=SC1091
    source "${HOME}/miniforge3/etc/profile.d/conda.sh"
    conda init zsh
    log "Miniforge installed. Restart your shell after setup completes."
else
    log "conda found: $(conda --version)"
fi

# ---------------------------------------------------------------------------
# 2. Environment (Python 3.9 — matches procthor/prior-era tooling)
# ---------------------------------------------------------------------------
if conda env list | awk '{print $1}' | grep -qx "${ENV_NAME}"; then
    log "conda env '${ENV_NAME}' already exists — reusing."
else
    log "creating conda env '${ENV_NAME}' (python ${PY_VERSION})..."
    conda create -y -n "${ENV_NAME}" "python=${PY_VERSION}"
fi

RUN=(conda run -n "${ENV_NAME}" --no-capture-output)

# ---------------------------------------------------------------------------
# 3. Python dependencies (pinned; see requirements.txt)
# ---------------------------------------------------------------------------
log "upgrading pip..."
"${RUN[@]}" python -m pip install --quiet --upgrade pip

log "installing pinned requirements (torch/MPS, SB3, gymnasium, prior, ...)..."
"${RUN[@]}" python -m pip install -r "${PROJECT_ROOT}/requirements.txt"

log "installing AI2-THOR ${AI2THOR_COMMIT:0:8} from ${AI2THOR_INDEX}..."
# numpy/opencv are re-stated here: ai2thor's unbounded opencv-python dep
# otherwise resolves to opencv 5.x, which force-upgrades numpy to 2.x and
# breaks torch 2.2.2 (compiled against numpy 1.x).
"${RUN[@]}" python -m pip install \
    --extra-index-url "${AI2THOR_INDEX}" \
    "ai2thor==0+${AI2THOR_COMMIT}" \
    "numpy==1.26.4" \
    "opencv-python==4.10.0.84"

# procthor (house *generation* library) is optional for this pipeline — we use
# pre-generated ProcTHOR-10k houses via `prior`. Best-effort install.
log "installing procthor (optional, best-effort)..."
"${RUN[@]}" python -m pip install procthor \
    || "${RUN[@]}" python -m pip install "procthor @ git+https://github.com/allenai/procthor.git" \
    || warn "procthor install failed — not required for the baseline pipeline."

# ---------------------------------------------------------------------------
# 4. Verification
# ---------------------------------------------------------------------------
log "verifying installation..."
"${RUN[@]}" python - <<'PY'
import platform
import ai2thor
import gymnasium
import numpy
import prior  # noqa: F401
import stable_baselines3 as sb3
import torch

print(f"  python            {platform.python_version()}")
print(f"  numpy             {numpy.__version__}")
print(f"  torch             {torch.__version__}")
print(f"  MPS available     {torch.backends.mps.is_available()}")
print(f"  gymnasium         {gymnasium.__version__}")
print(f"  stable-baselines3 {sb3.__version__}")
print(f"  ai2thor           {ai2thor.__version__}")
assert torch.backends.mps.is_available(), "MPS not available — check macOS/torch install"
PY

# ---------------------------------------------------------------------------
# 5. Lock file (exact resolved versions, for the paper's reproducibility appendix)
# ---------------------------------------------------------------------------
"${RUN[@]}" python -m pip freeze > "${PROJECT_ROOT}/requirements.lock.txt"
log "wrote requirements.lock.txt"

log "done. Activate with:  conda activate ${ENV_NAME}"
log "smoke-test the pipeline with:  python main.py --smoke"
