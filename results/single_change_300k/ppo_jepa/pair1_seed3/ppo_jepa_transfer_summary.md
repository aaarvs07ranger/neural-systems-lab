# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.694 |                21.840 |               9.906 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.720 | 0.586 |                60.480 |               7.162 |         25 |              0.200 |              0.217 |          0.108 |          0.156 |
| F_clut                                          |          0.840 | 0.614 |                37.120 |               8.930 |         25 |              0.080 |              0.087 |          0.080 |          0.115 |
| F_obj                                           |          1.000 | 0.717 |                 6.840 |              10.865 |         25 |             -0.080 |             -0.087 |         -0.023 |         -0.033 |
| F_tgt                                           |          0.760 | 0.585 |                52.880 |               7.824 |         25 |              0.160 |              0.174 |          0.109 |          0.157 |
| F_mat                                           |          0.240 | 0.240 |               152.320 |               0.937 |         25 |              0.680 |              0.739 |          0.454 |          0.654 |
| F_light                                         |          0.920 | 0.696 |                21.800 |               9.900 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_sky                                           |          0.920 | 0.696 |                21.800 |               9.900 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| B_L1 (materials + lighting)                     |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.720 |              0.783 |          0.494 |          0.712 |

- **F_objall: success drop 0.200 absolute, 21.7% relative · SPL drop 0.108 absolute**
- **F_clut: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **F_obj: success drop -0.080 absolute, -8.7% relative · SPL drop -0.023 absolute**
- **F_tgt: success drop 0.160 absolute, 17.4% relative · SPL drop 0.109 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.454 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**
- **L2noT: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.494 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
