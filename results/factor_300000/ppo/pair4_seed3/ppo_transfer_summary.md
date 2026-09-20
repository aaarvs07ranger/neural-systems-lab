# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.806 |                19.560 |              13.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.776 |                26.280 |              12.607 |         25 |              0.040 |              0.040 |          0.030 |          0.037 |
| F_clut                                          |          1.000 | 0.806 |                19.560 |              13.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.776 |                26.200 |              12.606 |         25 |              0.040 |              0.040 |          0.030 |          0.037 |
| F_tgt                                           |          1.000 | 0.808 |                19.520 |              13.236 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                                           |          0.200 | 0.159 |               162.640 |               0.875 |         25 |              0.800 |              0.800 |          0.646 |          0.802 |
| F_light                                         |          1.000 | 0.806 |                19.480 |              13.240 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.880 | 0.701 |                39.000 |              11.105 |         25 |              0.120 |              0.120 |          0.105 |          0.130 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.120 |              -0.844 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.120 |              -1.119 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.120 |              -1.111 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.120 |              -1.183 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.800 absolute, 80.0% relative · SPL drop 0.646 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.105 absolute**
- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**
- **L2noT: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
