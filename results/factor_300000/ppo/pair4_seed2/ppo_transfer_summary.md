# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.561 |                36.920 |              12.513 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.680 | 0.451 |                79.560 |               9.174 |         25 |              0.240 |              0.261 |          0.111 |          0.197 |
| F_clut                                          |          0.920 | 0.561 |                36.920 |              12.513 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.560 | 0.353 |               100.520 |               7.825 |         25 |              0.360 |              0.391 |          0.208 |          0.371 |
| F_tgt                                           |          0.920 | 0.594 |                36.080 |              12.392 |         25 |              0.000 |              0.000 |         -0.032 |         -0.057 |
| F_mat                                           |          0.560 | 0.353 |               101.840 |               6.880 |         25 |              0.360 |              0.391 |          0.208 |          0.371 |
| F_light                                         |          0.960 | 0.591 |                29.760 |              13.137 |         25 |             -0.040 |             -0.043 |         -0.029 |         -0.052 |
| F_sky                                           |          0.440 | 0.293 |               121.360 |               5.509 |         25 |              0.480 |              0.522 |          0.268 |          0.478 |
| B_L1 (materials + lighting)                     |          0.200 | 0.144 |               164.360 |               1.221 |         25 |              0.720 |              0.783 |          0.418 |          0.744 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.056 |               185.680 |              -0.258 |         25 |              0.840 |              0.913 |          0.505 |          0.900 |
| B_L2 (+ object appearance)                      |          0.120 | 0.098 |               178.400 |               0.111 |         25 |              0.800 |              0.870 |          0.464 |          0.826 |
| B_L3 (+ distractors)                            |          0.120 | 0.098 |               178.400 |               0.068 |         25 |              0.800 |              0.870 |          0.464 |          0.826 |

- **F_objall: success drop 0.240 absolute, 26.1% relative · SPL drop 0.111 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.360 absolute, 39.1% relative · SPL drop 0.208 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.032 absolute**
- **F_mat: success drop 0.360 absolute, 39.1% relative · SPL drop 0.208 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.029 absolute**
- **F_sky: success drop 0.480 absolute, 52.2% relative · SPL drop 0.268 absolute**
- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.418 absolute**
- **L2noT: success drop 0.840 absolute, 91.3% relative · SPL drop 0.505 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.464 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.464 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
