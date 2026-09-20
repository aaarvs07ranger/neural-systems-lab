# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.747 |                25.520 |              10.443 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.725 |                34.040 |               9.802 |         25 |              0.040 |              0.043 |          0.023 |          0.030 |
| F_clut                                          |          0.920 | 0.747 |                25.520 |              10.447 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.635 |                49.400 |               8.970 |         25 |              0.120 |              0.130 |          0.112 |          0.149 |
| F_tgt                                           |          0.920 | 0.753 |                25.360 |              10.416 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_mat                                           |          0.880 | 0.719 |                34.440 |               9.934 |         25 |              0.040 |              0.043 |          0.028 |          0.037 |
| F_light                                         |          0.960 | 0.775 |                18.400 |              10.978 |         25 |             -0.040 |             -0.043 |         -0.028 |         -0.038 |
| F_sky                                           |          0.920 | 0.729 |                25.840 |              10.494 |         25 |              0.000 |              0.000 |          0.018 |          0.024 |
| B_L1 (materials + lighting)                     |          0.760 | 0.638 |                56.360 |               8.260 |         25 |              0.160 |              0.174 |          0.109 |          0.146 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.600 |                65.240 |               8.059 |         25 |              0.200 |              0.217 |          0.147 |          0.197 |
| B_L2 (+ object appearance)                      |          0.800 | 0.654 |                50.120 |               8.802 |         25 |              0.120 |              0.130 |          0.093 |          0.124 |
| B_L3 (+ distractors)                            |          0.800 | 0.654 |                50.120 |               8.797 |         25 |              0.120 |              0.130 |          0.093 |          0.124 |

- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.023 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.120 absolute, 13.0% relative · SPL drop 0.112 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.028 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.028 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.018 absolute**
- **L1: success drop 0.160 absolute, 17.4% relative · SPL drop 0.109 absolute**
- **L2noT: success drop 0.200 absolute, 21.7% relative · SPL drop 0.147 absolute**
- **L2: success drop 0.120 absolute, 13.0% relative · SPL drop 0.093 absolute**
- **L3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.093 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
