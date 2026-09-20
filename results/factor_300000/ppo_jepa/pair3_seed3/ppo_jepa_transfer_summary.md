# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.760 | 0.576 |                62.720 |               9.168 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.680 | 0.506 |                76.560 |               8.121 |         25 |              0.080 |              0.105 |          0.069 |          0.120 |
| F_clut                                          |          0.760 | 0.577 |                62.680 |               9.169 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_obj                                           |          0.680 | 0.507 |                77.480 |               8.143 |         25 |              0.080 |              0.105 |          0.069 |          0.119 |
| F_tgt                                           |          0.760 | 0.579 |                62.440 |               9.151 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_mat                                           |          0.080 | 0.065 |               185.320 |               0.306 |         25 |              0.680 |              0.895 |          0.511 |          0.887 |
| F_light                                         |          0.680 | 0.508 |                76.760 |               8.070 |         25 |              0.080 |              0.105 |          0.068 |          0.118 |
| F_sky                                           |          0.840 | 0.618 |                49.120 |              10.379 |         25 |             -0.080 |             -0.105 |         -0.042 |         -0.073 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -0.425 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.876 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -0.631 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -0.840 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |

- **F_objall: success drop 0.080 absolute, 10.5% relative · SPL drop 0.069 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.080 absolute, 10.5% relative · SPL drop 0.069 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_mat: success drop 0.680 absolute, 89.5% relative · SPL drop 0.511 absolute**
- **F_light: success drop 0.080 absolute, 10.5% relative · SPL drop 0.068 absolute**
- **F_sky: success drop -0.080 absolute, -10.5% relative · SPL drop -0.042 absolute**
- **L1: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L2noT: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L2: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L3: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
