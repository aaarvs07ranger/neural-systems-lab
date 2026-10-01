# PPO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.740 |                13.840 |              10.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.700 |                21.640 |               9.755 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| F_clut                                          |          0.960 | 0.740 |                13.840 |              10.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.700 |                21.640 |               9.755 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| F_mat                                           |          0.720 | 0.563 |                59.760 |               7.193 |         25 |              0.240 |              0.250 |          0.178 |          0.240 |
| F_light                                         |          0.880 | 0.660 |                29.440 |               9.203 |         25 |              0.080 |              0.083 |          0.080 |          0.108 |
| F_sky                                           |          0.960 | 0.772 |                13.880 |              10.206 |         25 |              0.000 |              0.000 |         -0.032 |         -0.043 |
| B_L1 (materials + lighting)                     |          0.760 | 0.603 |                52.320 |               7.691 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |
| B_L2 (+ object appearance)                      |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |
| B_L3 (+ distractors)                            |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.240 absolute, 25.0% relative · SPL drop 0.178 absolute**
- **F_light: success drop 0.080 absolute, 8.3% relative · SPL drop 0.080 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.032 absolute**
- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**
- **L2noT: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**
- **L2: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
