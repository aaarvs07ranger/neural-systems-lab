# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.776 |                18.800 |              13.228 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.755 |                25.920 |              12.592 |         25 |              0.040 |              0.040 |          0.021 |          0.027 |
| F_clut                                          |          1.000 | 0.772 |                23.120 |              13.185 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_obj                                           |          0.960 | 0.753 |                27.520 |              12.582 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| F_tgt                                           |          0.960 | 0.758 |                25.560 |              12.612 |         25 |              0.040 |              0.040 |          0.018 |          0.023 |
| F_mat                                           |          0.760 | 0.576 |                68.720 |               9.543 |         25 |              0.240 |              0.240 |          0.200 |          0.257 |
| F_light                                         |          0.960 | 0.782 |                27.160 |              12.573 |         25 |              0.040 |              0.040 |         -0.006 |         -0.008 |
| F_sky                                           |          1.000 | 0.796 |                22.280 |              13.197 |         25 |              0.000 |              0.000 |         -0.020 |         -0.026 |
| B_L1 (materials + lighting)                     |          0.880 | 0.656 |                50.560 |              11.402 |         25 |              0.120 |              0.120 |          0.120 |          0.155 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.524 |                64.720 |              10.326 |         25 |              0.200 |              0.200 |          0.252 |          0.325 |
| B_L2 (+ object appearance)                      |          0.920 | 0.658 |                56.200 |              11.764 |         25 |              0.080 |              0.080 |          0.118 |          0.152 |
| B_L3 (+ distractors)                            |          0.800 | 0.530 |                79.360 |              10.101 |         25 |              0.200 |              0.200 |          0.246 |          0.316 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.021 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_tgt: success drop 0.040 absolute, 4.0% relative · SPL drop 0.018 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.200 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.020 absolute**
- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.252 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.118 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.246 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
