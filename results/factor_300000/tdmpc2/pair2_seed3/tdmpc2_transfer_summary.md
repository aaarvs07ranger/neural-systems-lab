# TDMPC2 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                10.520 |              10.685 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.778 |                13.120 |              10.650 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut                                          |          1.000 | 0.778 |                 9.800 |              10.686 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          1.000 | 0.777 |                15.280 |              10.647 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_mat                                           |          1.000 | 0.775 |                34.880 |              10.436 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_light                                         |          1.000 | 0.778 |                 8.880 |              10.714 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_sky                                           |          1.000 | 0.780 |                16.640 |              10.631 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| B_L1 (materials + lighting)                     |          0.960 | 0.734 |                30.560 |              10.062 |         25 |              0.040 |              0.040 |          0.044 |          0.056 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.960 | 0.736 |                34.080 |              10.008 |         25 |              0.040 |              0.040 |          0.042 |          0.054 |
| B_L2 (+ object appearance)                      |          0.880 | 0.652 |                50.320 |               9.013 |         25 |              0.120 |              0.120 |          0.126 |          0.162 |
| B_L3 (+ distractors)                            |          0.960 | 0.735 |                38.320 |               9.973 |         25 |              0.040 |              0.040 |          0.043 |          0.055 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.044 absolute**
- **L2noT: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **L2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.126 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.043 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
