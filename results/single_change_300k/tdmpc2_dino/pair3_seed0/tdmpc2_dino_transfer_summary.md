# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.759 |                22.000 |              12.565 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.705 |                37.880 |              11.320 |         25 |              0.080 |              0.080 |          0.054 |          0.071 |
| F_clut                                          |          1.000 | 0.763 |                20.720 |              12.561 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_obj                                           |          0.960 | 0.734 |                28.880 |              11.928 |         25 |              0.040 |              0.040 |          0.025 |          0.033 |
| F_tgt                                           |          1.000 | 0.758 |                23.920 |              12.553 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_mat                                           |          0.480 | 0.330 |               125.960 |               4.767 |         25 |              0.520 |              0.520 |          0.429 |          0.565 |
| F_light                                         |          0.960 | 0.733 |                32.520 |              11.929 |         25 |              0.040 |              0.040 |          0.026 |          0.034 |
| F_sky                                           |          1.000 | 0.758 |                22.480 |              12.562 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L1 (materials + lighting)                     |          0.640 | 0.426 |               103.200 |               7.219 |         25 |              0.360 |              0.360 |          0.333 |          0.438 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.520 | 0.338 |               122.840 |               5.375 |         25 |              0.480 |              0.480 |          0.421 |          0.554 |
| B_L2 (+ object appearance)                      |          0.600 | 0.407 |               115.640 |               6.270 |         25 |              0.400 |              0.400 |          0.352 |          0.464 |
| B_L3 (+ distractors)                            |          0.480 | 0.268 |               124.320 |               4.884 |         25 |              0.520 |              0.520 |          0.491 |          0.646 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.054 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.520 absolute, 52.0% relative · SPL drop 0.429 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.026 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.333 absolute**
- **L2noT: success drop 0.480 absolute, 48.0% relative · SPL drop 0.421 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.352 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.491 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
