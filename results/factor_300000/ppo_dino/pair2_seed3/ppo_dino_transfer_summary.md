# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.659 |                28.960 |               9.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.659 |                29.080 |               9.252 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_clut                                          |          0.920 | 0.699 |                21.480 |               9.771 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_obj                                           |          0.880 | 0.659 |                29.080 |               9.252 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.800 | 0.580 |                44.320 |               8.142 |         25 |              0.080 |              0.091 |          0.079 |          0.120 |
| F_light                                         |          0.920 | 0.699 |                21.480 |               9.771 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_sky                                           |          0.880 | 0.659 |                28.960 |               9.255 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.574 |                51.960 |               7.610 |         25 |              0.120 |              0.136 |          0.086 |          0.130 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.512 |                74.920 |               6.090 |         25 |              0.240 |              0.273 |          0.147 |          0.224 |
| B_L2 (+ object appearance)                      |          0.640 | 0.512 |                74.920 |               6.090 |         25 |              0.240 |              0.273 |          0.147 |          0.224 |
| B_L3 (+ distractors)                            |          0.640 | 0.512 |                74.920 |               6.109 |         25 |              0.240 |              0.273 |          0.147 |          0.224 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.080 absolute, 9.1% relative · SPL drop 0.079 absolute**
- **F_light: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.120 absolute, 13.6% relative · SPL drop 0.086 absolute**
- **L2noT: success drop 0.240 absolute, 27.3% relative · SPL drop 0.147 absolute**
- **L2: success drop 0.240 absolute, 27.3% relative · SPL drop 0.147 absolute**
- **L3: success drop 0.240 absolute, 27.3% relative · SPL drop 0.147 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
