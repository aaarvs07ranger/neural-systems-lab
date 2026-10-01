# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.816 |                11.840 |              11.582 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.648 |                53.360 |              10.319 |         25 |              0.080 |              0.080 |          0.168 |          0.206 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.633 |                60.040 |               9.133 |         25 |              0.160 |              0.160 |          0.183 |          0.225 |
| B_L2 (+ object appearance)                      |          0.560 | 0.358 |               122.480 |               5.514 |         25 |              0.440 |              0.440 |          0.458 |          0.561 |
| B_L3 (+ distractors)                            |          0.520 | 0.349 |               124.440 |               5.001 |         25 |              0.480 |              0.480 |          0.467 |          0.572 |

- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.168 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.183 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.458 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.467 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
