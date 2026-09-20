# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.732 |                25.880 |              10.492 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.472 |                86.400 |               6.364 |         25 |              0.320 |              0.348 |          0.260 |          0.355 |
| F_clut                                          |          0.880 | 0.700 |                33.240 |               9.958 |         25 |              0.040 |              0.043 |          0.032 |          0.044 |
| F_obj                                           |          0.800 | 0.620 |                49.080 |               8.992 |         25 |              0.120 |              0.130 |          0.112 |          0.153 |
| F_tgt                                           |          0.800 | 0.658 |                48.720 |               8.982 |         25 |              0.120 |              0.130 |          0.074 |          0.102 |
| F_mat                                           |          0.880 | 0.692 |                33.880 |               9.947 |         25 |              0.040 |              0.043 |          0.040 |          0.055 |
| F_light                                         |          0.920 | 0.735 |                25.800 |              10.496 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_sky                                           |          0.880 | 0.708 |                33.200 |               9.963 |         25 |              0.040 |              0.043 |          0.024 |          0.033 |
| B_L1 (materials + lighting)                     |          0.840 | 0.679 |                41.000 |               9.352 |         25 |              0.080 |              0.087 |          0.054 |          0.073 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.555 |                64.320 |               7.847 |         25 |              0.200 |              0.217 |          0.178 |          0.243 |
| B_L2 (+ object appearance)                      |          0.600 | 0.451 |                86.800 |               6.335 |         25 |              0.320 |              0.348 |          0.282 |          0.384 |
| B_L3 (+ distractors)                            |          0.600 | 0.451 |                86.840 |               6.339 |         25 |              0.320 |              0.348 |          0.282 |          0.384 |

- **F_objall: success drop 0.320 absolute, 34.8% relative · SPL drop 0.260 absolute**
- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.032 absolute**
- **F_obj: success drop 0.120 absolute, 13.0% relative · SPL drop 0.112 absolute**
- **F_tgt: success drop 0.120 absolute, 13.0% relative · SPL drop 0.074 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.024 absolute**
- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.054 absolute**
- **L2noT: success drop 0.200 absolute, 21.7% relative · SPL drop 0.178 absolute**
- **L2: success drop 0.320 absolute, 34.8% relative · SPL drop 0.282 absolute**
- **L3: success drop 0.320 absolute, 34.8% relative · SPL drop 0.282 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
