# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.716 |                27.000 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.670 |                33.880 |              11.876 |         25 |              0.040 |              0.042 |          0.046 |          0.064 |
| F_clut                                          |          0.960 | 0.715 |                27.040 |              12.596 |         25 |              0.000 |              0.000 |          0.000 |          0.001 |
| F_obj                                           |          0.920 | 0.679 |                34.120 |              11.882 |         25 |              0.040 |              0.042 |          0.037 |          0.052 |
| F_tgt                                           |          0.960 | 0.724 |                26.880 |              12.561 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| F_mat                                           |          0.720 | 0.490 |                69.240 |               8.875 |         25 |              0.240 |              0.250 |          0.226 |          0.316 |
| F_light                                         |          0.800 | 0.580 |                56.440 |              10.205 |         25 |              0.160 |              0.167 |          0.136 |          0.190 |
| F_sky                                           |          0.960 | 0.738 |                27.320 |              12.583 |         25 |              0.000 |              0.000 |         -0.022 |         -0.030 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -0.609 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -0.811 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -0.648 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -0.631 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.046 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.037 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.240 absolute, 25.0% relative · SPL drop 0.226 absolute**
- **F_light: success drop 0.160 absolute, 16.7% relative · SPL drop 0.136 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**
- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**
- **L2noT: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
