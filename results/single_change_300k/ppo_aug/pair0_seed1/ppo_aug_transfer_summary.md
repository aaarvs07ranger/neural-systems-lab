# PPO_AUG zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.771 |                19.920 |              11.092 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.680 | 0.541 |                72.760 |               7.680 |         25 |              0.280 |              0.292 |          0.230 |          0.299 |
| F_clut                                          |          0.960 | 0.771 |                19.920 |              11.092 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.777 |                19.280 |              11.090 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_tgt                                           |          0.640 | 0.524 |                80.040 |               7.178 |         25 |              0.320 |              0.333 |          0.248 |          0.321 |
| F_mat                                           |          0.800 | 0.631 |                51.000 |               8.711 |         25 |              0.160 |              0.167 |          0.140 |          0.182 |
| F_light                                         |          0.960 | 0.775 |                19.720 |              11.102 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_sky                                           |          0.920 | 0.734 |                27.760 |              10.619 |         25 |              0.040 |              0.042 |          0.037 |          0.048 |
| B_L1 (materials + lighting)                     |          0.440 | 0.348 |               116.840 |               4.045 |         25 |              0.520 |              0.542 |          0.423 |          0.549 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.377 |               110.080 |               4.517 |         25 |              0.480 |              0.500 |          0.395 |          0.511 |
| B_L2 (+ object appearance)                      |          0.280 | 0.191 |               149.360 |               1.869 |         25 |              0.680 |              0.708 |          0.581 |          0.752 |
| B_L3 (+ distractors)                            |          0.280 | 0.191 |               149.360 |               1.869 |         25 |              0.680 |              0.708 |          0.581 |          0.752 |

- **F_objall: success drop 0.280 absolute, 29.2% relative · SPL drop 0.230 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_tgt: success drop 0.320 absolute, 33.3% relative · SPL drop 0.248 absolute**
- **F_mat: success drop 0.160 absolute, 16.7% relative · SPL drop 0.140 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.037 absolute**
- **L1: success drop 0.520 absolute, 54.2% relative · SPL drop 0.423 absolute**
- **L2noT: success drop 0.480 absolute, 50.0% relative · SPL drop 0.395 absolute**
- **L2: success drop 0.680 absolute, 70.8% relative · SPL drop 0.581 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.581 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
