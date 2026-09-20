# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.812 |                12.560 |              11.582 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.755 |                27.520 |              11.008 |         25 |              0.040 |              0.040 |          0.056 |          0.069 |
| F_clut                                          |          1.000 | 0.807 |                12.360 |              11.592 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |
| F_obj                                           |          0.960 | 0.784 |                20.880 |              11.069 |         25 |              0.040 |              0.040 |          0.028 |          0.034 |
| F_tgt                                           |          1.000 | 0.804 |                15.560 |              11.549 |         25 |              0.000 |              0.000 |          0.008 |          0.010 |
| F_mat                                           |          0.920 | 0.698 |                44.480 |              10.288 |         25 |              0.080 |              0.080 |          0.113 |          0.140 |
| F_light                                         |          1.000 | 0.819 |                13.560 |              11.566 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_sky                                           |          1.000 | 0.709 |                33.400 |              11.371 |         25 |              0.000 |              0.000 |          0.103 |          0.126 |
| B_L1 (materials + lighting)                     |          0.840 | 0.602 |                59.000 |               9.220 |         25 |              0.160 |              0.160 |          0.210 |          0.258 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.705 |                48.400 |              10.678 |         25 |              0.040 |              0.040 |          0.107 |          0.132 |
| B_L2 (+ object appearance)                      |          0.680 | 0.473 |                98.520 |               6.982 |         25 |              0.320 |              0.320 |          0.338 |          0.417 |
| B_L3 (+ distractors)                            |          0.560 | 0.402 |               124.440 |               5.606 |         25 |              0.440 |              0.440 |          0.410 |          0.505 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.056 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.028 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.113 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.103 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.210 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.107 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.338 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.410 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
