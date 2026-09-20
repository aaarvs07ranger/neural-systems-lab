# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.817 |                14.720 |              11.545 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.200 | 0.165 |               167.440 |               1.510 |         25 |              0.800 |              0.800 |          0.652 |          0.798 |
| F_clut                                          |          1.000 | 0.817 |                14.720 |              11.545 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.788 |                15.400 |              11.548 |         25 |              0.000 |              0.000 |          0.029 |          0.035 |
| F_tgt                                           |          0.080 | 0.080 |               184.200 |               0.198 |         25 |              0.920 |              0.920 |          0.737 |          0.902 |
| F_mat                                           |          0.280 | 0.237 |               146.800 |               1.719 |         25 |              0.720 |              0.720 |          0.579 |          0.709 |
| F_light                                         |          1.000 | 0.813 |                14.840 |              11.555 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_sky                                           |          0.120 | 0.112 |               176.880 |              -0.175 |         25 |              0.880 |              0.880 |          0.705 |          0.863 |
| B_L1 (materials + lighting)                     |          0.960 | 0.778 |                24.120 |              11.006 |         25 |              0.040 |              0.040 |          0.039 |          0.048 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.666 |                42.480 |               9.783 |         25 |              0.120 |              0.120 |          0.150 |          0.184 |
| B_L2 (+ object appearance)                      |          0.120 | 0.120 |               177.600 |              -0.122 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |
| B_L3 (+ distractors)                            |          0.120 | 0.120 |               177.600 |              -0.143 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |

- **F_objall: success drop 0.800 absolute, 80.0% relative · SPL drop 0.652 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.029 absolute**
- **F_tgt: success drop 0.920 absolute, 92.0% relative · SPL drop 0.737 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.579 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_sky: success drop 0.880 absolute, 88.0% relative · SPL drop 0.705 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.150 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
