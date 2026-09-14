# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.782 |                20.040 |              10.949 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.555 |                69.640 |               9.060 |         25 |              0.120 |              0.125 |          0.228 |          0.291 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.478 |                94.920 |               7.327 |         25 |              0.240 |              0.250 |          0.304 |          0.389 |
| B_L2 (+ object appearance)                      |          0.600 | 0.413 |               113.160 |               5.794 |         25 |              0.360 |              0.375 |          0.370 |          0.472 |
| B_L3 (+ distractors)                            |          0.480 | 0.332 |               139.560 |               4.173 |         25 |              0.480 |              0.500 |          0.450 |          0.575 |

- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.228 absolute**
- **L2noT: success drop 0.240 absolute, 25.0% relative · SPL drop 0.304 absolute**
- **L2: success drop 0.360 absolute, 37.5% relative · SPL drop 0.370 absolute**
- **L3: success drop 0.480 absolute, 50.0% relative · SPL drop 0.450 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
