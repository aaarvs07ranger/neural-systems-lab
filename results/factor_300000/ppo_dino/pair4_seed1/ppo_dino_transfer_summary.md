# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.728 |                26.520 |              12.565 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.687 |                33.640 |              11.805 |         25 |              0.040 |              0.042 |          0.040 |          0.055 |
| F_clut                                          |          0.960 | 0.730 |                26.400 |              12.570 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          0.920 | 0.707 |                33.880 |              11.809 |         25 |              0.040 |              0.042 |          0.021 |          0.029 |
| F_tgt                                           |          0.960 | 0.713 |                26.520 |              12.551 |         25 |              0.000 |              0.000 |          0.015 |          0.020 |
| F_mat                                           |          0.640 | 0.406 |                82.760 |               7.867 |         25 |              0.320 |              0.333 |          0.322 |          0.442 |
| F_light                                         |          0.960 | 0.750 |                26.480 |              12.564 |         25 |              0.000 |              0.000 |         -0.022 |         -0.031 |
| F_sky                                           |          0.960 | 0.715 |                26.920 |              12.565 |         25 |              0.000 |              0.000 |          0.012 |          0.017 |
| B_L1 (materials + lighting)                     |          0.640 | 0.404 |                83.360 |               7.841 |         25 |              0.320 |              0.333 |          0.324 |          0.445 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.520 | 0.304 |               104.560 |               6.477 |         25 |              0.440 |              0.458 |          0.423 |          0.582 |
| B_L2 (+ object appearance)                      |          0.680 | 0.444 |                75.880 |               8.672 |         25 |              0.280 |              0.292 |          0.284 |          0.390 |
| B_L3 (+ distractors)                            |          0.560 | 0.330 |                97.200 |               6.933 |         25 |              0.400 |              0.417 |          0.398 |          0.547 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.040 absolute, 4.2% relative · SPL drop 0.021 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.322 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.324 absolute**
- **L2noT: success drop 0.440 absolute, 45.8% relative · SPL drop 0.423 absolute**
- **L2: success drop 0.280 absolute, 29.2% relative · SPL drop 0.284 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.398 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
