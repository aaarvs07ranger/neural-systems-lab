# TDMPC2_DINO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.712 |                 9.360 |              10.864 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.716 |                 8.080 |              10.863 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_clut                                          |          1.000 | 0.714 |                 8.240 |              10.863 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          1.000 | 0.709 |                 8.600 |              10.856 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_tgt                                           |          1.000 | 0.716 |                 8.640 |              10.838 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_mat                                           |          0.960 | 0.651 |                24.400 |              10.251 |         25 |              0.040 |              0.040 |          0.061 |          0.086 |
| F_light                                         |          1.000 | 0.711 |                 8.560 |              10.880 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_sky                                           |          1.000 | 0.713 |                 8.280 |              10.864 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| B_L1 (materials + lighting)                     |          0.880 | 0.656 |                37.640 |               9.227 |         25 |              0.120 |              0.120 |          0.056 |          0.078 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.662 |                25.760 |              10.248 |         25 |              0.040 |              0.040 |          0.050 |          0.070 |
| B_L2 (+ object appearance)                      |          0.880 | 0.578 |                34.960 |               9.290 |         25 |              0.120 |              0.120 |          0.134 |          0.188 |
| B_L3 (+ distractors)                            |          1.000 | 0.688 |                18.240 |              10.746 |         25 |              0.000 |              0.000 |          0.024 |          0.034 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.061 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.056 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.050 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.134 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.024 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
