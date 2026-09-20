# PPO_AUG zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.733 |                28.680 |              11.969 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.480 | 0.364 |               114.240 |               5.957 |         25 |              0.480 |              0.500 |          0.368 |          0.503 |
| F_clut                                          |          0.960 | 0.733 |                28.680 |              11.959 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.670 |                42.560 |              10.835 |         25 |              0.080 |              0.083 |          0.062 |          0.085 |
| F_tgt                                           |          0.760 | 0.561 |                65.560 |               9.485 |         25 |              0.200 |              0.208 |          0.172 |          0.234 |
| F_mat                                           |          0.640 | 0.505 |                81.960 |               6.592 |         25 |              0.320 |              0.333 |          0.227 |          0.310 |
| F_light                                         |          0.840 | 0.627 |                50.160 |              10.368 |         25 |              0.120 |              0.125 |          0.106 |          0.145 |
| F_sky                                           |          0.680 | 0.521 |                74.360 |               7.489 |         25 |              0.280 |              0.292 |          0.212 |          0.289 |
| B_L1 (materials + lighting)                     |          0.440 | 0.283 |               120.320 |               3.579 |         25 |              0.520 |              0.542 |          0.450 |          0.614 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.285 |               119.680 |               3.672 |         25 |              0.520 |              0.542 |          0.447 |          0.611 |
| B_L2 (+ object appearance)                      |          0.360 | 0.238 |               134.480 |               2.460 |         25 |              0.600 |              0.625 |          0.495 |          0.675 |
| B_L3 (+ distractors)                            |          0.360 | 0.238 |               134.480 |               2.426 |         25 |              0.600 |              0.625 |          0.495 |          0.675 |

- **F_objall: success drop 0.480 absolute, 50.0% relative · SPL drop 0.368 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.062 absolute**
- **F_tgt: success drop 0.200 absolute, 20.8% relative · SPL drop 0.172 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.227 absolute**
- **F_light: success drop 0.120 absolute, 12.5% relative · SPL drop 0.106 absolute**
- **F_sky: success drop 0.280 absolute, 29.2% relative · SPL drop 0.212 absolute**
- **L1: success drop 0.520 absolute, 54.2% relative · SPL drop 0.450 absolute**
- **L2noT: success drop 0.520 absolute, 54.2% relative · SPL drop 0.447 absolute**
- **L2: success drop 0.600 absolute, 62.5% relative · SPL drop 0.495 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
