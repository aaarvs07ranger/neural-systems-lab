# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.700 |                33.360 |              12.041 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.622 |                48.080 |              10.846 |         25 |              0.080 |              0.087 |          0.078 |          0.111 |
| F_clut                                          |          0.880 | 0.663 |                40.400 |              11.474 |         25 |              0.040 |              0.043 |          0.037 |          0.052 |
| F_obj                                           |          0.840 | 0.608 |                48.360 |              10.856 |         25 |              0.080 |              0.087 |          0.092 |          0.132 |
| F_tgt                                           |          0.880 | 0.672 |                40.200 |              11.447 |         25 |              0.040 |              0.043 |          0.028 |          0.040 |
| F_mat                                           |          0.240 | 0.182 |               154.480 |               1.760 |         25 |              0.680 |              0.739 |          0.518 |          0.740 |
| F_light                                         |          0.720 | 0.498 |                67.760 |               9.215 |         25 |              0.200 |              0.217 |          0.202 |          0.288 |
| F_sky                                           |          0.760 | 0.572 |                60.560 |               9.635 |         25 |              0.160 |              0.174 |          0.128 |          0.183 |
| B_L1 (materials + lighting)                     |          0.040 | 0.037 |               192.840 |              -0.597 |         25 |              0.880 |              0.957 |          0.663 |          0.947 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.538 |         25 |              0.920 |              1.000 |          0.700 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.140 |         25 |              0.920 |              1.000 |          0.700 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.136 |         25 |              0.920 |              1.000 |          0.700 |          1.000 |

- **F_objall: success drop 0.080 absolute, 8.7% relative · SPL drop 0.078 absolute**
- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.037 absolute**
- **F_obj: success drop 0.080 absolute, 8.7% relative · SPL drop 0.092 absolute**
- **F_tgt: success drop 0.040 absolute, 4.3% relative · SPL drop 0.028 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.518 absolute**
- **F_light: success drop 0.200 absolute, 21.7% relative · SPL drop 0.202 absolute**
- **F_sky: success drop 0.160 absolute, 17.4% relative · SPL drop 0.128 absolute**
- **L1: success drop 0.880 absolute, 95.7% relative · SPL drop 0.663 absolute**
- **L2noT: success drop 0.920 absolute, 100.0% relative · SPL drop 0.700 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.700 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.700 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
