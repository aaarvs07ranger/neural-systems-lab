# PPO_AUG zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                 9.680 |              10.674 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.779 |                 9.680 |              10.670 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut                                          |          1.000 | 0.779 |                 9.680 |              10.674 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.779 |                 9.680 |              10.670 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                                           |          0.800 | 0.579 |                47.920 |               8.262 |         25 |              0.200 |              0.200 |          0.200 |          0.257 |
| F_light                                         |          1.000 | 0.779 |                 9.600 |              10.662 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.699 |                25.040 |               9.705 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| B_L1 (materials + lighting)                     |          0.920 | 0.699 |                24.920 |               9.711 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |
| B_L2 (+ object appearance)                      |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |
| B_L3 (+ distractors)                            |          0.920 | 0.732 |                24.680 |               9.659 |         25 |              0.080 |              0.080 |          0.047 |          0.060 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.200 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
