# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.762 |                23.880 |              12.526 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.727 |                35.440 |              11.866 |         25 |              0.040 |              0.040 |          0.036 |          0.047 |
| F_clut                                          |          1.000 | 0.762 |                20.840 |              12.570 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.960 | 0.730 |                28.360 |              11.929 |         25 |              0.040 |              0.040 |          0.032 |          0.042 |
| F_tgt                                           |          0.920 | 0.702 |                47.040 |              11.315 |         25 |              0.080 |              0.080 |          0.060 |          0.079 |
| F_mat                                           |          0.520 | 0.349 |               119.720 |               5.518 |         25 |              0.480 |              0.480 |          0.413 |          0.542 |
| F_light                                         |          1.000 | 0.756 |                22.440 |              12.543 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| F_sky                                           |          1.000 | 0.758 |                21.800 |              12.570 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| B_L1 (materials + lighting)                     |          0.320 | 0.234 |               146.280 |               3.101 |         25 |              0.680 |              0.680 |          0.529 |          0.693 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.435 |               109.120 |               7.154 |         25 |              0.360 |              0.360 |          0.328 |          0.430 |
| B_L2 (+ object appearance)                      |          0.200 | 0.167 |               177.800 |               1.603 |         25 |              0.800 |              0.800 |          0.595 |          0.781 |
| B_L3 (+ distractors)                            |          0.200 | 0.139 |               184.120 |               1.589 |         25 |              0.800 |              0.800 |          0.623 |          0.817 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.032 absolute**
- **F_tgt: success drop 0.080 absolute, 8.0% relative · SPL drop 0.060 absolute**
- **F_mat: success drop 0.480 absolute, 48.0% relative · SPL drop 0.413 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L1: success drop 0.680 absolute, 68.0% relative · SPL drop 0.529 absolute**
- **L2noT: success drop 0.360 absolute, 36.0% relative · SPL drop 0.328 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.595 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.623 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
