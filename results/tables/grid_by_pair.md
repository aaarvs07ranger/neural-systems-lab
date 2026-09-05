# Grid — per-house breakdown (appendix)

Mean ± s.d. over 5 training seeds. `target swapped` records whether this pair's target object had a footprint-safe alternative asset: where it did not, L2 changes the appearance of everything EXCEPT the target, which is the study's natural control.

## pair2 — Bed, 128 reachable cells, 5 distractors, target swapped at L2: **NO**

| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|
| PPO | 0.93 | 0.86 ± 0.04 | 0.79 ± 0.08 | 0.79 ± 0.08 | 0.71 | 0.65 ± 0.04 | 0.60 ± 0.06 | 0.60 ± 0.06 |
| PPO + aug | 0.90 | 0.89 ± 0.09 | 0.86 ± 0.08 | 0.87 ± 0.09 | 0.68 | 0.67 ± 0.09 | 0.65 ± 0.07 | 0.66 ± 0.08 |
| TD-MPC2 | 1.00 | 0.90 ± 0.08 | 0.94 ± 0.07 | 0.95 ± 0.05 | 0.78 | 0.67 ± 0.08 | 0.73 ± 0.06 | 0.72 ± 0.05 |

## pair1 — Bed, 162 reachable cells, 2 distractors, target swapped at L2: **yes**

| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|
| PPO | 0.93 | 0.62 ± 0.26 | 0.20 ± 0.06 | 0.18 ± 0.04 | 0.69 | 0.49 ± 0.19 | 0.20 ± 0.06 | 0.18 ± 0.04 |
| PPO + aug | 0.96 | 0.55 ± 0.23 | 0.58 ± 0.25 | 0.48 ± 0.19 | 0.71 | 0.42 ± 0.18 | 0.45 ± 0.17 | 0.39 ± 0.10 |
| TD-MPC2 | 1.00 | 0.50 ± 0.20 | 0.55 ± 0.23 | 0.48 ± 0.23 | 0.71 | 0.38 ± 0.12 | 0.44 ± 0.13 | 0.37 ± 0.14 |

## pair0 — Fridge, 380 reachable cells, 4 distractors, target swapped at L2: **yes**

| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|
| PPO | 0.94 | 0.77 ± 0.16 | 0.14 ± 0.10 | 0.14 ± 0.10 | 0.77 | 0.62 ± 0.13 | 0.13 ± 0.09 | 0.13 ± 0.09 |
| PPO + aug | 0.99 | 0.65 ± 0.28 | 0.50 ± 0.32 | 0.50 ± 0.33 | 0.80 | 0.51 ± 0.22 | 0.36 ± 0.22 | 0.36 ± 0.24 |
| TD-MPC2 | 0.99 | 0.90 ± 0.07 | 0.66 ± 0.11 | 0.70 ± 0.18 | 0.81 | 0.62 ± 0.06 | 0.42 ± 0.05 | 0.46 ± 0.10 |

## pair3 — Bed, 460 reachable cells, 8 distractors, target swapped at L2: **yes**

| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|
| PPO | 0.86 | 0.06 ± 0.04 | 0.06 ± 0.05 | 0.06 ± 0.05 | 0.64 | 0.05 ± 0.03 | 0.05 ± 0.04 | 0.05 ± 0.04 |
| PPO + aug | 0.55 | 0.08 ± 0.10 | 0.07 ± 0.11 | 0.07 ± 0.11 | 0.41 | 0.05 ± 0.07 | 0.04 ± 0.07 | 0.04 ± 0.07 |
| TD-MPC2 | 0.95 | 0.11 ± 0.09 | 0.13 ± 0.10 | 0.14 ± 0.10 | 0.71 | 0.08 ± 0.06 | 0.10 ± 0.08 | 0.10 ± 0.06 |

## pair4 — Television, 681 reachable cells, 8 distractors, target swapped at L2: **yes**

| baseline | A success | L1 | L2 | L3 | A SPL | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|
| PPO | 0.94 | 0.27 ± 0.21 | 0.15 ± 0.17 | 0.15 ± 0.16 | 0.70 | 0.19 ± 0.14 | 0.11 ± 0.13 | 0.11 ± 0.12 |
| PPO + aug | 0.78 | 0.48 ± 0.15 | 0.35 ± 0.19 | 0.34 ± 0.17 | 0.49 | 0.28 ± 0.09 | 0.22 ± 0.11 | 0.21 ± 0.10 |
| TD-MPC2 | 0.98 | 0.68 ± 0.32 | 0.46 ± 0.33 | 0.42 ± 0.26 | 0.77 | 0.46 ± 0.23 | 0.27 ± 0.20 | 0.24 ± 0.17 |

