# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.796 |                13.240 |              11.582 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.802 |                12.920 |              11.578 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_clut                                          |          1.000 | 0.786 |                14.280 |              11.560 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| F_obj                                           |          1.000 | 0.788 |                15.760 |              11.556 |         25 |              0.000 |              0.000 |          0.009 |          0.011 |
| F_tgt                                           |          1.000 | 0.798 |                14.040 |              11.562 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_mat                                           |          1.000 | 0.770 |                20.160 |              11.492 |         25 |              0.000 |              0.000 |          0.026 |          0.033 |
| F_light                                         |          0.960 | 0.756 |                21.520 |              11.078 |         25 |              0.040 |              0.040 |          0.041 |          0.051 |
| F_sky                                           |          0.960 | 0.672 |                35.120 |              10.949 |         25 |              0.040 |              0.040 |          0.124 |          0.156 |
| B_L1 (materials + lighting)                     |          1.000 | 0.686 |                28.160 |              11.392 |         25 |              0.000 |              0.000 |          0.110 |          0.139 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.593 |                41.280 |              10.769 |         25 |              0.040 |              0.040 |          0.204 |          0.256 |
| B_L2 (+ object appearance)                      |          0.960 | 0.517 |                70.280 |              10.544 |         25 |              0.040 |              0.040 |          0.280 |          0.351 |
| B_L3 (+ distractors)                            |          0.920 | 0.524 |                70.240 |              10.113 |         25 |              0.080 |              0.080 |          0.273 |          0.343 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.026 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.124 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.110 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.204 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.280 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.273 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
