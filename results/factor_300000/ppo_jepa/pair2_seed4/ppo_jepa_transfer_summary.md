# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                 7.720 |              10.683 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.778 |                 7.680 |              10.684 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_clut                                          |          1.000 | 0.777 |                 7.720 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.778 |                 7.680 |              10.684 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                                           |          0.880 | 0.685 |                35.040 |               9.134 |         25 |              0.120 |              0.120 |          0.091 |          0.118 |
| F_light                                         |          1.000 | 0.779 |                 8.000 |              10.688 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_sky                                           |          1.000 | 0.779 |                 8.000 |              10.681 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| B_L1 (materials + lighting)                     |          0.320 | 0.320 |               138.200 |               2.113 |         25 |              0.680 |              0.680 |          0.457 |          0.588 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.645 |                43.960 |               8.656 |         25 |              0.160 |              0.160 |          0.131 |          0.169 |
| B_L2 (+ object appearance)                      |          0.840 | 0.645 |                43.960 |               8.656 |         25 |              0.160 |              0.160 |          0.131 |          0.169 |
| B_L3 (+ distractors)                            |          0.840 | 0.645 |                43.960 |               8.656 |         25 |              0.160 |              0.160 |          0.131 |          0.169 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.091 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.680 absolute, 68.0% relative · SPL drop 0.457 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.131 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.131 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.131 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
