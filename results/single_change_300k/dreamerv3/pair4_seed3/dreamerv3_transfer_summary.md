# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.040 | 0.020 |               192.240 |               2.292 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.320 | 0.190 |               141.680 |               5.388 |         25 |             -0.280 |             -7.000 |         -0.170 |         -8.506 |
| F_clut                                          |          0.040 | 0.006 |               192.760 |               2.294 |         25 |              0.000 |              0.000 |          0.014 |          0.714 |
| F_obj                                           |          0.080 | 0.016 |               186.280 |               2.676 |         25 |             -0.040 |             -1.000 |          0.004 |          0.200 |
| F_tgt                                           |          0.280 | 0.190 |               148.720 |               4.970 |         25 |             -0.240 |             -6.000 |         -0.170 |         -8.478 |
| F_mat                                           |          0.560 | 0.260 |               140.960 |               7.906 |         25 |             -0.520 |            -13.000 |         -0.240 |        -12.010 |
| F_light                                         |          0.000 | 0.000 |               200.000 |               1.841 |         25 |              0.040 |              1.000 |          0.020 |          1.000 |
| F_sky                                           |          0.040 | 0.007 |               192.640 |               2.283 |         25 |              0.000 |              0.000 |          0.013 |          0.667 |
| B_L1 (materials + lighting)                     |          0.840 | 0.321 |               111.840 |              10.916 |         25 |             -0.800 |            -20.000 |         -0.301 |        -15.047 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.426 |                83.560 |              11.632 |         25 |             -0.840 |            -21.000 |         -0.406 |        -20.281 |
| B_L2 (+ object appearance)                      |          1.000 | 0.587 |                36.960 |              13.133 |         25 |             -0.960 |            -24.000 |         -0.567 |        -28.375 |
| B_L3 (+ distractors)                            |          0.880 | 0.448 |                76.480 |              11.367 |         25 |             -0.840 |            -21.000 |         -0.428 |        -21.421 |

- **F_objall: success drop -0.280 absolute, -700.0% relative · SPL drop -0.170 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.014 absolute**
- **F_obj: success drop -0.040 absolute, -100.0% relative · SPL drop 0.004 absolute**
- **F_tgt: success drop -0.240 absolute, -600.0% relative · SPL drop -0.170 absolute**
- **F_mat: success drop -0.520 absolute, -1300.0% relative · SPL drop -0.240 absolute**
- **F_light: success drop 0.040 absolute, 100.0% relative · SPL drop 0.020 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **L1: success drop -0.800 absolute, -2000.0% relative · SPL drop -0.301 absolute**
- **L2noT: success drop -0.840 absolute, -2100.0% relative · SPL drop -0.406 absolute**
- **L2: success drop -0.960 absolute, -2400.0% relative · SPL drop -0.567 absolute**
- **L3: success drop -0.840 absolute, -2100.0% relative · SPL drop -0.428 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
