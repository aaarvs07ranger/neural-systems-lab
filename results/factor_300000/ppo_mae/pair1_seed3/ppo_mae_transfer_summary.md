# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.690 |                24.320 |               9.867 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.674 |                25.160 |               9.826 |         25 |              0.000 |              0.000 |          0.016 |          0.022 |
| F_clut                                          |          0.920 | 0.692 |                24.440 |               9.866 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_obj                                           |          0.920 | 0.690 |                24.360 |               9.866 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          0.960 | 0.699 |                17.280 |              10.319 |         25 |             -0.040 |             -0.043 |         -0.010 |         -0.014 |
| F_mat                                           |          0.800 | 0.643 |                48.440 |               8.187 |         25 |              0.120 |              0.130 |          0.047 |          0.068 |
| F_light                                         |          0.920 | 0.698 |                24.360 |               9.861 |         25 |              0.000 |              0.000 |         -0.009 |         -0.013 |
| F_sky                                           |          0.920 | 0.690 |                24.360 |               9.869 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               153.000 |               0.870 |         25 |              0.680 |              0.739 |          0.450 |          0.652 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               153.000 |               0.900 |         25 |              0.680 |              0.739 |          0.450 |          0.652 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.490 |          0.710 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.490 |          0.710 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.016 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop -0.040 absolute, -4.3% relative · SPL drop -0.010 absolute**
- **F_mat: success drop 0.120 absolute, 13.0% relative · SPL drop 0.047 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.450 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.450 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.490 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.490 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
