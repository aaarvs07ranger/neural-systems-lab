# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                12.000 |              10.680 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.690 |                69.640 |               9.224 |         25 |              0.080 |              0.080 |          0.088 |          0.113 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.569 |                70.240 |               7.967 |         25 |              0.200 |              0.200 |          0.209 |          0.268 |
| B_L2 (+ object appearance)                      |          0.760 | 0.563 |                93.320 |               7.229 |         25 |              0.240 |              0.240 |          0.215 |          0.277 |
| B_L3 (+ distractors)                            |          0.800 | 0.572 |                81.080 |               7.863 |         25 |              0.200 |              0.200 |          0.206 |          0.265 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.088 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.209 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.215 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.206 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
