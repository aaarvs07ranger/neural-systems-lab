# PPO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.480 | 0.399 |               115.680 |               6.068 |         25 |              0.520 |              0.520 |          0.361 |          0.475 |
| F_clut                                          |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.761 |                18.880 |              12.608 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_tgt                                           |          0.680 | 0.535 |                79.000 |               8.683 |         25 |              0.320 |              0.320 |          0.226 |          0.297 |
| F_mat                                           |          0.040 | 0.040 |               192.160 |              -1.540 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| F_light                                         |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.840 | 0.639 |                47.080 |              10.222 |         25 |              0.160 |              0.160 |          0.121 |          0.159 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -1.901 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |

- **F_objall: success drop 0.520 absolute, 52.0% relative · SPL drop 0.361 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_tgt: success drop 0.320 absolute, 32.0% relative · SPL drop 0.226 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.121 absolute**
- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **L2noT: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
