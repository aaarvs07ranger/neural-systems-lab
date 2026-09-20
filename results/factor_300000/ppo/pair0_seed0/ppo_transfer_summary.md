# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.774 |                17.640 |              10.981 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.240 | 0.196 |               153.880 |               2.010 |         25 |              0.720 |              0.750 |          0.578 |          0.747 |
| F_clut                                          |          0.880 | 0.730 |                32.440 |               9.872 |         25 |              0.080 |              0.083 |          0.044 |          0.057 |
| F_obj                                           |          0.880 | 0.725 |                32.840 |               9.966 |         25 |              0.080 |              0.083 |          0.049 |          0.063 |
| F_tgt                                           |          0.640 | 0.503 |                77.640 |               7.013 |         25 |              0.320 |              0.333 |          0.270 |          0.349 |
| F_mat                                           |          0.800 | 0.657 |                47.800 |               8.937 |         25 |              0.160 |              0.167 |          0.117 |          0.151 |
| F_light                                         |          0.960 | 0.774 |                17.640 |              10.981 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.680 | 0.540 |                71.320 |               7.362 |         25 |              0.280 |              0.292 |          0.234 |          0.302 |
| B_L1 (materials + lighting)                     |          0.720 | 0.589 |                63.200 |               7.843 |         25 |              0.240 |              0.250 |          0.184 |          0.238 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.555 |                70.960 |               7.339 |         25 |              0.280 |              0.292 |          0.219 |          0.283 |
| B_L2 (+ object appearance)                      |          0.120 | 0.098 |               176.600 |               0.153 |         25 |              0.840 |              0.875 |          0.676 |          0.874 |
| B_L3 (+ distractors)                            |          0.120 | 0.098 |               176.600 |               0.147 |         25 |              0.840 |              0.875 |          0.676 |          0.874 |

- **F_objall: success drop 0.720 absolute, 75.0% relative · SPL drop 0.578 absolute**
- **F_clut: success drop 0.080 absolute, 8.3% relative · SPL drop 0.044 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.049 absolute**
- **F_tgt: success drop 0.320 absolute, 33.3% relative · SPL drop 0.270 absolute**
- **F_mat: success drop 0.160 absolute, 16.7% relative · SPL drop 0.117 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.280 absolute, 29.2% relative · SPL drop 0.234 absolute**
- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.184 absolute**
- **L2noT: success drop 0.280 absolute, 29.2% relative · SPL drop 0.219 absolute**
- **L2: success drop 0.840 absolute, 87.5% relative · SPL drop 0.676 absolute**
- **L3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.676 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
