# PPO_JEPA zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.774 |                15.760 |              10.204 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.774 |                16.240 |              10.200 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut                                          |          1.000 | 0.779 |                 8.200 |              10.680 |         25 |             -0.040 |             -0.042 |         -0.006 |         -0.007 |
| F_obj                                           |          0.960 | 0.774 |                16.240 |              10.200 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                                           |          0.680 | 0.483 |                70.920 |               6.619 |         25 |              0.280 |              0.292 |          0.290 |          0.375 |
| F_light                                         |          0.960 | 0.772 |                16.280 |              10.205 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_sky                                           |          0.960 | 0.772 |                15.760 |              10.204 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| B_L1 (materials + lighting)                     |          0.160 | 0.160 |               168.640 |               0.147 |         25 |              0.800 |              0.833 |          0.614 |          0.793 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.440 |               115.800 |               3.553 |         25 |              0.520 |              0.542 |          0.334 |          0.431 |
| B_L2 (+ object appearance)                      |          0.440 | 0.440 |               115.800 |               3.553 |         25 |              0.520 |              0.542 |          0.334 |          0.431 |
| B_L3 (+ distractors)                            |          0.440 | 0.440 |               115.800 |               3.553 |         25 |              0.520 |              0.542 |          0.334 |          0.431 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.006 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.280 absolute, 29.2% relative · SPL drop 0.290 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L1: success drop 0.800 absolute, 83.3% relative · SPL drop 0.614 absolute**
- **L2noT: success drop 0.520 absolute, 54.2% relative · SPL drop 0.334 absolute**
- **L2: success drop 0.520 absolute, 54.2% relative · SPL drop 0.334 absolute**
- **L3: success drop 0.520 absolute, 54.2% relative · SPL drop 0.334 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
