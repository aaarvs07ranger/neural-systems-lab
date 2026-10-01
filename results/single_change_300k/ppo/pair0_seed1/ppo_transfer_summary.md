# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.674 |                41.920 |               9.612 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.160 | 0.150 |               169.120 |               0.687 |         25 |              0.680 |              0.810 |          0.525 |          0.778 |
| F_clut                                          |          0.840 | 0.665 |                42.080 |               9.617 |         25 |              0.000 |              0.000 |          0.009 |          0.014 |
| F_obj                                           |          0.920 | 0.777 |                26.840 |              10.548 |         25 |             -0.080 |             -0.095 |         -0.102 |         -0.152 |
| F_tgt                                           |          0.200 | 0.167 |               161.520 |               1.378 |         25 |              0.640 |              0.762 |          0.508 |          0.753 |
| F_mat                                           |          0.480 | 0.423 |               108.440 |               4.393 |         25 |              0.360 |              0.429 |          0.251 |          0.372 |
| F_light                                         |          0.840 | 0.674 |                41.920 |               9.619 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.720 | 0.586 |                64.120 |               7.854 |         25 |              0.120 |              0.143 |          0.088 |          0.131 |
| B_L1 (materials + lighting)                     |          0.480 | 0.409 |               108.840 |               4.685 |         25 |              0.360 |              0.429 |          0.266 |          0.394 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.491 |                86.160 |               5.985 |         25 |              0.240 |              0.286 |          0.183 |          0.272 |
| B_L2 (+ object appearance)                      |          0.200 | 0.154 |               162.480 |               0.682 |         25 |              0.640 |              0.762 |          0.521 |          0.772 |
| B_L3 (+ distractors)                            |          0.240 | 0.194 |               154.760 |               1.157 |         25 |              0.600 |              0.714 |          0.481 |          0.713 |

- **F_objall: success drop 0.680 absolute, 81.0% relative · SPL drop 0.525 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_obj: success drop -0.080 absolute, -9.5% relative · SPL drop -0.102 absolute**
- **F_tgt: success drop 0.640 absolute, 76.2% relative · SPL drop 0.508 absolute**
- **F_mat: success drop 0.360 absolute, 42.9% relative · SPL drop 0.251 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.120 absolute, 14.3% relative · SPL drop 0.088 absolute**
- **L1: success drop 0.360 absolute, 42.9% relative · SPL drop 0.266 absolute**
- **L2noT: success drop 0.240 absolute, 28.6% relative · SPL drop 0.183 absolute**
- **L2: success drop 0.640 absolute, 76.2% relative · SPL drop 0.521 absolute**
- **L3: success drop 0.600 absolute, 71.4% relative · SPL drop 0.481 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
