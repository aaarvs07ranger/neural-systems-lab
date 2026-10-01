# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.616 |                37.240 |               8.920 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.591 |                45.160 |               8.304 |         25 |              0.040 |              0.048 |          0.025 |          0.041 |
| F_clut                                          |          0.840 | 0.638 |                37.160 |               8.870 |         25 |              0.000 |              0.000 |         -0.022 |         -0.036 |
| F_obj                                           |          0.920 | 0.694 |                21.720 |               9.917 |         25 |             -0.080 |             -0.095 |         -0.078 |         -0.127 |
| F_tgt                                           |          0.960 | 0.697 |                14.440 |              10.384 |         25 |             -0.120 |             -0.143 |         -0.081 |         -0.131 |
| F_mat                                           |          0.240 | 0.240 |               152.280 |               0.967 |         25 |              0.600 |              0.714 |          0.376 |          0.611 |
| F_light                                         |          0.840 | 0.614 |                37.560 |               8.933 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_sky                                           |          0.840 | 0.616 |                37.280 |               8.924 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.240 |               0.438 |         25 |              0.640 |              0.762 |          0.416 |          0.675 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.280 |               0.877 |         25 |              0.600 |              0.714 |          0.376 |          0.611 |
| B_L2 (+ object appearance)                      |          0.160 | 0.160 |               168.200 |              -0.082 |         25 |              0.680 |              0.810 |          0.456 |          0.740 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               168.200 |              -0.082 |         25 |              0.680 |              0.810 |          0.456 |          0.740 |

- **F_objall: success drop 0.040 absolute, 4.8% relative · SPL drop 0.025 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**
- **F_obj: success drop -0.080 absolute, -9.5% relative · SPL drop -0.078 absolute**
- **F_tgt: success drop -0.120 absolute, -14.3% relative · SPL drop -0.081 absolute**
- **F_mat: success drop 0.600 absolute, 71.4% relative · SPL drop 0.376 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.640 absolute, 76.2% relative · SPL drop 0.416 absolute**
- **L2noT: success drop 0.600 absolute, 71.4% relative · SPL drop 0.376 absolute**
- **L2: success drop 0.680 absolute, 81.0% relative · SPL drop 0.456 absolute**
- **L3: success drop 0.680 absolute, 81.0% relative · SPL drop 0.456 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
