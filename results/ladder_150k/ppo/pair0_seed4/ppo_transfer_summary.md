# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.668 |                40.800 |               9.494 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.590 |                49.800 |               8.998 |         25 |              0.040 |              0.048 |          0.078 |          0.117 |
| B_L2 (+ object appearance)  |          0.320 | 0.298 |               138.680 |               2.531 |         25 |              0.520 |              0.619 |          0.370 |          0.554 |
| B_L3 (+ distractors)        |          0.320 | 0.278 |               139.240 |               2.543 |         25 |              0.520 |              0.619 |          0.390 |          0.584 |

- **L1: success drop 0.040 absolute, 4.8% relative · SPL drop 0.078 absolute**
- **L2: success drop 0.520 absolute, 61.9% relative · SPL drop 0.370 absolute**
- **L3: success drop 0.520 absolute, 61.9% relative · SPL drop 0.390 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
