# PPO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.699 |                21.960 |               9.760 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.580 |                44.880 |               8.251 |         25 |              0.120 |              0.130 |          0.118 |          0.169 |
| F_clut                                          |          0.920 | 0.699 |                22.040 |               9.768 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.580 |                44.880 |               8.251 |         25 |              0.120 |              0.130 |          0.118 |          0.169 |
| F_mat                                           |          0.920 | 0.698 |                22.000 |               9.765 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_light                                         |          0.920 | 0.699 |                22.040 |               9.771 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.699 |                22.040 |               9.771 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.698 |                22.000 |               9.765 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |
| B_L2 (+ object appearance)                      |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |
| B_L3 (+ distractors)                            |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |

- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.118 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.120 absolute, 13.0% relative · SPL drop 0.118 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L2noT: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
