# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.621 |                46.280 |              12.283 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.578 |                57.840 |              11.165 |         25 |              0.080 |              0.080 |          0.043 |          0.070 |
| F_clut                                          |          0.960 | 0.575 |                50.520 |              11.836 |         25 |              0.040 |              0.040 |          0.046 |          0.074 |
| F_obj                                           |          0.920 | 0.576 |                52.920 |              11.087 |         25 |              0.080 |              0.080 |          0.045 |          0.073 |
| F_tgt                                           |          0.960 | 0.593 |                47.320 |              11.823 |         25 |              0.040 |              0.040 |          0.028 |          0.045 |
| F_mat                                           |          0.520 | 0.329 |               127.680 |               5.571 |         25 |              0.480 |              0.480 |          0.292 |          0.470 |
| F_light                                         |          0.960 | 0.609 |                56.720 |              11.769 |         25 |              0.040 |              0.040 |          0.012 |          0.019 |
| F_sky                                           |          1.000 | 0.614 |                44.200 |              12.309 |         25 |              0.000 |              0.000 |          0.007 |          0.011 |
| B_L1 (materials + lighting)                     |          0.120 | 0.085 |               180.960 |              -0.156 |         25 |              0.880 |              0.880 |          0.536 |          0.864 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.080 |               185.520 |              -1.314 |         25 |              0.920 |              0.920 |          0.541 |          0.871 |
| B_L2 (+ object appearance)                      |          0.320 | 0.244 |               145.640 |               2.211 |         25 |              0.680 |              0.680 |          0.377 |          0.608 |
| B_L3 (+ distractors)                            |          0.400 | 0.284 |               150.640 |               3.109 |         25 |              0.600 |              0.600 |          0.337 |          0.543 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.043 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.046 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.045 absolute**
- **F_tgt: success drop 0.040 absolute, 4.0% relative · SPL drop 0.028 absolute**
- **F_mat: success drop 0.480 absolute, 48.0% relative · SPL drop 0.292 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.012 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L1: success drop 0.880 absolute, 88.0% relative · SPL drop 0.536 absolute**
- **L2noT: success drop 0.920 absolute, 92.0% relative · SPL drop 0.541 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.377 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.337 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
