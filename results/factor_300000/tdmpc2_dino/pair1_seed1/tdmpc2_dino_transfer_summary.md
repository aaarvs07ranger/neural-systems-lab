# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.720 |                 7.400 |              10.848 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.721 |                 7.760 |              10.866 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_clut                                          |          1.000 | 0.716 |                 8.320 |              10.859 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_obj                                           |          1.000 | 0.720 |                 9.400 |              10.852 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          1.000 | 0.716 |                 8.520 |              10.882 |         25 |              0.000 |              0.000 |          0.003 |          0.005 |
| F_mat                                           |          0.960 | 0.665 |                22.160 |              10.293 |         25 |              0.040 |              0.040 |          0.055 |          0.076 |
| F_light                                         |          1.000 | 0.712 |                 9.920 |              10.867 |         25 |              0.000 |              0.000 |          0.007 |          0.010 |
| F_sky                                           |          1.000 | 0.714 |                 8.280 |              10.879 |         25 |              0.000 |              0.000 |          0.005 |          0.008 |
| B_L1 (materials + lighting)                     |          0.960 | 0.676 |                22.800 |              10.285 |         25 |              0.040 |              0.040 |          0.044 |          0.061 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.680 |                21.520 |              10.321 |         25 |              0.040 |              0.040 |          0.040 |          0.055 |
| B_L2 (+ object appearance)                      |          0.960 | 0.690 |                20.840 |              10.327 |         25 |              0.040 |              0.040 |          0.030 |          0.042 |
| B_L3 (+ distractors)                            |          0.920 | 0.640 |                31.800 |               9.747 |         25 |              0.080 |              0.080 |          0.080 |          0.111 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.055 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.044 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
