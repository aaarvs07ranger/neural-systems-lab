# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.670 |                14.920 |              10.924 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.695 |                11.360 |              10.821 |         25 |              0.000 |              0.000 |         -0.025 |         -0.038 |
| F_clut                                          |          1.000 | 0.679 |                15.360 |              10.904 |         25 |              0.000 |              0.000 |         -0.009 |         -0.014 |
| F_obj                                           |          1.000 | 0.674 |                13.720 |              10.910 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_tgt                                           |          1.000 | 0.677 |                14.400 |              10.941 |         25 |              0.000 |              0.000 |         -0.008 |         -0.012 |
| F_mat                                           |          0.240 | 0.240 |               153.080 |               0.306 |         25 |              0.760 |              0.760 |          0.430 |          0.642 |
| F_light                                         |          1.000 | 0.666 |                15.480 |              10.917 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_sky                                           |          1.000 | 0.669 |                14.800 |              10.924 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.280 | 0.280 |               145.440 |               0.731 |         25 |              0.720 |              0.720 |          0.390 |          0.582 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.320 |               138.960 |               1.278 |         25 |              0.680 |              0.680 |          0.350 |          0.522 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.400 |              -0.453 |         25 |              0.800 |              0.800 |          0.470 |          0.701 |
| B_L3 (+ distractors)                            |          0.320 | 0.320 |               138.840 |               1.597 |         25 |              0.680 |              0.680 |          0.350 |          0.522 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.025 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.760 absolute, 76.0% relative · SPL drop 0.430 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.720 absolute, 72.0% relative · SPL drop 0.390 absolute**
- **L2noT: success drop 0.680 absolute, 68.0% relative · SPL drop 0.350 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.470 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.350 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
