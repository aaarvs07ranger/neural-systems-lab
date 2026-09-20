# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.777 |                10.040 |              10.706 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.778 |                12.320 |              10.672 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_clut                                          |          1.000 | 0.779 |                10.000 |              10.677 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          1.000 | 0.779 |                 8.360 |              10.695 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                                           |          1.000 | 0.776 |                24.680 |              10.549 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_light                                         |          1.000 | 0.775 |                13.840 |              10.626 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_sky                                           |          0.920 | 0.695 |                28.720 |               9.664 |         25 |              0.080 |              0.080 |          0.082 |          0.105 |
| B_L1 (materials + lighting)                     |          1.000 | 0.767 |                37.720 |              10.422 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.724 |                55.680 |               9.403 |         25 |              0.080 |              0.080 |          0.053 |          0.068 |
| B_L2 (+ object appearance)                      |          1.000 | 0.774 |                33.360 |              10.464 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| B_L3 (+ distractors)                            |          1.000 | 0.767 |                30.280 |              10.466 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.082 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.053 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
