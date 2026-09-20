# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 8.360 |              10.721 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.698 |                23.440 |               9.760 |         25 |              0.080 |              0.080 |          0.078 |          0.101 |
| F_clut                                          |          1.000 | 0.777 |                 8.440 |              10.722 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.698 |                23.440 |               9.760 |         25 |              0.080 |              0.080 |          0.078 |          0.101 |
| F_mat                                           |          0.760 | 0.540 |                54.440 |               7.821 |         25 |              0.240 |              0.240 |          0.236 |          0.304 |
| F_light                                         |          0.800 | 0.580 |                46.840 |               8.302 |         25 |              0.200 |              0.200 |          0.196 |          0.253 |
| F_sky                                           |          0.920 | 0.700 |                23.440 |               9.758 |         25 |              0.080 |              0.080 |          0.076 |          0.098 |
| B_L1 (materials + lighting)                     |          0.840 | 0.616 |                43.520 |               8.722 |         25 |              0.160 |              0.160 |          0.161 |          0.207 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.560 | 0.464 |                93.720 |               5.222 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |
| B_L2 (+ object appearance)                      |          0.560 | 0.464 |                93.720 |               5.222 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |
| B_L3 (+ distractors)                            |          0.560 | 0.464 |                93.720 |               5.222 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.078 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.078 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.236 absolute**
- **F_light: success drop 0.200 absolute, 20.0% relative · SPL drop 0.196 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.076 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.161 absolute**
- **L2noT: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
