# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.779 |                14.400 |              10.646 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.779 |                22.680 |              10.556 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_clut                                          |          1.000 | 0.777 |                15.680 |              10.629 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_obj                                           |          1.000 | 0.778 |                19.560 |              10.595 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_mat                                           |          0.920 | 0.698 |                38.840 |               9.557 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| F_light                                         |          1.000 | 0.778 |                27.560 |              10.498 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_sky                                           |          0.920 | 0.693 |                32.360 |               9.651 |         25 |              0.080 |              0.080 |          0.086 |          0.110 |
| B_L1 (materials + lighting)                     |          0.880 | 0.679 |                61.760 |               8.861 |         25 |              0.120 |              0.120 |          0.099 |          0.127 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.645 |                79.320 |               8.649 |         25 |              0.120 |              0.120 |          0.133 |          0.171 |
| B_L2 (+ object appearance)                      |          0.880 | 0.641 |                81.080 |               8.633 |         25 |              0.120 |              0.120 |          0.138 |          0.177 |
| B_L3 (+ distractors)                            |          0.920 | 0.694 |                57.840 |               9.338 |         25 |              0.080 |              0.080 |          0.085 |          0.109 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.086 absolute**
- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.099 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.133 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.138 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.085 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
