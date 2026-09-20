# DREAMERV3 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.597 |                24.800 |              13.911 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.638 |                29.640 |              12.992 |         25 |              0.040 |              0.040 |         -0.041 |         -0.068 |
| F_clut                                          |          1.000 | 0.595 |                24.400 |              13.930 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.606 |                25.240 |              13.866 |         25 |              0.000 |              0.000 |         -0.009 |         -0.015 |
| F_tgt                                           |          1.000 | 0.662 |                22.360 |              13.692 |         25 |              0.000 |              0.000 |         -0.065 |         -0.109 |
| F_mat                                           |          1.000 | 0.541 |                28.880 |              13.917 |         25 |              0.000 |              0.000 |          0.057 |          0.095 |
| F_light                                         |          1.000 | 0.596 |                25.320 |              13.914 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_sky                                           |          1.000 | 0.599 |                25.360 |              13.895 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| B_L1 (materials + lighting)                     |          1.000 | 0.570 |                28.560 |              13.856 |         25 |              0.000 |              0.000 |          0.027 |          0.045 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.577 |                35.400 |              13.764 |         25 |              0.000 |              0.000 |          0.020 |          0.034 |
| B_L2 (+ object appearance)                      |          0.920 | 0.608 |                44.240 |              12.337 |         25 |              0.080 |              0.080 |         -0.010 |         -0.017 |
| B_L3 (+ distractors)                            |          0.920 | 0.557 |                49.040 |              12.322 |         25 |              0.080 |              0.080 |          0.040 |          0.068 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop -0.041 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.065 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.057 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.027 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop -0.010 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.040 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
