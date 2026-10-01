# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.658 |                29.640 |               9.410 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.280 | 0.238 |               145.200 |               1.789 |         25 |              0.600 |              0.682 |          0.420 |          0.638 |
| F_clut                                          |          0.880 | 0.658 |                29.640 |               9.410 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.658 |                29.680 |               9.410 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_tgt                                           |          0.480 | 0.395 |               106.480 |               4.385 |         25 |              0.400 |              0.455 |          0.264 |          0.400 |
| F_mat                                           |          0.760 | 0.631 |                53.720 |               7.508 |         25 |              0.120 |              0.136 |          0.028 |          0.042 |
| F_light                                         |          0.920 | 0.698 |                21.840 |               9.897 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_sky                                           |          0.840 | 0.618 |                37.200 |               8.863 |         25 |              0.040 |              0.045 |          0.040 |          0.061 |
| B_L1 (materials + lighting)                     |          0.360 | 0.360 |               129.960 |               2.508 |         25 |              0.520 |              0.591 |          0.298 |          0.453 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.360 |               129.560 |               2.512 |         25 |              0.520 |              0.591 |          0.298 |          0.453 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.680 |              0.773 |          0.458 |          0.696 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.680 |              0.773 |          0.458 |          0.696 |

- **F_objall: success drop 0.600 absolute, 68.2% relative · SPL drop 0.420 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_tgt: success drop 0.400 absolute, 45.5% relative · SPL drop 0.264 absolute**
- **F_mat: success drop 0.120 absolute, 13.6% relative · SPL drop 0.028 absolute**
- **F_light: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.520 absolute, 59.1% relative · SPL drop 0.298 absolute**
- **L2noT: success drop 0.520 absolute, 59.1% relative · SPL drop 0.298 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.458 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.458 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
