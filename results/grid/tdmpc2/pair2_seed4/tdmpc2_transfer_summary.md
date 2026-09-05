# TDMPC2 zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.778 |                12.960 |              10.639 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.645 |                60.520 |               8.929 |         25 |              0.120 |              0.120 |          0.133 |          0.171 |
| B_L2 (+ object appearance)  |          0.920 | 0.690 |                51.840 |               9.436 |         25 |              0.080 |              0.080 |          0.088 |          0.113 |
| B_L3 (+ distractors)        |          1.000 | 0.765 |                44.160 |              10.328 |         25 |              0.000 |              0.000 |          0.012 |          0.016 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.133 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.088 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
