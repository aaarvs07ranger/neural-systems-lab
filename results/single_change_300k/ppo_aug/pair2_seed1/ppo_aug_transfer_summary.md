# PPO_AUG zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.739 |                14.200 |              10.236 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.691 |                29.920 |               9.237 |         25 |              0.080 |              0.083 |          0.048 |          0.065 |
| F_clut                                          |          0.960 | 0.739 |                14.080 |              10.238 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.691 |                29.920 |               9.237 |         25 |              0.080 |              0.083 |          0.048 |          0.065 |
| F_mat                                           |          0.920 | 0.699 |                22.400 |               9.762 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| F_light                                         |          0.960 | 0.739 |                14.440 |              10.237 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.699 |                22.040 |               9.725 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| B_L1 (materials + lighting)                     |          0.800 | 0.643 |                45.080 |               8.195 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.643 |                45.040 |               8.199 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |
| B_L2 (+ object appearance)                      |          0.800 | 0.643 |                45.040 |               8.199 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |
| B_L3 (+ distractors)                            |          0.800 | 0.643 |                45.040 |               8.199 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |

- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.048 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.048 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**
- **L2noT: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
