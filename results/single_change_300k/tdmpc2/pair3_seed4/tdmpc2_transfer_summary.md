# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.677 |                39.760 |              11.555 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.709 |                41.120 |              11.870 |         25 |             -0.040 |             -0.043 |         -0.031 |         -0.046 |
| F_clut                                          |          0.960 | 0.708 |                29.440 |              12.077 |         25 |             -0.040 |             -0.043 |         -0.031 |         -0.046 |
| F_obj                                           |          0.920 | 0.677 |                47.840 |              11.180 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_tgt                                           |          0.960 | 0.700 |                44.400 |              11.944 |         25 |             -0.040 |             -0.043 |         -0.023 |         -0.034 |
| F_mat                                           |          0.080 | 0.051 |               194.760 |              -1.393 |         25 |              0.840 |              0.913 |          0.626 |          0.924 |
| F_light                                         |          0.920 | 0.683 |                40.440 |              11.416 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| F_sky                                           |          0.960 | 0.696 |                36.480 |              11.871 |         25 |             -0.040 |             -0.043 |         -0.019 |         -0.028 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               193.640 |              -1.572 |         25 |              0.880 |              0.957 |          0.637 |          0.941 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               195.480 |              -1.777 |         25 |              0.880 |              0.957 |          0.637 |          0.941 |
| B_L2 (+ object appearance)                      |          0.040 | 0.005 |               194.160 |              -1.708 |         25 |              0.880 |              0.957 |          0.672 |          0.992 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.531 |         25 |              0.920 |              1.000 |          0.677 |          1.000 |

- **F_objall: success drop -0.040 absolute, -4.3% relative · SPL drop -0.031 absolute**
- **F_clut: success drop -0.040 absolute, -4.3% relative · SPL drop -0.031 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_tgt: success drop -0.040 absolute, -4.3% relative · SPL drop -0.023 absolute**
- **F_mat: success drop 0.840 absolute, 91.3% relative · SPL drop 0.626 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop -0.040 absolute, -4.3% relative · SPL drop -0.019 absolute**
- **L1: success drop 0.880 absolute, 95.7% relative · SPL drop 0.637 absolute**
- **L2noT: success drop 0.880 absolute, 95.7% relative · SPL drop 0.637 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.672 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.677 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
