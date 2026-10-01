# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.700 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.280 |               0.903 |         25 |              0.680 |              0.739 |          0.460 |          0.657 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.440 |               0.885 |         25 |              0.680 |              0.739 |          0.460 |          0.657 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.440 |               0.386 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.460 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.460 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
