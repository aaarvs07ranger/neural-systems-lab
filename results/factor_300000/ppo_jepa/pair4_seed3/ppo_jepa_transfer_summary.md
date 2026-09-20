# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.725 |                27.800 |              12.573 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.670 |                34.720 |              12.093 |         25 |              0.040 |              0.042 |          0.055 |          0.076 |
| F_clut                                          |          0.960 | 0.727 |                27.840 |              12.571 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          0.960 | 0.723 |                27.800 |              12.575 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_tgt                                           |          0.960 | 0.713 |                27.640 |              12.555 |         25 |              0.000 |              0.000 |          0.013 |          0.017 |
| F_mat                                           |          0.520 | 0.358 |               105.760 |               5.761 |         25 |              0.440 |              0.458 |          0.368 |          0.507 |
| F_light                                         |          0.920 | 0.696 |                34.560 |              11.888 |         25 |              0.040 |              0.042 |          0.029 |          0.040 |
| F_sky                                           |          0.960 | 0.727 |                27.800 |              12.567 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| B_L1 (materials + lighting)                     |          0.560 | 0.357 |                98.440 |               6.136 |         25 |              0.400 |              0.417 |          0.368 |          0.507 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.320 | 0.209 |               140.400 |               3.562 |         25 |              0.640 |              0.667 |          0.517 |          0.712 |
| B_L2 (+ object appearance)                      |          0.400 | 0.288 |               126.880 |               4.397 |         25 |              0.560 |              0.583 |          0.438 |          0.603 |
| B_L3 (+ distractors)                            |          0.320 | 0.241 |               140.880 |               3.276 |         25 |              0.640 |              0.667 |          0.485 |          0.668 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.055 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **F_mat: success drop 0.440 absolute, 45.8% relative · SPL drop 0.368 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.029 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L1: success drop 0.400 absolute, 41.7% relative · SPL drop 0.368 absolute**
- **L2noT: success drop 0.640 absolute, 66.7% relative · SPL drop 0.517 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.438 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.485 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
