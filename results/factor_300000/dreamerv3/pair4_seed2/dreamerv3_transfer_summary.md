# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.582 |                25.320 |              13.914 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.650 |                24.080 |              13.631 |         25 |              0.000 |              0.000 |         -0.068 |         -0.117 |
| F_clut                                          |          0.960 | 0.559 |                32.000 |              13.373 |         25 |              0.040 |              0.040 |          0.023 |          0.040 |
| F_obj                                           |          1.000 | 0.596 |                30.920 |              13.788 |         25 |              0.000 |              0.000 |         -0.014 |         -0.023 |
| F_tgt                                           |          1.000 | 0.653 |                23.000 |              13.688 |         25 |              0.000 |              0.000 |         -0.070 |         -0.121 |
| F_mat                                           |          0.960 | 0.461 |                44.280 |              13.195 |         25 |              0.040 |              0.040 |          0.121 |          0.208 |
| F_light                                         |          1.000 | 0.591 |                25.560 |              13.897 |         25 |              0.000 |              0.000 |         -0.009 |         -0.015 |
| F_sky                                           |          1.000 | 0.590 |                25.480 |              13.897 |         25 |              0.000 |              0.000 |         -0.008 |         -0.014 |
| B_L1 (materials + lighting)                     |          0.920 | 0.454 |                43.080 |              12.679 |         25 |              0.080 |              0.080 |          0.128 |          0.220 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.460 |                47.520 |              12.566 |         25 |              0.080 |              0.080 |          0.122 |          0.209 |
| B_L2 (+ object appearance)                      |          0.880 | 0.492 |                47.280 |              11.751 |         25 |              0.120 |              0.120 |          0.090 |          0.155 |
| B_L3 (+ distractors)                            |          0.800 | 0.450 |                64.360 |              10.754 |         25 |              0.200 |              0.200 |          0.132 |          0.226 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.068 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.014 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.070 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.121 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.128 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.122 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.090 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.132 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
