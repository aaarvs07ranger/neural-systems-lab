# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.811 |                10.720 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.531 |                64.120 |               7.868 |         25 |              0.280 |              0.280 |          0.280 |          0.345 |
| F_clut                                          |          1.000 | 0.811 |                10.720 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.840 | 0.635 |                41.280 |               9.386 |         25 |              0.160 |              0.160 |          0.176 |          0.217 |
| F_tgt                                           |          1.000 | 0.819 |                10.560 |              11.581 |         25 |              0.000 |              0.000 |         -0.008 |         -0.010 |
| F_mat                                           |          0.920 | 0.748 |                24.960 |              10.415 |         25 |              0.080 |              0.080 |          0.063 |          0.077 |
| F_light                                         |          1.000 | 0.816 |                10.640 |              11.598 |         25 |              0.000 |              0.000 |         -0.005 |         -0.006 |
| F_sky                                           |          1.000 | 0.807 |                10.800 |              11.613 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| B_L1 (materials + lighting)                     |          0.920 | 0.743 |                25.160 |              10.401 |         25 |              0.080 |              0.080 |          0.068 |          0.084 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.644 |                41.080 |               9.347 |         25 |              0.160 |              0.160 |          0.167 |          0.206 |
| B_L2 (+ object appearance)                      |          0.720 | 0.559 |                63.840 |               7.843 |         25 |              0.280 |              0.280 |          0.252 |          0.310 |
| B_L3 (+ distractors)                            |          0.640 | 0.517 |                78.600 |               6.740 |         25 |              0.360 |              0.360 |          0.294 |          0.363 |

- **F_objall: success drop 0.280 absolute, 28.0% relative · SPL drop 0.280 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.160 absolute, 16.0% relative · SPL drop 0.176 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.063 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.068 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.167 absolute**
- **L2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.252 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.294 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
