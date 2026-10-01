# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.789 |                18.040 |              10.966 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.782 |                20.960 |              10.913 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| F_clut                                          |          0.960 | 0.789 |                18.240 |              10.962 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.780 |                23.840 |              10.911 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |
| F_tgt                                           |          0.960 | 0.792 |                18.680 |              10.942 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_mat                                           |          0.960 | 0.774 |                19.120 |              10.953 |         25 |              0.000 |              0.000 |          0.015 |          0.019 |
| F_light                                         |          1.000 | 0.817 |                11.520 |              11.590 |         25 |             -0.040 |             -0.042 |         -0.028 |         -0.036 |
| F_sky                                           |          0.960 | 0.789 |                18.360 |              10.958 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.747 |                28.680 |              10.405 |         25 |              0.040 |              0.042 |          0.042 |          0.053 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.753 |                24.080 |              10.910 |         25 |              0.000 |              0.000 |          0.036 |          0.046 |
| B_L2 (+ object appearance)                      |          0.880 | 0.705 |                46.160 |               9.758 |         25 |              0.080 |              0.083 |          0.083 |          0.106 |
| B_L3 (+ distractors)                            |          0.880 | 0.678 |                42.480 |               9.841 |         25 |              0.080 |              0.083 |          0.111 |          0.140 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **F_light: success drop -0.040 absolute, -4.2% relative · SPL drop -0.028 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.042 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.036 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.083 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.111 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
