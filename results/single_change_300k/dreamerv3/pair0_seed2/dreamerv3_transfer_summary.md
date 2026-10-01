# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                13.400 |              11.595 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.785 |                14.040 |              11.557 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_clut                                          |          1.000 | 0.775 |                13.600 |              11.590 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.769 |                13.960 |              11.570 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| F_tgt                                           |          1.000 | 0.793 |                13.440 |              11.564 |         25 |              0.000 |              0.000 |         -0.014 |         -0.018 |
| F_mat                                           |          1.000 | 0.753 |                17.960 |              11.517 |         25 |              0.000 |              0.000 |          0.026 |          0.033 |
| F_light                                         |          1.000 | 0.778 |                14.320 |              11.565 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_sky                                           |          0.840 | 0.627 |                48.240 |               9.135 |         25 |              0.160 |              0.160 |          0.151 |          0.194 |
| B_L1 (materials + lighting)                     |          1.000 | 0.760 |                19.880 |              11.506 |         25 |              0.000 |              0.000 |          0.019 |          0.025 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.684 |                27.240 |              11.441 |         25 |              0.000 |              0.000 |          0.095 |          0.122 |
| B_L2 (+ object appearance)                      |          1.000 | 0.645 |                32.800 |              11.348 |         25 |              0.000 |              0.000 |          0.133 |          0.171 |
| B_L3 (+ distractors)                            |          1.000 | 0.630 |                40.840 |              11.262 |         25 |              0.000 |              0.000 |          0.148 |          0.190 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.014 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.026 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.151 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.019 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.095 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.133 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
