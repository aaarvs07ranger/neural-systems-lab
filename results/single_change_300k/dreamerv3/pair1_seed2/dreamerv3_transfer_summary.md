# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.320 | 0.244 |               140.120 |               2.453 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.400 | 0.321 |               127.040 |               3.477 |         25 |             -0.080 |             -0.250 |         -0.077 |         -0.317 |
| F_clut                                          |          0.360 | 0.284 |               132.640 |               2.885 |         25 |             -0.040 |             -0.125 |         -0.040 |         -0.164 |
| F_obj                                           |          0.400 | 0.324 |               123.440 |               3.449 |         25 |             -0.080 |             -0.250 |         -0.080 |         -0.328 |
| F_tgt                                           |          0.280 | 0.208 |               147.440 |               1.983 |         25 |              0.040 |              0.125 |          0.036 |          0.148 |
| F_mat                                           |          0.600 | 0.397 |               117.160 |               5.375 |         25 |             -0.280 |             -0.875 |         -0.153 |         -0.627 |
| F_light                                         |          0.360 | 0.284 |               132.760 |               2.866 |         25 |             -0.040 |             -0.125 |         -0.040 |         -0.164 |
| F_sky                                           |          0.200 | 0.128 |               162.320 |               1.013 |         25 |              0.120 |              0.375 |          0.116 |          0.475 |
| B_L1 (materials + lighting)                     |          0.800 | 0.507 |                68.400 |               8.204 |         25 |             -0.480 |             -1.500 |         -0.263 |         -1.080 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.492 |                78.920 |               7.596 |         25 |             -0.440 |             -1.375 |         -0.248 |         -1.018 |
| B_L2 (+ object appearance)                      |          0.800 | 0.471 |                63.960 |               8.339 |         25 |             -0.480 |             -1.500 |         -0.227 |         -0.930 |
| B_L3 (+ distractors)                            |          0.560 | 0.407 |               106.800 |               5.150 |         25 |             -0.240 |             -0.750 |         -0.163 |         -0.669 |

- **F_objall: success drop -0.080 absolute, -25.0% relative · SPL drop -0.077 absolute**
- **F_clut: success drop -0.040 absolute, -12.5% relative · SPL drop -0.040 absolute**
- **F_obj: success drop -0.080 absolute, -25.0% relative · SPL drop -0.080 absolute**
- **F_tgt: success drop 0.040 absolute, 12.5% relative · SPL drop 0.036 absolute**
- **F_mat: success drop -0.280 absolute, -87.5% relative · SPL drop -0.153 absolute**
- **F_light: success drop -0.040 absolute, -12.5% relative · SPL drop -0.040 absolute**
- **F_sky: success drop 0.120 absolute, 37.5% relative · SPL drop 0.116 absolute**
- **L1: success drop -0.480 absolute, -150.0% relative · SPL drop -0.263 absolute**
- **L2noT: success drop -0.440 absolute, -137.5% relative · SPL drop -0.248 absolute**
- **L2: success drop -0.480 absolute, -150.0% relative · SPL drop -0.227 absolute**
- **L3: success drop -0.240 absolute, -75.0% relative · SPL drop -0.163 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
