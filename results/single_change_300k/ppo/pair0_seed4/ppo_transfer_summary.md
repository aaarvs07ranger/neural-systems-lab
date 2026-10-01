# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.742 |                25.160 |              10.488 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.040 | 0.040 |               192.080 |              -1.148 |         25 |              0.880 |              0.957 |          0.702 |          0.946 |
| F_clut                                          |          0.880 | 0.705 |                32.400 |               9.898 |         25 |              0.040 |              0.043 |          0.037 |          0.050 |
| F_obj                                           |          0.920 | 0.734 |                25.280 |              10.501 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |
| F_tgt                                           |          0.360 | 0.289 |               132.720 |               3.290 |         25 |              0.560 |              0.609 |          0.453 |          0.610 |
| F_mat                                           |          0.720 | 0.589 |                63.400 |               7.692 |         25 |              0.200 |              0.217 |          0.153 |          0.206 |
| F_light                                         |          0.920 | 0.742 |                25.160 |              10.492 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.600 | 0.535 |                85.200 |               6.109 |         25 |              0.320 |              0.348 |          0.207 |          0.279 |
| B_L1 (materials + lighting)                     |          0.600 | 0.511 |                84.680 |               6.165 |         25 |              0.320 |              0.348 |          0.231 |          0.311 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.393 |               114.640 |               4.000 |         25 |              0.480 |              0.522 |          0.349 |          0.470 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.565 |         25 |              0.920 |              1.000 |          0.742 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.615 |         25 |              0.920 |              1.000 |          0.742 |          1.000 |

- **F_objall: success drop 0.880 absolute, 95.7% relative · SPL drop 0.702 absolute**
- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.037 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_tgt: success drop 0.560 absolute, 60.9% relative · SPL drop 0.453 absolute**
- **F_mat: success drop 0.200 absolute, 21.7% relative · SPL drop 0.153 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.320 absolute, 34.8% relative · SPL drop 0.207 absolute**
- **L1: success drop 0.320 absolute, 34.8% relative · SPL drop 0.231 absolute**
- **L2noT: success drop 0.480 absolute, 52.2% relative · SPL drop 0.349 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.742 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.742 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
