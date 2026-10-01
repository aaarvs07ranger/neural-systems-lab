# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                21.800 |               9.920 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.320 | 0.276 |               137.480 |               2.088 |         25 |              0.600 |              0.652 |          0.422 |          0.604 |
| F_clut                                          |          0.920 | 0.698 |                21.800 |               9.923 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.920 | 0.698 |                21.840 |               9.917 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_tgt                                           |          0.320 | 0.296 |               137.440 |               2.302 |         25 |              0.600 |              0.652 |          0.402 |          0.575 |
| F_mat                                           |          0.680 | 0.581 |                69.680 |               6.483 |         25 |              0.240 |              0.261 |          0.117 |          0.167 |
| F_light                                         |          0.920 | 0.698 |                21.800 |               9.927 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.960 | 0.710 |                14.440 |              10.393 |         25 |             -0.040 |             -0.043 |         -0.011 |         -0.016 |
| B_L1 (materials + lighting)                     |          0.600 | 0.530 |                84.600 |               5.524 |         25 |              0.320 |              0.348 |          0.168 |          0.241 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.570 |                76.920 |               6.011 |         25 |              0.280 |              0.304 |          0.128 |          0.184 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.520 |               0.395 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.520 |               0.395 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |

- **F_objall: success drop 0.600 absolute, 65.2% relative · SPL drop 0.422 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_tgt: success drop 0.600 absolute, 65.2% relative · SPL drop 0.402 absolute**
- **F_mat: success drop 0.240 absolute, 26.1% relative · SPL drop 0.117 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop -0.040 absolute, -4.3% relative · SPL drop -0.011 absolute**
- **L1: success drop 0.320 absolute, 34.8% relative · SPL drop 0.168 absolute**
- **L2noT: success drop 0.280 absolute, 30.4% relative · SPL drop 0.128 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
