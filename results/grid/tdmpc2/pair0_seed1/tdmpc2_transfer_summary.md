# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.819 |                14.840 |              11.556 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.623 |                66.000 |              10.102 |         25 |              0.080 |              0.080 |          0.196 |          0.239 |
| B_L2 (+ object appearance)  |          0.520 | 0.389 |               126.800 |               4.737 |         25 |              0.480 |              0.480 |          0.429 |          0.524 |
| B_L3 (+ distractors)        |          0.520 | 0.368 |               126.040 |               4.750 |         25 |              0.480 |              0.480 |          0.451 |          0.551 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.196 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.429 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.451 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
