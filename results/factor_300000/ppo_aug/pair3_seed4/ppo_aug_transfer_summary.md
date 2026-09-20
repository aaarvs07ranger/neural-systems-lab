# PPO_AUG zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.735 |                27.760 |              11.994 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.320 | 0.255 |               139.600 |               3.750 |         25 |              0.640 |              0.667 |          0.480 |          0.653 |
| F_clut                                          |          0.920 | 0.709 |                34.280 |              11.362 |         25 |              0.040 |              0.042 |          0.026 |          0.035 |
| F_obj                                           |          0.840 | 0.645 |                48.920 |              10.258 |         25 |              0.120 |              0.125 |          0.090 |          0.122 |
| F_tgt                                           |          0.240 | 0.171 |               154.640 |               3.016 |         25 |              0.720 |              0.750 |          0.564 |          0.767 |
| F_mat                                           |          0.320 | 0.231 |               140.160 |               2.426 |         25 |              0.640 |              0.667 |          0.504 |          0.686 |
| F_light                                         |          0.920 | 0.712 |                34.920 |              11.415 |         25 |              0.040 |              0.042 |          0.022 |          0.030 |
| F_sky                                           |          0.440 | 0.317 |               119.360 |               4.295 |         25 |              0.520 |              0.542 |          0.418 |          0.569 |
| B_L1 (materials + lighting)                     |          0.360 | 0.253 |               135.080 |               3.032 |         25 |              0.600 |              0.625 |          0.482 |          0.656 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.141 |               156.000 |               1.349 |         25 |              0.720 |              0.750 |          0.594 |          0.809 |
| B_L2 (+ object appearance)                      |          0.280 | 0.191 |               147.960 |               1.842 |         25 |              0.680 |              0.708 |          0.544 |          0.740 |
| B_L3 (+ distractors)                            |          0.280 | 0.191 |               147.960 |               1.777 |         25 |              0.680 |              0.708 |          0.544 |          0.740 |

- **F_objall: success drop 0.640 absolute, 66.7% relative · SPL drop 0.480 absolute**
- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.026 absolute**
- **F_obj: success drop 0.120 absolute, 12.5% relative · SPL drop 0.090 absolute**
- **F_tgt: success drop 0.720 absolute, 75.0% relative · SPL drop 0.564 absolute**
- **F_mat: success drop 0.640 absolute, 66.7% relative · SPL drop 0.504 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_sky: success drop 0.520 absolute, 54.2% relative · SPL drop 0.418 absolute**
- **L1: success drop 0.600 absolute, 62.5% relative · SPL drop 0.482 absolute**
- **L2noT: success drop 0.720 absolute, 75.0% relative · SPL drop 0.594 absolute**
- **L2: success drop 0.680 absolute, 70.8% relative · SPL drop 0.544 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.544 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
