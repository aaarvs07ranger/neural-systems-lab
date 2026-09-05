# TDMPC2 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.772 |                26.400 |              12.667 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.602 |                62.680 |              10.720 |         25 |              0.120 |              0.125 |          0.170 |          0.220 |
| B_L2 (+ object appearance)  |          0.720 | 0.442 |               100.440 |               8.677 |         25 |              0.240 |              0.250 |          0.330 |          0.427 |
| B_L3 (+ distractors)        |          0.560 | 0.371 |               113.440 |               6.190 |         25 |              0.400 |              0.417 |          0.401 |          0.520 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.170 absolute**
- **L2: success drop 0.240 absolute, 25.0% relative · SPL drop 0.330 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.401 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
