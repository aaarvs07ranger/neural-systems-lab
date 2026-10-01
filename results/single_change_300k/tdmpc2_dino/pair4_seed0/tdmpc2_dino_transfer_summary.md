# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.785 |                19.560 |              13.234 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.734 |                35.840 |              12.004 |         25 |              0.080 |              0.080 |          0.052 |          0.066 |
| F_clut                                          |          1.000 | 0.811 |                19.040 |              13.244 |         25 |              0.000 |              0.000 |         -0.025 |         -0.032 |
| F_obj                                           |          0.960 | 0.768 |                27.720 |              12.607 |         25 |              0.040 |              0.040 |          0.018 |          0.022 |
| F_tgt                                           |          1.000 | 0.814 |                18.280 |              13.222 |         25 |              0.000 |              0.000 |         -0.029 |         -0.037 |
| F_mat                                           |          0.880 | 0.650 |                44.280 |              11.384 |         25 |              0.120 |              0.120 |          0.136 |          0.173 |
| F_light                                         |          0.960 | 0.778 |                24.800 |              12.675 |         25 |              0.040 |              0.040 |          0.007 |          0.009 |
| F_sky                                           |          0.960 | 0.751 |                25.600 |              12.624 |         25 |              0.040 |              0.040 |          0.034 |          0.043 |
| B_L1 (materials + lighting)                     |          0.920 | 0.683 |                47.040 |              11.867 |         25 |              0.080 |              0.080 |          0.103 |          0.131 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.880 | 0.626 |                49.040 |              11.469 |         25 |              0.120 |              0.120 |          0.159 |          0.203 |
| B_L2 (+ object appearance)                      |          0.920 | 0.634 |                43.000 |              11.904 |         25 |              0.080 |              0.080 |          0.151 |          0.192 |
| B_L3 (+ distractors)                            |          0.800 | 0.532 |                60.440 |              10.166 |         25 |              0.200 |              0.200 |          0.253 |          0.322 |

- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.052 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.025 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.018 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.029 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.136 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.007 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.034 absolute**
- **L1: success drop 0.080 absolute, 8.0% relative · SPL drop 0.103 absolute**
- **L2noT: success drop 0.120 absolute, 12.0% relative · SPL drop 0.159 absolute**
- **L2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.151 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.253 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
