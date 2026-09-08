# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.785 |                20.920 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.586 |                66.440 |               7.694 |         25 |              0.240 |              0.250 |          0.199 |          0.254 |
| B_L2 (+ object appearance)  |          0.160 | 0.140 |               169.600 |               0.297 |         25 |              0.800 |              0.833 |          0.646 |          0.822 |
| B_L3 (+ distractors)        |          0.160 | 0.140 |               169.600 |               0.290 |         25 |              0.800 |              0.833 |          0.646 |          0.822 |

- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.199 absolute**
- **L2: success drop 0.800 absolute, 83.3% relative · SPL drop 0.646 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.646 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
