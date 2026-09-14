# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.715 |                 8.680 |              10.845 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.560 | 0.396 |               118.800 |               4.672 |         25 |              0.440 |              0.440 |          0.320 |          0.447 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.360 |               155.160 |               1.811 |         25 |              0.640 |              0.640 |          0.355 |          0.497 |
| B_L2 (+ object appearance)                      |          0.480 | 0.361 |               128.680 |               3.550 |         25 |              0.520 |              0.520 |          0.355 |          0.496 |
| B_L3 (+ distractors)                            |          0.360 | 0.300 |               138.640 |               2.159 |         25 |              0.640 |              0.640 |          0.415 |          0.581 |

- **L1: success drop 0.440 absolute, 44.0% relative · SPL drop 0.320 absolute**
- **L2noT: success drop 0.640 absolute, 64.0% relative · SPL drop 0.355 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.355 absolute**
- **L3: success drop 0.640 absolute, 64.0% relative · SPL drop 0.415 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
