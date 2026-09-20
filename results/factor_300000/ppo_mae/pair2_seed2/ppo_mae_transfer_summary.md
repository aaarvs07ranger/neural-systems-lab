# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 8.440 |              10.720 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.618 |                38.640 |               8.784 |         25 |              0.160 |              0.160 |          0.158 |          0.204 |
| F_clut                                          |          1.000 | 0.777 |                 8.440 |              10.720 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.840 | 0.618 |                38.640 |               8.784 |         25 |              0.160 |              0.160 |          0.158 |          0.204 |
| F_mat                                           |          0.040 | 0.040 |               192.040 |              -1.454 |         25 |              0.960 |              0.960 |          0.737 |          0.949 |
| F_light                                         |          0.680 | 0.460 |                70.120 |               6.849 |         25 |              0.320 |              0.320 |          0.316 |          0.407 |
| F_sky                                           |          0.800 | 0.578 |                46.760 |               8.298 |         25 |              0.200 |              0.200 |          0.198 |          0.255 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.737 |          0.949 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.737 |          0.949 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.737 |          0.949 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.737 |          0.949 |

- **F_objall: success drop 0.160 absolute, 16.0% relative · SPL drop 0.158 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.160 absolute, 16.0% relative · SPL drop 0.158 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.737 absolute**
- **F_light: success drop 0.320 absolute, 32.0% relative · SPL drop 0.316 absolute**
- **F_sky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.198 absolute**
- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.737 absolute**
- **L2noT: success drop 0.960 absolute, 96.0% relative · SPL drop 0.737 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.737 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.737 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
