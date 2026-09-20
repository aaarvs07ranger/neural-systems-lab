# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.600 | 0.462 |                88.720 |               5.835 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.541 |                83.040 |               6.309 |         25 |             -0.040 |             -0.067 |         -0.079 |         -0.170 |
| F_clut                                          |          0.720 | 0.545 |                68.080 |               7.241 |         25 |             -0.120 |             -0.200 |         -0.082 |         -0.178 |
| F_obj                                           |          0.680 | 0.542 |                75.440 |               6.797 |         25 |             -0.080 |             -0.133 |         -0.080 |         -0.173 |
| F_mat                                           |          0.960 | 0.724 |                26.400 |              10.131 |         25 |             -0.360 |             -0.600 |         -0.261 |         -0.565 |
| F_light                                         |          0.600 | 0.462 |                87.760 |               5.867 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.800 | 0.590 |                59.240 |               8.163 |         25 |             -0.200 |             -0.333 |         -0.128 |         -0.277 |
| B_L1 (materials + lighting)                     |          1.000 | 0.764 |                26.720 |              10.512 |         25 |             -0.400 |             -0.667 |         -0.302 |         -0.653 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.754 |                33.920 |              10.019 |         25 |             -0.360 |             -0.600 |         -0.292 |         -0.632 |
| B_L2 (+ object appearance)                      |          1.000 | 0.758 |                23.640 |              10.521 |         25 |             -0.400 |             -0.667 |         -0.296 |         -0.640 |
| B_L3 (+ distractors)                            |          0.960 | 0.727 |                25.360 |              10.105 |         25 |             -0.360 |             -0.600 |         -0.265 |         -0.573 |

- **F_objall: success drop -0.040 absolute, -6.7% relative · SPL drop -0.079 absolute**
- **F_clut: success drop -0.120 absolute, -20.0% relative · SPL drop -0.082 absolute**
- **F_obj: success drop -0.080 absolute, -13.3% relative · SPL drop -0.080 absolute**
- **F_mat: success drop -0.360 absolute, -60.0% relative · SPL drop -0.261 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop -0.200 absolute, -33.3% relative · SPL drop -0.128 absolute**
- **L1: success drop -0.400 absolute, -66.7% relative · SPL drop -0.302 absolute**
- **L2noT: success drop -0.360 absolute, -60.0% relative · SPL drop -0.292 absolute**
- **L2: success drop -0.400 absolute, -66.7% relative · SPL drop -0.296 absolute**
- **L3: success drop -0.360 absolute, -60.0% relative · SPL drop -0.265 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
