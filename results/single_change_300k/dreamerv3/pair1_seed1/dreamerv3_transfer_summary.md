# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.560 | 0.386 |                97.080 |               5.553 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.654 |                37.400 |              10.278 |         25 |             -0.400 |             -0.714 |         -0.268 |         -0.695 |
| F_clut                                          |          0.560 | 0.374 |                98.920 |               5.558 |         25 |              0.000 |              0.000 |          0.012 |          0.030 |
| F_obj                                           |          0.600 | 0.431 |                89.120 |               5.978 |         25 |             -0.040 |             -0.071 |         -0.045 |         -0.118 |
| F_tgt                                           |          0.920 | 0.656 |                36.960 |               9.864 |         25 |             -0.360 |             -0.643 |         -0.270 |         -0.700 |
| F_mat                                           |          0.400 | 0.264 |               143.480 |               3.299 |         25 |              0.160 |              0.286 |          0.121 |          0.315 |
| F_light                                         |          0.640 | 0.435 |                83.040 |               6.548 |         25 |             -0.080 |             -0.143 |         -0.049 |         -0.127 |
| F_sky                                           |          0.480 | 0.357 |               112.720 |               4.601 |         25 |              0.080 |              0.143 |          0.029 |          0.076 |
| B_L1 (materials + lighting)                     |          0.400 | 0.298 |               148.600 |               3.324 |         25 |              0.160 |              0.286 |          0.088 |          0.228 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.350 |               130.640 |               4.340 |         25 |              0.080 |              0.143 |          0.035 |          0.092 |
| B_L2 (+ object appearance)                      |          0.520 | 0.302 |               136.440 |               4.706 |         25 |              0.040 |              0.071 |          0.084 |          0.218 |
| B_L3 (+ distractors)                            |          0.440 | 0.328 |               142.720 |               3.841 |         25 |              0.120 |              0.214 |          0.058 |          0.150 |

- **F_objall: success drop -0.400 absolute, -71.4% relative · SPL drop -0.268 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_obj: success drop -0.040 absolute, -7.1% relative · SPL drop -0.045 absolute**
- **F_tgt: success drop -0.360 absolute, -64.3% relative · SPL drop -0.270 absolute**
- **F_mat: success drop 0.160 absolute, 28.6% relative · SPL drop 0.121 absolute**
- **F_light: success drop -0.080 absolute, -14.3% relative · SPL drop -0.049 absolute**
- **F_sky: success drop 0.080 absolute, 14.3% relative · SPL drop 0.029 absolute**
- **L1: success drop 0.160 absolute, 28.6% relative · SPL drop 0.088 absolute**
- **L2noT: success drop 0.080 absolute, 14.3% relative · SPL drop 0.035 absolute**
- **L2: success drop 0.040 absolute, 7.1% relative · SPL drop 0.084 absolute**
- **L3: success drop 0.120 absolute, 21.4% relative · SPL drop 0.058 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
