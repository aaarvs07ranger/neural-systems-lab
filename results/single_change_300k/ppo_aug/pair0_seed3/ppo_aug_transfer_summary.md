# PPO_AUG zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.737 |                27.440 |              10.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.670 |                50.240 |               9.034 |         25 |              0.120 |              0.130 |          0.067 |          0.091 |
| F_clut                                          |          0.920 | 0.737 |                27.440 |              10.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.815 |                12.320 |              11.601 |         25 |             -0.080 |             -0.087 |         -0.078 |         -0.106 |
| F_tgt                                           |          0.680 | 0.551 |                73.160 |               7.654 |         25 |              0.240 |              0.261 |          0.185 |          0.252 |
| F_mat                                           |          0.640 | 0.508 |                79.720 |               6.644 |         25 |              0.280 |              0.304 |          0.229 |          0.310 |
| F_light                                         |          0.880 | 0.709 |                34.800 |              10.106 |         25 |              0.040 |              0.043 |          0.028 |          0.038 |
| F_sky                                           |          0.600 | 0.471 |                88.640 |               6.309 |         25 |              0.320 |              0.348 |          0.266 |          0.361 |
| B_L1 (materials + lighting)                     |          0.280 | 0.253 |               146.440 |               1.706 |         25 |              0.640 |              0.696 |          0.484 |          0.657 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.273 |               139.240 |               2.207 |         25 |              0.600 |              0.652 |          0.464 |          0.630 |
| B_L2 (+ object appearance)                      |          0.200 | 0.180 |               161.560 |               0.541 |         25 |              0.720 |              0.783 |          0.557 |          0.756 |
| B_L3 (+ distractors)                            |          0.200 | 0.180 |               161.560 |               0.485 |         25 |              0.720 |              0.783 |          0.557 |          0.756 |

- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.067 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.080 absolute, -8.7% relative · SPL drop -0.078 absolute**
- **F_tgt: success drop 0.240 absolute, 26.1% relative · SPL drop 0.185 absolute**
- **F_mat: success drop 0.280 absolute, 30.4% relative · SPL drop 0.229 absolute**
- **F_light: success drop 0.040 absolute, 4.3% relative · SPL drop 0.028 absolute**
- **F_sky: success drop 0.320 absolute, 34.8% relative · SPL drop 0.266 absolute**
- **L1: success drop 0.640 absolute, 69.6% relative · SPL drop 0.484 absolute**
- **L2noT: success drop 0.600 absolute, 65.2% relative · SPL drop 0.464 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.557 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
