# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.761 |                26.320 |              12.623 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.740 |                32.680 |              11.939 |         25 |              0.040 |              0.042 |          0.022 |          0.028 |
| F_clut                                          |          0.960 | 0.777 |                29.920 |              12.555 |         25 |              0.000 |              0.000 |         -0.016 |         -0.021 |
| F_obj                                           |          0.960 | 0.765 |                26.280 |              12.595 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_tgt                                           |          0.920 | 0.743 |                32.600 |              11.942 |         25 |              0.040 |              0.042 |          0.018 |          0.024 |
| F_mat                                           |          0.880 | 0.653 |                42.600 |              11.424 |         25 |              0.080 |              0.083 |          0.109 |          0.143 |
| F_light                                         |          0.920 | 0.730 |                33.560 |              12.012 |         25 |              0.040 |              0.042 |          0.031 |          0.041 |
| F_sky                                           |          0.960 | 0.770 |                29.440 |              12.583 |         25 |              0.000 |              0.000 |         -0.009 |         -0.011 |
| B_L1 (materials + lighting)                     |          0.880 | 0.630 |                43.600 |              11.445 |         25 |              0.080 |              0.083 |          0.132 |          0.173 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.660 |                44.240 |              12.065 |         25 |              0.040 |              0.042 |          0.102 |          0.133 |
| B_L2 (+ object appearance)                      |          0.960 | 0.691 |                36.840 |              12.548 |         25 |              0.000 |              0.000 |          0.071 |          0.093 |
| B_L3 (+ distractors)                            |          0.840 | 0.595 |                55.520 |              10.939 |         25 |              0.120 |              0.125 |          0.167 |          0.219 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_tgt: success drop 0.040 absolute, 4.2% relative · SPL drop 0.018 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.109 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L1: success drop 0.080 absolute, 8.3% relative · SPL drop 0.132 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.102 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.071 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.167 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
