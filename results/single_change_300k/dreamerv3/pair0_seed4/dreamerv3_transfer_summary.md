# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.765 |                13.520 |              11.588 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.774 |                12.800 |              11.553 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| F_clut                                          |          1.000 | 0.746 |                13.480 |              11.606 |         25 |              0.000 |              0.000 |          0.019 |          0.025 |
| F_obj                                           |          1.000 | 0.761 |                13.280 |              11.572 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_tgt                                           |          1.000 | 0.763 |                14.200 |              11.563 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_mat                                           |          1.000 | 0.687 |                24.800 |              11.452 |         25 |              0.000 |              0.000 |          0.077 |          0.101 |
| F_light                                         |          1.000 | 0.770 |                13.560 |              11.580 |         25 |              0.000 |              0.000 |         -0.006 |         -0.007 |
| F_sky                                           |          1.000 | 0.681 |                27.320 |              11.437 |         25 |              0.000 |              0.000 |          0.084 |          0.109 |
| B_L1 (materials + lighting)                     |          1.000 | 0.672 |                31.040 |              11.395 |         25 |              0.000 |              0.000 |          0.093 |          0.122 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.667 |                28.800 |              11.383 |         25 |              0.000 |              0.000 |          0.098 |          0.128 |
| B_L2 (+ object appearance)                      |          1.000 | 0.590 |                40.640 |              11.279 |         25 |              0.000 |              0.000 |          0.175 |          0.228 |
| B_L3 (+ distractors)                            |          0.960 | 0.543 |                49.120 |              10.766 |         25 |              0.040 |              0.040 |          0.222 |          0.290 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.019 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.077 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.084 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.093 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.098 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.175 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.222 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
