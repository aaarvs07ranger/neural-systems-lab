# PPO_AUG zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.631 |                57.920 |               9.829 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.160 | 0.115 |               169.800 |               1.462 |         25 |              0.640 |              0.800 |          0.516 |          0.818 |
| F_clut                                          |          0.800 | 0.630 |                57.960 |               9.832 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_obj                                           |          0.760 | 0.577 |                65.040 |               9.168 |         25 |              0.040 |              0.050 |          0.054 |          0.085 |
| F_tgt                                           |          0.160 | 0.115 |               169.800 |               1.598 |         25 |              0.640 |              0.800 |          0.516 |          0.818 |
| F_mat                                           |          0.360 | 0.258 |               132.320 |               2.984 |         25 |              0.440 |              0.550 |          0.373 |          0.591 |
| F_light                                         |          0.800 | 0.644 |                56.840 |               9.691 |         25 |              0.000 |              0.000 |         -0.013 |         -0.020 |
| F_sky                                           |          0.720 | 0.548 |                71.720 |               8.576 |         25 |              0.080 |              0.100 |          0.083 |          0.132 |
| B_L1 (materials + lighting)                     |          0.360 | 0.258 |               132.520 |               2.759 |         25 |              0.440 |              0.550 |          0.373 |          0.591 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.215 |               140.000 |               2.231 |         25 |              0.480 |              0.600 |          0.416 |          0.659 |
| B_L2 (+ object appearance)                      |          0.320 | 0.218 |               140.000 |               2.187 |         25 |              0.480 |              0.600 |          0.413 |          0.655 |
| B_L3 (+ distractors)                            |          0.320 | 0.218 |               140.000 |               2.187 |         25 |              0.480 |              0.600 |          0.413 |          0.655 |

- **F_objall: success drop 0.640 absolute, 80.0% relative · SPL drop 0.516 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop 0.040 absolute, 5.0% relative · SPL drop 0.054 absolute**
- **F_tgt: success drop 0.640 absolute, 80.0% relative · SPL drop 0.516 absolute**
- **F_mat: success drop 0.440 absolute, 55.0% relative · SPL drop 0.373 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.013 absolute**
- **F_sky: success drop 0.080 absolute, 10.0% relative · SPL drop 0.083 absolute**
- **L1: success drop 0.440 absolute, 55.0% relative · SPL drop 0.373 absolute**
- **L2noT: success drop 0.480 absolute, 60.0% relative · SPL drop 0.416 absolute**
- **L2: success drop 0.480 absolute, 60.0% relative · SPL drop 0.413 absolute**
- **L3: success drop 0.480 absolute, 60.0% relative · SPL drop 0.413 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
