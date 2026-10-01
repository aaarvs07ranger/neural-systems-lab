# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 8.160 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.600 | 0.533 |                85.160 |               5.664 |         25 |              0.400 |              0.400 |          0.243 |          0.313 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.600 |                85.960 |               5.672 |         25 |              0.400 |              0.400 |          0.177 |          0.228 |
| B_L2 (+ object appearance)                      |          0.600 | 0.600 |                85.960 |               5.672 |         25 |              0.400 |              0.400 |          0.177 |          0.228 |
| B_L3 (+ distractors)                            |          0.640 | 0.613 |                78.880 |               6.157 |         25 |              0.360 |              0.360 |          0.163 |          0.210 |

- **L1: success drop 0.400 absolute, 40.0% relative · SPL drop 0.243 absolute**
- **L2noT: success drop 0.400 absolute, 40.0% relative · SPL drop 0.177 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.177 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.163 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
