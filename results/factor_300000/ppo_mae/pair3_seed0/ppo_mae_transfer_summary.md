# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.751 |                20.600 |              12.579 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.552 |                69.280 |               8.801 |         25 |              0.280 |              0.280 |          0.199 |          0.265 |
| F_clut                                          |          1.000 | 0.749 |                20.680 |              12.583 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_obj                                           |          0.960 | 0.735 |                27.480 |              11.978 |         25 |              0.040 |              0.040 |          0.015 |          0.021 |
| F_tgt                                           |          0.760 | 0.588 |                62.120 |               9.323 |         25 |              0.240 |              0.240 |          0.163 |          0.217 |
| F_mat                                           |          0.600 | 0.453 |                89.320 |               6.154 |         25 |              0.400 |              0.400 |          0.298 |          0.397 |
| F_light                                         |          1.000 | 0.750 |                20.560 |              12.575 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.960 | 0.705 |                29.040 |              12.079 |         25 |              0.040 |              0.040 |          0.045 |          0.060 |
| B_L1 (materials + lighting)                     |          0.640 | 0.469 |                82.120 |               6.892 |         25 |              0.360 |              0.360 |          0.282 |          0.375 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.426 |                89.520 |               6.449 |         25 |              0.400 |              0.400 |          0.325 |          0.433 |
| B_L2 (+ object appearance)                      |          0.480 | 0.365 |               111.520 |               5.007 |         25 |              0.520 |              0.520 |          0.386 |          0.514 |
| B_L3 (+ distractors)                            |          0.480 | 0.365 |               111.520 |               5.007 |         25 |              0.520 |              0.520 |          0.386 |          0.514 |

- **F_objall: success drop 0.280 absolute, 28.0% relative · SPL drop 0.199 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.015 absolute**
- **F_tgt: success drop 0.240 absolute, 24.0% relative · SPL drop 0.163 absolute**
- **F_mat: success drop 0.400 absolute, 40.0% relative · SPL drop 0.298 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.045 absolute**
- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.282 absolute**
- **L2noT: success drop 0.400 absolute, 40.0% relative · SPL drop 0.325 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.386 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.386 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
