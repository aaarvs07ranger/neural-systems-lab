# PPO_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.769 |                25.680 |              12.609 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.704 |                39.240 |              11.230 |         25 |              0.080 |              0.083 |          0.065 |          0.085 |
| F_clut                                          |          0.960 | 0.770 |                25.640 |              12.576 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_obj                                           |          0.880 | 0.694 |                39.480 |              11.248 |         25 |              0.080 |              0.083 |          0.075 |          0.098 |
| F_tgt                                           |          0.960 | 0.770 |                25.640 |              12.586 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_mat                                           |          0.880 | 0.708 |                40.160 |              11.537 |         25 |              0.080 |              0.083 |          0.061 |          0.079 |
| F_light                                         |          0.960 | 0.769 |                25.720 |              12.570 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_sky                                           |          0.920 | 0.734 |                32.480 |              11.899 |         25 |              0.040 |              0.042 |          0.035 |          0.045 |
| B_L1 (materials + lighting)                     |          0.920 | 0.716 |                33.360 |              12.069 |         25 |              0.040 |              0.042 |          0.053 |          0.069 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.666 |                47.160 |              10.737 |         25 |              0.120 |              0.125 |          0.103 |          0.134 |
| B_L2 (+ object appearance)                      |          0.840 | 0.666 |                47.080 |              10.734 |         25 |              0.120 |              0.125 |          0.103 |          0.134 |
| B_L3 (+ distractors)                            |          0.760 | 0.603 |                60.920 |               9.703 |         25 |              0.200 |              0.208 |          0.166 |          0.216 |

- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.065 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.075 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.061 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_sky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.035 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.053 absolute**
- **L2noT: success drop 0.120 absolute, 12.5% relative · SPL drop 0.103 absolute**
- **L2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.103 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.166 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
