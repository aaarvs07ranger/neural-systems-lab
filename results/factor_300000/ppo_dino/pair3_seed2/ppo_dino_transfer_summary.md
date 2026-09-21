# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.653 |                40.520 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.760 | 0.570 |                61.240 |               9.350 |         25 |              0.120 |              0.136 |          0.084 |          0.128 |
| F_clut                                          |          0.920 | 0.682 |                34.120 |              11.487 |         25 |             -0.040 |             -0.045 |         -0.029 |         -0.044 |
| F_obj                                           |          0.760 | 0.574 |                62.520 |               9.249 |         25 |              0.120 |              0.136 |          0.079 |          0.121 |
| F_tgt                                           |          0.880 | 0.669 |                39.000 |              10.835 |         25 |              0.000 |              0.000 |         -0.015 |         -0.024 |
| F_mat                                           |          0.640 | 0.498 |                82.880 |               7.146 |         25 |              0.240 |              0.273 |          0.156 |          0.238 |
| F_light                                         |          0.880 | 0.653 |                40.600 |              10.852 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.880 | 0.653 |                40.640 |              10.860 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.680 | 0.522 |                77.960 |               7.747 |         25 |              0.200 |              0.227 |          0.132 |          0.201 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.480 |                93.080 |               6.696 |         25 |              0.280 |              0.318 |          0.173 |          0.265 |
| B_L2 (+ object appearance)                      |          0.400 | 0.323 |               128.120 |               4.094 |         25 |              0.480 |              0.545 |          0.330 |          0.506 |
| B_L3 (+ distractors)                            |          0.400 | 0.324 |               128.320 |               4.096 |         25 |              0.480 |              0.545 |          0.329 |          0.503 |

- **F_objall: success drop 0.120 absolute, 13.6% relative · SPL drop 0.084 absolute**
- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.029 absolute**
- **F_obj: success drop 0.120 absolute, 13.6% relative · SPL drop 0.079 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.015 absolute**
- **F_mat: success drop 0.240 absolute, 27.3% relative · SPL drop 0.156 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.200 absolute, 22.7% relative · SPL drop 0.132 absolute**
- **L2noT: success drop 0.280 absolute, 31.8% relative · SPL drop 0.173 absolute**
- **L2: success drop 0.480 absolute, 54.5% relative · SPL drop 0.330 absolute**
- **L3: success drop 0.480 absolute, 54.5% relative · SPL drop 0.329 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
