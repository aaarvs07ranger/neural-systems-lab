# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.720 | 0.552 |                82.640 |               9.099 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.667 |                67.640 |              12.048 |         25 |             -0.280 |             -0.389 |         -0.115 |         -0.208 |
| F_clut                                          |          0.880 | 0.667 |                66.240 |              10.882 |         25 |             -0.160 |             -0.222 |         -0.115 |         -0.208 |
| F_obj                                           |          0.520 | 0.352 |               128.960 |               6.567 |         25 |              0.200 |              0.278 |          0.200 |          0.362 |
| F_tgt                                           |          1.000 | 0.668 |                64.560 |              12.082 |         25 |             -0.280 |             -0.389 |         -0.116 |         -0.210 |
| F_mat                                           |          0.280 | 0.174 |               178.480 |               1.788 |         25 |              0.440 |              0.611 |          0.378 |          0.685 |
| F_light                                         |          0.600 | 0.447 |               105.560 |               7.638 |         25 |              0.120 |              0.167 |          0.105 |          0.191 |
| F_sky                                           |          0.760 | 0.556 |                78.320 |               9.532 |         25 |             -0.040 |             -0.056 |         -0.004 |         -0.008 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.120 |              -1.920 |         25 |              0.680 |              0.944 |          0.512 |          0.928 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.558 |         25 |              0.720 |              1.000 |          0.552 |          1.000 |
| B_L2 (+ object appearance)                      |          0.040 | 0.011 |               193.680 |              -1.910 |         25 |              0.680 |              0.944 |          0.540 |          0.979 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.684 |         25 |              0.720 |              1.000 |          0.552 |          1.000 |

- **F_objall: success drop -0.280 absolute, -38.9% relative · SPL drop -0.115 absolute**
- **F_clut: success drop -0.160 absolute, -22.2% relative · SPL drop -0.115 absolute**
- **F_obj: success drop 0.200 absolute, 27.8% relative · SPL drop 0.200 absolute**
- **F_tgt: success drop -0.280 absolute, -38.9% relative · SPL drop -0.116 absolute**
- **F_mat: success drop 0.440 absolute, 61.1% relative · SPL drop 0.378 absolute**
- **F_light: success drop 0.120 absolute, 16.7% relative · SPL drop 0.105 absolute**
- **F_sky: success drop -0.040 absolute, -5.6% relative · SPL drop -0.004 absolute**
- **L1: success drop 0.680 absolute, 94.4% relative · SPL drop 0.512 absolute**
- **L2noT: success drop 0.720 absolute, 100.0% relative · SPL drop 0.552 absolute**
- **L2: success drop 0.680 absolute, 94.4% relative · SPL drop 0.540 absolute**
- **L3: success drop 0.720 absolute, 100.0% relative · SPL drop 0.552 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
