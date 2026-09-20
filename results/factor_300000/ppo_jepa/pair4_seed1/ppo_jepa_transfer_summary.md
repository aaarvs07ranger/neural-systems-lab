# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.710 |                34.480 |              12.052 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.606 |                56.360 |              10.422 |         25 |              0.120 |              0.130 |          0.105 |          0.147 |
| F_clut                                          |          0.920 | 0.705 |                34.400 |              12.058 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_obj                                           |          0.840 | 0.644 |                48.520 |              10.918 |         25 |              0.080 |              0.087 |          0.066 |          0.093 |
| F_tgt                                           |          0.840 | 0.641 |                49.640 |              11.048 |         25 |              0.080 |              0.087 |          0.069 |          0.098 |
| F_mat                                           |          0.080 | 0.080 |               184.240 |              -0.249 |         25 |              0.840 |              0.913 |          0.630 |          0.887 |
| F_light                                         |          0.920 | 0.719 |                34.320 |              12.071 |         25 |              0.000 |              0.000 |         -0.008 |         -0.012 |
| F_sky                                           |          0.880 | 0.678 |                41.080 |              11.364 |         25 |              0.040 |              0.043 |          0.032 |          0.045 |
| B_L1 (materials + lighting)                     |          0.560 | 0.381 |                99.360 |               6.762 |         25 |              0.360 |              0.391 |          0.329 |          0.463 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.086 |               178.360 |               1.334 |         25 |              0.800 |              0.870 |          0.624 |          0.879 |
| B_L2 (+ object appearance)                      |          0.240 | 0.195 |               155.760 |               2.684 |         25 |              0.680 |              0.739 |          0.516 |          0.726 |
| B_L3 (+ distractors)                            |          0.120 | 0.099 |               177.560 |               1.406 |         25 |              0.800 |              0.870 |          0.611 |          0.860 |

- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.105 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_obj: success drop 0.080 absolute, 8.7% relative · SPL drop 0.066 absolute**
- **F_tgt: success drop 0.080 absolute, 8.7% relative · SPL drop 0.069 absolute**
- **F_mat: success drop 0.840 absolute, 91.3% relative · SPL drop 0.630 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.032 absolute**
- **L1: success drop 0.360 absolute, 39.1% relative · SPL drop 0.329 absolute**
- **L2noT: success drop 0.800 absolute, 87.0% relative · SPL drop 0.624 absolute**
- **L2: success drop 0.680 absolute, 73.9% relative · SPL drop 0.516 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.611 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
