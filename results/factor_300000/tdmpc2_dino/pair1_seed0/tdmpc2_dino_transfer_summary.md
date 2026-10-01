# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.707 |                10.000 |              10.868 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.708 |                12.280 |              10.895 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_clut                                          |          1.000 | 0.716 |                 8.480 |              10.851 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| F_obj                                           |          1.000 | 0.713 |                13.920 |              10.808 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_tgt                                           |          1.000 | 0.715 |                 8.720 |              10.889 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| F_mat                                           |          1.000 | 0.697 |                11.360 |              10.826 |         25 |              0.000 |              0.000 |          0.011 |          0.015 |
| F_light                                         |          1.000 | 0.716 |                 9.640 |              10.866 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| F_sky                                           |          1.000 | 0.717 |                 8.320 |              10.860 |         25 |              0.000 |              0.000 |         -0.009 |         -0.013 |
| B_L1 (materials + lighting)                     |          1.000 | 0.697 |                10.440 |              10.839 |         25 |              0.000 |              0.000 |          0.010 |          0.015 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.696 |                13.840 |              10.815 |         25 |              0.000 |              0.000 |          0.011 |          0.016 |
| B_L2 (+ object appearance)                      |          1.000 | 0.706 |                14.080 |              10.826 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L3 (+ distractors)                            |          1.000 | 0.702 |                10.800 |              10.855 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
