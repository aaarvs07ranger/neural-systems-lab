# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.808 |                11.280 |              11.604 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.200 | 0.188 |               162.160 |               1.501 |         25 |              0.800 |              0.800 |          0.620 |          0.767 |
| F_clut                                          |          1.000 | 0.808 |                11.200 |              11.605 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.760 |                19.320 |              11.093 |         25 |              0.040 |              0.040 |          0.048 |          0.060 |
| F_tgt                                           |          0.360 | 0.310 |               131.400 |               3.587 |         25 |              0.640 |              0.640 |          0.498 |          0.616 |
| F_mat                                           |          0.520 | 0.441 |               100.920 |               4.688 |         25 |              0.480 |              0.480 |          0.367 |          0.454 |
| F_light                                         |          1.000 | 0.814 |                11.160 |              11.599 |         25 |              0.000 |              0.000 |         -0.006 |         -0.008 |
| F_sky                                           |          0.400 | 0.346 |               124.760 |               3.433 |         25 |              0.600 |              0.600 |          0.462 |          0.572 |
| B_L1 (materials + lighting)                     |          0.480 | 0.395 |               109.960 |               4.667 |         25 |              0.520 |              0.520 |          0.413 |          0.511 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.480 | 0.379 |               111.440 |               4.770 |         25 |              0.520 |              0.520 |          0.430 |          0.532 |
| B_L2 (+ object appearance)                      |          0.240 | 0.211 |               155.800 |               1.567 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |
| B_L3 (+ distractors)                            |          0.240 | 0.211 |               155.800 |               1.567 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |

- **F_objall: success drop 0.800 absolute, 80.0% relative · SPL drop 0.620 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.048 absolute**
- **F_tgt: success drop 0.640 absolute, 64.0% relative · SPL drop 0.498 absolute**
- **F_mat: success drop 0.480 absolute, 48.0% relative · SPL drop 0.367 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_sky: success drop 0.600 absolute, 60.0% relative · SPL drop 0.462 absolute**
- **L1: success drop 0.520 absolute, 52.0% relative · SPL drop 0.413 absolute**
- **L2noT: success drop 0.520 absolute, 52.0% relative · SPL drop 0.430 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
