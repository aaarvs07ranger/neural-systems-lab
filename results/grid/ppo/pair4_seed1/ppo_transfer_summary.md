# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.630 |                38.080 |              12.502 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.212 |               140.920 |               4.284 |         25 |              0.560 |              0.609 |          0.417 |          0.663 |
| B_L2 (+ object appearance)  |          0.120 | 0.074 |               178.640 |               0.087 |         25 |              0.800 |              0.870 |          0.556 |          0.883 |
| B_L3 (+ distractors)        |          0.160 | 0.114 |               172.320 |               0.694 |         25 |              0.760 |              0.826 |          0.516 |          0.819 |

- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.417 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.556 absolute**
- **L3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.516 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
