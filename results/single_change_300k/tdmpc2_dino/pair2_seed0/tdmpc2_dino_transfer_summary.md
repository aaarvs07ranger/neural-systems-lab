# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 7.920 |              10.701 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.779 |                 9.480 |              10.685 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_clut                                          |          1.000 | 0.780 |                 8.600 |              10.679 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_obj                                           |          1.000 | 0.780 |                 8.880 |              10.680 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_mat                                           |          1.000 | 0.777 |                 9.600 |              10.670 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_light                                         |          1.000 | 0.779 |                 9.240 |              10.686 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_sky                                           |          1.000 | 0.778 |                 9.160 |              10.696 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.777 |                 9.800 |              10.686 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.737 |                18.000 |              10.204 |         25 |              0.040 |              0.040 |          0.040 |          0.052 |
| B_L2 (+ object appearance)                      |          1.000 | 0.777 |                11.040 |              10.678 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L3 (+ distractors)                            |          1.000 | 0.777 |                11.640 |              10.667 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
