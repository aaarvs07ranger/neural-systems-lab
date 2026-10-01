# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.816 |                12.560 |              11.597 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.556 |                66.120 |               9.122 |         25 |              0.160 |              0.160 |          0.260 |          0.319 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.575 |                68.000 |               9.633 |         25 |              0.120 |              0.120 |          0.241 |          0.295 |
| B_L2 (+ object appearance)                      |          0.520 | 0.388 |               118.920 |               4.873 |         25 |              0.480 |              0.480 |          0.428 |          0.525 |
| B_L3 (+ distractors)                            |          0.600 | 0.397 |               116.360 |               5.794 |         25 |              0.400 |              0.400 |          0.419 |          0.513 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.260 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.241 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.428 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.419 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
