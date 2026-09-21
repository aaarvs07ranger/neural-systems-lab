# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.720 |                 6.560 |              10.884 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.720 |                 6.600 |              10.884 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_clut                                          |          1.000 | 0.720 |                 6.680 |              10.875 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.708 |                14.000 |              10.396 |         25 |              0.040 |              0.040 |          0.011 |          0.016 |
| F_tgt                                           |          1.000 | 0.720 |                 6.640 |              10.890 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.920 | 0.656 |                22.120 |               9.847 |         25 |              0.080 |              0.080 |          0.064 |          0.089 |
| F_light                                         |          1.000 | 0.720 |                 6.560 |              10.884 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          1.000 | 0.720 |                 6.640 |              10.875 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.670 |                14.880 |              10.378 |         25 |              0.040 |              0.040 |          0.050 |          0.070 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.671 |                14.720 |              10.372 |         25 |              0.040 |              0.040 |          0.048 |          0.067 |
| B_L2 (+ object appearance)                      |          0.960 | 0.670 |                14.880 |              10.401 |         25 |              0.040 |              0.040 |          0.050 |          0.069 |
| B_L3 (+ distractors)                            |          0.880 | 0.590 |                30.360 |               9.418 |         25 |              0.120 |              0.120 |          0.130 |          0.180 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.011 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.064 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.050 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.048 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.050 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.130 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
