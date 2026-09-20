# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.707 |                10.320 |              10.846 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.712 |                 8.120 |              10.866 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_clut                                          |          1.000 | 0.714 |                 9.560 |              10.821 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_obj                                           |          1.000 | 0.712 |                 8.200 |              10.870 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_tgt                                           |          1.000 | 0.714 |                 8.280 |              10.868 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| F_mat                                           |          0.920 | 0.591 |                74.640 |               9.324 |         25 |              0.080 |              0.080 |          0.116 |          0.164 |
| F_light                                         |          1.000 | 0.714 |                 8.520 |              10.826 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| F_sky                                           |          1.000 | 0.716 |                 8.480 |              10.837 |         25 |              0.000 |              0.000 |         -0.008 |         -0.012 |
| B_L1 (materials + lighting)                     |          0.640 | 0.451 |               119.160 |               5.750 |         25 |              0.360 |              0.360 |          0.257 |          0.363 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.674 |                61.240 |               9.453 |         25 |              0.080 |              0.080 |          0.033 |          0.047 |
| B_L2 (+ object appearance)                      |          0.520 | 0.463 |               116.680 |               4.377 |         25 |              0.480 |              0.480 |          0.244 |          0.345 |
| B_L3 (+ distractors)                            |          0.760 | 0.556 |                91.120 |               7.409 |         25 |              0.240 |              0.240 |          0.151 |          0.214 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.116 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.257 absolute**
- **L2noT: success drop 0.080 absolute, 8.0% relative · SPL drop 0.033 absolute**
- **L2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.244 absolute**
- **L3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.151 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
