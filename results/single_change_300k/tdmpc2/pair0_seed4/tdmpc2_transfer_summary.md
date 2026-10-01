# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                20.120 |              10.966 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.744 |                36.840 |              10.360 |         25 |              0.040 |              0.042 |          0.038 |          0.049 |
| F_clut                                          |          0.960 | 0.785 |                20.680 |              10.935 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          0.960 | 0.774 |                20.920 |              10.953 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |
| F_tgt                                           |          0.960 | 0.771 |                29.040 |              10.845 |         25 |              0.000 |              0.000 |          0.012 |          0.015 |
| F_mat                                           |          0.720 | 0.518 |               106.000 |               7.204 |         25 |              0.240 |              0.250 |          0.264 |          0.338 |
| F_light                                         |          0.960 | 0.781 |                21.720 |              10.923 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_sky                                           |          0.920 | 0.654 |                45.760 |              10.171 |         25 |              0.040 |              0.042 |          0.129 |          0.164 |
| B_L1 (materials + lighting)                     |          0.920 | 0.608 |                68.160 |              10.040 |         25 |              0.040 |              0.042 |          0.174 |          0.223 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.704 |                43.200 |              11.257 |         25 |             -0.040 |             -0.042 |          0.079 |          0.100 |
| B_L2 (+ object appearance)                      |          0.680 | 0.422 |               108.960 |               6.799 |         25 |              0.280 |              0.292 |          0.361 |          0.461 |
| B_L3 (+ distractors)                            |          0.480 | 0.339 |               142.920 |               4.124 |         25 |              0.480 |              0.500 |          0.444 |          0.567 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.038 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_mat: success drop 0.240 absolute, 25.0% relative · SPL drop 0.264 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.129 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.174 absolute**
- **L2noT: success drop -0.040 absolute, -4.2% relative · SPL drop 0.079 absolute**
- **L2: success drop 0.280 absolute, 29.2% relative · SPL drop 0.361 absolute**
- **L3: success drop 0.480 absolute, 50.0% relative · SPL drop 0.444 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
