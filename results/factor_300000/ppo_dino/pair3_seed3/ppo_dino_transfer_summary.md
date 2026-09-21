# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.690 |                33.760 |              11.455 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.565 |                57.360 |               9.970 |         25 |              0.120 |              0.130 |          0.125 |          0.181 |
| F_clut                                          |          0.880 | 0.660 |                40.360 |              10.839 |         25 |              0.040 |              0.043 |          0.030 |          0.043 |
| F_obj                                           |          0.920 | 0.686 |                34.320 |              11.453 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_tgt                                           |          0.800 | 0.589 |                54.720 |               9.898 |         25 |              0.120 |              0.130 |          0.101 |          0.146 |
| F_mat                                           |          0.320 | 0.200 |               141.480 |               3.188 |         25 |              0.600 |              0.652 |          0.490 |          0.710 |
| F_light                                         |          0.920 | 0.689 |                33.760 |              11.465 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_sky                                           |          0.840 | 0.631 |                47.000 |              10.215 |         25 |              0.080 |              0.087 |          0.059 |          0.085 |
| B_L1 (materials + lighting)                     |          0.360 | 0.219 |               134.520 |               3.590 |         25 |              0.560 |              0.609 |          0.471 |          0.682 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.166 |               148.280 |               2.457 |         25 |              0.640 |              0.696 |          0.524 |          0.759 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.160 |              -0.574 |         25 |              0.880 |              0.957 |          0.650 |          0.942 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.160 |              -0.613 |         25 |              0.880 |              0.957 |          0.650 |          0.942 |

- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.125 absolute**
- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.030 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_tgt: success drop 0.120 absolute, 13.0% relative · SPL drop 0.101 absolute**
- **F_mat: success drop 0.600 absolute, 65.2% relative · SPL drop 0.490 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.080 absolute, 8.7% relative · SPL drop 0.059 absolute**
- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.471 absolute**
- **L2noT: success drop 0.640 absolute, 69.6% relative · SPL drop 0.524 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.650 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.650 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
