# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.757 |                24.800 |              10.470 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.675 |                40.240 |               9.404 |         25 |              0.080 |              0.087 |          0.082 |          0.108 |
| F_clut                                          |          0.920 | 0.757 |                24.800 |              10.452 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.735 |                25.320 |              10.401 |         25 |              0.000 |              0.000 |          0.022 |          0.029 |
| F_tgt                                           |          0.920 | 0.763 |                24.760 |              10.465 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_mat                                           |          0.880 | 0.732 |                32.240 |               9.914 |         25 |              0.040 |              0.043 |          0.024 |          0.032 |
| F_light                                         |          0.960 | 0.779 |                17.400 |              10.978 |         25 |             -0.040 |             -0.043 |         -0.022 |         -0.030 |
| F_sky                                           |          0.920 | 0.757 |                24.760 |              10.474 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.758 |                25.040 |              10.452 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.712 |                32.640 |               9.857 |         25 |              0.040 |              0.043 |          0.045 |          0.059 |
| B_L2 (+ object appearance)                      |          0.880 | 0.710 |                32.640 |               9.854 |         25 |              0.040 |              0.043 |          0.046 |          0.061 |
| B_L3 (+ distractors)                            |          0.880 | 0.712 |                32.560 |               9.858 |         25 |              0.040 |              0.043 |          0.044 |          0.059 |

- **F_objall: success drop 0.080 absolute, 8.7% relative · SPL drop 0.082 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.022 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.024 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.022 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L2noT: success drop 0.040 absolute, 4.3% relative · SPL drop 0.045 absolute**
- **L2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.046 absolute**
- **L3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.044 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
