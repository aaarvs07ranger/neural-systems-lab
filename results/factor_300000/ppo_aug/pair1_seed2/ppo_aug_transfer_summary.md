# PPO_AUG zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.719 |                 9.840 |              10.824 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.610 |                41.680 |               8.883 |         25 |              0.160 |              0.160 |          0.110 |          0.152 |
| F_clut                                          |          0.960 | 0.711 |                17.240 |              10.321 |         25 |              0.040 |              0.040 |          0.008 |          0.011 |
| F_obj                                           |          0.960 | 0.711 |                17.200 |              10.314 |         25 |              0.040 |              0.040 |          0.008 |          0.011 |
| F_tgt                                           |          0.880 | 0.588 |                35.040 |               9.375 |         25 |              0.120 |              0.120 |          0.131 |          0.182 |
| F_mat                                           |          0.200 | 0.138 |               160.960 |               0.271 |         25 |              0.800 |              0.800 |          0.581 |          0.808 |
| F_light                                         |          1.000 | 0.719 |                 9.840 |              10.824 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          0.920 | 0.671 |                24.840 |               9.797 |         25 |              0.080 |              0.080 |          0.048 |          0.067 |
| B_L1 (materials + lighting)                     |          0.160 | 0.129 |               168.520 |              -0.200 |         25 |              0.840 |              0.840 |          0.590 |          0.821 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.188 |               146.560 |               1.384 |         25 |              0.720 |              0.720 |          0.531 |          0.739 |
| B_L2 (+ object appearance)                      |          0.160 | 0.160 |               169.120 |              -0.130 |         25 |              0.840 |              0.840 |          0.559 |          0.778 |
| B_L3 (+ distractors)                            |          0.160 | 0.160 |               169.120 |              -0.130 |         25 |              0.840 |              0.840 |          0.559 |          0.778 |

- **F_objall: success drop 0.160 absolute, 16.0% relative · SPL drop 0.110 absolute**
- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.008 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.008 absolute**
- **F_tgt: success drop 0.120 absolute, 12.0% relative · SPL drop 0.131 absolute**
- **F_mat: success drop 0.800 absolute, 80.0% relative · SPL drop 0.581 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.048 absolute**
- **L1: success drop 0.840 absolute, 84.0% relative · SPL drop 0.590 absolute**
- **L2noT: success drop 0.720 absolute, 72.0% relative · SPL drop 0.531 absolute**
- **L2: success drop 0.840 absolute, 84.0% relative · SPL drop 0.559 absolute**
- **L3: success drop 0.840 absolute, 84.0% relative · SPL drop 0.559 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
