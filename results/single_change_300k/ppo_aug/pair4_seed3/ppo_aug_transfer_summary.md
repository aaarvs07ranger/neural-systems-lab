# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.514 |                50.880 |              10.984 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.410 |                93.560 |               7.466 |         25 |              0.240 |              0.286 |          0.104 |          0.202 |
| F_clut                                          |          0.720 | 0.437 |                70.720 |               9.226 |         25 |              0.120 |              0.143 |          0.077 |          0.150 |
| F_obj                                           |          0.560 | 0.372 |               101.120 |               7.033 |         25 |              0.280 |              0.333 |          0.142 |          0.276 |
| F_tgt                                           |          0.840 | 0.535 |                50.200 |              10.909 |         25 |              0.000 |              0.000 |         -0.021 |         -0.041 |
| F_mat                                           |          0.680 | 0.409 |                79.000 |               8.435 |         25 |              0.160 |              0.190 |          0.104 |          0.203 |
| F_light                                         |          0.800 | 0.486 |                57.840 |              10.514 |         25 |              0.040 |              0.048 |          0.027 |          0.053 |
| F_sky                                           |          0.800 | 0.493 |                57.080 |              10.365 |         25 |              0.040 |              0.048 |          0.021 |          0.041 |
| B_L1 (materials + lighting)                     |          0.600 | 0.358 |                92.760 |               7.121 |         25 |              0.240 |              0.286 |          0.156 |          0.303 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.213 |               143.680 |               3.186 |         25 |              0.520 |              0.619 |          0.301 |          0.586 |
| B_L2 (+ object appearance)                      |          0.360 | 0.248 |               135.800 |               3.683 |         25 |              0.480 |              0.571 |          0.266 |          0.518 |
| B_L3 (+ distractors)                            |          0.400 | 0.276 |               128.480 |               4.306 |         25 |              0.440 |              0.524 |          0.238 |          0.463 |

- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.104 absolute**
- **F_clut: success drop 0.120 absolute, 14.3% relative · SPL drop 0.077 absolute**
- **F_obj: success drop 0.280 absolute, 33.3% relative · SPL drop 0.142 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.021 absolute**
- **F_mat: success drop 0.160 absolute, 19.0% relative · SPL drop 0.104 absolute**
- **F_light: success drop 0.040 absolute, 4.8% relative · SPL drop 0.027 absolute**
- **F_sky: success drop 0.040 absolute, 4.8% relative · SPL drop 0.021 absolute**
- **L1: success drop 0.240 absolute, 28.6% relative · SPL drop 0.156 absolute**
- **L2noT: success drop 0.520 absolute, 61.9% relative · SPL drop 0.301 absolute**
- **L2: success drop 0.480 absolute, 57.1% relative · SPL drop 0.266 absolute**
- **L3: success drop 0.440 absolute, 52.4% relative · SPL drop 0.238 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
