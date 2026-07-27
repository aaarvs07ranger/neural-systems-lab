# Vendored: NM512/dreamerv3-torch

- **Upstream:** https://github.com/NM512/dreamerv3-torch
- **Pinned commit:** `6ef8646d807cd10ce0c88e10a7e943211e7fc44c` (merge of PR #81, 2026-03-08)
- **License:** MIT (`LICENSE` copied verbatim)
- **Files taken:** `dreamer.py`, `models.py`, `networks.py`, `tools.py`,
  `exploration.py`, `parallel.py`, `configs.yaml`, `LICENSE`.
  The upstream `envs/` suite adapters, `Dockerfile`, and `xvfb_run.sh` are
  NOT vendored — our ProcTHOR env adapter lives in `../thor_env.py`.

## Local patches (keep this list exhaustive)

1. **Relative imports** — upstream uses flat top-level imports
   (`import tools`, `import models`, ...) which collide with this repo's
   top-level `models/` package. All intra-package imports were rewritten to
   relative form (`from . import tools`, ...) in `dreamer.py`, `models.py`,
   `networks.py`, `exploration.py`.
2. **`dreamer.py`: dropped `import envs.wrappers as wrappers`** — it requires
   OpenAI `gym` (not installed; we use gymnasium). The only consumer is the
   upstream `make_env()` suite dispatcher, which this project never calls
   (name resolves at call time, so the dangling reference is harmless).
3. **`dreamer.py`: `ruamel.yaml` → `yaml` (pyyaml)** — only `safe_load` is
   used, and only in the upstream `__main__` block.
4. **`dreamer.py`: removed `os.environ["MUJOCO_GL"]` and `sys.path.append`
   lines** — MuJoCo is unused and the path hack is superseded by packaging.

No behavioral/algorithmic changes. MPS compatibility is handled purely via
config (`device: mps`, `compile: False`, `precision: 32`,
`video_pred_log: False`) in `config.py:DreamerV3Config` + `../adapter.py`,
not by patching vendored code.
