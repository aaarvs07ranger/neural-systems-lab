# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.680 | 0.510 |                75.760 |               7.895 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.461 |                84.040 |               7.509 |         25 |              0.040 |              0.059 |          0.048 |          0.095 |
| F_clut                                          |          0.720 | 0.537 |                69.040 |               8.536 |         25 |             -0.040 |             -0.059 |         -0.027 |         -0.054 |
| F_obj                                           |          0.720 | 0.540 |                69.280 |               8.508 |         25 |             -0.040 |             -0.059 |         -0.030 |         -0.058 |
| F_tgt                                           |          0.640 | 0.453 |                84.320 |               7.522 |         25 |              0.040 |              0.059 |          0.057 |          0.112 |
| F_mat                                           |          0.040 | 0.040 |               192.160 |              -1.526 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| F_light                                         |          0.760 | 0.549 |                62.680 |               9.244 |         25 |             -0.080 |             -0.118 |         -0.039 |         -0.076 |
| F_sky                                           |          0.840 | 0.615 |                48.640 |              10.207 |         25 |             -0.160 |             -0.235 |         -0.105 |         -0.207 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.486 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.943 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -1.252 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -1.130 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |

- **F_objall: success drop 0.040 absolute, 5.9% relative · SPL drop 0.048 absolute**
- **F_clut: success drop -0.040 absolute, -5.9% relative · SPL drop -0.027 absolute**
- **F_obj: success drop -0.040 absolute, -5.9% relative · SPL drop -0.030 absolute**
- **F_tgt: success drop 0.040 absolute, 5.9% relative · SPL drop 0.057 absolute**
- **F_mat: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **F_light: success drop -0.080 absolute, -11.8% relative · SPL drop -0.039 absolute**
- **F_sky: success drop -0.160 absolute, -23.5% relative · SPL drop -0.105 absolute**
- **L1: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L2noT: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L2: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L3: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
