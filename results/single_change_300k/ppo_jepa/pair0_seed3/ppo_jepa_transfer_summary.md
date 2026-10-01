# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.750 |                18.120 |              10.969 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.760 | 0.579 |                56.240 |               8.289 |         25 |              0.200 |              0.208 |          0.171 |          0.227 |
| F_clut                                          |          0.960 | 0.750 |                18.120 |              10.973 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.598 |                49.160 |               8.938 |         25 |              0.160 |              0.167 |          0.152 |          0.203 |
| F_tgt                                           |          0.960 | 0.782 |                17.640 |              10.954 |         25 |              0.000 |              0.000 |         -0.031 |         -0.042 |
| F_mat                                           |          0.960 | 0.754 |                18.160 |              10.966 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_light                                         |          0.960 | 0.763 |                17.920 |              10.971 |         25 |              0.000 |              0.000 |         -0.013 |         -0.018 |
| F_sky                                           |          0.880 | 0.689 |                33.400 |               9.880 |         25 |              0.080 |              0.083 |          0.061 |          0.081 |
| B_L1 (materials + lighting)                     |          0.920 | 0.718 |                25.640 |              10.392 |         25 |              0.040 |              0.042 |          0.032 |          0.042 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.500 |                78.760 |               6.712 |         25 |              0.320 |              0.333 |          0.250 |          0.334 |
| B_L2 (+ object appearance)                      |          0.560 | 0.435 |                95.280 |               5.750 |         25 |              0.400 |              0.417 |          0.315 |          0.420 |
| B_L3 (+ distractors)                            |          0.560 | 0.435 |                95.280 |               5.727 |         25 |              0.400 |              0.417 |          0.315 |          0.420 |

- **F_objall: success drop 0.200 absolute, 20.8% relative · SPL drop 0.171 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.160 absolute, 16.7% relative · SPL drop 0.152 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.031 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.013 absolute**
- **F_sky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.061 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.032 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.250 absolute**
- **L2: success drop 0.400 absolute, 41.7% relative · SPL drop 0.315 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.315 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
