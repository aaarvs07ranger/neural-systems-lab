# PPO_AUG zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.733 |                27.160 |              12.483 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.880 | 0.655 |                40.560 |              11.071 |         25 |              0.080 |              0.083 |          0.078 |          0.106 |
| F_clut                                          |          0.960 | 0.733 |                27.160 |              12.483 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.648 |                40.560 |              11.082 |         25 |              0.080 |              0.083 |          0.085 |          0.116 |
| F_tgt                                           |          0.960 | 0.734 |                27.120 |              12.483 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                                           |          0.000 | 0.000 |               200.000 |              -2.751 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |
| F_light                                         |          0.920 | 0.711 |                33.720 |              11.814 |         25 |              0.040 |              0.042 |          0.021 |          0.029 |
| F_sky                                           |          0.840 | 0.663 |                50.000 |              10.916 |         25 |              0.120 |              0.125 |          0.070 |          0.096 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.340 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.211 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.213 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.213 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |

- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.078 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.085 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**
- **F_light: success drop 0.040 absolute, 4.2% relative · SPL drop 0.021 absolute**
- **F_sky: success drop 0.120 absolute, 12.5% relative · SPL drop 0.070 absolute**
- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**
- **L2noT: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
