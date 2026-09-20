# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                 8.080 |              10.682 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.780 |                 8.600 |              10.699 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_clut                                          |          1.000 | 0.779 |                 8.080 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.780 |                 8.600 |              10.699 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                                           |          0.920 | 0.725 |                25.720 |               9.721 |         25 |              0.080 |              0.080 |          0.053 |          0.068 |
| F_light                                         |          1.000 | 0.779 |                 8.240 |              10.692 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          1.000 | 0.779 |                 8.080 |              10.682 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.540 |                56.800 |               7.791 |         25 |              0.240 |              0.240 |          0.238 |          0.306 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.447 |                86.480 |               5.869 |         25 |              0.400 |              0.400 |          0.332 |          0.426 |
| B_L2 (+ object appearance)                      |          0.600 | 0.447 |                86.480 |               5.869 |         25 |              0.400 |              0.400 |          0.332 |          0.426 |
| B_L3 (+ distractors)                            |          0.600 | 0.447 |                86.480 |               5.869 |         25 |              0.400 |              0.400 |          0.332 |          0.426 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.053 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.238 absolute**
- **L2noT: success drop 0.400 absolute, 40.0% relative · SPL drop 0.332 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.332 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.332 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
