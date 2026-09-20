# TDMPC2 zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.801 |                24.680 |              13.197 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.628 |                44.880 |              11.796 |         25 |              0.080 |              0.080 |          0.173 |          0.215 |
| F_clut                                          |          1.000 | 0.774 |                20.400 |              13.225 |         25 |              0.000 |              0.000 |          0.027 |          0.034 |
| F_obj                                           |          0.960 | 0.682 |                36.160 |              12.520 |         25 |              0.040 |              0.040 |          0.119 |          0.148 |
| F_tgt                                           |          1.000 | 0.810 |                25.480 |              13.166 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| F_mat                                           |          0.800 | 0.523 |                87.440 |              10.010 |         25 |              0.200 |              0.200 |          0.278 |          0.347 |
| F_light                                         |          0.920 | 0.704 |                36.640 |              11.940 |         25 |              0.080 |              0.080 |          0.097 |          0.121 |
| F_sky                                           |          0.960 | 0.774 |                28.520 |              12.589 |         25 |              0.040 |              0.040 |          0.027 |          0.033 |
| B_L1 (materials + lighting)                     |          0.840 | 0.437 |                99.880 |              10.282 |         25 |              0.160 |              0.160 |          0.364 |          0.455 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.082 |               165.680 |               1.820 |         25 |              0.720 |              0.720 |          0.719 |          0.897 |
| B_L2 (+ object appearance)                      |          0.440 | 0.183 |               147.360 |               4.022 |         25 |              0.560 |              0.560 |          0.618 |          0.772 |
| B_L3 (+ distractors)                            |          0.360 | 0.211 |               157.040 |               2.891 |         25 |              0.640 |              0.640 |          0.590 |          0.737 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.173 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.027 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.119 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.278 absolute**
- **F_light: success drop 0.080 absolute, 8.0% relative · SPL drop 0.097 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.027 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.364 absolute**
- **L2noT: success drop 0.720 absolute, 72.0% relative · SPL drop 0.719 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.618 absolute**
- **L3: success drop 0.640 absolute, 64.0% relative · SPL drop 0.590 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
