# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 8.280 |              10.722 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.616 |                43.560 |               8.727 |         25 |              0.160 |              0.160 |          0.161 |          0.207 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.560 | 0.464 |                94.440 |               5.216 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |
| B_L2 (+ object appearance)                      |          0.560 | 0.464 |                94.440 |               5.216 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |
| B_L3 (+ distractors)                            |          0.560 | 0.464 |                94.440 |               5.216 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.161 absolute**
- **L2noT: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
