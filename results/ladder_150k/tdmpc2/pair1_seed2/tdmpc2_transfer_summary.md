# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.716 |                10.240 |              10.826 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.587 |                76.840 |               8.025 |         25 |              0.200 |              0.200 |          0.129 |          0.180 |
| B_L2 (+ object appearance)  |          0.920 | 0.654 |                57.800 |               9.396 |         25 |              0.080 |              0.080 |          0.062 |          0.086 |
| B_L3 (+ distractors)        |          0.840 | 0.605 |                67.760 |               8.405 |         25 |              0.160 |              0.160 |          0.111 |          0.155 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.129 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.062 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.111 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
