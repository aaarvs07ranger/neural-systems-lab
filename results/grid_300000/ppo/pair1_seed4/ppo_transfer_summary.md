# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.658 |                29.640 |               9.410 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.360 |               129.960 |               2.508 |         25 |              0.520 |              0.591 |          0.298 |          0.453 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.680 |              0.773 |          0.458 |          0.696 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.680 |              0.773 |          0.458 |          0.696 |

- **L1: success drop 0.520 absolute, 59.1% relative · SPL drop 0.298 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.458 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.458 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
