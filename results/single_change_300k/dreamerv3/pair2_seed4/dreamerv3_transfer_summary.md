# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.752 |                13.880 |              10.951 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.767 |                13.080 |              10.945 |         25 |              0.000 |              0.000 |         -0.015 |         -0.020 |
| F_clut                                          |          1.000 | 0.752 |                13.320 |              10.963 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.755 |                13.760 |              10.928 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_mat                                           |          0.800 | 0.599 |                76.960 |               8.103 |         25 |              0.200 |              0.200 |          0.153 |          0.204 |
| F_light                                         |          1.000 | 0.768 |                12.800 |              10.926 |         25 |              0.000 |              0.000 |         -0.015 |         -0.020 |
| F_sky                                           |          1.000 | 0.755 |                14.480 |              10.938 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| B_L1 (materials + lighting)                     |          0.640 | 0.480 |                82.080 |               6.272 |         25 |              0.360 |              0.360 |          0.272 |          0.362 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.518 |                87.160 |               6.658 |         25 |              0.320 |              0.320 |          0.234 |          0.311 |
| B_L2 (+ object appearance)                      |          0.680 | 0.548 |                75.800 |               6.730 |         25 |              0.320 |              0.320 |          0.204 |          0.271 |
| B_L3 (+ distractors)                            |          0.720 | 0.561 |                72.520 |               7.207 |         25 |              0.280 |              0.280 |          0.191 |          0.254 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.015 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.153 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.015 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.272 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.234 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.204 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.191 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
