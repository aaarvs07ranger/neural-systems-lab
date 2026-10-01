# PPO_MAE zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.692 |                21.680 |               9.913 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.718 |                 6.920 |              10.894 |         25 |             -0.080 |             -0.087 |         -0.025 |         -0.037 |
| F_clut                                          |          0.960 | 0.704 |                14.120 |              10.376 |         25 |             -0.040 |             -0.043 |         -0.012 |         -0.017 |
| F_obj                                           |          0.920 | 0.692 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          1.000 | 0.719 |                 6.880 |              10.903 |         25 |             -0.080 |             -0.087 |         -0.027 |         -0.039 |
| F_mat                                           |          0.400 | 0.373 |               121.160 |               3.038 |         25 |              0.520 |              0.565 |          0.319 |          0.461 |
| F_light                                         |          0.840 | 0.620 |                37.360 |               8.934 |         25 |              0.080 |              0.087 |          0.072 |          0.104 |
| F_sky                                           |          0.880 | 0.652 |                29.400 |               9.389 |         25 |              0.040 |              0.043 |          0.040 |          0.058 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.240 |               0.428 |         25 |              0.720 |              0.783 |          0.492 |          0.711 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.240 |               152.480 |               0.905 |         25 |              0.680 |              0.739 |          0.452 |          0.653 |
| B_L2 (+ object appearance)                      |          0.160 | 0.160 |               168.400 |              -0.084 |         25 |              0.760 |              0.826 |          0.532 |          0.769 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.520 |               0.386 |         25 |              0.720 |              0.783 |          0.492 |          0.711 |

- **F_objall: success drop -0.080 absolute, -8.7% relative · SPL drop -0.025 absolute**
- **F_clut: success drop -0.040 absolute, -4.3% relative · SPL drop -0.012 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop -0.080 absolute, -8.7% relative · SPL drop -0.027 absolute**
- **F_mat: success drop 0.520 absolute, 56.5% relative · SPL drop 0.319 absolute**
- **F_light: success drop 0.080 absolute, 8.7% relative · SPL drop 0.072 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.492 absolute**
- **L2noT: success drop 0.680 absolute, 73.9% relative · SPL drop 0.452 absolute**
- **L2: success drop 0.760 absolute, 82.6% relative · SPL drop 0.532 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.492 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
