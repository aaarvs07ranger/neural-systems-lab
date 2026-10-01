# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.320 | 0.171 |               154.440 |               5.691 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.448 |                94.240 |              10.041 |         25 |             -0.400 |             -1.250 |         -0.277 |         -1.615 |
| F_clut                                          |          0.400 | 0.208 |               148.520 |               6.591 |         25 |             -0.080 |             -0.250 |         -0.037 |         -0.214 |
| F_obj                                           |          0.520 | 0.267 |               140.880 |               7.827 |         25 |             -0.200 |             -0.625 |         -0.095 |         -0.555 |
| F_tgt                                           |          0.960 | 0.600 |                42.600 |              12.962 |         25 |             -0.640 |             -2.000 |         -0.429 |         -2.503 |
| F_mat                                           |          0.520 | 0.245 |               135.720 |               7.622 |         25 |             -0.200 |             -0.625 |         -0.073 |         -0.428 |
| F_light                                         |          0.920 | 0.475 |                71.000 |              12.469 |         25 |             -0.600 |             -1.875 |         -0.303 |         -1.770 |
| F_sky                                           |          0.080 | 0.058 |               188.120 |               2.597 |         25 |              0.240 |              0.750 |          0.113 |          0.660 |
| B_L1 (materials + lighting)                     |          0.960 | 0.470 |                63.880 |              12.891 |         25 |             -0.640 |             -2.000 |         -0.299 |         -1.745 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.427 |                87.760 |              12.200 |         25 |             -0.600 |             -1.875 |         -0.256 |         -1.491 |
| B_L2 (+ object appearance)                      |          0.800 | 0.391 |                83.920 |              10.238 |         25 |             -0.480 |             -1.500 |         -0.220 |         -1.284 |
| B_L3 (+ distractors)                            |          0.880 | 0.446 |                81.640 |              11.493 |         25 |             -0.560 |             -1.750 |         -0.275 |         -1.603 |

- **F_objall: success drop -0.400 absolute, -125.0% relative · SPL drop -0.277 absolute**
- **F_clut: success drop -0.080 absolute, -25.0% relative · SPL drop -0.037 absolute**
- **F_obj: success drop -0.200 absolute, -62.5% relative · SPL drop -0.095 absolute**
- **F_tgt: success drop -0.640 absolute, -200.0% relative · SPL drop -0.429 absolute**
- **F_mat: success drop -0.200 absolute, -62.5% relative · SPL drop -0.073 absolute**
- **F_light: success drop -0.600 absolute, -187.5% relative · SPL drop -0.303 absolute**
- **F_sky: success drop 0.240 absolute, 75.0% relative · SPL drop 0.113 absolute**
- **L1: success drop -0.640 absolute, -200.0% relative · SPL drop -0.299 absolute**
- **L2noT: success drop -0.600 absolute, -187.5% relative · SPL drop -0.256 absolute**
- **L2: success drop -0.480 absolute, -150.0% relative · SPL drop -0.220 absolute**
- **L3: success drop -0.560 absolute, -175.0% relative · SPL drop -0.275 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
