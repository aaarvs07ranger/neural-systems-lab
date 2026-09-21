# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.766 |                20.320 |              13.234 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.743 |                27.520 |              12.704 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| F_clut                                          |          0.960 | 0.739 |                26.440 |              12.593 |         25 |              0.040 |              0.040 |          0.027 |          0.035 |
| F_obj                                           |          0.960 | 0.733 |                27.800 |              12.753 |         25 |              0.040 |              0.040 |          0.033 |          0.043 |
| F_tgt                                           |          1.000 | 0.763 |                20.400 |              13.225 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_mat                                           |          0.800 | 0.559 |                55.760 |              10.505 |         25 |              0.200 |              0.200 |          0.207 |          0.270 |
| F_light                                         |          0.960 | 0.757 |                26.640 |              12.584 |         25 |              0.040 |              0.040 |          0.009 |          0.012 |
| F_sky                                           |          0.960 | 0.751 |                26.680 |              12.587 |         25 |              0.040 |              0.040 |          0.014 |          0.019 |
| B_L1 (materials + lighting)                     |          0.800 | 0.558 |                54.560 |              10.317 |         25 |              0.200 |              0.200 |          0.208 |          0.272 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.614 |                42.120 |              11.347 |         25 |              0.120 |              0.120 |          0.152 |          0.198 |
| B_L2 (+ object appearance)                      |          0.840 | 0.596 |                49.000 |              10.809 |         25 |              0.160 |              0.160 |          0.169 |          0.221 |
| B_L3 (+ distractors)                            |          0.880 | 0.620 |                41.960 |              11.330 |         25 |              0.120 |              0.120 |          0.146 |          0.191 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.027 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.207 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.009 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.014 absolute**
- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.208 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.152 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.169 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.146 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
