# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.780 |                11.360 |              10.668 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.740 |                19.320 |              10.188 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| F_clut                                          |          1.000 | 0.779 |                10.560 |              10.670 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_obj                                           |          1.000 | 0.780 |                10.280 |              10.680 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.960 | 0.740 |                24.040 |              10.135 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| F_light                                         |          1.000 | 0.777 |                10.280 |              10.699 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_sky                                           |          0.960 | 0.739 |                16.000 |              10.211 |         25 |              0.040 |              0.040 |          0.041 |          0.052 |
| B_L1 (materials + lighting)                     |          0.920 | 0.698 |                28.600 |               9.688 |         25 |              0.080 |              0.080 |          0.082 |          0.105 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.740 |                16.000 |              10.215 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| B_L2 (+ object appearance)                      |          0.960 | 0.740 |                15.720 |              10.217 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| B_L3 (+ distractors)                            |          1.000 | 0.780 |                10.000 |              10.686 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.041 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.082 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
