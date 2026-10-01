# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.674 |                41.920 |               9.612 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.480 | 0.409 |               108.840 |               4.685 |         25 |              0.360 |              0.429 |          0.266 |          0.394 |
| B_L2 (+ object appearance)  |          0.200 | 0.154 |               162.480 |               0.682 |         25 |              0.640 |              0.762 |          0.521 |          0.772 |
| B_L3 (+ distractors)        |          0.240 | 0.194 |               154.760 |               1.157 |         25 |              0.600 |              0.714 |          0.481 |          0.713 |

- **L1: success drop 0.360 absolute, 42.9% relative · SPL drop 0.266 absolute**
- **L2: success drop 0.640 absolute, 76.2% relative · SPL drop 0.521 absolute**
- **L3: success drop 0.600 absolute, 71.4% relative · SPL drop 0.481 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
