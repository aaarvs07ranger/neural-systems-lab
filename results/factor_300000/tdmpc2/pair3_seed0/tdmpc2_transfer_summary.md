# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.764 |                25.120 |              12.521 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.741 |                36.200 |              12.435 |         25 |              0.000 |              0.000 |          0.023 |          0.030 |
| F_clut                                          |          0.960 | 0.728 |                33.800 |              12.039 |         25 |              0.040 |              0.040 |          0.036 |          0.047 |
| F_obj                                           |          1.000 | 0.761 |                26.440 |              12.538 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_tgt                                           |          0.920 | 0.686 |                43.040 |              11.346 |         25 |              0.080 |              0.080 |          0.078 |          0.102 |
| F_mat                                           |          0.480 | 0.377 |               138.360 |               4.174 |         25 |              0.520 |              0.520 |          0.386 |          0.506 |
| F_light                                         |          0.960 | 0.717 |                34.360 |              12.017 |         25 |              0.040 |              0.040 |          0.047 |          0.062 |
| F_sky                                           |          0.920 | 0.685 |                49.640 |              11.287 |         25 |              0.080 |              0.080 |          0.079 |          0.103 |
| B_L1 (materials + lighting)                     |          0.240 | 0.165 |               172.360 |               1.090 |         25 |              0.760 |              0.760 |          0.598 |          0.784 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.240 | 0.181 |               166.760 |               0.701 |         25 |              0.760 |              0.760 |          0.583 |          0.763 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               199.760 |              -1.892 |         25 |              0.960 |              0.960 |          0.724 |          0.948 |
| B_L3 (+ distractors)                            |          0.080 | 0.050 |               198.240 |              -1.396 |         25 |              0.920 |              0.920 |          0.713 |          0.934 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.023 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.080 absolute, 8.0% relative · SPL drop 0.078 absolute**
- **F_mat: success drop 0.520 absolute, 52.0% relative · SPL drop 0.386 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.047 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.079 absolute**
- **L1: success drop 0.760 absolute, 76.0% relative · SPL drop 0.598 absolute**
- **L2noT: success drop 0.760 absolute, 76.0% relative · SPL drop 0.583 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.724 absolute**
- **L3: success drop 0.920 absolute, 92.0% relative · SPL drop 0.713 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
