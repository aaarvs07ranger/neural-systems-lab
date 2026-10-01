# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.819 |                11.600 |              11.589 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.677 |                42.720 |               9.451 |         25 |              0.160 |              0.160 |          0.142 |          0.174 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.756 |                32.320 |              10.977 |         25 |              0.040 |              0.040 |          0.064 |          0.078 |
| B_L2 (+ object appearance)                      |          0.840 | 0.629 |                50.760 |               9.502 |         25 |              0.160 |              0.160 |          0.190 |          0.232 |
| B_L3 (+ distractors)                            |          0.800 | 0.596 |                72.240 |               8.758 |         25 |              0.200 |              0.200 |          0.224 |          0.273 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.142 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.064 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.190 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.224 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
