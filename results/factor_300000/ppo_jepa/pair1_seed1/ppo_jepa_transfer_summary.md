# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.656 |                29.280 |               9.389 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.560 | 0.455 |                91.320 |               5.205 |         25 |              0.320 |              0.364 |          0.201 |          0.307 |
| F_clut                                          |          0.920 | 0.694 |                21.720 |               9.900 |         25 |             -0.040 |             -0.045 |         -0.038 |         -0.058 |
| F_obj                                           |          0.760 | 0.560 |                52.560 |               7.921 |         25 |              0.120 |              0.136 |          0.096 |          0.146 |
| F_tgt                                           |          0.920 | 0.658 |                22.480 |               9.860 |         25 |             -0.040 |             -0.045 |         -0.002 |         -0.002 |
| F_mat                                           |          0.400 | 0.323 |               121.640 |               3.034 |         25 |              0.480 |              0.545 |          0.333 |          0.508 |
| F_light                                         |          0.920 | 0.700 |                21.680 |               9.889 |         25 |             -0.040 |             -0.045 |         -0.044 |         -0.067 |
| F_sky                                           |          0.920 | 0.696 |                21.640 |               9.891 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| B_L1 (materials + lighting)                     |          0.320 | 0.300 |               136.720 |               1.882 |         25 |              0.560 |              0.636 |          0.356 |          0.543 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.280 |               144.480 |               1.365 |         25 |              0.600 |              0.682 |          0.376 |          0.573 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.456 |          0.695 |

- **F_objall: success drop 0.320 absolute, 36.4% relative · SPL drop 0.201 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.038 absolute**
- **F_obj: success drop 0.120 absolute, 13.6% relative · SPL drop 0.096 absolute**
- **F_tgt: success drop -0.040 absolute, -4.5% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.480 absolute, 54.5% relative · SPL drop 0.333 absolute**
- **F_light: success drop -0.040 absolute, -4.5% relative · SPL drop -0.044 absolute**
- **F_sky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **L1: success drop 0.560 absolute, 63.6% relative · SPL drop 0.356 absolute**
- **L2noT: success drop 0.600 absolute, 68.2% relative · SPL drop 0.376 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.456 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
