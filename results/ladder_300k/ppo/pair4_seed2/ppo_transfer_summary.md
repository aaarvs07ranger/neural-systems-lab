# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.561 |                36.920 |              12.513 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.200 | 0.144 |               164.360 |               1.221 |         25 |              0.720 |              0.783 |          0.418 |          0.744 |
| B_L2 (+ object appearance)  |          0.120 | 0.098 |               178.400 |               0.111 |         25 |              0.800 |              0.870 |          0.464 |          0.826 |
| B_L3 (+ distractors)        |          0.120 | 0.098 |               178.400 |               0.068 |         25 |              0.800 |              0.870 |          0.464 |          0.826 |

- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.418 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.464 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.464 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
