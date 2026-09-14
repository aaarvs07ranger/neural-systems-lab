# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                14.720 |              10.647 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.603 |                85.800 |               8.221 |         25 |              0.160 |              0.160 |          0.175 |          0.225 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.695 |                59.440 |               9.296 |         25 |              0.080 |              0.080 |          0.083 |          0.106 |
| B_L2 (+ object appearance)                      |          0.840 | 0.610 |                74.640 |               8.300 |         25 |              0.160 |              0.160 |          0.168 |          0.216 |
| B_L3 (+ distractors)                            |          0.840 | 0.640 |                86.240 |               8.241 |         25 |              0.160 |              0.160 |          0.138 |          0.177 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.175 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.083 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.168 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.138 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
