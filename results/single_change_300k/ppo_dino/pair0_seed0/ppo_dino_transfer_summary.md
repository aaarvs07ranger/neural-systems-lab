# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.780 |                17.560 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.688 |                33.560 |               9.927 |         25 |              0.080 |              0.083 |          0.092 |          0.118 |
| F_clut                                          |          0.960 | 0.778 |                17.600 |              10.970 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_obj                                           |          0.880 | 0.688 |                33.400 |               9.870 |         25 |              0.080 |              0.083 |          0.092 |          0.118 |
| F_tgt                                           |          0.960 | 0.783 |                17.480 |              10.964 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_mat                                           |          0.960 | 0.771 |                18.240 |              11.121 |         25 |              0.000 |              0.000 |          0.009 |          0.011 |
| F_light                                         |          0.960 | 0.767 |                17.840 |              10.961 |         25 |              0.000 |              0.000 |          0.013 |          0.017 |
| F_sky                                           |          1.000 | 0.791 |                10.680 |              11.610 |         25 |             -0.040 |             -0.042 |         -0.011 |         -0.014 |
| B_L1 (materials + lighting)                     |          0.960 | 0.773 |                18.320 |              11.106 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.667 |                40.520 |               9.429 |         25 |              0.120 |              0.125 |          0.113 |          0.145 |
| B_L2 (+ object appearance)                      |          0.800 | 0.640 |                48.760 |               8.855 |         25 |              0.160 |              0.167 |          0.140 |          0.179 |
| B_L3 (+ distractors)                            |          0.720 | 0.580 |                64.040 |               7.886 |         25 |              0.240 |              0.250 |          0.200 |          0.256 |

- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.092 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.092 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **F_sky: success drop -0.040 absolute, -4.2% relative · SPL drop -0.011 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L2noT: success drop 0.120 absolute, 12.5% relative · SPL drop 0.113 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.140 absolute**
- **L3: success drop 0.240 absolute, 25.0% relative · SPL drop 0.200 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
