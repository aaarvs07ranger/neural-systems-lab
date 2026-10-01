# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.811 |                10.720 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.737 |                25.240 |              10.415 |         25 |              0.080 |              0.080 |          0.074 |          0.092 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.640 |                41.160 |               9.353 |         25 |              0.160 |              0.160 |          0.171 |          0.211 |
| B_L2 (+ object appearance)                      |          0.720 | 0.555 |                63.960 |               7.846 |         25 |              0.280 |              0.280 |          0.256 |          0.315 |
| B_L3 (+ distractors)                            |          0.640 | 0.511 |                78.760 |               6.742 |         25 |              0.360 |              0.360 |          0.300 |          0.370 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.074 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.171 absolute**
- **L2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.256 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.300 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
