# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.710 |                14.160 |              10.391 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.360 | 0.330 |               129.120 |               2.465 |         25 |              0.600 |              0.625 |          0.380 |          0.535 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.330 |               129.240 |               2.430 |         25 |              0.600 |              0.625 |          0.380 |          0.535 |
| B_L2 (+ object appearance)                      |          0.160 | 0.160 |               168.200 |              -0.077 |         25 |              0.800 |              0.833 |          0.550 |          0.775 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               168.200 |              -0.121 |         25 |              0.800 |              0.833 |          0.550 |          0.775 |

- **L1: success drop 0.600 absolute, 62.5% relative · SPL drop 0.380 absolute**
- **L2noT: success drop 0.600 absolute, 62.5% relative · SPL drop 0.380 absolute**
- **L2: success drop 0.800 absolute, 83.3% relative · SPL drop 0.550 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.550 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
