# PPO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                34.760 |              11.415 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.040 | 0.040 |               192.160 |              -0.291 |         25 |              0.880 |              0.957 |          0.658 |          0.943 |
| F_clut                                          |          0.920 | 0.698 |                34.760 |              11.415 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.670 |                41.440 |              10.786 |         25 |              0.040 |              0.043 |          0.028 |          0.040 |
| F_tgt                                           |          0.040 | 0.040 |               192.160 |              -0.197 |         25 |              0.880 |              0.957 |          0.658 |          0.943 |
| F_mat                                           |          0.200 | 0.155 |               162.360 |               0.882 |         25 |              0.720 |              0.783 |          0.543 |          0.777 |
| F_light                                         |          0.920 | 0.710 |                33.960 |              11.290 |         25 |              0.000 |              0.000 |         -0.012 |         -0.016 |
| F_sky                                           |          0.400 | 0.279 |               125.320 |               3.503 |         25 |              0.520 |              0.565 |          0.419 |          0.600 |
| B_L1 (materials + lighting)                     |          0.200 | 0.155 |               162.240 |               0.688 |         25 |              0.720 |              0.783 |          0.543 |          0.777 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.200 | 0.155 |               162.240 |               0.684 |         25 |              0.720 |              0.783 |          0.543 |          0.777 |
| B_L2 (+ object appearance)                      |          0.120 | 0.102 |               176.960 |              -0.447 |         25 |              0.800 |              0.870 |          0.596 |          0.854 |
| B_L3 (+ distractors)                            |          0.120 | 0.102 |               176.960 |              -0.447 |         25 |              0.800 |              0.870 |          0.596 |          0.854 |

- **F_objall: success drop 0.880 absolute, 95.7% relative · SPL drop 0.658 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.3% relative · SPL drop 0.028 absolute**
- **F_tgt: success drop 0.880 absolute, 95.7% relative · SPL drop 0.658 absolute**
- **F_mat: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **F_sky: success drop 0.520 absolute, 56.5% relative · SPL drop 0.419 absolute**
- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **L2noT: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.596 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.596 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
