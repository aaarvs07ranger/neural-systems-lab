# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.811 |                15.320 |              11.563 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.764 |                29.440 |              10.431 |         25 |              0.080 |              0.080 |          0.047 |          0.058 |
| B_L2 (+ object appearance)  |          0.120 | 0.120 |               176.400 |               0.027 |         25 |              0.880 |              0.880 |          0.691 |          0.852 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               176.400 |               0.027 |         25 |              0.880 |              0.880 |          0.691 |          0.852 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.691 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.691 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
