# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                19.760 |              10.954 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.700 |                41.760 |               9.297 |         25 |              0.120 |              0.125 |          0.083 |          0.105 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.720 |                35.320 |               9.816 |         25 |              0.080 |              0.083 |          0.063 |          0.080 |
| B_L2 (+ object appearance)                      |          0.680 | 0.586 |                72.920 |               7.243 |         25 |              0.280 |              0.292 |          0.197 |          0.251 |
| B_L3 (+ distractors)                            |          0.680 | 0.586 |                72.920 |               7.243 |         25 |              0.280 |              0.292 |          0.197 |          0.251 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.083 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.063 absolute**
- **L2: success drop 0.280 absolute, 29.2% relative · SPL drop 0.197 absolute**
- **L3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.197 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
