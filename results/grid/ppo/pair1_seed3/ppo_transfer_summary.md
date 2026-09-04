# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.706 |                14.600 |              10.382 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.657 |                40.080 |               8.608 |         25 |              0.120 |              0.125 |          0.048 |          0.068 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.760 |              0.792 |          0.506 |          0.717 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.760 |              0.792 |          0.506 |          0.717 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.048 absolute**
- **L2: success drop 0.760 absolute, 79.2% relative · SPL drop 0.506 absolute**
- **L3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.506 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
