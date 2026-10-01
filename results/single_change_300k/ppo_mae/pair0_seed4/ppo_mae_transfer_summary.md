# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                19.960 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.782 |                21.040 |              10.946 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_clut                                          |          0.960 | 0.783 |                19.960 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.774 |                19.960 |              10.944 |         25 |              0.000 |              0.000 |          0.009 |          0.011 |
| F_tgt                                           |          0.960 | 0.792 |                20.160 |              10.936 |         25 |              0.000 |              0.000 |         -0.009 |         -0.011 |
| F_mat                                           |          0.920 | 0.761 |                27.680 |              10.426 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| F_light                                         |          1.000 | 0.814 |                13.520 |              11.584 |         25 |             -0.040 |             -0.042 |         -0.031 |         -0.040 |
| F_sky                                           |          0.960 | 0.762 |                20.360 |              10.978 |         25 |              0.000 |              0.000 |          0.021 |          0.027 |
| B_L1 (materials + lighting)                     |          0.920 | 0.761 |                28.200 |              10.441 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.755 |                28.040 |              10.444 |         25 |              0.040 |              0.042 |          0.028 |          0.036 |
| B_L2 (+ object appearance)                      |          0.640 | 0.536 |                81.800 |               6.787 |         25 |              0.320 |              0.333 |          0.247 |          0.315 |
| B_L3 (+ distractors)                            |          0.640 | 0.536 |                82.280 |               6.782 |         25 |              0.320 |              0.333 |          0.247 |          0.315 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_light: success drop -0.040 absolute, -4.2% relative · SPL drop -0.031 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.028 absolute**
- **L2: success drop 0.320 absolute, 33.3% relative · SPL drop 0.247 absolute**
- **L3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.247 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
