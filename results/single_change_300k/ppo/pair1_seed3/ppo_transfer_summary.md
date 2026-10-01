# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.678 |                29.160 |               9.333 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.466 |                84.080 |               5.887 |         25 |              0.280 |              0.318 |          0.212 |          0.313 |
| F_clut                                          |          0.840 | 0.638 |                37.080 |               8.863 |         25 |              0.040 |              0.045 |          0.040 |          0.059 |
| F_obj                                           |          0.840 | 0.638 |                36.960 |               8.848 |         25 |              0.040 |              0.045 |          0.040 |          0.059 |
| F_tgt                                           |          0.640 | 0.456 |                76.000 |               6.382 |         25 |              0.240 |              0.273 |          0.222 |          0.328 |
| F_mat                                           |          0.760 | 0.627 |                53.920 |               7.588 |         25 |              0.120 |              0.136 |          0.051 |          0.075 |
| F_light                                         |          0.880 | 0.678 |                29.120 |               9.342 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.690 |                21.880 |               9.897 |         25 |             -0.040 |             -0.045 |         -0.012 |         -0.018 |
| B_L1 (materials + lighting)                     |          0.760 | 0.631 |                53.840 |               7.534 |         25 |              0.120 |              0.136 |          0.047 |          0.070 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.551 |                69.280 |               6.578 |         25 |              0.200 |              0.227 |          0.127 |          0.188 |
| B_L2 (+ object appearance)                      |          0.120 | 0.120 |               176.160 |              -0.540 |         25 |              0.760 |              0.864 |          0.558 |          0.823 |
| B_L3 (+ distractors)                            |          0.120 | 0.120 |               176.160 |              -0.571 |         25 |              0.760 |              0.864 |          0.558 |          0.823 |

- **F_objall: success drop 0.280 absolute, 31.8% relative · SPL drop 0.212 absolute**
- **F_clut: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_obj: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_tgt: success drop 0.240 absolute, 27.3% relative · SPL drop 0.222 absolute**
- **F_mat: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.012 absolute**
- **L1: success drop 0.120 absolute, 13.6% relative · SPL drop 0.047 absolute**
- **L2noT: success drop 0.200 absolute, 22.7% relative · SPL drop 0.127 absolute**
- **L2: success drop 0.760 absolute, 86.4% relative · SPL drop 0.558 absolute**
- **L3: success drop 0.760 absolute, 86.4% relative · SPL drop 0.558 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
