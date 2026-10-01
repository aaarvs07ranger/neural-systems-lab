# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.687 |                34.320 |              12.086 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.634 |                48.400 |              10.869 |         25 |              0.080 |              0.087 |          0.053 |          0.077 |
| F_clut                                          |          0.920 | 0.698 |                34.000 |              12.071 |         25 |              0.000 |              0.000 |         -0.012 |         -0.017 |
| F_obj                                           |          0.880 | 0.655 |                41.040 |              11.371 |         25 |              0.040 |              0.043 |          0.032 |          0.047 |
| F_tgt                                           |          0.920 | 0.687 |                34.240 |              12.078 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_mat                                           |          0.880 | 0.657 |                42.400 |              11.593 |         25 |              0.040 |              0.043 |          0.030 |          0.043 |
| F_light                                         |          0.960 | 0.723 |                26.760 |              12.576 |         25 |             -0.040 |             -0.043 |         -0.036 |         -0.052 |
| F_sky                                           |          0.920 | 0.690 |                34.480 |              12.075 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| B_L1 (materials + lighting)                     |          0.880 | 0.643 |                43.200 |              11.604 |         25 |              0.040 |              0.043 |          0.044 |          0.064 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.653 |                41.880 |              11.364 |         25 |              0.040 |              0.043 |          0.034 |          0.049 |
| B_L2 (+ object appearance)                      |          0.920 | 0.680 |                35.440 |              12.046 |         25 |              0.000 |              0.000 |          0.007 |          0.010 |
| B_L3 (+ distractors)                            |          0.880 | 0.642 |                41.720 |              11.479 |         25 |              0.040 |              0.043 |          0.045 |          0.066 |

- **F_objall: success drop 0.080 absolute, 8.7% relative · SPL drop 0.053 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.032 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.030 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.036 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L1: success drop 0.040 absolute, 4.3% relative · SPL drop 0.044 absolute**
- **L2noT: success drop 0.040 absolute, 4.3% relative · SPL drop 0.034 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.045 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
