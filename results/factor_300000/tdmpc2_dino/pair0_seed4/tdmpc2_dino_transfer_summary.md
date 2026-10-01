# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.778 |                22.400 |              10.921 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.770 |                21.120 |              10.908 |         25 |              0.000 |              0.000 |          0.008 |          0.010 |
| F_clut                                          |          0.920 | 0.757 |                27.040 |              10.444 |         25 |              0.040 |              0.042 |          0.021 |          0.027 |
| F_obj                                           |          0.920 | 0.740 |                27.600 |              10.428 |         25 |              0.040 |              0.042 |          0.038 |          0.049 |
| F_tgt                                           |          0.960 | 0.792 |                19.000 |              10.944 |         25 |              0.000 |              0.000 |         -0.014 |         -0.018 |
| F_mat                                           |          0.960 | 0.784 |                23.640 |              11.032 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_light                                         |          0.920 | 0.761 |                26.800 |              10.441 |         25 |              0.040 |              0.042 |          0.017 |          0.022 |
| F_sky                                           |          0.960 | 0.790 |                19.480 |              11.078 |         25 |              0.000 |              0.000 |         -0.012 |         -0.015 |
| B_L1 (materials + lighting)                     |          0.920 | 0.757 |                28.280 |              10.485 |         25 |              0.040 |              0.042 |          0.020 |          0.026 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.747 |                32.720 |              10.416 |         25 |              0.040 |              0.042 |          0.031 |          0.040 |
| B_L2 (+ object appearance)                      |          0.840 | 0.693 |                46.520 |               9.272 |         25 |              0.120 |              0.125 |          0.085 |          0.109 |
| B_L3 (+ distractors)                            |          0.840 | 0.699 |                57.520 |               9.201 |         25 |              0.120 |              0.125 |          0.079 |          0.101 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.021 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.038 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.014 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.017 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.020 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **L2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.085 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
