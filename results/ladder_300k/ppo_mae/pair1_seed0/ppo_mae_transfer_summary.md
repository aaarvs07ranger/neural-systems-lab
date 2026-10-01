# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.652 |                29.680 |               9.438 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.240 |               0.418 |         25 |              0.680 |              0.773 |          0.452 |          0.693 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.160 |               168.160 |              -0.062 |         25 |              0.720 |              0.818 |          0.492 |          0.755 |
| B_L2 (+ object appearance)                      |          0.080 | 0.080 |               184.080 |              -1.041 |         25 |              0.800 |              0.909 |          0.572 |          0.877 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               168.440 |              -0.094 |         25 |              0.720 |              0.818 |          0.492 |          0.755 |

- **L1: success drop 0.680 absolute, 77.3% relative · SPL drop 0.452 absolute**
- **L2noT: success drop 0.720 absolute, 81.8% relative · SPL drop 0.492 absolute**
- **L2: success drop 0.800 absolute, 90.9% relative · SPL drop 0.572 absolute**
- **L3: success drop 0.720 absolute, 81.8% relative · SPL drop 0.492 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
