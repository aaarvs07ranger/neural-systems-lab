# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.774 |                17.920 |              10.956 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.647 |                41.280 |               9.405 |         25 |              0.120 |              0.125 |          0.127 |          0.164 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.660 |                36.600 |               9.953 |         25 |              0.080 |              0.083 |          0.114 |          0.147 |
| B_L2 (+ object appearance)                      |          0.800 | 0.633 |                52.360 |               8.704 |         25 |              0.160 |              0.167 |          0.141 |          0.182 |
| B_L3 (+ distractors)                            |          0.600 | 0.511 |                87.120 |               5.981 |         25 |              0.360 |              0.375 |          0.263 |          0.340 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.127 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.114 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.141 absolute**
- **L3: success drop 0.360 absolute, 37.5% relative · SPL drop 0.263 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
