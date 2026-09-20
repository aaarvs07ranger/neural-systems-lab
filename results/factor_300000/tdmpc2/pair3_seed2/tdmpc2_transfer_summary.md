# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.735 |                31.480 |              11.912 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.667 |                58.720 |              10.622 |         25 |              0.080 |              0.083 |          0.068 |          0.093 |
| F_clut                                          |          0.960 | 0.720 |                30.440 |              12.085 |         25 |              0.000 |              0.000 |          0.015 |          0.021 |
| F_obj                                           |          0.920 | 0.704 |                38.880 |              11.416 |         25 |              0.040 |              0.042 |          0.031 |          0.043 |
| F_tgt                                           |          0.880 | 0.671 |                49.680 |              10.777 |         25 |              0.080 |              0.083 |          0.064 |          0.087 |
| F_mat                                           |          0.040 | 0.010 |               196.240 |              -1.501 |         25 |              0.920 |              0.958 |          0.725 |          0.986 |
| F_light                                         |          0.880 | 0.641 |                47.480 |              11.077 |         25 |              0.080 |              0.083 |          0.094 |          0.128 |
| F_sky                                           |          0.920 | 0.650 |                46.440 |              11.499 |         25 |              0.040 |              0.042 |          0.086 |          0.116 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.179 |         25 |              0.960 |              1.000 |          0.735 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.360 |              -2.096 |         25 |              0.920 |              0.958 |          0.695 |          0.946 |
| B_L2 (+ object appearance)                      |          0.200 | 0.142 |               176.680 |               0.420 |         25 |              0.760 |              0.792 |          0.593 |          0.807 |
| B_L3 (+ distractors)                            |          0.320 | 0.235 |               168.920 |               1.649 |         25 |              0.640 |              0.667 |          0.501 |          0.681 |

- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.068 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.031 absolute**
- **F_tgt: success drop 0.080 absolute, 8.3% relative · SPL drop 0.064 absolute**
- **F_mat: success drop 0.920 absolute, 95.8% relative · SPL drop 0.725 absolute**
- **F_light: success drop 0.080 absolute, 8.3% relative · SPL drop 0.094 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.086 absolute**
- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.735 absolute**
- **L2noT: success drop 0.920 absolute, 95.8% relative · SPL drop 0.695 absolute**
- **L2: success drop 0.760 absolute, 79.2% relative · SPL drop 0.593 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.501 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
