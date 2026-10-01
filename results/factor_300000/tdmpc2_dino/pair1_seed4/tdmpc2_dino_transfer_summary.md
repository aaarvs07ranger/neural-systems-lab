# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.715 |                 8.000 |              10.869 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.711 |                 7.680 |              10.884 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_clut                                          |          1.000 | 0.712 |                 8.440 |              10.846 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_obj                                           |          1.000 | 0.715 |                 7.560 |              10.869 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          1.000 | 0.715 |                 7.720 |              10.912 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.960 | 0.685 |                23.040 |              10.288 |         25 |              0.040 |              0.040 |          0.030 |          0.042 |
| F_light                                         |          1.000 | 0.716 |                 8.440 |              10.849 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_sky                                           |          1.000 | 0.715 |                 7.840 |              10.854 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.655 |                25.640 |               9.840 |         25 |              0.080 |              0.080 |          0.060 |          0.084 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.694 |                12.640 |              10.810 |         25 |              0.000 |              0.000 |          0.021 |          0.029 |
| B_L2 (+ object appearance)                      |          0.960 | 0.643 |                22.520 |              10.328 |         25 |              0.040 |              0.040 |          0.072 |          0.101 |
| B_L3 (+ distractors)                            |          0.920 | 0.635 |                26.400 |               9.813 |         25 |              0.080 |              0.080 |          0.080 |          0.112 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.060 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.072 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
