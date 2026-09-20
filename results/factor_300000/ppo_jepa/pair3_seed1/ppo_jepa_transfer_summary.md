# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.800 | 0.597 |                55.080 |               9.748 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.464 |                83.040 |               7.385 |         25 |              0.160 |              0.200 |          0.133 |          0.223 |
| F_clut                                          |          0.800 | 0.598 |                55.040 |               9.750 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_obj                                           |          0.680 | 0.500 |                75.560 |               7.894 |         25 |              0.120 |              0.150 |          0.098 |          0.163 |
| F_tgt                                           |          0.840 | 0.634 |                48.040 |              10.221 |         25 |             -0.040 |             -0.050 |         -0.037 |         -0.062 |
| F_mat                                           |          0.040 | 0.040 |               192.160 |              -1.289 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| F_light                                         |          0.800 | 0.599 |                55.200 |               9.760 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_sky                                           |          0.800 | 0.594 |                55.160 |               9.728 |         25 |              0.000 |              0.000 |          0.003 |          0.006 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.282 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.120 |               177.080 |              -0.037 |         25 |              0.680 |              0.850 |          0.477 |          0.799 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -1.279 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -1.272 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |

- **F_objall: success drop 0.160 absolute, 20.0% relative · SPL drop 0.133 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.120 absolute, 15.0% relative · SPL drop 0.098 absolute**
- **F_tgt: success drop -0.040 absolute, -5.0% relative · SPL drop -0.037 absolute**
- **F_mat: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L1: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **L2noT: success drop 0.680 absolute, 85.0% relative · SPL drop 0.477 absolute**
- **L2: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
