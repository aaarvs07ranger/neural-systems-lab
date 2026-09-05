# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.814 |                14.480 |              11.582 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.546 |                67.720 |               9.118 |         25 |              0.160 |              0.160 |          0.268 |          0.329 |
| B_L2 (+ object appearance)  |          0.760 | 0.441 |                97.800 |               7.829 |         25 |              0.240 |              0.240 |          0.373 |          0.458 |
| B_L3 (+ distractors)        |          0.920 | 0.588 |                75.560 |               9.997 |         25 |              0.080 |              0.080 |          0.226 |          0.278 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.268 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.373 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.226 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
