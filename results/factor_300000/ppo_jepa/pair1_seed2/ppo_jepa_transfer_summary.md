# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.678 |                29.120 |               9.330 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.320 | 0.219 |               137.920 |               2.394 |         25 |              0.560 |              0.636 |          0.459 |          0.678 |
| F_clut                                          |          0.880 | 0.678 |                29.120 |               9.336 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.800 | 0.618 |                44.680 |               8.356 |         25 |              0.080 |              0.091 |          0.060 |          0.089 |
| F_tgt                                           |          0.480 | 0.353 |               106.840 |               4.417 |         25 |              0.400 |              0.455 |          0.325 |          0.479 |
| F_mat                                           |          0.280 | 0.250 |               144.520 |               1.673 |         25 |              0.600 |              0.682 |          0.428 |          0.631 |
| F_light                                         |          0.880 | 0.682 |                29.160 |               9.331 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_sky                                           |          0.880 | 0.678 |                29.200 |               9.335 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.240 |               0.586 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.200 | 0.200 |               160.240 |               0.418 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |

- **F_objall: success drop 0.560 absolute, 63.6% relative · SPL drop 0.459 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.080 absolute, 9.1% relative · SPL drop 0.060 absolute**
- **F_tgt: success drop 0.400 absolute, 45.5% relative · SPL drop 0.325 absolute**
- **F_mat: success drop 0.600 absolute, 68.2% relative · SPL drop 0.428 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L2noT: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
