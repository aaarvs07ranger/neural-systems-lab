# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.320 | 0.159 |               150.600 |               5.696 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.509 |                62.920 |              13.031 |         25 |             -0.640 |             -2.000 |         -0.350 |         -2.199 |
| B_L2 (+ object appearance)  |          0.800 | 0.460 |                80.000 |              10.224 |         25 |             -0.480 |             -1.500 |         -0.301 |         -1.889 |
| B_L3 (+ distractors)        |          0.720 | 0.424 |                88.120 |               9.033 |         25 |             -0.400 |             -1.250 |         -0.265 |         -1.665 |

- **L1: success drop -0.640 absolute, -200.0% relative · SPL drop -0.350 absolute**
- **L2: success drop -0.480 absolute, -150.0% relative · SPL drop -0.301 absolute**
- **L3: success drop -0.400 absolute, -125.0% relative · SPL drop -0.265 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
