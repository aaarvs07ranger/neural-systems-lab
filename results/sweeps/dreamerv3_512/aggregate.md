# DreamerV3 (ratio 512) 5-seed sweep — aggregate zero-shot transfer results

- **Runs:** klone job `37948923` (array 0–4), 2026-07-31. Training seeds 0–4, 150k env steps each
  at the upstream published compute recipe (`--train-ratio 512` ≈ 74k grad updates), `ckpt`
  partition, ~10–12 h/run in parallel (several tasks preempted + auto-resumed; all COMPLETED 0:0).
- **Protocol:** identical frozen-policy paired A/B eval as all other baselines (25 episodes/variant,
  eval seeds 10000+, paired start poses). Per-seed raw tables in `seed<N>/`. The n=1 parity run
  (default seed, 2026-07-30, jobs 37923581) showed A 0.96 / B 1.00 — consistent with this range.

## Aggregate (mean ± std over 5 training seeds)

| metric | A (train visuals) | B (zero-shot) |
|---|---|---|
| Success rate | 0.992 ± 0.018 | 0.936 ± 0.073 |
| SPL | 0.612 ± 0.028 | 0.518 ± 0.040 |
| Mean episode length | 25.6 ± 6.7 | 54.6 ± 15.6 |

- **Relative success drop A→B: 5.7% ± 6.7%** — per-seed: 16.0, 0.0, 4.0, 0.0, 8.3 (%).
- **Relative SPL drop A→B: 15.4% ± 4.3%** — per-seed: 23.0, 12.7, 14.9, 13.5, 13.0 (%).

## Reading (vs PPO 5-seed sweep, `results/sweeps/ppo/aggregate.md`)

1. **Success transfer: DreamerV3 is ~6× more robust and ~4× more consistent than PPO**
   (5.7% ± 6.7 vs 32.4% ± 29.6 relative drop) at matched-and-higher A-competency
   (0.992 vs 0.896). Two of five Dreamer seeds transfer *perfectly* on success.
2. **But the visual shift is not free: every seed pays an efficiency tax.** SPL drops
   13–23% and episode length roughly doubles (2.1×) in the shifted variant, with much
   lower variance than the success metric. The world model reliably still *finds* the
   goal — it just wanders getting there.
3. **Refined headline for the abstract:** with a reconstruction world model at full
   compute, the visual-binding problem manifests as *inefficiency, not failure* at this
   task scale — while model-free PPO fails outright on unlucky seeds. SPL is the
   sensitive, low-variance metric; success rate saturates in a small single-room house.
4. Caveats: n=1 house pair, mild visual shift (textures/lighting). The severity ladder
   and multi-house grid test whether these conclusions survive harder shifts.
