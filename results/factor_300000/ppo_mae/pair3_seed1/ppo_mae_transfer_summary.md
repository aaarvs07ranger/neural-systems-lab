# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.571 |                56.720 |               9.718 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.498 |                71.640 |               8.674 |         25 |              0.080 |              0.100 |          0.073 |          0.128 |
| F_clut                                          |          0.800 | 0.573 |                56.520 |               9.760 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_obj                                           |          0.720 | 0.491 |                71.840 |               8.691 |         25 |              0.080 |              0.100 |          0.080 |          0.140 |
| F_tgt                                           |          0.840 | 0.614 |                48.840 |              10.181 |         25 |             -0.040 |             -0.050 |         -0.044 |         -0.076 |
| F_mat                                           |          0.080 | 0.038 |               184.560 |              -0.371 |         25 |              0.720 |              0.900 |          0.533 |          0.933 |
| F_light                                         |          0.840 | 0.611 |                48.800 |              10.257 |         25 |             -0.040 |             -0.050 |         -0.040 |         -0.070 |
| F_sky                                           |          0.720 | 0.534 |                68.520 |               8.350 |         25 |              0.080 |              0.100 |          0.037 |          0.065 |
| B_L1 (materials + lighting)                     |          0.200 | 0.135 |               164.320 |               0.852 |         25 |              0.600 |              0.750 |          0.436 |          0.763 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.090 |               170.120 |               0.402 |         25 |              0.640 |              0.800 |          0.481 |          0.843 |
| B_L2 (+ object appearance)                      |          0.040 | 0.025 |               192.320 |              -1.239 |         25 |              0.760 |              0.950 |          0.546 |          0.956 |
| B_L3 (+ distractors)                            |          0.040 | 0.025 |               192.320 |              -1.180 |         25 |              0.760 |              0.950 |          0.546 |          0.956 |

- **F_objall: success drop 0.080 absolute, 10.0% relative · SPL drop 0.073 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.080 absolute, 10.0% relative · SPL drop 0.080 absolute**
- **F_tgt: success drop -0.040 absolute, -5.0% relative · SPL drop -0.044 absolute**
- **F_mat: success drop 0.720 absolute, 90.0% relative · SPL drop 0.533 absolute**
- **F_light: success drop -0.040 absolute, -5.0% relative · SPL drop -0.040 absolute**
- **F_sky: success drop 0.080 absolute, 10.0% relative · SPL drop 0.037 absolute**
- **L1: success drop 0.600 absolute, 75.0% relative · SPL drop 0.436 absolute**
- **L2noT: success drop 0.640 absolute, 80.0% relative · SPL drop 0.481 absolute**
- **L2: success drop 0.760 absolute, 95.0% relative · SPL drop 0.546 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.546 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
