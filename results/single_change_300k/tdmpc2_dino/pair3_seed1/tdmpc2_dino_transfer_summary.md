# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.762 |                21.040 |              12.571 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.733 |                30.040 |              11.904 |         25 |              0.040 |              0.040 |          0.030 |          0.039 |
| F_clut                                          |          1.000 | 0.764 |                21.400 |              12.570 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_obj                                           |          0.920 | 0.708 |                36.400 |              11.291 |         25 |              0.080 |              0.080 |          0.054 |          0.071 |
| F_tgt                                           |          0.960 | 0.716 |                31.880 |              12.066 |         25 |              0.040 |              0.040 |          0.046 |          0.060 |
| F_mat                                           |          0.760 | 0.499 |                91.560 |               8.915 |         25 |              0.240 |              0.240 |          0.263 |          0.345 |
| F_light                                         |          1.000 | 0.762 |                27.800 |              12.517 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.960 | 0.731 |                27.040 |              11.946 |         25 |              0.040 |              0.040 |          0.031 |          0.041 |
| B_L1 (materials + lighting)                     |          0.720 | 0.526 |                88.120 |               8.428 |         25 |              0.280 |              0.280 |          0.236 |          0.310 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.516 |                83.200 |               9.105 |         25 |              0.240 |              0.240 |          0.247 |          0.324 |
| B_L2 (+ object appearance)                      |          0.800 | 0.573 |                86.720 |               9.578 |         25 |              0.200 |              0.200 |          0.190 |          0.249 |
| B_L3 (+ distractors)                            |          0.680 | 0.460 |                99.920 |               8.391 |         25 |              0.320 |              0.320 |          0.302 |          0.396 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.054 absolute**
- **F_tgt: success drop 0.040 absolute, 4.0% relative · SPL drop 0.046 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.263 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.031 absolute**
- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.236 absolute**
- **L2noT: success drop 0.240 absolute, 24.0% relative · SPL drop 0.247 absolute**
- **L2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.190 absolute**
- **L3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.302 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
