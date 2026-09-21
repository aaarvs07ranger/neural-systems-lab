# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.738 |                14.320 |              10.230 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.652 |                37.360 |               8.786 |         25 |              0.120 |              0.125 |          0.086 |          0.116 |
| F_clut                                          |          0.960 | 0.738 |                14.320 |              10.230 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.840 | 0.652 |                37.360 |               8.786 |         25 |              0.120 |              0.125 |          0.086 |          0.116 |
| F_mat                                           |          0.880 | 0.692 |                30.280 |               9.250 |         25 |              0.080 |              0.083 |          0.046 |          0.062 |
| F_light                                         |          0.920 | 0.698 |                22.600 |               9.756 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| F_sky                                           |          0.880 | 0.692 |                29.720 |               9.282 |         25 |              0.080 |              0.083 |          0.046 |          0.062 |
| B_L1 (materials + lighting)                     |          0.800 | 0.645 |                45.680 |               8.216 |         25 |              0.160 |              0.167 |          0.092 |          0.125 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.840 | 0.651 |                38.520 |               8.687 |         25 |              0.120 |              0.125 |          0.087 |          0.117 |
| B_L2 (+ object appearance)                      |          0.840 | 0.651 |                38.520 |               8.687 |         25 |              0.120 |              0.125 |          0.087 |          0.117 |
| B_L3 (+ distractors)                            |          0.880 | 0.691 |                31.000 |               9.164 |         25 |              0.080 |              0.083 |          0.047 |          0.063 |

- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.086 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.120 absolute, 12.5% relative · SPL drop 0.086 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.046 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_sky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.046 absolute**
- **L1: success drop 0.160 absolute, 16.7% relative · SPL drop 0.092 absolute**
- **L2noT: success drop 0.120 absolute, 12.5% relative · SPL drop 0.087 absolute**
- **L2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.087 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.047 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
