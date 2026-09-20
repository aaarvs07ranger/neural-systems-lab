# PPO_AUG zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.700 |                24.600 |               9.743 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.660 |                31.800 |               9.262 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_clut                                          |          0.920 | 0.700 |                24.600 |               9.743 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.660 |                31.800 |               9.262 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_mat                                           |          0.760 | 0.540 |                55.360 |               7.823 |         25 |              0.160 |              0.174 |          0.160 |          0.228 |
| F_light                                         |          0.920 | 0.700 |                24.680 |               9.748 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.880 | 0.660 |                31.200 |               9.258 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| B_L1 (materials + lighting)                     |          0.840 | 0.620 |                39.880 |               8.788 |         25 |              0.080 |              0.087 |          0.080 |          0.114 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |
| B_L2 (+ object appearance)                      |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |
| B_L3 (+ distractors)                            |          0.760 | 0.607 |                55.040 |               7.836 |         25 |              0.160 |              0.174 |          0.093 |          0.133 |

- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **L2noT: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.093 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
