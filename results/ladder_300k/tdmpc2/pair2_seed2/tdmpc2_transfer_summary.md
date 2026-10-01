# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.779 |                12.480 |              10.663 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.574 |                76.200 |               7.848 |         25 |              0.200 |              0.200 |          0.205 |          0.263 |
| B_L2 (+ object appearance)  |          0.840 | 0.613 |                74.920 |               8.323 |         25 |              0.160 |              0.160 |          0.166 |          0.213 |
| B_L3 (+ distractors)        |          0.800 | 0.563 |                90.480 |               7.784 |         25 |              0.200 |              0.200 |          0.216 |          0.277 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.205 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.166 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.216 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
