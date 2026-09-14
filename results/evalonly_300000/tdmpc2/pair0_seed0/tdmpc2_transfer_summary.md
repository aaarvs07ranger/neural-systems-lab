# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.820 |                12.480 |              11.575 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.840 | 0.614 |                65.080 |               9.120 |         25 |              0.160 |              0.160 |          0.206 |          0.251 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.632 |                51.240 |              10.148 |         25 |              0.080 |              0.080 |          0.188 |          0.230 |
| B_L2 (+ object appearance)                      |          0.560 | 0.391 |               124.480 |               5.099 |         25 |              0.440 |              0.440 |          0.429 |          0.523 |
| B_L3 (+ distractors)                            |          0.560 | 0.379 |               122.520 |               5.302 |         25 |              0.440 |              0.440 |          0.441 |          0.538 |

- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.206 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.188 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.429 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.441 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
