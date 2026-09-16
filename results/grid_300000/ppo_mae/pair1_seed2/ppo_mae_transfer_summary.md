# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.695 |                21.760 |               9.908 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.440 |               0.876 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.440 |               0.876 |         25 |              0.680 |              0.739 |          0.455 |          0.655 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.495 |          0.712 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.495 |          0.712 |

- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.455 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.495 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
