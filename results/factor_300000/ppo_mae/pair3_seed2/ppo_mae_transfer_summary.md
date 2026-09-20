# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.660 |                41.240 |              10.807 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.560 | 0.406 |                96.080 |               6.311 |         25 |              0.320 |              0.364 |          0.254 |          0.385 |
| F_clut                                          |          0.920 | 0.682 |                34.840 |              11.435 |         25 |             -0.040 |             -0.045 |         -0.022 |         -0.034 |
| F_obj                                           |          0.760 | 0.566 |                60.960 |               8.953 |         25 |              0.120 |              0.136 |          0.094 |          0.142 |
| F_tgt                                           |          0.800 | 0.599 |                54.520 |               9.787 |         25 |              0.080 |              0.091 |          0.061 |          0.092 |
| F_mat                                           |          0.440 | 0.323 |               117.480 |               4.167 |         25 |              0.440 |              0.500 |          0.337 |          0.510 |
| F_light                                         |          0.960 | 0.717 |                27.680 |              11.983 |         25 |             -0.080 |             -0.091 |         -0.056 |         -0.085 |
| F_sky                                           |          0.880 | 0.664 |                40.720 |              10.708 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| B_L1 (materials + lighting)                     |          0.160 | 0.103 |               169.880 |               0.200 |         25 |              0.720 |              0.818 |          0.557 |          0.843 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.082 |               178.080 |              -0.250 |         25 |              0.760 |              0.864 |          0.578 |          0.876 |
| B_L2 (+ object appearance)                      |          0.040 | 0.016 |               192.240 |              -1.503 |         25 |              0.840 |              0.955 |          0.644 |          0.976 |
| B_L3 (+ distractors)                            |          0.040 | 0.016 |               192.240 |              -1.503 |         25 |              0.840 |              0.955 |          0.644 |          0.976 |

- **F_objall: success drop 0.320 absolute, 36.4% relative · SPL drop 0.254 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.022 absolute**
- **F_obj: success drop 0.120 absolute, 13.6% relative · SPL drop 0.094 absolute**
- **F_tgt: success drop 0.080 absolute, 9.1% relative · SPL drop 0.061 absolute**
- **F_mat: success drop 0.440 absolute, 50.0% relative · SPL drop 0.337 absolute**
- **F_light: success drop -0.080 absolute, -9.1% relative · SPL drop -0.056 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **L1: success drop 0.720 absolute, 81.8% relative · SPL drop 0.557 absolute**
- **L2noT: success drop 0.760 absolute, 86.4% relative · SPL drop 0.578 absolute**
- **L2: success drop 0.840 absolute, 95.5% relative · SPL drop 0.644 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.644 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
