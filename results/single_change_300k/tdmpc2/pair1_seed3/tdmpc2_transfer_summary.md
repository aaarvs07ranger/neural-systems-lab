# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.712 |                10.680 |              10.841 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.713 |                10.320 |              10.852 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_clut                                          |          1.000 | 0.709 |                20.280 |              10.730 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.714 |                 9.000 |              10.852 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_tgt                                           |          1.000 | 0.715 |                10.640 |              10.865 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_mat                                           |          0.400 | 0.301 |               140.320 |               2.438 |         25 |              0.600 |              0.600 |          0.410 |          0.577 |
| F_light                                         |          1.000 | 0.720 |                10.680 |              10.815 |         25 |              0.000 |              0.000 |         -0.008 |         -0.011 |
| F_sky                                           |          1.000 | 0.718 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| B_L1 (materials + lighting)                     |          0.360 | 0.307 |               141.080 |               1.929 |         25 |              0.640 |              0.640 |          0.404 |          0.568 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.372 |               134.520 |               2.903 |         25 |              0.560 |              0.560 |          0.340 |          0.478 |
| B_L2 (+ object appearance)                      |          0.440 | 0.404 |               133.040 |               3.099 |         25 |              0.560 |              0.560 |          0.308 |          0.433 |
| B_L3 (+ distractors)                            |          0.400 | 0.331 |               139.320 |               2.381 |         25 |              0.600 |              0.600 |          0.381 |          0.535 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.600 absolute, 60.0% relative · SPL drop 0.410 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **L1: success drop 0.640 absolute, 64.0% relative · SPL drop 0.404 absolute**
- **L2noT: success drop 0.560 absolute, 56.0% relative · SPL drop 0.340 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.308 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.381 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
