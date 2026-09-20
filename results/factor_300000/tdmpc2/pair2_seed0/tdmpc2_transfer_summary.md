# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                11.480 |              10.652 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.779 |                12.400 |              10.663 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_clut                                          |          1.000 | 0.776 |                14.920 |              10.622 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_obj                                           |          1.000 | 0.779 |                19.280 |              10.590 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_mat                                           |          1.000 | 0.773 |                32.880 |              10.454 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |
| F_light                                         |          1.000 | 0.778 |                14.680 |              10.632 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.693 |                32.360 |               9.643 |         25 |              0.080 |              0.080 |          0.084 |          0.108 |
| B_L1 (materials + lighting)                     |          0.800 | 0.639 |                74.120 |               7.884 |         25 |              0.200 |              0.200 |          0.139 |          0.179 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.650 |                64.400 |               8.843 |         25 |              0.120 |              0.120 |          0.128 |          0.164 |
| B_L2 (+ object appearance)                      |          0.800 | 0.603 |                66.880 |               8.002 |         25 |              0.200 |              0.200 |          0.175 |          0.225 |
| B_L3 (+ distractors)                            |          0.800 | 0.606 |                79.920 |               7.870 |         25 |              0.200 |              0.200 |          0.172 |          0.221 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.084 absolute**
- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.139 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.128 absolute**
- **L2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.175 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.172 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
