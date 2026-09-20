# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.661 |                22.880 |              13.758 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.605 |                43.520 |              12.118 |         25 |              0.120 |              0.120 |          0.056 |          0.085 |
| F_clut                                          |          0.960 | 0.626 |                29.760 |              13.248 |         25 |              0.040 |              0.040 |          0.035 |          0.052 |
| F_obj                                           |          0.720 | 0.444 |                72.360 |              10.353 |         25 |              0.280 |              0.280 |          0.217 |          0.328 |
| F_tgt                                           |          1.000 | 0.694 |                22.040 |              13.624 |         25 |              0.000 |              0.000 |         -0.034 |         -0.051 |
| F_mat                                           |          0.720 | 0.438 |                73.280 |               9.267 |         25 |              0.280 |              0.280 |          0.223 |          0.338 |
| F_light                                         |          1.000 | 0.663 |                22.880 |              13.763 |         25 |              0.000 |              0.000 |         -0.002 |         -0.004 |
| F_sky                                           |          0.920 | 0.629 |                37.120 |              12.554 |         25 |              0.080 |              0.080 |          0.032 |          0.049 |
| B_L1 (materials + lighting)                     |          0.600 | 0.386 |                95.680 |               7.604 |         25 |              0.400 |              0.400 |          0.275 |          0.416 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.170 |               151.200 |               3.430 |         25 |              0.720 |              0.720 |          0.491 |          0.743 |
| B_L2 (+ object appearance)                      |          0.360 | 0.251 |               136.160 |               4.230 |         25 |              0.640 |              0.640 |          0.410 |          0.620 |
| B_L3 (+ distractors)                            |          0.280 | 0.195 |               149.920 |               3.166 |         25 |              0.720 |              0.720 |          0.466 |          0.705 |

- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.056 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.035 absolute**
- **F_obj: success drop 0.280 absolute, 28.0% relative · SPL drop 0.217 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.034 absolute**
- **F_mat: success drop 0.280 absolute, 28.0% relative · SPL drop 0.223 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.032 absolute**
- **L1: success drop 0.400 absolute, 40.0% relative · SPL drop 0.275 absolute**
- **L2noT: success drop 0.720 absolute, 72.0% relative · SPL drop 0.491 absolute**
- **L2: success drop 0.640 absolute, 64.0% relative · SPL drop 0.410 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.466 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
