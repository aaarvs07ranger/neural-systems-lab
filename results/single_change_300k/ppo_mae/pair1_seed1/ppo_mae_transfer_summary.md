# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.700 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.679 |                14.840 |              10.413 |         25 |             -0.040 |             -0.043 |          0.021 |          0.030 |
| F_clut                                          |          0.920 | 0.698 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_obj                                           |          0.920 | 0.700 |                21.720 |               9.909 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          1.000 | 0.721 |                 6.840 |              10.898 |         25 |             -0.080 |             -0.087 |         -0.021 |         -0.030 |
| F_mat                                           |          0.480 | 0.450 |               106.240 |               3.982 |         25 |              0.440 |              0.478 |          0.250 |          0.357 |
| F_light                                         |          0.880 | 0.680 |                29.400 |               9.394 |         25 |              0.040 |              0.043 |          0.020 |          0.029 |
| F_sky                                           |          0.880 | 0.660 |                29.400 |               9.393 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               152.280 |               0.903 |         25 |              0.680 |              0.739 |          0.460 |          0.657 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.440 |               0.885 |         25 |              0.680 |              0.739 |          0.460 |          0.657 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.440 |               0.396 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.440 |               0.386 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **F_objall: success drop -0.040 absolute, -4.3% relative · SPL drop 0.021 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop -0.080 absolute, -8.7% relative · SPL drop -0.021 absolute**
- **F_mat: success drop 0.440 absolute, 47.8% relative · SPL drop 0.250 absolute**
- **F_light: success drop 0.040 absolute, 4.3% relative · SPL drop 0.020 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.680 absolute, 73.9% relative · SPL drop 0.460 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.460 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
