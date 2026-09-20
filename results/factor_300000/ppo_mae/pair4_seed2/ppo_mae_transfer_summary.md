# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.720 |                33.080 |              11.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.729 |                27.520 |              12.564 |         25 |             -0.040 |             -0.043 |         -0.009 |         -0.012 |
| F_clut                                          |          0.920 | 0.720 |                33.160 |              11.881 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.709 |                28.120 |              12.584 |         25 |             -0.040 |             -0.043 |          0.012 |          0.016 |
| F_tgt                                           |          0.920 | 0.703 |                33.040 |              11.869 |         25 |              0.000 |              0.000 |          0.017 |          0.024 |
| F_mat                                           |          0.120 | 0.095 |               177.240 |               0.268 |         25 |              0.800 |              0.870 |          0.626 |          0.869 |
| F_light                                         |          0.840 | 0.621 |                49.160 |              10.935 |         25 |              0.080 |              0.087 |          0.100 |          0.138 |
| F_sky                                           |          0.840 | 0.657 |                47.080 |              10.544 |         25 |              0.080 |              0.087 |          0.064 |          0.089 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.134 |         25 |              0.920 |              1.000 |          0.720 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.817 |         25 |              0.920 |              1.000 |          0.720 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.645 |         25 |              0.920 |              1.000 |          0.720 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.616 |         25 |              0.920 |              1.000 |          0.720 |          1.000 |

- **F_objall: success drop -0.040 absolute, -4.3% relative · SPL drop -0.009 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.040 absolute, -4.3% relative · SPL drop 0.012 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.017 absolute**
- **F_mat: success drop 0.800 absolute, 87.0% relative · SPL drop 0.626 absolute**
- **F_light: success drop 0.080 absolute, 8.7% relative · SPL drop 0.100 absolute**
- **F_sky: success drop 0.080 absolute, 8.7% relative · SPL drop 0.064 absolute**
- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.720 absolute**
- **L2noT: success drop 0.920 absolute, 100.0% relative · SPL drop 0.720 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.720 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.720 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
