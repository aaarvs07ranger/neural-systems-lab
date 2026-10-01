# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.658 |                29.600 |               9.436 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.681 |                14.440 |              10.407 |         25 |             -0.080 |             -0.091 |         -0.023 |         -0.035 |
| F_clut                                          |          0.880 | 0.658 |                29.600 |               9.436 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.670 |                22.080 |               9.916 |         25 |             -0.040 |             -0.045 |         -0.011 |         -0.017 |
| F_tgt                                           |          0.920 | 0.661 |                22.240 |               9.907 |         25 |             -0.040 |             -0.045 |         -0.003 |         -0.004 |
| F_mat                                           |          0.800 | 0.564 |                45.080 |               8.359 |         25 |              0.080 |              0.091 |          0.094 |          0.143 |
| F_light                                         |          0.880 | 0.658 |                29.560 |               9.429 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.840 | 0.618 |                37.280 |               8.914 |         25 |              0.040 |              0.045 |          0.040 |          0.061 |
| B_L1 (materials + lighting)                     |          0.840 | 0.604 |                37.520 |               8.875 |         25 |              0.040 |              0.045 |          0.054 |          0.082 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.564 |                45.120 |               8.359 |         25 |              0.080 |              0.091 |          0.094 |          0.143 |
| B_L2 (+ object appearance)                      |          0.840 | 0.554 |                37.680 |               8.881 |         25 |              0.040 |              0.045 |          0.104 |          0.158 |
| B_L3 (+ distractors)                            |          0.840 | 0.576 |                37.640 |               8.869 |         25 |              0.040 |              0.045 |          0.083 |          0.126 |

- **F_objall: success drop -0.080 absolute, -9.1% relative · SPL drop -0.023 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop -0.040 absolute, -4.5% relative · SPL drop -0.011 absolute**
- **F_tgt: success drop -0.040 absolute, -4.5% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.080 absolute, 9.1% relative · SPL drop 0.094 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **L1: success drop 0.040 absolute, 4.5% relative · SPL drop 0.054 absolute**
- **L2noT: success drop 0.080 absolute, 9.1% relative · SPL drop 0.094 absolute**
- **L2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.104 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.083 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
