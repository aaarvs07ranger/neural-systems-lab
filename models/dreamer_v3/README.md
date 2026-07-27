# DreamerV3 baseline (IMPLEMENTED)

Vendored PyTorch DreamerV3 (`NM512/dreamerv3-torch`, pinned commit — see
`vendor/VENDOR.md`) driven through the shared `BaselineAdapter` protocol so
the A→B transfer eval and reporting are byte-identical to the PPO baseline.

## Layout

- `vendor/` — upstream implementation, MIT-licensed, minimally patched
  (relative imports + dropped OpenAI-gym-only code paths; exhaustive patch
  list in `vendor/VENDOR.md`). No algorithmic changes.
- `thor_env.py` — folds upstream's OneHotAction/SelectAction/TimeLimit/UUID
  wrappers into one old-gym-style adapter around
  `envs.procthor_env.ProcTHORObjectNavEnv`; downscales THOR's 128×128 frames
  to Dreamer's native 64×64.
- `adapter.py` — `DreamerV3Adapter` (train / load / predict / reset_episode).
  `train()` re-implements upstream `dreamer.py:main()` with a single env and
  no interleaved eval (a second Unity process is too heavy on the M4 Air).

## Running

```bash
python main.py --smoke --baseline dreamerv3   # fast mechanics check
python main.py --baseline dreamerv3           # full 150k-step experiment
python main.py --baseline dreamerv3 --stage eval  # re-eval saved model
tensorboard --logdir results/logs/dreamerv3   # training curves
```

Checkpoints: `results/checkpoints/dreamerv3/{latest.pt,dreamer_final.pt}`
(resume is automatic from `latest.pt`; replay episodes persist in
`results/logs/dreamerv3/train_eps`). Delete both directories for a fresh run.

## MPS notes (all handled in config, not code)

`device=mps`, `compile=False` (no inductor-MPS on torch 2.2), `precision=32`
(AMP contexts become no-ops), `video_pred_log=False` (TB video summaries need
moviepy/ffmpeg), `PYTORCH_ENABLE_MPS_FALLBACK=1` (set by adapter import).
Discrete-action recipe follows upstream atari100k/crafter:
`actor.dist=onehot`, `imag_gradient=reinforce`.

Knobs live in `config.py:DreamerV3Config`. `train_ratio=32` (replayed frames
per env step) is the compute/quality lever — upstream uses 512 on GPU rigs;
raise it first if the world model underfits and wall-clock allows.
