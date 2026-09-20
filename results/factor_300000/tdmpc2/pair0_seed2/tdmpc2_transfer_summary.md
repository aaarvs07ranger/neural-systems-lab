# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.815 |                12.000 |              11.592 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.793 |                23.680 |              11.470 |         25 |              0.000 |              0.000 |          0.021 |          0.026 |
| F_clut                                          |          1.000 | 0.818 |                12.720 |              11.571 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_obj                                           |          1.000 | 0.814 |                11.520 |              11.604 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_tgt                                           |          1.000 | 0.808 |                23.320 |              11.463 |         25 |              0.000 |              0.000 |          0.006 |          0.008 |
| F_mat                                           |          0.960 | 0.744 |                41.400 |              10.886 |         25 |              0.040 |              0.040 |          0.071 |          0.087 |
| F_light                                         |          0.960 | 0.792 |                19.520 |              11.076 |         25 |              0.040 |              0.040 |          0.023 |          0.028 |
| F_sky                                           |          0.680 | 0.502 |                88.960 |               6.797 |         25 |              0.320 |              0.320 |          0.313 |          0.384 |
| B_L1 (materials + lighting)                     |          0.960 | 0.618 |                50.600 |              10.689 |         25 |              0.040 |              0.040 |          0.196 |          0.241 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.605 |                55.320 |              10.139 |         25 |              0.080 |              0.080 |          0.210 |          0.258 |
| B_L2 (+ object appearance)                      |          0.960 | 0.604 |                59.080 |              10.542 |         25 |              0.040 |              0.040 |          0.211 |          0.259 |
| B_L3 (+ distractors)                            |          0.880 | 0.565 |                70.840 |               9.475 |         25 |              0.120 |              0.120 |          0.250 |          0.307 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.071 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_sky: success drop 0.320 absolute, 32.0% relative · SPL drop 0.313 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.196 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.210 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.211 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.250 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
