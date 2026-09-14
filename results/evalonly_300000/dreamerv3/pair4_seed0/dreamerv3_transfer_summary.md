# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.280 | 0.131 |               159.720 |               5.258 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.445 |                75.400 |              12.141 |         25 |             -0.640 |             -2.286 |         -0.314 |         -2.388 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.378 |                94.320 |              10.829 |         25 |             -0.560 |             -2.000 |         -0.247 |         -1.880 |
| B_L2 (+ object appearance)                      |          0.760 | 0.406 |                86.840 |               9.948 |         25 |             -0.480 |             -1.714 |         -0.275 |         -2.092 |
| B_L3 (+ distractors)                            |          0.920 | 0.458 |                76.920 |              12.037 |         25 |             -0.640 |             -2.286 |         -0.327 |         -2.489 |

- **L1: success drop -0.640 absolute, -228.6% relative · SPL drop -0.314 absolute**
- **L2noT: success drop -0.560 absolute, -200.0% relative · SPL drop -0.247 absolute**
- **L2: success drop -0.480 absolute, -171.4% relative · SPL drop -0.275 absolute**
- **L3: success drop -0.640 absolute, -228.6% relative · SPL drop -0.327 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
