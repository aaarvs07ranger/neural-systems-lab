# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.806 |                15.560 |              11.566 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.604 |                61.280 |               8.286 |         25 |              0.240 |              0.240 |          0.202 |          0.250 |
| B_L2 (+ object appearance)  |          0.080 | 0.080 |               184.240 |              -0.878 |         25 |              0.920 |              0.920 |          0.726 |          0.901 |
| B_L3 (+ distractors)        |          0.080 | 0.080 |               184.240 |              -0.873 |         25 |              0.920 |              0.920 |          0.726 |          0.901 |

- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.202 absolute**
- **L2: success drop 0.920 absolute, 92.0% relative · SPL drop 0.726 absolute**
- **L3: success drop 0.920 absolute, 92.0% relative · SPL drop 0.726 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
