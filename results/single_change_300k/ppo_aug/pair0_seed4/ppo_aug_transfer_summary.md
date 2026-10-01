# PPO_AUG zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.688 |                41.000 |               9.505 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.500 |                86.600 |               6.238 |         25 |              0.240 |              0.286 |          0.188 |          0.273 |
| F_clut                                          |          0.840 | 0.685 |                41.160 |               9.506 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_obj                                           |          0.760 | 0.624 |                55.800 |               8.355 |         25 |              0.080 |              0.095 |          0.064 |          0.093 |
| F_tgt                                           |          0.880 | 0.712 |                34.320 |               9.980 |         25 |             -0.040 |             -0.048 |         -0.024 |         -0.035 |
| F_mat                                           |          0.920 | 0.754 |                25.960 |              10.423 |         25 |             -0.080 |             -0.095 |         -0.067 |         -0.097 |
| F_light                                         |          0.840 | 0.688 |                41.000 |               9.507 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.880 | 0.713 |                34.080 |               9.946 |         25 |             -0.040 |             -0.048 |         -0.025 |         -0.037 |
| B_L1 (materials + lighting)                     |          0.840 | 0.676 |                41.680 |               9.398 |         25 |              0.000 |              0.000 |          0.012 |          0.017 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.608 |                56.760 |               8.375 |         25 |              0.080 |              0.095 |          0.080 |          0.116 |
| B_L2 (+ object appearance)                      |          0.200 | 0.186 |               161.640 |               1.252 |         25 |              0.640 |              0.762 |          0.502 |          0.730 |
| B_L3 (+ distractors)                            |          0.200 | 0.166 |               161.680 |               1.228 |         25 |              0.640 |              0.762 |          0.522 |          0.759 |

- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.188 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_obj: success drop 0.080 absolute, 9.5% relative · SPL drop 0.064 absolute**
- **F_tgt: success drop -0.040 absolute, -4.8% relative · SPL drop -0.024 absolute**
- **F_mat: success drop -0.080 absolute, -9.5% relative · SPL drop -0.067 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop -0.040 absolute, -4.8% relative · SPL drop -0.025 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L2noT: success drop 0.080 absolute, 9.5% relative · SPL drop 0.080 absolute**
- **L2: success drop 0.640 absolute, 76.2% relative · SPL drop 0.502 absolute**
- **L3: success drop 0.640 absolute, 76.2% relative · SPL drop 0.522 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
