# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.770 |                18.280 |              10.964 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.656 |                42.120 |               9.483 |         25 |              0.120 |              0.125 |          0.114 |          0.148 |
| F_clut                                          |          0.960 | 0.770 |                18.240 |              10.958 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.840 | 0.668 |                42.200 |               9.635 |         25 |              0.120 |              0.125 |          0.103 |          0.133 |
| F_tgt                                           |          0.960 | 0.779 |                18.120 |              10.938 |         25 |              0.000 |              0.000 |         -0.009 |         -0.011 |
| F_mat                                           |          0.960 | 0.761 |                18.680 |              11.126 |         25 |              0.000 |              0.000 |          0.010 |          0.012 |
| F_light                                         |          0.960 | 0.767 |                18.320 |              10.966 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_sky                                           |          0.880 | 0.690 |                33.440 |               9.980 |         25 |              0.080 |              0.083 |          0.081 |          0.105 |
| B_L1 (materials + lighting)                     |          0.760 | 0.612 |                55.840 |               8.343 |         25 |              0.200 |              0.208 |          0.158 |          0.205 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.507 |                79.400 |               6.979 |         25 |              0.320 |              0.333 |          0.263 |          0.341 |
| B_L2 (+ object appearance)                      |          0.640 | 0.492 |                79.320 |               6.833 |         25 |              0.320 |              0.333 |          0.278 |          0.361 |
| B_L3 (+ distractors)                            |          0.640 | 0.486 |                79.400 |               6.847 |         25 |              0.320 |              0.333 |          0.284 |          0.369 |

- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.114 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.120 absolute, 12.5% relative · SPL drop 0.103 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.081 absolute**
- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.158 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.263 absolute**
- **L2: success drop 0.320 absolute, 33.3% relative · SPL drop 0.278 absolute**
- **L3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.284 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
