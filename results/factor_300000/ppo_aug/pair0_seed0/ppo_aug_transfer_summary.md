# PPO_AUG zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.785 |                20.920 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.160 | 0.149 |               169.040 |               0.792 |         25 |              0.800 |              0.833 |          0.636 |          0.810 |
| F_clut                                          |          0.960 | 0.785 |                20.920 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.775 |                21.000 |              10.958 |         25 |              0.000 |              0.000 |          0.011 |          0.014 |
| F_tgt                                           |          0.760 | 0.594 |                62.080 |               8.211 |         25 |              0.200 |              0.208 |          0.191 |          0.244 |
| F_mat                                           |          0.840 | 0.702 |                44.240 |               9.309 |         25 |              0.120 |              0.125 |          0.084 |          0.107 |
| F_light                                         |          0.960 | 0.783 |                20.840 |              10.967 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| F_sky                                           |          0.960 | 0.785 |                21.160 |              10.949 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.586 |                66.440 |               7.694 |         25 |              0.240 |              0.250 |          0.199 |          0.254 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.566 |                78.200 |               7.024 |         25 |              0.280 |              0.292 |          0.219 |          0.279 |
| B_L2 (+ object appearance)                      |          0.160 | 0.140 |               169.600 |               0.297 |         25 |              0.800 |              0.833 |          0.646 |          0.822 |
| B_L3 (+ distractors)                            |          0.160 | 0.140 |               169.600 |               0.290 |         25 |              0.800 |              0.833 |          0.646 |          0.822 |

- **F_objall: success drop 0.800 absolute, 83.3% relative · SPL drop 0.636 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.011 absolute**
- **F_tgt: success drop 0.200 absolute, 20.8% relative · SPL drop 0.191 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.084 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.199 absolute**
- **L2noT: success drop 0.280 absolute, 29.2% relative · SPL drop 0.219 absolute**
- **L2: success drop 0.800 absolute, 83.3% relative · SPL drop 0.646 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.646 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
