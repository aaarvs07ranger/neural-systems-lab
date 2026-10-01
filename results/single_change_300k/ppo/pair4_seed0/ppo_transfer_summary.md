# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.621 |                23.320 |              13.786 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.616 |                35.720 |              12.468 |         25 |              0.080 |              0.080 |          0.004 |          0.007 |
| F_clut                                          |          1.000 | 0.619 |                23.280 |              13.789 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_obj                                           |          0.840 | 0.542 |                51.600 |              11.656 |         25 |              0.160 |              0.160 |          0.079 |          0.127 |
| F_tgt                                           |          1.000 | 0.664 |                22.200 |              13.643 |         25 |              0.000 |              0.000 |         -0.043 |         -0.069 |
| F_mat                                           |          1.000 | 0.600 |                28.000 |              13.801 |         25 |              0.000 |              0.000 |          0.020 |          0.033 |
| F_light                                         |          1.000 | 0.628 |                23.040 |              13.769 |         25 |              0.000 |              0.000 |         -0.007 |         -0.011 |
| F_sky                                           |          0.720 | 0.397 |                80.280 |              10.257 |         25 |              0.280 |              0.280 |          0.224 |          0.361 |
| B_L1 (materials + lighting)                     |          0.440 | 0.245 |               123.960 |               6.462 |         25 |              0.560 |              0.560 |          0.376 |          0.605 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.131 |               158.320 |               3.692 |         25 |              0.760 |              0.760 |          0.490 |          0.789 |
| B_L2 (+ object appearance)                      |          0.360 | 0.254 |               136.320 |               4.986 |         25 |              0.640 |              0.640 |          0.366 |          0.590 |
| B_L3 (+ distractors)                            |          0.320 | 0.220 |               143.280 |               4.356 |         25 |              0.680 |              0.680 |          0.401 |          0.646 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.160 absolute, 16.0% relative · SPL drop 0.079 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.043 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_sky: success drop 0.280 absolute, 28.0% relative · SPL drop 0.224 absolute**
- **L1: success drop 0.560 absolute, 56.0% relative · SPL drop 0.376 absolute**
- **L2noT: success drop 0.760 absolute, 76.0% relative · SPL drop 0.490 absolute**
- **L2: success drop 0.640 absolute, 64.0% relative · SPL drop 0.366 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.401 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
