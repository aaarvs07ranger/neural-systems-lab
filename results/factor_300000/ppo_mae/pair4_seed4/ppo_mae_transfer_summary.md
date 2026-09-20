# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.723 |                26.600 |              12.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.726 |                27.560 |              12.556 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_clut                                          |          0.960 | 0.723 |                26.600 |              12.576 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.960 | 0.719 |                27.800 |              12.586 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_tgt                                           |          0.960 | 0.745 |                26.520 |              12.564 |         25 |              0.000 |              0.000 |         -0.022 |         -0.031 |
| F_mat                                           |          0.080 | 0.059 |               184.880 |              -0.101 |         25 |              0.880 |              0.917 |          0.664 |          0.919 |
| F_light                                         |          0.800 | 0.570 |                54.960 |              10.330 |         25 |              0.160 |              0.167 |          0.153 |          0.211 |
| F_sky                                           |          0.840 | 0.664 |                47.120 |              10.633 |         25 |              0.120 |              0.125 |          0.059 |          0.081 |
| B_L1 (materials + lighting)                     |          0.160 | 0.127 |               171.320 |               1.142 |         25 |              0.800 |              0.833 |          0.596 |          0.825 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.114 |               170.640 |               0.999 |         25 |              0.800 |              0.833 |          0.609 |          0.843 |
| B_L2 (+ object appearance)                      |          0.240 | 0.191 |               156.400 |               2.157 |         25 |              0.720 |              0.750 |          0.532 |          0.736 |
| B_L3 (+ distractors)                            |          0.240 | 0.191 |               156.400 |               2.206 |         25 |              0.720 |              0.750 |          0.532 |          0.736 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**
- **F_mat: success drop 0.880 absolute, 91.7% relative · SPL drop 0.664 absolute**
- **F_light: success drop 0.160 absolute, 16.7% relative · SPL drop 0.153 absolute**
- **F_sky: success drop 0.120 absolute, 12.5% relative · SPL drop 0.059 absolute**
- **L1: success drop 0.800 absolute, 83.3% relative · SPL drop 0.596 absolute**
- **L2noT: success drop 0.800 absolute, 83.3% relative · SPL drop 0.609 absolute**
- **L2: success drop 0.720 absolute, 75.0% relative · SPL drop 0.532 absolute**
- **L3: success drop 0.720 absolute, 75.0% relative · SPL drop 0.532 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
