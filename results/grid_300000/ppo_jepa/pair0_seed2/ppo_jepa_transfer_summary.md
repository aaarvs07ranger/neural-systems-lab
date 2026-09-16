# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.732 |                25.880 |              10.492 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.679 |                41.000 |               9.352 |         25 |              0.080 |              0.087 |          0.054 |          0.073 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.555 |                64.320 |               7.847 |         25 |              0.200 |              0.217 |          0.178 |          0.243 |
| B_L2 (+ object appearance)                      |          0.600 | 0.451 |                86.800 |               6.335 |         25 |              0.320 |              0.348 |          0.282 |          0.384 |
| B_L3 (+ distractors)                            |          0.600 | 0.451 |                86.840 |               6.339 |         25 |              0.320 |              0.348 |          0.282 |          0.384 |

- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.054 absolute**
- **L2noT: success drop 0.200 absolute, 21.7% relative · SPL drop 0.178 absolute**
- **L2: success drop 0.320 absolute, 34.8% relative · SPL drop 0.282 absolute**
- **L3: success drop 0.320 absolute, 34.8% relative · SPL drop 0.282 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
