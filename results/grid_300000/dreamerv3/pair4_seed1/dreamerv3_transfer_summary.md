# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.601 |                24.160 |              13.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.512 |                39.600 |              12.641 |         25 |              0.080 |              0.080 |          0.089 |          0.148 |
| B_L2 (+ object appearance)  |          1.000 | 0.610 |                29.120 |              13.603 |         25 |              0.000 |              0.000 |         -0.009 |         -0.015 |
| B_L3 (+ distractors)        |          0.920 | 0.571 |                43.760 |              12.484 |         25 |              0.080 |              0.080 |          0.030 |          0.049 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.089 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.030 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
