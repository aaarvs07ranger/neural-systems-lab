# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.686 |                34.520 |              10.002 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.679 |                34.240 |               9.955 |         25 |              0.000 |              0.000 |          0.007 |          0.011 |
| F_clut                                          |          0.880 | 0.686 |                34.520 |               9.997 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.680 |                34.520 |               9.984 |         25 |              0.000 |              0.000 |          0.006 |          0.009 |
| F_tgt                                           |          0.920 | 0.728 |                27.320 |              10.645 |         25 |             -0.040 |             -0.045 |         -0.042 |         -0.062 |
| F_mat                                           |          0.920 | 0.755 |                27.080 |              10.443 |         25 |             -0.040 |             -0.045 |         -0.069 |         -0.101 |
| F_light                                         |          0.840 | 0.658 |                42.720 |               9.528 |         25 |              0.040 |              0.045 |          0.028 |          0.041 |
| F_sky                                           |          0.880 | 0.663 |                34.480 |               9.995 |         25 |              0.000 |              0.000 |          0.023 |          0.034 |
| B_L1 (materials + lighting)                     |          0.920 | 0.747 |                26.800 |              10.399 |         25 |             -0.040 |             -0.045 |         -0.061 |         -0.089 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.713 |                27.760 |              10.480 |         25 |             -0.040 |             -0.045 |         -0.027 |         -0.040 |
| B_L2 (+ object appearance)                      |          0.760 | 0.607 |                58.360 |               8.334 |         25 |              0.120 |              0.136 |          0.079 |          0.115 |
| B_L3 (+ distractors)                            |          0.760 | 0.607 |                58.360 |               8.334 |         25 |              0.120 |              0.136 |          0.079 |          0.115 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_tgt: success drop -0.040 absolute, -4.5% relative · SPL drop -0.042 absolute**
- **F_mat: success drop -0.040 absolute, -4.5% relative · SPL drop -0.069 absolute**
- **F_light: success drop 0.040 absolute, 4.5% relative · SPL drop 0.028 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.023 absolute**
- **L1: success drop -0.040 absolute, -4.5% relative · SPL drop -0.061 absolute**
- **L2noT: success drop -0.040 absolute, -4.5% relative · SPL drop -0.027 absolute**
- **L2: success drop 0.120 absolute, 13.6% relative · SPL drop 0.079 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
