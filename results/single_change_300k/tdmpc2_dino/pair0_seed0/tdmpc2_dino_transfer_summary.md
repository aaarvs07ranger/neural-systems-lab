# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.822 |                11.160 |              11.596 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.768 |                34.240 |              10.393 |         25 |              0.080 |              0.080 |          0.054 |          0.066 |
| F_clut                                          |          0.960 | 0.785 |                18.560 |              10.964 |         25 |              0.040 |              0.040 |          0.037 |          0.045 |
| F_obj                                           |          0.960 | 0.779 |                19.600 |              10.949 |         25 |              0.040 |              0.040 |          0.043 |          0.052 |
| F_tgt                                           |          0.960 | 0.791 |                19.200 |              10.930 |         25 |              0.040 |              0.040 |          0.031 |          0.038 |
| F_mat                                           |          0.920 | 0.756 |                26.360 |              10.464 |         25 |              0.080 |              0.080 |          0.066 |          0.080 |
| F_light                                         |          1.000 | 0.825 |                14.080 |              11.552 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_sky                                           |          0.960 | 0.786 |                17.880 |              10.974 |         25 |              0.040 |              0.040 |          0.036 |          0.044 |
| B_L1 (materials + lighting)                     |          0.960 | 0.790 |                19.560 |              11.072 |         25 |              0.040 |              0.040 |          0.032 |          0.039 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.753 |                34.360 |              10.325 |         25 |              0.080 |              0.080 |          0.070 |          0.085 |
| B_L2 (+ object appearance)                      |          0.920 | 0.752 |                33.320 |              10.365 |         25 |              0.080 |              0.080 |          0.070 |          0.085 |
| B_L3 (+ distractors)                            |          0.880 | 0.711 |                38.040 |               9.908 |         25 |              0.120 |              0.120 |          0.112 |          0.136 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.054 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.037 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**
- **F_tgt: success drop 0.040 absolute, 4.0% relative · SPL drop 0.031 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.066 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.032 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.070 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.070 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.112 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
