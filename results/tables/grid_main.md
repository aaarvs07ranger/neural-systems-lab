# Grid — main table

Relative drop vs each agent's own house A, pooled over 5 house pairs x 5 seeds. `range` is across HOUSES (the mean of each house's 5 seeds), because the between-house spread is a result in its own right and a pooled mean alone would describe no house in the study.

| baseline | class | rung | success drop | range over houses | SPL drop | range over houses | n |
|---|---|---|---|---|---|---|---|
| PPO | model-free | L1 | 44.3% | 7%–93% | 44.3% | 8%–93% | 25 |
| PPO | model-free | L2 | 70.9% | 14%–93% | 69.1% | 15%–93% | 25 |
| PPO | model-free | L3 | 71.3% | 14%–93% | 69.6% | 15%–93% | 25 |
| PPO + aug | model-free + DR | L1 | 40.2% | 1%–84% | 41.1% | 1%–85% | 25 |
| PPO + aug | model-free + DR | L2 | 46.6% | 4%–85% | 47.3% | 3%–87% | 25 |
| PPO + aug | model-free + DR | L3 | 48.7% | 3%–85% | 48.9% | 2%–87% | 25 |
| DreamerV3 | reconstruction WM | L1 | -9.4% | -97%–82% | -8.0% | -88%–83% | 25 |
| DreamerV3 | reconstruction WM | L2 | -0.1% | -85%–85% | -0.7% | -72%–80% | 25 |
| DreamerV3 | reconstruction WM | L3 | -6.0% | -72%–84% | -4.0% | -66%–80% | 25 |
| TD-MPC2 | decoder-free WM | L1 | 37.5% | 9%–88% | 42.7% | 13%–89% | 25 |
| TD-MPC2 | decoder-free WM | L2 | 45.0% | 6%–87% | 48.9% | 6%–86% | 25 |
| TD-MPC2 | decoder-free WM | L3 | 46.1% | 5%–86% | 50.8% | 7%–86% | 25 |
