# PPO_AUG zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.660 |                30.720 |               9.398 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.508 |                61.880 |               7.289 |         25 |              0.160 |              0.182 |          0.152 |          0.231 |
| F_clut                                          |          0.920 | 0.663 |                23.560 |               9.848 |         25 |             -0.040 |             -0.045 |         -0.003 |         -0.004 |
| F_obj                                           |          0.920 | 0.700 |                22.920 |               9.890 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_tgt                                           |          0.640 | 0.510 |                76.760 |               6.271 |         25 |              0.240 |              0.273 |          0.151 |          0.228 |
| F_mat                                           |          0.720 | 0.526 |                66.400 |               7.164 |         25 |              0.160 |              0.182 |          0.134 |          0.203 |
| F_light                                         |          0.920 | 0.700 |                22.880 |               9.882 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_sky                                           |          0.880 | 0.660 |                30.960 |               9.395 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.583 |                57.880 |               7.642 |         25 |              0.120 |              0.136 |          0.077 |          0.116 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.612 |                42.320 |               8.758 |         25 |              0.040 |              0.045 |          0.048 |          0.072 |
| B_L2 (+ object appearance)                      |          0.440 | 0.316 |               116.920 |               3.591 |         25 |              0.440 |              0.500 |          0.344 |          0.522 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.460 |          0.697 |

- **F_objall: success drop 0.160 absolute, 18.2% relative · SPL drop 0.152 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.003 absolute**
- **F_obj: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_tgt: success drop 0.240 absolute, 27.3% relative · SPL drop 0.151 absolute**
- **F_mat: success drop 0.160 absolute, 18.2% relative · SPL drop 0.134 absolute**
- **F_light: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.120 absolute, 13.6% relative · SPL drop 0.077 absolute**
- **L2noT: success drop 0.040 absolute, 4.5% relative · SPL drop 0.048 absolute**
- **L2: success drop 0.440 absolute, 50.0% relative · SPL drop 0.344 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.460 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
