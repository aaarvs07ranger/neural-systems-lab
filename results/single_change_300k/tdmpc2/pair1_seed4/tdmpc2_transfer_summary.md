# TDMPC2 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.713 |                 9.040 |              10.827 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.718 |                11.880 |              10.831 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_clut                                          |          1.000 | 0.711 |                21.040 |              10.710 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          1.000 | 0.714 |                11.000 |              10.802 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_tgt                                           |          1.000 | 0.720 |                11.360 |              10.837 |         25 |              0.000 |              0.000 |         -0.006 |         -0.009 |
| F_mat                                           |          0.680 | 0.492 |                97.840 |               6.480 |         25 |              0.320 |              0.320 |          0.222 |          0.311 |
| F_light                                         |          1.000 | 0.716 |                11.280 |              10.821 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_sky                                           |          1.000 | 0.717 |                10.600 |              10.846 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| B_L1 (materials + lighting)                     |          0.400 | 0.366 |               130.640 |               2.736 |         25 |              0.600 |              0.600 |          0.348 |          0.487 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.487 |               104.440 |               5.734 |         25 |              0.360 |              0.360 |          0.226 |          0.317 |
| B_L2 (+ object appearance)                      |          0.240 | 0.211 |               157.880 |               0.901 |         25 |              0.760 |              0.760 |          0.502 |          0.704 |
| B_L3 (+ distractors)                            |          0.280 | 0.280 |               148.760 |               1.124 |         25 |              0.720 |              0.720 |          0.433 |          0.607 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.222 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **L1: success drop 0.600 absolute, 60.0% relative · SPL drop 0.348 absolute**
- **L2noT: success drop 0.360 absolute, 36.0% relative · SPL drop 0.226 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.502 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.433 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
