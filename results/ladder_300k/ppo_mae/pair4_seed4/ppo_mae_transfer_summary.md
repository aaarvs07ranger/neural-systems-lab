# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.723 |                26.600 |              12.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.160 | 0.127 |               171.320 |               1.142 |         25 |              0.800 |              0.833 |          0.596 |          0.825 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.114 |               170.640 |               0.999 |         25 |              0.800 |              0.833 |          0.609 |          0.843 |
| B_L2 (+ object appearance)                      |          0.240 | 0.191 |               156.400 |               2.157 |         25 |              0.720 |              0.750 |          0.532 |          0.736 |
| B_L3 (+ distractors)                            |          0.200 | 0.166 |               163.480 |               1.690 |         25 |              0.760 |              0.792 |          0.557 |          0.771 |

- **L1: success drop 0.800 absolute, 83.3% relative · SPL drop 0.596 absolute**
- **L2noT: success drop 0.800 absolute, 83.3% relative · SPL drop 0.609 absolute**
- **L2: success drop 0.720 absolute, 75.0% relative · SPL drop 0.532 absolute**
- **L3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
