# PPO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.694 |                36.560 |              11.440 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.587 |                56.720 |               9.505 |         25 |              0.120 |              0.130 |          0.107 |          0.155 |
| F_clut                                          |          0.920 | 0.694 |                36.560 |              11.442 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.591 |                56.880 |               9.506 |         25 |              0.120 |              0.130 |          0.103 |          0.148 |
| F_tgt                                           |          0.840 | 0.651 |                50.080 |              10.241 |         25 |              0.080 |              0.087 |          0.043 |          0.062 |
| F_mat                                           |          0.040 | 0.040 |               192.160 |              -1.522 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |
| F_light                                         |          0.960 | 0.734 |                29.080 |              11.910 |         25 |             -0.040 |             -0.043 |         -0.040 |         -0.058 |
| F_sky                                           |          0.960 | 0.727 |                28.760 |              11.906 |         25 |             -0.040 |             -0.043 |         -0.033 |         -0.047 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.999 |         25 |              0.920 |              1.000 |          0.694 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.036 |         25 |              0.920 |              1.000 |          0.694 |          1.000 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.240 |              -1.540 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.240 |              -1.540 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |

- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.107 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.120 absolute, 13.0% relative · SPL drop 0.103 absolute**
- **F_tgt: success drop 0.080 absolute, 8.7% relative · SPL drop 0.043 absolute**
- **F_mat: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**
- **F_light: success drop -0.040 absolute, -4.3% relative · SPL drop -0.040 absolute**
- **F_sky: success drop -0.040 absolute, -4.3% relative · SPL drop -0.033 absolute**
- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.694 absolute**
- **L2noT: success drop 0.920 absolute, 100.0% relative · SPL drop 0.694 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
