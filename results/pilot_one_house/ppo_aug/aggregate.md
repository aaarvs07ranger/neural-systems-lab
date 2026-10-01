# ppo_aug 5-seed sweep — does visual augmentation fix zero-shot transfer?

- **Runs:** klone jobs `38800341` (seeds 0, 4), `38801317` (seeds 1, 3), `38806927` (seed 2),
  2026-08-24. Training seeds 0–4, 150k steps each, `ckpt` partition, ~26–40 min/run.
  Three execution failures on seed 2 and one round on seeds 1/3 (shared-node CloudRendering
  contention, not a code fault — see CLAUDE.md 4n); every reported run exited 0.
- **Recipe:** `PPOAugConfig` — identical to `PPOConfig` in every hyperparameter, budget and
  protocol. The ONLY difference is train-time photometric jitter
  (brightness/contrast/saturation ±40%, hue ±36°, resampled once per episode;
  `envs/augmentation.py`). **Eval envs are built raw — the A/B protocol is untouched.**
- **Protocol:** frozen-policy paired A/B eval, 25 episodes/variant, eval seeds 10000+,
  paired start poses. Per-seed raw tables in `seed<N>/`.

## Aggregate (mean ± std over 5 training seeds)

| metric | A (train visuals) | B (zero-shot) |
|---|---|---|
| Success rate | 0.896 ± 0.046 | 0.680 ± 0.279 |
| SPL | 0.610 ± 0.023 | 0.434 ± 0.165 |
| Mean episode length | 32.7 ± 8.0 | 74.3 ± 51.5 |

**Relative success drop A→B: mean 24.8% ± 28.9%** — per-seed: 4.5%, 52.4%, 12.5%, 59.1%, −4.3%.

## Head-to-head vs vanilla PPO (same budget, same protocol, same seeds)

| metric | PPO | ppo_aug | exact permutation test |
|---|---|---|---|
| A success (in-domain) | 0.896 ± 0.022 | 0.896 ± 0.046 | **p = 1.000** |
| B success (zero-shot) | 0.608 ± 0.270 | 0.680 ± 0.279 | p = 0.690 |
| Relative success drop | 32.4% ± 29.6 | 24.8% ± 28.9 | p = 0.683 |
| Relative SPL drop | 29.4% ± 26.5 | 28.9% ± 26.1 | p = 0.968 |

Two-sided exact permutation tests over all 252 seed-label assignments (n=5 vs 5), on the
per-seed values. No transfer metric is distinguishable.

## Reading

1. **Photometric domain randomization does not fix the visual-binding problem.** The nominal
   7.6-point improvement in relative drop is indistinguishable from noise (p = 0.68) against a
   between-seed spread of ±29. The defensible claim is **"no detectable effect"**, never
   "augmentation helps a little".
2. **The control is clean.** In-domain competency is *identical* (0.896 vs 0.896, p = 1.000),
   so augmentation neither helped nor hurt learning the task — any transfer difference would
   have been attributable to the augmentation alone. There is none.
3. **The seed lottery survives augmentation.** Per-seed drops stay bimodal (−4.3%, 4.5%, 12.5%
   vs 52.4%, 59.1%): some seeds land on appearance-invariant features, most don't, and jitter
   does not change those odds. Same qualitative pattern as vanilla PPO.
4. **Why it fails is visible, not just inferable.** `results/plots/augmentation_examples.png`
   shows the training jitter is *more* aggressive in colour than the A→B shift — yet A→B swaps
   the floor **material** (visible wood grain), which no colour transform can synthesise.
   Augmentation buys invariance only to nuisance dimensions you can enumerate and simulate in
   advance. That is precisely the gap a learned, task-informed perceptual bottleneck targets.
5. **For the abstract:** this is the answer to "why not just augment?", pre-registered as a
   distinct architecture class rather than argued in prose. Note also that TD-MPC2 already
   contains DrQ-style *geometric* (random-shift) augmentation internally and still drops
   13.6% — the two augmentation families fail independently.

## Caveats

- One house pair, one severity rung (L1: textures + lighting). A stronger augmentation family
  (material/texture randomisation) is untested and would be the fair next probe.
- Eval start poses are not held out from training (protocol-v2 item, applies to all baselines).
