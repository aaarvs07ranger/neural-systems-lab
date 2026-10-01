# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.658 |                22.240 |              10.727 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.688 |                12.640 |              10.847 |         25 |              0.000 |              0.000 |         -0.030 |         -0.046 |
| F_clut                                          |          1.000 | 0.661 |                22.000 |              10.788 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_obj                                           |          0.960 | 0.619 |                30.400 |              10.226 |         25 |              0.040 |              0.040 |          0.039 |          0.059 |
| F_tgt                                           |          1.000 | 0.691 |                15.880 |              10.827 |         25 |              0.000 |              0.000 |         -0.033 |         -0.050 |
| F_mat                                           |          0.680 | 0.500 |                73.680 |               6.513 |         25 |              0.320 |              0.320 |          0.158 |          0.241 |
| F_light                                         |          0.960 | 0.655 |                28.520 |              10.304 |         25 |              0.040 |              0.040 |          0.004 |          0.006 |
| F_sky                                           |          0.920 | 0.583 |                35.920 |               9.785 |         25 |              0.080 |              0.080 |          0.076 |          0.115 |
| B_L1 (materials + lighting)                     |          0.960 | 0.646 |                42.080 |              10.089 |         25 |              0.040 |              0.040 |          0.013 |          0.019 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.607 |                50.760 |               9.068 |         25 |              0.120 |              0.120 |          0.052 |          0.078 |
| B_L2 (+ object appearance)                      |          0.880 | 0.634 |                53.880 |               9.100 |         25 |              0.120 |              0.120 |          0.025 |          0.038 |
| B_L3 (+ distractors)                            |          0.960 | 0.578 |                57.160 |               9.837 |         25 |              0.040 |              0.040 |          0.081 |          0.123 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.030 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.033 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.158 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.076 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.013 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.052 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.025 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.081 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
