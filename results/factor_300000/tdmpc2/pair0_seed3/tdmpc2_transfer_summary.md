# TDMPC2 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.815 |                12.560 |              11.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.809 |                23.400 |              11.483 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_clut                                          |          1.000 | 0.817 |                11.680 |              11.584 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_obj                                           |          0.960 | 0.793 |                19.600 |              11.103 |         25 |              0.040 |              0.040 |          0.022 |          0.027 |
| F_tgt                                           |          1.000 | 0.811 |                16.800 |              11.522 |         25 |              0.000 |              0.000 |          0.004 |          0.004 |
| F_mat                                           |          0.960 | 0.744 |                45.360 |              10.783 |         25 |              0.040 |              0.040 |          0.071 |          0.087 |
| F_light                                         |          1.000 | 0.822 |                15.920 |              11.551 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_sky                                           |          0.840 | 0.536 |                69.440 |               8.965 |         25 |              0.160 |              0.160 |          0.279 |          0.343 |
| B_L1 (materials + lighting)                     |          0.960 | 0.650 |                62.040 |              10.588 |         25 |              0.040 |              0.040 |          0.165 |          0.203 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.587 |                78.880 |               8.994 |         25 |              0.160 |              0.160 |          0.228 |          0.280 |
| B_L2 (+ object appearance)                      |          0.480 | 0.324 |               130.480 |               4.495 |         25 |              0.520 |              0.520 |          0.491 |          0.602 |
| B_L3 (+ distractors)                            |          0.640 | 0.454 |               110.040 |               6.363 |         25 |              0.360 |              0.360 |          0.361 |          0.443 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.022 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.071 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_sky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.279 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.165 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.228 absolute**
- **L2: success drop 0.520 absolute, 52.0% relative · SPL drop 0.491 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.361 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
