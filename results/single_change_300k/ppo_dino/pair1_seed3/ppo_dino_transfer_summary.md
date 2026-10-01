# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.717 |                 6.640 |              10.887 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.637 |                21.880 |               9.849 |         25 |              0.080 |              0.080 |          0.080 |          0.112 |
| F_clut                                          |          1.000 | 0.717 |                 6.600 |              10.882 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.637 |                21.800 |               9.846 |         25 |              0.080 |              0.080 |          0.080 |          0.112 |
| F_tgt                                           |          1.000 | 0.717 |                 6.520 |              10.889 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          0.680 | 0.463 |                68.240 |               6.833 |         25 |              0.320 |              0.320 |          0.254 |          0.354 |
| F_light                                         |          0.960 | 0.677 |                14.560 |              10.400 |         25 |              0.040 |              0.040 |          0.040 |          0.056 |
| F_sky                                           |          1.000 | 0.716 |                 6.640 |              10.878 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L1 (materials + lighting)                     |          0.840 | 0.570 |                38.000 |               8.923 |         25 |              0.160 |              0.160 |          0.147 |          0.206 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.570 |                37.880 |               8.884 |         25 |              0.160 |              0.160 |          0.147 |          0.205 |
| B_L2 (+ object appearance)                      |          0.720 | 0.445 |                61.480 |               7.436 |         25 |              0.280 |              0.280 |          0.272 |          0.379 |
| B_L3 (+ distractors)                            |          0.840 | 0.569 |                37.960 |               8.904 |         25 |              0.160 |              0.160 |          0.148 |          0.207 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.254 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.147 absolute**
- **L2noT: success drop 0.160 absolute, 16.0% relative · SPL drop 0.147 absolute**
- **L2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.272 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
