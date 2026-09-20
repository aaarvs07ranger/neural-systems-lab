# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.755 |                13.640 |              10.903 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.729 |                20.440 |              10.401 |         25 |              0.040 |              0.040 |          0.025 |          0.034 |
| F_clut                                          |          1.000 | 0.752 |                13.120 |              10.899 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.769 |                13.480 |              10.902 |         25 |              0.000 |              0.000 |         -0.015 |         -0.019 |
| F_mat                                           |          1.000 | 0.771 |                17.080 |              10.841 |         25 |              0.000 |              0.000 |         -0.016 |         -0.021 |
| F_light                                         |          1.000 | 0.768 |                12.880 |              10.894 |         25 |              0.000 |              0.000 |         -0.013 |         -0.017 |
| F_sky                                           |          1.000 | 0.767 |                13.200 |              10.862 |         25 |              0.000 |              0.000 |         -0.012 |         -0.016 |
| B_L1 (materials + lighting)                     |          1.000 | 0.746 |                40.960 |              10.450 |         25 |              0.000 |              0.000 |          0.009 |          0.012 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.749 |                58.440 |               9.810 |         25 |              0.040 |              0.040 |          0.006 |          0.007 |
| B_L2 (+ object appearance)                      |          1.000 | 0.759 |                52.200 |              10.378 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| B_L3 (+ distractors)                            |          0.920 | 0.721 |                63.400 |               9.420 |         25 |              0.080 |              0.080 |          0.033 |          0.044 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.025 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.015 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.013 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.006 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.033 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
