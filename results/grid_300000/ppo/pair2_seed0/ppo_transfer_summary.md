# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.700 |                23.720 |               9.739 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.700 |                24.320 |               9.742 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L2 (+ object appearance)  |          0.800 | 0.647 |                47.120 |               8.302 |         25 |              0.120 |              0.130 |          0.053 |          0.076 |
| B_L3 (+ distractors)        |          0.800 | 0.647 |                47.120 |               8.302 |         25 |              0.120 |              0.130 |          0.053 |          0.076 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L2: success drop 0.120 absolute, 13.0% relative · SPL drop 0.053 absolute**
- **L3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.053 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
