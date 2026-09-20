# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.715 |                 8.520 |              10.848 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.712 |                10.240 |              10.848 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_clut                                          |          1.000 | 0.713 |                10.600 |              10.846 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.720 |                 8.520 |              10.825 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_tgt                                           |          1.000 | 0.714 |                 9.840 |              10.850 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_mat                                           |          0.960 | 0.614 |                43.560 |              10.041 |         25 |              0.040 |              0.040 |          0.101 |          0.142 |
| F_light                                         |          1.000 | 0.710 |                 8.600 |              10.860 |         25 |              0.000 |              0.000 |          0.005 |          0.008 |
| F_sky                                           |          1.000 | 0.716 |                 8.640 |              10.854 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.563 |                74.600 |               7.869 |         25 |              0.200 |              0.200 |          0.153 |          0.213 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.550 |                76.440 |               7.939 |         25 |              0.200 |              0.200 |          0.165 |          0.231 |
| B_L2 (+ object appearance)                      |          0.960 | 0.644 |                55.200 |               9.978 |         25 |              0.040 |              0.040 |          0.071 |          0.099 |
| B_L3 (+ distractors)                            |          0.720 | 0.552 |               100.560 |               6.912 |         25 |              0.280 |              0.280 |          0.164 |          0.229 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.101 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.153 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.165 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.071 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.164 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
