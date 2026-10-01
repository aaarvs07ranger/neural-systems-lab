# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.560 | 0.277 |               123.760 |               8.162 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.585 |                44.280 |              12.830 |         25 |             -0.400 |             -0.714 |         -0.307 |         -1.107 |
| F_clut                                          |          0.640 | 0.345 |               102.440 |               9.065 |         25 |             -0.080 |             -0.143 |         -0.068 |         -0.245 |
| F_obj                                           |          0.480 | 0.232 |               126.080 |               7.155 |         25 |              0.080 |              0.143 |          0.045 |          0.162 |
| F_tgt                                           |          0.880 | 0.508 |                59.080 |              11.930 |         25 |             -0.320 |             -0.571 |         -0.230 |         -0.831 |
| F_mat                                           |          0.680 | 0.293 |               110.360 |               8.192 |         25 |             -0.120 |             -0.214 |         -0.016 |         -0.057 |
| F_light                                         |          0.720 | 0.359 |                94.160 |               9.977 |         25 |             -0.160 |             -0.286 |         -0.082 |         -0.296 |
| F_sky                                           |          0.960 | 0.508 |                56.240 |              12.692 |         25 |             -0.400 |             -0.714 |         -0.230 |         -0.831 |
| B_L1 (materials + lighting)                     |          0.680 | 0.259 |               117.160 |               8.298 |         25 |             -0.120 |             -0.214 |          0.018 |          0.065 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.096 |               164.240 |               3.185 |         25 |              0.240 |              0.429 |          0.181 |          0.652 |
| B_L2 (+ object appearance)                      |          0.400 | 0.122 |               154.200 |               4.135 |         25 |              0.160 |              0.286 |          0.156 |          0.561 |
| B_L3 (+ distractors)                            |          0.400 | 0.163 |               145.120 |               3.958 |         25 |              0.160 |              0.286 |          0.114 |          0.412 |

- **F_objall: success drop -0.400 absolute, -71.4% relative · SPL drop -0.307 absolute**
- **F_clut: success drop -0.080 absolute, -14.3% relative · SPL drop -0.068 absolute**
- **F_obj: success drop 0.080 absolute, 14.3% relative · SPL drop 0.045 absolute**
- **F_tgt: success drop -0.320 absolute, -57.1% relative · SPL drop -0.230 absolute**
- **F_mat: success drop -0.120 absolute, -21.4% relative · SPL drop -0.016 absolute**
- **F_light: success drop -0.160 absolute, -28.6% relative · SPL drop -0.082 absolute**
- **F_sky: success drop -0.400 absolute, -71.4% relative · SPL drop -0.230 absolute**
- **L1: success drop -0.120 absolute, -21.4% relative · SPL drop 0.018 absolute**
- **L2noT: success drop 0.240 absolute, 42.9% relative · SPL drop 0.181 absolute**
- **L2: success drop 0.160 absolute, 28.6% relative · SPL drop 0.156 absolute**
- **L3: success drop 0.160 absolute, 28.6% relative · SPL drop 0.114 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
