# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.592 |                45.040 |               9.479 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.684 |                12.360 |              10.788 |         25 |             -0.120 |             -0.136 |         -0.092 |         -0.156 |
| F_clut                                          |          0.800 | 0.552 |                56.280 |               8.459 |         25 |              0.080 |              0.091 |          0.039 |          0.067 |
| F_obj                                           |          0.800 | 0.591 |                58.720 |               8.303 |         25 |              0.080 |              0.091 |          0.001 |          0.001 |
| F_tgt                                           |          1.000 | 0.680 |                13.640 |              10.795 |         25 |             -0.120 |             -0.136 |         -0.088 |         -0.149 |
| F_mat                                           |          0.440 | 0.404 |               132.040 |               3.391 |         25 |              0.440 |              0.500 |          0.187 |          0.317 |
| F_light                                         |          0.800 | 0.524 |                53.480 |               8.474 |         25 |              0.080 |              0.091 |          0.068 |          0.115 |
| F_sky                                           |          0.840 | 0.581 |                46.600 |               9.013 |         25 |              0.040 |              0.045 |          0.011 |          0.019 |
| B_L1 (materials + lighting)                     |          0.280 | 0.280 |               146.880 |               0.892 |         25 |              0.600 |              0.682 |          0.312 |          0.527 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.320 |               142.480 |               1.439 |         25 |              0.560 |              0.636 |          0.272 |          0.459 |
| B_L2 (+ object appearance)                      |          0.240 | 0.240 |               154.120 |               0.297 |         25 |              0.640 |              0.727 |          0.352 |          0.594 |
| B_L3 (+ distractors)                            |          0.400 | 0.300 |               136.800 |               2.760 |         25 |              0.480 |              0.545 |          0.292 |          0.494 |

- **F_objall: success drop -0.120 absolute, -13.6% relative · SPL drop -0.092 absolute**
- **F_clut: success drop 0.080 absolute, 9.1% relative · SPL drop 0.039 absolute**
- **F_obj: success drop 0.080 absolute, 9.1% relative · SPL drop 0.001 absolute**
- **F_tgt: success drop -0.120 absolute, -13.6% relative · SPL drop -0.088 absolute**
- **F_mat: success drop 0.440 absolute, 50.0% relative · SPL drop 0.187 absolute**
- **F_light: success drop 0.080 absolute, 9.1% relative · SPL drop 0.068 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.011 absolute**
- **L1: success drop 0.600 absolute, 68.2% relative · SPL drop 0.312 absolute**
- **L2noT: success drop 0.560 absolute, 63.6% relative · SPL drop 0.272 absolute**
- **L2: success drop 0.640 absolute, 72.7% relative · SPL drop 0.352 absolute**
- **L3: success drop 0.480 absolute, 54.5% relative · SPL drop 0.292 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
