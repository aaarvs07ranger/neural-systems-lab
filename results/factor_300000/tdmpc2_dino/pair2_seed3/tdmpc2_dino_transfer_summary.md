# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                17.840 |              10.607 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.780 |                10.840 |              10.674 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_clut                                          |          1.000 | 0.778 |                14.280 |              10.637 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_obj                                           |          0.960 | 0.739 |                19.840 |              10.176 |         25 |              0.040 |              0.040 |          0.039 |          0.050 |
| F_mat                                           |          1.000 | 0.777 |                12.680 |              10.676 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_light                                         |          1.000 | 0.779 |                14.960 |              10.624 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          1.000 | 0.778 |                17.080 |              10.608 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          1.000 | 0.778 |                 7.960 |              10.687 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.738 |                17.320 |              10.185 |         25 |              0.040 |              0.040 |          0.040 |          0.051 |
| B_L2 (+ object appearance)                      |          1.000 | 0.779 |                11.680 |              10.661 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| B_L3 (+ distractors)                            |          1.000 | 0.779 |                10.360 |              10.670 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
