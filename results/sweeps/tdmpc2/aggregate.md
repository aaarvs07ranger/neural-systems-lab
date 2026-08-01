# TD-MPC2 5-seed sweep — aggregate zero-shot transfer results

- **Runs:** klone jobs `37982716` → resumed as `37997516` (array 0–4) after the
  buffer-wraparound fix (VENDOR.md patch #10), 2026-08-01. Training seeds 0–4, 150k env
  steps each at the upstream published recipe (1 update/env step, batch 256, MPPI 6×512,
  model_size 5, rgb 3-frame stack), `ckpt` partition. All COMPLETED 0:0.
- **Protocol:** identical frozen-policy paired A/B eval as PPO and DreamerV3
  (25 episodes/variant, eval seeds 10000+, paired start poses).

## Aggregate (mean ± std over 5 training seeds)

| metric | A (train visuals) | B (zero-shot) |
|---|---|---|
| Success rate | 1.000 ± 0.000 | 0.864 ± 0.083 |
| SPL | 0.726 ± 0.004 | 0.513 ± 0.079 |
| Mean episode length | 17.3 ± 2.8 | 71.2 ± 16.0 |

- **Relative success drop A→B: 13.6% ± 8.3%** — per-seed: 20.0, 20.0, 16.0, 12.0, 0.0 (%).
- **Relative SPL drop A→B: 29.2% ± 11.1%** — per-seed: 39.6, 31.4, 39.8, 17.6, 17.8 (%).

## The three-baseline table (all at published recipes, 5 seeds each)

| baseline | class | A success | B success | rel. success drop | A SPL | B SPL | rel. SPL drop |
|---|---|---|---|---|---|---|---|
| PPO | model-free on-policy | 0.896 ± 0.022 | 0.608 ± 0.270 | 32.4% ± 29.6 | 0.629 ± 0.026 | 0.448 ± 0.179 | ~28.8% |
| DreamerV3 (ratio 512) | reconstruction world model | 0.992 ± 0.018 | 0.936 ± 0.073 | **5.7% ± 6.7** | 0.612 ± 0.028 | 0.518 ± 0.040 | 15.4% ± 4.3 |
| TD-MPC2 | decoder-free latent WM + planner | **1.000 ± 0.000** | 0.864 ± 0.083 | 13.6% ± 8.3 | **0.726 ± 0.004** | 0.513 ± 0.079 | 29.2% ± 11.1 |

## Reading

1. **TD-MPC2 is the strongest in-domain agent** — perfect success on every seed and the
   best SPL of all three (0.726; test-time planning finds shorter paths than either
   learned reflex). Its transfer competency claim is therefore maximally fair.
2. **The Session-9 APC-framing prediction is REFUTED.** We predicted the decoder-free,
   reward/value-predictive latent (TD-MPC2) would transfer *better* than the
   reconstruction latent (DreamerV3). The opposite holds on every aggregate metric:
   Dreamer 5.7% vs TD-MPC2 13.6% success drop; 15.4% vs 29.2% SPL drop. A candidate
   interpretation: a latent trained only to predict reward/value is free to exploit
   *any* discriminative shortcut, including appearance; reconstruction forces the latent
   to model the whole scene — which includes its appearance-invariant structure — and
   Dreamer's stochastic latent + KL acts as an information bottleneck. This needs the
   multi-house grid before it hardens into a claim.
3. **The universal signature holds:** every architecture class pays a large efficiency
   tax under pure appearance shift (SPL −15% to −29%, episode length ×2–×4), even when
   success survives. Transfer ordering: **DreamerV3 > TD-MPC2 > PPO**, with PPO both
   worst and wildly seed-dependent.
4. Caveats: n=1 house pair, mild (texture/lighting) shift; TD-MPC2 eval actions are
   mildly stochastic (upstream ShiftAug active at eval — see vendor/VENDOR.md).
