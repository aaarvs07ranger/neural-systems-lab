# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.819 |                12.720 |              11.579 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.772 |                26.320 |              11.003 |         25 |              0.040 |              0.040 |          0.047 |          0.057 |
| F_clut                                          |          1.000 | 0.822 |                12.840 |              11.575 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          1.000 | 0.814 |                14.080 |              11.589 |         25 |              0.000 |              0.000 |          0.006 |          0.007 |
| F_tgt                                           |          1.000 | 0.804 |                17.560 |              11.513 |         25 |              0.000 |              0.000 |          0.016 |          0.019 |
| F_mat                                           |          0.920 | 0.701 |                55.040 |              10.234 |         25 |              0.080 |              0.080 |          0.119 |          0.145 |
| F_light                                         |          0.960 | 0.787 |                23.320 |              11.003 |         25 |              0.040 |              0.040 |          0.032 |          0.040 |
| F_sky                                           |          0.840 | 0.590 |                74.040 |               8.997 |         25 |              0.160 |              0.160 |          0.229 |          0.280 |
| B_L1 (materials + lighting)                     |          0.880 | 0.632 |                64.160 |               9.656 |         25 |              0.120 |              0.120 |          0.187 |          0.229 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.634 |                56.400 |               9.155 |         25 |              0.160 |              0.160 |          0.185 |          0.226 |
| B_L2 (+ object appearance)                      |          0.400 | 0.295 |               135.560 |               3.331 |         25 |              0.600 |              0.600 |          0.524 |          0.639 |
| B_L3 (+ distractors)                            |          0.560 | 0.385 |               115.920 |               5.382 |         25 |              0.440 |              0.440 |          0.434 |          0.530 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.047 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.016 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.119 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.032 absolute**
- **F_sky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.229 absolute**
- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.187 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.185 absolute**
- **L2: success drop 0.600 absolute, 60.0% relative · SPL drop 0.524 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.434 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
