# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.742 |                25.160 |              10.488 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.511 |                84.680 |               6.165 |         25 |              0.320 |              0.348 |          0.231 |          0.311 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -1.565 |         25 |              0.920 |              1.000 |          0.742 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -1.615 |         25 |              0.920 |              1.000 |          0.742 |          1.000 |

- **L1: success drop 0.320 absolute, 34.8% relative · SPL drop 0.231 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.742 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.742 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
