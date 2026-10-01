# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.761 |                21.360 |              12.586 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.722 |                33.960 |              12.021 |         25 |              0.040 |              0.040 |          0.040 |          0.052 |
| F_clut                                          |          1.000 | 0.762 |                21.480 |              12.578 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_obj                                           |          1.000 | 0.759 |                20.480 |              12.592 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_tgt                                           |          1.000 | 0.757 |                20.840 |              12.581 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |
| F_mat                                           |          0.840 | 0.624 |                58.720 |              10.183 |         25 |              0.160 |              0.160 |          0.137 |          0.180 |
| F_light                                         |          1.000 | 0.762 |                19.840 |              12.608 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_sky                                           |          1.000 | 0.761 |                20.440 |              12.567 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.590 |                88.120 |               8.821 |         25 |              0.240 |              0.240 |          0.172 |          0.226 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.680 | 0.472 |                94.480 |               7.520 |         25 |              0.320 |              0.320 |          0.289 |          0.380 |
| B_L2 (+ object appearance)                      |          0.440 | 0.295 |               147.720 |               4.491 |         25 |              0.560 |              0.560 |          0.467 |          0.613 |
| B_L3 (+ distractors)                            |          0.400 | 0.310 |               131.000 |               4.069 |         25 |              0.600 |              0.600 |          0.451 |          0.592 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.040 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_mat: success drop 0.160 absolute, 16.0% relative · SPL drop 0.137 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.172 absolute**
- **L2noT: success drop 0.320 absolute, 32.0% relative · SPL drop 0.289 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.467 absolute**
- **L3: success drop 0.600 absolute, 60.0% relative · SPL drop 0.451 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
