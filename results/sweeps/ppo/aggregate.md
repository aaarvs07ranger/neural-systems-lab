# PPO 5-seed sweep — aggregate zero-shot transfer results

- **Runs:** klone job `37923582` (array 0–4), 2026-07-30. Training seeds 0–4 (one per array task),
  150k steps each at the standard `PPOConfig` recipe, `ckpt` partition, ~26 min/run in parallel.
- **Protocol:** identical frozen-policy paired A/B eval as all prior runs (25 episodes/variant,
  eval seeds 10000+, paired start poses). Per-seed raw tables in `seed<N>/`.

## Aggregate (mean ± std over 5 training seeds)

| metric | A (train visuals) | B (zero-shot) |
|---|---|---|
| Success rate | 0.896 ± 0.022 | 0.608 ± 0.270 |
| SPL | 0.629 ± 0.026 | 0.448 ± 0.179 |
| Mean episode length | 31.6 ± 4.2 | 85.2 ± 50.0 |

**Relative success drop A→B: mean 32.4% ± 29.6%** — per-seed: 4.5%, 4.3%, 72.7%, 30.4%, 50.0%.

## Reading

1. **Training competency is seed-stable** (A: 0.88–0.92 across all seeds; SPL std 0.026).
2. **Zero-shot transfer is wildly seed-dependent** (B success 0.24–0.88). Whether PPO's learned
   features happen to be appearance-invariant is essentially luck of the initialization/experience
   draw — the visual-binding failure is not a constant offset but a high-variance lottery.
3. The original n=1 result (8.3% rel drop) came from a *lucky* seed; the expected drop is ~4×
   larger. Single-seed transfer claims in this setting are unpublishable — exactly why the
   roadmap requires 5 seeds per cell.
