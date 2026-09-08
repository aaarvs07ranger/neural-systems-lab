# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.734 |                25.480 |              10.502 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.589 |                63.200 |               7.843 |         25 |              0.200 |              0.217 |          0.144 |          0.197 |
| B_L2 (+ object appearance)  |          0.120 | 0.098 |               176.600 |               0.157 |         25 |              0.800 |              0.870 |          0.636 |          0.867 |
| B_L3 (+ distractors)        |          0.120 | 0.098 |               176.600 |               0.152 |         25 |              0.800 |              0.870 |          0.636 |          0.867 |

- **L1: success drop 0.200 absolute, 21.7% relative · SPL drop 0.144 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.636 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.636 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
