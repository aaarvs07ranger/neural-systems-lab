# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.745 |                23.280 |              13.185 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.677 |                37.440 |              11.776 |         25 |              0.080 |              0.080 |          0.068 |          0.091 |
| F_clut                                          |          1.000 | 0.741 |                23.400 |              13.187 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_obj                                           |          0.920 | 0.676 |                37.520 |              11.808 |         25 |              0.080 |              0.080 |          0.069 |          0.093 |
| F_tgt                                           |          1.000 | 0.751 |                23.000 |              13.159 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_mat                                           |          0.040 | 0.020 |               192.200 |              -1.613 |         25 |              0.960 |              0.960 |          0.725 |          0.973 |
| F_light                                         |          1.000 | 0.746 |                23.280 |              13.177 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_sky                                           |          1.000 | 0.733 |                23.720 |              13.176 |         25 |              0.000 |              0.000 |          0.012 |          0.016 |
| B_L1 (materials + lighting)                     |          0.040 | 0.020 |               192.200 |              -1.584 |         25 |              0.960 |              0.960 |          0.725 |          0.973 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.054 |         25 |              1.000 |              1.000 |          0.745 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.053 |         25 |              1.000 |              1.000 |          0.745 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.064 |         25 |              1.000 |              1.000 |          0.745 |          1.000 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.068 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.069 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.725 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.725 absolute**
- **L2noT: success drop 1.000 absolute, 100.0% relative · SPL drop 0.745 absolute**
- **L2: success drop 1.000 absolute, 100.0% relative · SPL drop 0.745 absolute**
- **L3: success drop 1.000 absolute, 100.0% relative · SPL drop 0.745 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
