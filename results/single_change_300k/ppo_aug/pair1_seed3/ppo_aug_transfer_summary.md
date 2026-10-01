# PPO_AUG zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.648 |                33.240 |               9.377 |         25 |              0.120 |              0.120 |          0.069 |          0.097 |
| F_clut                                          |          1.000 | 0.717 |                 9.160 |              10.831 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.715 |                10.320 |              10.818 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_tgt                                           |          1.000 | 0.721 |                 9.240 |              10.833 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_mat                                           |          0.800 | 0.647 |                46.440 |               8.151 |         25 |              0.200 |              0.200 |          0.070 |          0.098 |
| F_light                                         |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.617 |                61.600 |               7.110 |         25 |              0.280 |              0.280 |          0.100 |          0.139 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.573 |                69.440 |               6.634 |         25 |              0.320 |              0.320 |          0.144 |          0.201 |
| B_L2 (+ object appearance)                      |          0.240 | 0.240 |               152.960 |               0.898 |         25 |              0.760 |              0.760 |          0.477 |          0.665 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.640 |               0.412 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.069 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.070 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.100 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.144 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.477 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
