# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.040 | 0.023 |               198.160 |               0.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.240 | 0.161 |               177.560 |               3.190 |         25 |             -0.200 |             -5.000 |         -0.138 |         -5.993 |
| F_clut                                          |          0.120 | 0.056 |               189.640 |               1.804 |         25 |             -0.080 |             -2.000 |         -0.033 |         -1.413 |
| F_obj                                           |          0.000 | 0.000 |               200.000 |               0.282 |         25 |              0.040 |              1.000 |          0.023 |          1.000 |
| F_tgt                                           |          0.240 | 0.139 |               170.640 |               3.246 |         25 |             -0.200 |             -5.000 |         -0.116 |         -5.006 |
| F_mat                                           |          0.200 | 0.159 |               176.160 |               0.981 |         25 |             -0.160 |             -4.000 |         -0.136 |         -5.903 |
| F_light                                         |          0.080 | 0.038 |               188.920 |               1.418 |         25 |             -0.040 |             -1.000 |         -0.015 |         -0.652 |
| F_sky                                           |          0.040 | 0.024 |               198.080 |               0.897 |         25 |              0.000 |              0.000 |         -0.000 |         -0.019 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.682 |         25 |              0.040 |              1.000 |          0.023 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.335 |         25 |              0.040 |              1.000 |          0.023 |          1.000 |
| B_L2 (+ object appearance)                      |          0.080 | 0.080 |               187.560 |              -1.419 |         25 |             -0.040 |             -1.000 |         -0.057 |         -2.466 |
| B_L3 (+ distractors)                            |          0.120 | 0.086 |               182.160 |              -0.892 |         25 |             -0.080 |             -2.000 |         -0.063 |         -2.714 |

- **F_objall: success drop -0.200 absolute, -500.0% relative · SPL drop -0.138 absolute**
- **F_clut: success drop -0.080 absolute, -200.0% relative · SPL drop -0.033 absolute**
- **F_obj: success drop 0.040 absolute, 100.0% relative · SPL drop 0.023 absolute**
- **F_tgt: success drop -0.200 absolute, -500.0% relative · SPL drop -0.116 absolute**
- **F_mat: success drop -0.160 absolute, -400.0% relative · SPL drop -0.136 absolute**
- **F_light: success drop -0.040 absolute, -100.0% relative · SPL drop -0.015 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **L1: success drop 0.040 absolute, 100.0% relative · SPL drop 0.023 absolute**
- **L2noT: success drop 0.040 absolute, 100.0% relative · SPL drop 0.023 absolute**
- **L2: success drop -0.040 absolute, -100.0% relative · SPL drop -0.057 absolute**
- **L3: success drop -0.080 absolute, -200.0% relative · SPL drop -0.063 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
