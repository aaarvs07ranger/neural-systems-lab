# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.750 |                29.600 |              12.484 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.160 | 0.115 |               185.640 |              -0.511 |         25 |              0.840 |              0.840 |          0.634 |          0.846 |
| B_L2 (+ object appearance)  |          0.240 | 0.187 |               167.360 |               0.607 |         25 |              0.760 |              0.760 |          0.563 |          0.751 |
| B_L3 (+ distractors)        |          0.280 | 0.148 |               160.920 |               0.894 |         25 |              0.720 |              0.720 |          0.602 |          0.803 |

- **L1: success drop 0.840 absolute, 84.0% relative · SPL drop 0.634 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.563 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.602 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
