# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.774 |                17.920 |              10.956 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.495 |                86.640 |               6.499 |         25 |              0.360 |              0.375 |          0.279 |          0.361 |
| F_clut                                          |          0.960 | 0.776 |                17.720 |              10.962 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          0.840 | 0.663 |                42.080 |               9.476 |         25 |              0.120 |              0.125 |          0.111 |          0.144 |
| F_tgt                                           |          0.920 | 0.761 |                25.320 |              10.428 |         25 |              0.040 |              0.042 |          0.013 |          0.017 |
| F_mat                                           |          0.880 | 0.679 |                33.760 |               9.975 |         25 |              0.080 |              0.083 |          0.095 |          0.122 |
| F_light                                         |          0.960 | 0.763 |                18.280 |              10.962 |         25 |              0.000 |              0.000 |          0.011 |          0.014 |
| F_sky                                           |          0.960 | 0.777 |                17.880 |              10.962 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| B_L1 (materials + lighting)                     |          0.840 | 0.645 |                41.200 |               9.402 |         25 |              0.120 |              0.125 |          0.129 |          0.166 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.635 |                44.000 |               9.473 |         25 |              0.120 |              0.125 |          0.140 |          0.180 |
| B_L2 (+ object appearance)                      |          0.800 | 0.628 |                53.600 |               8.735 |         25 |              0.160 |              0.167 |          0.146 |          0.189 |
| B_L3 (+ distractors)                            |          0.520 | 0.453 |               101.160 |               5.064 |         25 |              0.440 |              0.458 |          0.321 |          0.414 |

- **F_objall: success drop 0.360 absolute, 37.5% relative · SPL drop 0.279 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.120 absolute, 12.5% relative · SPL drop 0.111 absolute**
- **F_tgt: success drop 0.040 absolute, 4.2% relative · SPL drop 0.013 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.095 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L1: success drop 0.120 absolute, 12.5% relative · SPL drop 0.129 absolute**
- **L2noT: success drop 0.120 absolute, 12.5% relative · SPL drop 0.140 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.146 absolute**
- **L3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.321 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
