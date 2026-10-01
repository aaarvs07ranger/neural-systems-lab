# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 8.160 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.697 |                23.560 |               9.741 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| F_clut                                          |          1.000 | 0.777 |                 8.160 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.697 |                23.560 |               9.741 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| F_mat                                           |          0.680 | 0.485 |                70.680 |               6.838 |         25 |              0.320 |              0.320 |          0.291 |          0.375 |
| F_light                                         |          1.000 | 0.780 |                 8.240 |              10.719 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_sky                                           |          0.920 | 0.697 |                23.520 |               9.747 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| B_L1 (materials + lighting)                     |          0.560 | 0.533 |                93.080 |               5.194 |         25 |              0.440 |              0.440 |          0.243 |          0.313 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.613 |                78.880 |               6.146 |         25 |              0.360 |              0.360 |          0.163 |          0.210 |
| B_L2 (+ object appearance)                      |          0.640 | 0.613 |                78.880 |               6.146 |         25 |              0.360 |              0.360 |          0.163 |          0.210 |
| B_L3 (+ distractors)                            |          0.640 | 0.613 |                78.880 |               6.146 |         25 |              0.360 |              0.360 |          0.163 |          0.210 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.291 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **L1: success drop 0.440 absolute, 44.0% relative · SPL drop 0.243 absolute**
- **L2noT: success drop 0.360 absolute, 36.0% relative · SPL drop 0.163 absolute**
- **L2: success drop 0.360 absolute, 36.0% relative · SPL drop 0.163 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.163 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
