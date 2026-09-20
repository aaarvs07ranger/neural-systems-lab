# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.717 |                 6.720 |              10.889 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.480 | 0.380 |               106.520 |               4.279 |         25 |              0.520 |              0.520 |          0.338 |          0.471 |
| F_clut                                          |          1.000 | 0.717 |                 6.720 |              10.889 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.637 |                21.920 |               9.849 |         25 |              0.080 |              0.080 |          0.080 |          0.112 |
| F_tgt                                           |          0.320 | 0.268 |               137.520 |               2.390 |         25 |              0.680 |              0.680 |          0.449 |          0.626 |
| F_mat                                           |          0.880 | 0.679 |                31.880 |               9.284 |         25 |              0.120 |              0.120 |          0.038 |          0.053 |
| F_light                                         |          1.000 | 0.717 |                 6.720 |              10.891 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_sky                                           |          0.880 | 0.621 |                29.280 |               9.271 |         25 |              0.120 |              0.120 |          0.096 |          0.135 |
| B_L1 (materials + lighting)                     |          0.760 | 0.635 |                53.680 |               7.671 |         25 |              0.240 |              0.240 |          0.082 |          0.115 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.645 |                46.080 |               8.183 |         25 |              0.200 |              0.200 |          0.072 |          0.101 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **F_objall: success drop 0.520 absolute, 52.0% relative · SPL drop 0.338 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_tgt: success drop 0.680 absolute, 68.0% relative · SPL drop 0.449 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.038 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_sky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.096 absolute**
- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.082 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.072 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
