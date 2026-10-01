# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.714 |                26.920 |              12.095 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.400 | 0.349 |               124.200 |               4.119 |         25 |              0.560 |              0.583 |          0.365 |          0.511 |
| F_clut                                          |          0.960 | 0.714 |                26.920 |              12.071 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.840 | 0.626 |                47.440 |              10.311 |         25 |              0.120 |              0.125 |          0.088 |          0.124 |
| F_tgt                                           |          0.560 | 0.456 |                96.160 |               6.462 |         25 |              0.400 |              0.417 |          0.258 |          0.362 |
| F_mat                                           |          0.360 | 0.319 |               133.440 |               3.765 |         25 |              0.600 |              0.625 |          0.395 |          0.554 |
| F_light                                         |          0.960 | 0.717 |                26.840 |              12.084 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_sky                                           |          0.960 | 0.710 |                27.120 |              12.083 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| B_L1 (materials + lighting)                     |          0.280 | 0.251 |               147.200 |               2.480 |         25 |              0.680 |              0.708 |          0.464 |          0.649 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.251 |               147.240 |               2.465 |         25 |              0.680 |              0.708 |          0.464 |          0.649 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -0.712 |         25 |              0.920 |              0.958 |          0.674 |          0.944 |
| B_L3 (+ distractors)                            |          0.080 | 0.080 |               185.200 |              -0.291 |         25 |              0.880 |              0.917 |          0.634 |          0.888 |

- **F_objall: success drop 0.560 absolute, 58.3% relative · SPL drop 0.365 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.120 absolute, 12.5% relative · SPL drop 0.088 absolute**
- **F_tgt: success drop 0.400 absolute, 41.7% relative · SPL drop 0.258 absolute**
- **F_mat: success drop 0.600 absolute, 62.5% relative · SPL drop 0.395 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L1: success drop 0.680 absolute, 70.8% relative · SPL drop 0.464 absolute**
- **L2noT: success drop 0.680 absolute, 70.8% relative · SPL drop 0.464 absolute**
- **L2: success drop 0.920 absolute, 95.8% relative · SPL drop 0.674 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.634 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
