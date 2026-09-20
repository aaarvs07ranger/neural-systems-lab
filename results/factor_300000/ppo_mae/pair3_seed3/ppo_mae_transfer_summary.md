# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.608 |                55.480 |               9.789 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.280 | 0.224 |               147.760 |               2.678 |         25 |              0.520 |              0.650 |          0.384 |          0.632 |
| F_clut                                          |          0.800 | 0.607 |                55.600 |               9.793 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_obj                                           |          0.760 | 0.569 |                62.200 |               9.148 |         25 |              0.040 |              0.050 |          0.039 |          0.064 |
| F_tgt                                           |          0.440 | 0.363 |               120.080 |               4.914 |         25 |              0.360 |              0.450 |          0.245 |          0.403 |
| F_mat                                           |          0.360 | 0.232 |               133.160 |               3.302 |         25 |              0.440 |              0.550 |          0.376 |          0.619 |
| F_light                                         |          0.840 | 0.613 |                49.360 |              10.434 |         25 |             -0.040 |             -0.050 |         -0.005 |         -0.009 |
| F_sky                                           |          0.880 | 0.637 |                41.880 |              10.910 |         25 |             -0.080 |             -0.100 |         -0.029 |         -0.048 |
| B_L1 (materials + lighting)                     |          0.280 | 0.169 |               147.960 |               2.177 |         25 |              0.520 |              0.650 |          0.439 |          0.721 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.209 |               140.200 |               2.583 |         25 |              0.480 |              0.600 |          0.399 |          0.656 |
| B_L2 (+ object appearance)                      |          0.120 | 0.069 |               177.160 |              -0.218 |         25 |              0.680 |              0.850 |          0.539 |          0.886 |
| B_L3 (+ distractors)                            |          0.120 | 0.069 |               177.160 |              -0.219 |         25 |              0.680 |              0.850 |          0.539 |          0.886 |

- **F_objall: success drop 0.520 absolute, 65.0% relative · SPL drop 0.384 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop 0.040 absolute, 5.0% relative · SPL drop 0.039 absolute**
- **F_tgt: success drop 0.360 absolute, 45.0% relative · SPL drop 0.245 absolute**
- **F_mat: success drop 0.440 absolute, 55.0% relative · SPL drop 0.376 absolute**
- **F_light: success drop -0.040 absolute, -5.0% relative · SPL drop -0.005 absolute**
- **F_sky: success drop -0.080 absolute, -10.0% relative · SPL drop -0.029 absolute**
- **L1: success drop 0.520 absolute, 65.0% relative · SPL drop 0.439 absolute**
- **L2noT: success drop 0.480 absolute, 60.0% relative · SPL drop 0.399 absolute**
- **L2: success drop 0.680 absolute, 85.0% relative · SPL drop 0.539 absolute**
- **L3: success drop 0.680 absolute, 85.0% relative · SPL drop 0.539 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
