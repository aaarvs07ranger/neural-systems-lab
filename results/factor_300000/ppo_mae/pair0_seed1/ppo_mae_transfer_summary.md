# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.814 |                13.280 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.752 |                27.000 |              11.009 |         25 |              0.040 |              0.040 |          0.062 |          0.077 |
| F_clut                                          |          1.000 | 0.814 |                13.240 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.774 |                20.080 |              10.972 |         25 |              0.040 |              0.040 |          0.040 |          0.049 |
| F_tgt                                           |          0.840 | 0.699 |                44.080 |               9.455 |         25 |              0.160 |              0.160 |          0.115 |          0.141 |
| F_mat                                           |          0.920 | 0.758 |                28.360 |              10.412 |         25 |              0.080 |              0.080 |          0.056 |          0.069 |
| F_light                                         |          1.000 | 0.814 |                13.080 |              11.598 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.960 | 0.781 |                20.200 |              10.992 |         25 |              0.040 |              0.040 |          0.033 |          0.041 |
| B_L1 (materials + lighting)                     |          0.800 | 0.676 |                50.960 |               8.867 |         25 |              0.200 |              0.200 |          0.139 |          0.170 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.673 |                50.880 |               8.957 |         25 |              0.200 |              0.200 |          0.141 |          0.174 |
| B_L2 (+ object appearance)                      |          0.480 | 0.406 |               109.240 |               4.876 |         25 |              0.520 |              0.520 |          0.409 |          0.502 |
| B_L3 (+ distractors)                            |          0.480 | 0.406 |               109.240 |               4.876 |         25 |              0.520 |              0.520 |          0.409 |          0.502 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.062 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **F_tgt: success drop 0.160 absolute, 16.0% relative · SPL drop 0.115 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.056 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.139 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.141 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.409 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.409 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
