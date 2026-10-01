# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.520 | 0.400 |               102.400 |               5.349 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.520 | 0.404 |               102.160 |               5.325 |         25 |              0.000 |              0.000 |         -0.005 |         -0.012 |
| F_clut                                          |          0.520 | 0.400 |               102.360 |               5.344 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.480 | 0.363 |               109.760 |               4.840 |         25 |              0.040 |              0.077 |          0.037 |          0.092 |
| F_tgt                                           |          0.520 | 0.404 |               102.440 |               5.335 |         25 |              0.000 |              0.000 |         -0.005 |         -0.012 |
| F_mat                                           |          0.400 | 0.302 |               126.240 |               3.731 |         25 |              0.120 |              0.231 |          0.097 |          0.243 |
| F_light                                         |          0.520 | 0.403 |               102.280 |               5.345 |         25 |              0.000 |              0.000 |         -0.003 |         -0.009 |
| F_sky                                           |          0.480 | 0.357 |               109.880 |               4.863 |         25 |              0.040 |              0.077 |          0.042 |          0.106 |
| B_L1 (materials + lighting)                     |          0.280 | 0.217 |               147.920 |               2.146 |         25 |              0.240 |              0.462 |          0.182 |          0.456 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.097 |               169.920 |               0.533 |         25 |              0.360 |              0.692 |          0.302 |          0.756 |
| B_L2 (+ object appearance)                      |          0.480 | 0.382 |               111.960 |               4.679 |         25 |              0.040 |              0.077 |          0.018 |          0.044 |
| B_L3 (+ distractors)                            |          0.520 | 0.422 |               104.360 |               5.199 |         25 |              0.000 |              0.000 |         -0.022 |         -0.056 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 7.7% relative · SPL drop 0.037 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.120 absolute, 23.1% relative · SPL drop 0.097 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.040 absolute, 7.7% relative · SPL drop 0.042 absolute**
- **L1: success drop 0.240 absolute, 46.2% relative · SPL drop 0.182 absolute**
- **L2noT: success drop 0.360 absolute, 69.2% relative · SPL drop 0.302 absolute**
- **L2: success drop 0.040 absolute, 7.7% relative · SPL drop 0.018 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
