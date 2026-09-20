# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.657 |                30.560 |               9.269 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.738 |                15.040 |              10.247 |         25 |             -0.080 |             -0.091 |         -0.082 |         -0.124 |
| F_clut                                          |          0.880 | 0.657 |                30.560 |               9.269 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.738 |                15.040 |              10.247 |         25 |             -0.080 |             -0.091 |         -0.082 |         -0.124 |
| F_mat                                           |          0.080 | 0.080 |               184.480 |              -1.036 |         25 |              0.800 |              0.909 |          0.577 |          0.878 |
| F_light                                         |          0.200 | 0.200 |               160.840 |               0.789 |         25 |              0.680 |              0.773 |          0.457 |          0.695 |
| F_sky                                           |          0.600 | 0.539 |                83.480 |               5.673 |         25 |              0.280 |              0.318 |          0.118 |          0.179 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.840 |              0.955 |          0.617 |          0.939 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.840 |              0.955 |          0.617 |          0.939 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.840 |              0.955 |          0.617 |          0.939 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.840 |              0.955 |          0.617 |          0.939 |

- **F_objall: success drop -0.080 absolute, -9.1% relative · SPL drop -0.082 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.080 absolute, -9.1% relative · SPL drop -0.082 absolute**
- **F_mat: success drop 0.800 absolute, 90.9% relative · SPL drop 0.577 absolute**
- **F_light: success drop 0.680 absolute, 77.3% relative · SPL drop 0.457 absolute**
- **F_sky: success drop 0.280 absolute, 31.8% relative · SPL drop 0.118 absolute**
- **L1: success drop 0.840 absolute, 95.5% relative · SPL drop 0.617 absolute**
- **L2noT: success drop 0.840 absolute, 95.5% relative · SPL drop 0.617 absolute**
- **L2: success drop 0.840 absolute, 95.5% relative · SPL drop 0.617 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.617 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
