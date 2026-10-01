# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.785 |                17.720 |              10.972 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.610 |                55.800 |               8.262 |         25 |              0.200 |              0.208 |          0.176 |          0.224 |
| B_L2 (+ object appearance)  |          0.120 | 0.093 |               176.920 |               0.097 |         25 |              0.840 |              0.875 |          0.692 |          0.881 |
| B_L3 (+ distractors)        |          0.120 | 0.093 |               176.920 |               0.119 |         25 |              0.840 |              0.875 |          0.692 |          0.881 |

- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.176 absolute**
- **L2: success drop 0.840 absolute, 87.5% relative · SPL drop 0.692 absolute**
- **L3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.692 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
