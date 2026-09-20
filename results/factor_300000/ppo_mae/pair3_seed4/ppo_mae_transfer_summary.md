# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.632 |                49.280 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.320 | 0.231 |               141.640 |               3.627 |         25 |              0.520 |              0.619 |          0.401 |          0.634 |
| F_clut                                          |          0.840 | 0.632 |                49.280 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.720 | 0.544 |                70.520 |               8.559 |         25 |              0.120 |              0.143 |          0.088 |          0.139 |
| F_tgt                                           |          0.400 | 0.297 |               126.640 |               4.945 |         25 |              0.440 |              0.524 |          0.335 |          0.530 |
| F_mat                                           |          0.000 | 0.000 |               200.000 |              -1.980 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| F_light                                         |          0.760 | 0.585 |                62.760 |               9.163 |         25 |              0.080 |              0.095 |          0.046 |          0.073 |
| F_sky                                           |          0.800 | 0.583 |                58.240 |               9.787 |         25 |              0.040 |              0.048 |          0.049 |          0.077 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.873 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.963 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.986 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.986 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |

- **F_objall: success drop 0.520 absolute, 61.9% relative · SPL drop 0.401 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.120 absolute, 14.3% relative · SPL drop 0.088 absolute**
- **F_tgt: success drop 0.440 absolute, 52.4% relative · SPL drop 0.335 absolute**
- **F_mat: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **F_light: success drop 0.080 absolute, 9.5% relative · SPL drop 0.046 absolute**
- **F_sky: success drop 0.040 absolute, 4.8% relative · SPL drop 0.049 absolute**
- **L1: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L2noT: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L2: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
