# PPO_AUG zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.655 |                31.040 |               9.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.655 |                30.760 |               9.262 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut                                          |          0.880 | 0.655 |                31.040 |               9.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.655 |                30.760 |               9.262 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                                           |          0.880 | 0.655 |                31.120 |               9.265 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_light                                         |          0.960 | 0.735 |                15.400 |              10.220 |         25 |             -0.080 |             -0.091 |         -0.080 |         -0.122 |
| F_sky                                           |          0.960 | 0.735 |                15.640 |              10.219 |         25 |             -0.080 |             -0.091 |         -0.080 |         -0.122 |
| B_L1 (materials + lighting)                     |          0.880 | 0.655 |                31.120 |               9.265 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.575 |                46.440 |               8.294 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |
| B_L2 (+ object appearance)                      |          0.800 | 0.575 |                46.440 |               8.294 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |
| B_L3 (+ distractors)                            |          0.800 | 0.575 |                46.440 |               8.294 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_light: success drop -0.080 absolute, -9.1% relative · SPL drop -0.080 absolute**
- **F_sky: success drop -0.080 absolute, -9.1% relative · SPL drop -0.080 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L2noT: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**
- **L2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**
- **L3: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
