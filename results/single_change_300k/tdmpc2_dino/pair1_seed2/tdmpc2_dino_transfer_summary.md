# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.701 |                15.040 |              10.306 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.700 |                15.520 |              10.323 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_clut                                          |          1.000 | 0.714 |                12.480 |              10.835 |         25 |             -0.040 |             -0.042 |         -0.012 |         -0.018 |
| F_obj                                           |          0.960 | 0.699 |                15.600 |              10.295 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_tgt                                           |          0.960 | 0.698 |                15.560 |              10.314 |         25 |              0.000 |              0.000 |          0.003 |          0.005 |
| F_mat                                           |          0.880 | 0.602 |                38.280 |               9.189 |         25 |              0.080 |              0.083 |          0.100 |          0.142 |
| F_light                                         |          0.960 | 0.701 |                15.040 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.960 | 0.697 |                15.280 |              10.300 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| B_L1 (materials + lighting)                     |          0.960 | 0.651 |                25.280 |              10.234 |         25 |              0.000 |              0.000 |          0.051 |          0.072 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.594 |                46.040 |               9.069 |         25 |              0.080 |              0.083 |          0.108 |          0.154 |
| B_L2 (+ object appearance)                      |          0.760 | 0.543 |                67.640 |               7.564 |         25 |              0.200 |              0.208 |          0.158 |          0.225 |
| B_L3 (+ distractors)                            |          0.760 | 0.573 |                70.680 |               7.579 |         25 |              0.200 |              0.208 |          0.129 |          0.184 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.012 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.100 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.051 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.108 absolute**
- **L2: success drop 0.200 absolute, 20.8% relative · SPL drop 0.158 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.129 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
