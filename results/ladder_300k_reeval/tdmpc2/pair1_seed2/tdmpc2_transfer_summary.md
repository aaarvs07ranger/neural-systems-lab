# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.716 |                 8.040 |              10.860 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.586 |                72.400 |               8.520 |         25 |              0.160 |              0.160 |          0.129 |          0.181 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.613 |                55.200 |               9.012 |         25 |              0.120 |              0.120 |          0.102 |          0.143 |
| B_L2 (+ object appearance)                      |          0.960 | 0.630 |                59.800 |               9.952 |         25 |              0.040 |              0.040 |          0.086 |          0.120 |
| B_L3 (+ distractors)                            |          0.720 | 0.513 |                93.720 |               6.897 |         25 |              0.280 |              0.280 |          0.202 |          0.283 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.129 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.102 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.086 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.202 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
