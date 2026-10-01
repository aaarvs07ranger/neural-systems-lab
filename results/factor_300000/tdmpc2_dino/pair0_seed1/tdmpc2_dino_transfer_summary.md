# TDMPC2_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.785 |                18.600 |              10.962 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.734 |                28.720 |              10.411 |         25 |              0.040 |              0.042 |          0.051 |          0.065 |
| F_clut                                          |          0.960 | 0.789 |                18.400 |              10.970 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_obj                                           |          0.920 | 0.728 |                27.800 |              10.430 |         25 |              0.040 |              0.042 |          0.057 |          0.072 |
| F_tgt                                           |          0.960 | 0.794 |                19.040 |              10.937 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| F_mat                                           |          0.880 | 0.723 |                34.880 |               9.966 |         25 |              0.080 |              0.083 |          0.061 |          0.078 |
| F_light                                         |          0.920 | 0.763 |                25.960 |              10.468 |         25 |              0.040 |              0.042 |          0.022 |          0.028 |
| F_sky                                           |          0.920 | 0.763 |                26.360 |              10.467 |         25 |              0.040 |              0.042 |          0.022 |          0.028 |
| B_L1 (materials + lighting)                     |          0.960 | 0.774 |                22.320 |              10.932 |         25 |              0.000 |              0.000 |          0.011 |          0.013 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.771 |                24.360 |              10.897 |         25 |              0.000 |              0.000 |          0.014 |          0.018 |
| B_L2 (+ object appearance)                      |          0.880 | 0.708 |                40.200 |               9.818 |         25 |              0.080 |              0.083 |          0.077 |          0.098 |
| B_L3 (+ distractors)                            |          0.920 | 0.731 |                40.960 |              10.284 |         25 |              0.040 |              0.042 |          0.054 |          0.069 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.051 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.057 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.061 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.014 absolute**
- **L2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.077 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.054 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
