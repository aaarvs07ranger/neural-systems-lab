# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.807 |                12.400 |              11.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.808 |                12.680 |              11.561 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_clut                                          |          1.000 | 0.810 |                12.560 |              11.582 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_obj                                           |          1.000 | 0.805 |                12.640 |              11.604 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_tgt                                           |          1.000 | 0.815 |                12.040 |              11.564 |         25 |              0.000 |              0.000 |         -0.008 |         -0.010 |
| F_mat                                           |          1.000 | 0.758 |                22.920 |              11.480 |         25 |              0.000 |              0.000 |          0.049 |          0.061 |
| F_light                                         |          1.000 | 0.807 |                13.160 |              11.582 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          1.000 | 0.708 |                24.240 |              11.464 |         25 |              0.000 |              0.000 |          0.100 |          0.124 |
| B_L1 (materials + lighting)                     |          1.000 | 0.746 |                22.560 |              11.465 |         25 |              0.000 |              0.000 |          0.061 |          0.076 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.656 |                40.520 |              11.275 |         25 |              0.000 |              0.000 |          0.151 |          0.187 |
| B_L2 (+ object appearance)                      |          1.000 | 0.586 |                60.520 |              11.067 |         25 |              0.000 |              0.000 |          0.221 |          0.274 |
| B_L3 (+ distractors)                            |          0.960 | 0.626 |                50.960 |              10.701 |         25 |              0.040 |              0.040 |          0.182 |          0.225 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.049 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.100 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.061 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.151 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.221 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.182 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
