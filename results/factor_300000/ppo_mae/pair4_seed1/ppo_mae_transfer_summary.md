# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.706 |                33.600 |              11.997 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.686 |                34.120 |              11.978 |         25 |              0.000 |              0.000 |          0.021 |          0.029 |
| F_clut                                          |          0.880 | 0.669 |                40.800 |              11.398 |         25 |              0.040 |              0.043 |          0.037 |          0.053 |
| F_obj                                           |          0.920 | 0.673 |                34.120 |              12.003 |         25 |              0.000 |              0.000 |          0.033 |          0.047 |
| F_tgt                                           |          0.960 | 0.744 |                26.480 |              12.545 |         25 |             -0.040 |             -0.043 |         -0.038 |         -0.054 |
| F_mat                                           |          0.360 | 0.260 |               132.960 |               3.861 |         25 |              0.560 |              0.609 |          0.446 |          0.632 |
| F_light                                         |          0.600 | 0.419 |                90.880 |               7.722 |         25 |              0.320 |              0.348 |          0.287 |          0.406 |
| F_sky                                           |          0.760 | 0.569 |                62.200 |               9.807 |         25 |              0.160 |              0.174 |          0.137 |          0.194 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.458 |         25 |              0.920 |              1.000 |          0.706 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.954 |         25 |              0.920 |              1.000 |          0.706 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.898 |         25 |              0.920 |              1.000 |          0.706 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.925 |         25 |              0.920 |              1.000 |          0.706 |          1.000 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.037 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.033 absolute**
- **F_tgt: success drop -0.040 absolute, -4.3% relative · SPL drop -0.038 absolute**
- **F_mat: success drop 0.560 absolute, 60.9% relative · SPL drop 0.446 absolute**
- **F_light: success drop 0.320 absolute, 34.8% relative · SPL drop 0.287 absolute**
- **F_sky: success drop 0.160 absolute, 17.4% relative · SPL drop 0.137 absolute**
- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.706 absolute**
- **L2noT: success drop 0.920 absolute, 100.0% relative · SPL drop 0.706 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.706 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.706 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
