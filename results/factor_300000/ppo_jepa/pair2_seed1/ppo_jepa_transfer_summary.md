# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.651 |                37.240 |               8.792 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.698 |                21.760 |               9.745 |         25 |             -0.080 |             -0.095 |         -0.047 |         -0.073 |
| F_clut                                          |          0.840 | 0.651 |                37.240 |               8.792 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.698 |                21.760 |               9.745 |         25 |             -0.080 |             -0.095 |         -0.047 |         -0.073 |
| F_mat                                           |          0.840 | 0.620 |                37.520 |               8.778 |         25 |              0.000 |              0.000 |          0.031 |          0.047 |
| F_light                                         |          0.920 | 0.698 |                21.800 |               9.750 |         25 |             -0.080 |             -0.095 |         -0.047 |         -0.072 |
| F_sky                                           |          0.800 | 0.612 |                44.920 |               8.310 |         25 |              0.040 |              0.048 |          0.039 |          0.060 |
| B_L1 (materials + lighting)                     |          0.600 | 0.444 |                83.880 |               5.732 |         25 |              0.240 |              0.286 |          0.207 |          0.318 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.484 |                75.960 |               6.248 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |
| B_L2 (+ object appearance)                      |          0.640 | 0.484 |                75.960 |               6.248 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |
| B_L3 (+ distractors)                            |          0.640 | 0.484 |                75.920 |               6.242 |         25 |              0.200 |              0.238 |          0.167 |          0.256 |

- **F_objall: success drop -0.080 absolute, -9.5% relative · SPL drop -0.047 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.080 absolute, -9.5% relative · SPL drop -0.047 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.031 absolute**
- **F_light: success drop -0.080 absolute, -9.5% relative · SPL drop -0.047 absolute**
- **F_sky: success drop 0.040 absolute, 4.8% relative · SPL drop 0.039 absolute**
- **L1: success drop 0.240 absolute, 28.6% relative · SPL drop 0.207 absolute**
- **L2noT: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **L2: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **L3: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
