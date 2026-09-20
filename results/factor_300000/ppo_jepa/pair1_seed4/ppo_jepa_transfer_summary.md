# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.656 |                29.560 |               9.423 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.240 | 0.240 |               152.680 |               1.309 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| F_clut                                          |          0.920 | 0.694 |                21.680 |               9.896 |         25 |             -0.040 |             -0.045 |         -0.038 |         -0.058 |
| F_obj                                           |          0.800 | 0.615 |                45.280 |               8.403 |         25 |              0.080 |              0.091 |          0.041 |          0.063 |
| F_tgt                                           |          0.600 | 0.478 |                84.320 |               6.026 |         25 |              0.280 |              0.318 |          0.178 |          0.271 |
| F_mat                                           |          0.240 | 0.240 |               152.320 |               0.937 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| F_light                                         |          0.920 | 0.700 |                21.680 |               9.891 |         25 |             -0.040 |             -0.045 |         -0.044 |         -0.067 |
| F_sky                                           |          0.880 | 0.654 |                29.520 |               9.421 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.320 |               0.907 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.280 |               0.877 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |

- **F_objall: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.038 absolute**
- **F_obj: success drop 0.080 absolute, 9.1% relative · SPL drop 0.041 absolute**
- **F_tgt: success drop 0.280 absolute, 31.8% relative · SPL drop 0.178 absolute**
- **F_mat: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **F_light: success drop -0.040 absolute, -4.5% relative · SPL drop -0.044 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L1: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **L2noT: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
