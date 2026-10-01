# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.762 |                20.600 |              12.591 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.737 |                37.480 |              11.837 |         25 |              0.040 |              0.040 |          0.025 |          0.033 |
| F_clut                                          |          0.960 | 0.740 |                27.160 |              12.021 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| F_obj                                           |          0.960 | 0.735 |                26.760 |              11.961 |         25 |              0.040 |              0.040 |          0.027 |          0.035 |
| F_tgt                                           |          1.000 | 0.762 |                21.320 |              12.572 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.880 | 0.604 |                63.720 |              10.771 |         25 |              0.120 |              0.120 |          0.158 |          0.207 |
| F_light                                         |          1.000 | 0.760 |                20.160 |              12.599 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_sky                                           |          1.000 | 0.760 |                21.960 |              12.586 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L1 (materials + lighting)                     |          0.720 | 0.498 |                99.320 |               8.372 |         25 |              0.280 |              0.280 |          0.265 |          0.347 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.546 |                84.920 |               8.680 |         25 |              0.240 |              0.240 |          0.216 |          0.283 |
| B_L2 (+ object appearance)                      |          0.440 | 0.314 |               139.400 |               4.662 |         25 |              0.560 |              0.560 |          0.448 |          0.588 |
| B_L3 (+ distractors)                            |          0.440 | 0.318 |               134.760 |               4.976 |         25 |              0.560 |              0.560 |          0.444 |          0.583 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.027 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.158 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.265 absolute**
- **L2noT: success drop 0.240 absolute, 24.0% relative · SPL drop 0.216 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.448 absolute**
- **L3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.444 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
