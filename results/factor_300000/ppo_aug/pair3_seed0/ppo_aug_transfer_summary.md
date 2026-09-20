# PPO_AUG zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.736 |                22.280 |              12.541 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.760 | 0.602 |                62.200 |               9.215 |         25 |              0.240 |              0.240 |          0.134 |          0.182 |
| F_clut                                          |          1.000 | 0.736 |                22.280 |              12.541 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.920 | 0.690 |                35.320 |              11.299 |         25 |              0.080 |              0.080 |          0.047 |          0.063 |
| F_tgt                                           |          1.000 | 0.734 |                23.600 |              12.546 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_mat                                           |          0.040 | 0.026 |               193.000 |              -1.146 |         25 |              0.960 |              0.960 |          0.710 |          0.965 |
| F_light                                         |          1.000 | 0.735 |                22.280 |              12.524 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_sky                                           |          0.840 | 0.612 |                50.040 |              10.214 |         25 |              0.160 |              0.160 |          0.124 |          0.168 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.223 |         25 |              1.000 |              1.000 |          0.736 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.213 |         25 |              1.000 |              1.000 |          0.736 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.212 |         25 |              1.000 |              1.000 |          0.736 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.212 |         25 |              1.000 |              1.000 |          0.736 |          1.000 |

- **F_objall: success drop 0.240 absolute, 24.0% relative · SPL drop 0.134 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.0% relative · SPL drop 0.047 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.710 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.124 absolute**
- **L1: success drop 1.000 absolute, 100.0% relative · SPL drop 0.736 absolute**
- **L2noT: success drop 1.000 absolute, 100.0% relative · SPL drop 0.736 absolute**
- **L2: success drop 1.000 absolute, 100.0% relative · SPL drop 0.736 absolute**
- **L3: success drop 1.000 absolute, 100.0% relative · SPL drop 0.736 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
