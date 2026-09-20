# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.716 |                32.040 |              12.060 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.676 |                45.600 |              11.779 |         25 |              0.000 |              0.000 |          0.039 |          0.055 |
| F_clut                                          |          0.960 | 0.722 |                34.800 |              12.022 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_obj                                           |          0.920 | 0.688 |                39.200 |              11.441 |         25 |              0.040 |              0.042 |          0.028 |          0.039 |
| F_tgt                                           |          1.000 | 0.714 |                35.680 |              12.413 |         25 |             -0.040 |             -0.042 |          0.001 |          0.002 |
| F_mat                                           |          0.600 | 0.380 |               115.120 |               6.065 |         25 |              0.360 |              0.375 |          0.336 |          0.469 |
| F_light                                         |          0.800 | 0.593 |                61.480 |               9.667 |         25 |              0.160 |              0.167 |          0.123 |          0.171 |
| F_sky                                           |          0.880 | 0.655 |                60.160 |              10.659 |         25 |              0.080 |              0.083 |          0.060 |          0.084 |
| B_L1 (materials + lighting)                     |          0.240 | 0.190 |               173.600 |               1.190 |         25 |              0.720 |              0.750 |          0.525 |          0.734 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.279 |               150.360 |               3.017 |         25 |              0.600 |              0.625 |          0.436 |          0.610 |
| B_L2 (+ object appearance)                      |          0.240 | 0.191 |               175.120 |               1.208 |         25 |              0.720 |              0.750 |          0.524 |          0.733 |
| B_L3 (+ distractors)                            |          0.320 | 0.264 |               163.720 |               2.098 |         25 |              0.640 |              0.667 |          0.451 |          0.631 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.039 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.028 absolute**
- **F_tgt: success drop -0.040 absolute, -4.2% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.360 absolute, 37.5% relative · SPL drop 0.336 absolute**
- **F_light: success drop 0.160 absolute, 16.7% relative · SPL drop 0.123 absolute**
- **F_sky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.060 absolute**
- **L1: success drop 0.720 absolute, 75.0% relative · SPL drop 0.525 absolute**
- **L2noT: success drop 0.600 absolute, 62.5% relative · SPL drop 0.436 absolute**
- **L2: success drop 0.720 absolute, 75.0% relative · SPL drop 0.524 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.451 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
