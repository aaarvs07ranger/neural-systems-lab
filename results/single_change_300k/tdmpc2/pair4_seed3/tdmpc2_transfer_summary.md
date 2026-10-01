# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.754 |                26.040 |              12.601 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.739 |                31.560 |              12.391 |         25 |              0.000 |              0.000 |          0.014 |          0.019 |
| F_clut                                          |          1.000 | 0.786 |                19.200 |              13.228 |         25 |             -0.040 |             -0.042 |         -0.032 |         -0.043 |
| F_obj                                           |          0.920 | 0.701 |                38.400 |              11.704 |         25 |              0.040 |              0.042 |          0.053 |          0.070 |
| F_tgt                                           |          1.000 | 0.778 |                25.440 |              13.163 |         25 |             -0.040 |             -0.042 |         -0.025 |         -0.033 |
| F_mat                                           |          0.920 | 0.637 |                57.800 |              11.648 |         25 |              0.040 |              0.042 |          0.117 |          0.155 |
| F_light                                         |          0.920 | 0.737 |                37.720 |              11.962 |         25 |              0.040 |              0.042 |          0.017 |          0.023 |
| F_sky                                           |          0.880 | 0.679 |                40.720 |              11.459 |         25 |              0.080 |              0.083 |          0.075 |          0.099 |
| B_L1 (materials + lighting)                     |          0.800 | 0.505 |                83.800 |              10.632 |         25 |              0.160 |              0.167 |          0.248 |          0.330 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.364 |               116.520 |               8.292 |         25 |              0.280 |              0.292 |          0.390 |          0.518 |
| B_L2 (+ object appearance)                      |          0.600 | 0.330 |               121.560 |               6.993 |         25 |              0.360 |              0.375 |          0.423 |          0.562 |
| B_L3 (+ distractors)                            |          0.520 | 0.338 |               135.880 |               6.261 |         25 |              0.440 |              0.458 |          0.415 |          0.551 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.014 absolute**
- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.032 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.053 absolute**
- **F_tgt: success drop -0.040 absolute, -4.2% relative · SPL drop -0.025 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.117 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.017 absolute**
- **F_sky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.075 absolute**
- **L1: success drop 0.160 absolute, 16.7% relative · SPL drop 0.248 absolute**
- **L2noT: success drop 0.280 absolute, 29.2% relative · SPL drop 0.390 absolute**
- **L2: success drop 0.360 absolute, 37.5% relative · SPL drop 0.423 absolute**
- **L3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.415 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
