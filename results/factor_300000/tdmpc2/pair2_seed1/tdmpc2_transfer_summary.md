# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                12.920 |              10.680 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.780 |                14.200 |              10.640 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_clut                                          |          1.000 | 0.779 |                14.240 |              10.646 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_obj                                           |          1.000 | 0.779 |                19.680 |              10.581 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_mat                                           |          0.960 | 0.728 |                30.400 |              10.079 |         25 |              0.040 |              0.040 |          0.049 |          0.063 |
| F_light                                         |          1.000 | 0.778 |                 9.240 |              10.698 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.960 | 0.739 |                29.520 |              10.084 |         25 |              0.040 |              0.040 |          0.039 |          0.050 |
| B_L1 (materials + lighting)                     |          0.920 | 0.689 |                51.680 |               9.447 |         25 |              0.080 |              0.080 |          0.088 |          0.114 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.610 |                65.240 |               8.395 |         25 |              0.160 |              0.160 |          0.167 |          0.215 |
| B_L2 (+ object appearance)                      |          0.840 | 0.641 |                55.920 |               8.576 |         25 |              0.160 |              0.160 |          0.136 |          0.175 |
| B_L3 (+ distractors)                            |          0.840 | 0.645 |                63.480 |               8.432 |         25 |              0.160 |              0.160 |          0.133 |          0.170 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.049 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.088 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.167 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.136 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.133 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
