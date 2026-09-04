# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                22.320 |               9.883 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.240 | 0.240 |               153.000 |               0.870 |         25 |              0.680 |              0.739 |          0.454 |          0.654 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |

- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.454 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
