# PPO_AUG zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.785 |                17.720 |              10.972 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.484 |                86.760 |               6.557 |         25 |              0.360 |              0.375 |          0.302 |          0.384 |
| F_clut                                          |          0.960 | 0.785 |                17.720 |              10.972 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.742 |                25.680 |              10.491 |         25 |              0.040 |              0.042 |          0.043 |          0.055 |
| F_tgt                                           |          0.760 | 0.609 |                56.640 |               8.542 |         25 |              0.200 |              0.208 |          0.176 |          0.224 |
| F_mat                                           |          0.840 | 0.705 |                40.920 |               9.477 |         25 |              0.120 |              0.125 |          0.080 |          0.102 |
| F_light                                         |          0.960 | 0.785 |                17.720 |              10.972 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.743 |                25.680 |              10.509 |         25 |              0.040 |              0.042 |          0.043 |          0.055 |
| B_L1 (materials + lighting)                     |          0.760 | 0.610 |                55.800 |               8.262 |         25 |              0.200 |              0.208 |          0.176 |          0.224 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.520 | 0.412 |               100.480 |               4.950 |         25 |              0.440 |              0.458 |          0.373 |          0.475 |
| B_L2 (+ object appearance)                      |          0.120 | 0.093 |               176.920 |               0.097 |         25 |              0.840 |              0.875 |          0.692 |          0.881 |
| B_L3 (+ distractors)                            |          0.120 | 0.093 |               176.920 |               0.119 |         25 |              0.840 |              0.875 |          0.692 |          0.881 |

- **F_objall: success drop 0.360 absolute, 37.5% relative · SPL drop 0.302 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.043 absolute**
- **F_tgt: success drop 0.200 absolute, 20.8% relative · SPL drop 0.176 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.080 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.043 absolute**
- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.176 absolute**
- **L2noT: success drop 0.440 absolute, 45.8% relative · SPL drop 0.373 absolute**
- **L2: success drop 0.840 absolute, 87.5% relative · SPL drop 0.692 absolute**
- **L3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.692 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
