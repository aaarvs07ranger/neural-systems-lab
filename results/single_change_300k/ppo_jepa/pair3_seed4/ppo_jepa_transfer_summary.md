# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.671 |                42.720 |              10.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.540 |                73.480 |               8.853 |         25 |              0.160 |              0.182 |          0.131 |          0.195 |
| F_clut                                          |          0.880 | 0.671 |                42.720 |              10.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.608 |                57.320 |               9.789 |         25 |              0.080 |              0.091 |          0.063 |          0.093 |
| F_tgt                                           |          0.760 | 0.582 |                65.600 |               9.526 |         25 |              0.120 |              0.136 |          0.089 |          0.133 |
| F_mat                                           |          0.680 | 0.484 |                78.320 |               7.875 |         25 |              0.200 |              0.227 |          0.187 |          0.278 |
| F_light                                         |          0.880 | 0.676 |                42.640 |              10.923 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_sky                                           |          0.880 | 0.670 |                42.800 |              10.920 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| B_L1 (materials + lighting)                     |          0.560 | 0.398 |                99.400 |               6.235 |         25 |              0.320 |              0.364 |          0.273 |          0.406 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.470 |                84.600 |               7.288 |         25 |              0.240 |              0.273 |          0.201 |          0.299 |
| B_L2 (+ object appearance)                      |          0.360 | 0.244 |               134.120 |               3.925 |         25 |              0.520 |              0.591 |          0.427 |          0.637 |
| B_L3 (+ distractors)                            |          0.360 | 0.245 |               134.160 |               3.974 |         25 |              0.520 |              0.591 |          0.426 |          0.635 |

- **F_objall: success drop 0.160 absolute, 18.2% relative · SPL drop 0.131 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 9.1% relative · SPL drop 0.063 absolute**
- **F_tgt: success drop 0.120 absolute, 13.6% relative · SPL drop 0.089 absolute**
- **F_mat: success drop 0.200 absolute, 22.7% relative · SPL drop 0.187 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.320 absolute, 36.4% relative · SPL drop 0.273 absolute**
- **L2noT: success drop 0.240 absolute, 27.3% relative · SPL drop 0.201 absolute**
- **L2: success drop 0.520 absolute, 59.1% relative · SPL drop 0.427 absolute**
- **L3: success drop 0.520 absolute, 59.1% relative · SPL drop 0.426 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
