# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.781 |                19.360 |              13.231 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.713 |                28.160 |              13.120 |         25 |              0.000 |              0.000 |          0.068 |          0.087 |
| F_clut                                          |          1.000 | 0.789 |                20.320 |              13.258 |         25 |              0.000 |              0.000 |         -0.009 |         -0.011 |
| F_obj                                           |          0.960 | 0.658 |                38.280 |              12.409 |         25 |              0.040 |              0.040 |          0.122 |          0.156 |
| F_tgt                                           |          1.000 | 0.784 |                20.640 |              13.224 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_mat                                           |          0.920 | 0.605 |                60.680 |              11.622 |         25 |              0.080 |              0.080 |          0.176 |          0.225 |
| F_light                                         |          0.960 | 0.729 |                27.640 |              12.610 |         25 |              0.040 |              0.040 |          0.051 |          0.066 |
| F_sky                                           |          0.960 | 0.754 |                27.680 |              12.581 |         25 |              0.040 |              0.040 |          0.026 |          0.034 |
| B_L1 (materials + lighting)                     |          0.920 | 0.645 |                65.920 |              11.761 |         25 |              0.080 |              0.080 |          0.135 |          0.173 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.453 |               121.720 |               8.405 |         25 |              0.280 |              0.280 |          0.328 |          0.420 |
| B_L2 (+ object appearance)                      |          0.480 | 0.294 |               140.800 |               4.316 |         25 |              0.520 |              0.520 |          0.486 |          0.623 |
| B_L3 (+ distractors)                            |          0.600 | 0.326 |               127.200 |               6.772 |         25 |              0.400 |              0.400 |          0.454 |          0.582 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.068 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.122 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.176 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.051 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.026 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.135 absolute**
- **L2noT: success drop 0.280 absolute, 28.0% relative · SPL drop 0.328 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.486 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.454 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
