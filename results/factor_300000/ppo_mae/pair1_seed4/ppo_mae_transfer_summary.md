# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.710 |                14.160 |              10.391 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.718 |                 7.000 |              10.901 |         25 |             -0.040 |             -0.042 |         -0.008 |         -0.011 |
| F_clut                                          |          0.960 | 0.708 |                14.240 |              10.388 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_obj                                           |          0.960 | 0.710 |                14.160 |              10.394 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_tgt                                           |          1.000 | 0.720 |                 6.760 |              10.904 |         25 |             -0.040 |             -0.042 |         -0.010 |         -0.014 |
| F_mat                                           |          0.680 | 0.473 |                68.640 |               6.853 |         25 |              0.280 |              0.292 |          0.237 |          0.334 |
| F_light                                         |          0.800 | 0.600 |                45.040 |               8.411 |         25 |              0.160 |              0.167 |          0.110 |          0.154 |
| F_sky                                           |          0.920 | 0.698 |                21.640 |               9.908 |         25 |              0.040 |              0.042 |          0.011 |          0.016 |
| B_L1 (materials + lighting)                     |          0.360 | 0.330 |               129.120 |               2.435 |         25 |              0.600 |              0.625 |          0.380 |          0.535 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.330 |               129.240 |               2.440 |         25 |              0.600 |              0.625 |          0.380 |          0.535 |
| B_L2 (+ object appearance)                      |          0.160 | 0.160 |               168.200 |              -0.049 |         25 |              0.800 |              0.833 |          0.550 |          0.775 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               168.240 |              -0.030 |         25 |              0.800 |              0.833 |          0.550 |          0.775 |

- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.008 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_tgt: success drop -0.040 absolute, -4.2% relative · SPL drop -0.010 absolute**
- **F_mat: success drop 0.280 absolute, 29.2% relative · SPL drop 0.237 absolute**
- **F_light: success drop 0.160 absolute, 16.7% relative · SPL drop 0.110 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.011 absolute**
- **L1: success drop 0.600 absolute, 62.5% relative · SPL drop 0.380 absolute**
- **L2noT: success drop 0.600 absolute, 62.5% relative · SPL drop 0.380 absolute**
- **L2: success drop 0.800 absolute, 83.3% relative · SPL drop 0.550 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.550 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
