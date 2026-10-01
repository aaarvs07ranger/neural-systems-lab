# TDMPC2_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.780 |                12.880 |              10.657 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.780 |                12.560 |              10.644 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_clut                                          |          1.000 | 0.780 |                 9.960 |              10.681 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          1.000 | 0.780 |                 8.040 |              10.699 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                                           |          1.000 | 0.777 |                11.120 |              10.664 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_light                                         |          1.000 | 0.779 |                12.200 |              10.665 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_sky                                           |          1.000 | 0.778 |                12.480 |              10.673 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| B_L1 (materials + lighting)                     |          1.000 | 0.778 |                16.480 |              10.628 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.776 |                17.800 |              10.621 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| B_L2 (+ object appearance)                      |          1.000 | 0.778 |                13.520 |              10.643 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| B_L3 (+ distractors)                            |          1.000 | 0.779 |                10.360 |              10.695 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
