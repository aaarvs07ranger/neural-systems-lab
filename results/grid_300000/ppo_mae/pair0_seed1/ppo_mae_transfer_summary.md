# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.814 |                13.280 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.719 |                42.920 |               9.429 |         25 |              0.160 |              0.160 |          0.096 |          0.117 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.708 |                43.920 |               9.454 |         25 |              0.160 |              0.160 |          0.106 |          0.130 |
| B_L2 (+ object appearance)                      |          0.560 | 0.476 |                94.360 |               5.847 |         25 |              0.440 |              0.440 |          0.338 |          0.415 |
| B_L3 (+ distractors)                            |          0.600 | 0.513 |                87.240 |               6.320 |         25 |              0.400 |              0.400 |          0.302 |          0.370 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.096 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.106 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.338 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.302 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
