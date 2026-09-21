# PPO_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.705 |                13.960 |              10.317 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.665 |                21.840 |               9.828 |         25 |              0.040 |              0.042 |          0.040 |          0.057 |
| F_clut                                          |          0.960 | 0.705 |                14.040 |              10.311 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.960 | 0.705 |                13.880 |              10.310 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_tgt                                           |          0.920 | 0.665 |                21.720 |               9.831 |         25 |              0.040 |              0.042 |          0.040 |          0.057 |
| F_mat                                           |          0.880 | 0.610 |                30.280 |               9.388 |         25 |              0.080 |              0.083 |          0.095 |          0.135 |
| F_light                                         |          0.960 | 0.683 |                14.600 |              10.397 |         25 |              0.000 |              0.000 |          0.022 |          0.031 |
| F_sky                                           |          0.960 | 0.682 |                14.600 |              10.397 |         25 |              0.000 |              0.000 |          0.023 |          0.033 |
| B_L1 (materials + lighting)                     |          0.920 | 0.650 |                22.520 |               9.876 |         25 |              0.040 |              0.042 |          0.055 |          0.078 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.607 |                30.480 |               9.384 |         25 |              0.080 |              0.083 |          0.098 |          0.139 |
| B_L2 (+ object appearance)                      |          0.840 | 0.564 |                38.400 |               8.927 |         25 |              0.120 |              0.125 |          0.141 |          0.200 |
| B_L3 (+ distractors)                            |          0.920 | 0.644 |                22.760 |               9.909 |         25 |              0.040 |              0.042 |          0.061 |          0.086 |

- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_tgt: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.095 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.022 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.023 absolute**
- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.055 absolute**
- **L2noT: success drop 0.080 absolute, 8.3% relative · SPL drop 0.098 absolute**
- **L2: success drop 0.120 absolute, 12.5% relative · SPL drop 0.141 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.061 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
