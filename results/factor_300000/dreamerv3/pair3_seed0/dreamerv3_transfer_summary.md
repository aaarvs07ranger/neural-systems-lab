# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.688 |                28.480 |              12.756 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.670 |                35.480 |              12.650 |         25 |              0.000 |              0.000 |          0.018 |          0.027 |
| F_clut                                          |          1.000 | 0.698 |                27.600 |              12.782 |         25 |              0.000 |              0.000 |         -0.010 |         -0.014 |
| F_obj                                           |          1.000 | 0.697 |                28.880 |              12.704 |         25 |              0.000 |              0.000 |         -0.009 |         -0.013 |
| F_tgt                                           |          1.000 | 0.683 |                28.360 |              12.747 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_mat                                           |          0.120 | 0.093 |               177.840 |               0.353 |         25 |              0.880 |              0.880 |          0.595 |          0.864 |
| F_light                                         |          1.000 | 0.690 |                28.440 |              12.782 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_sky                                           |          1.000 | 0.683 |                29.720 |              12.748 |         25 |              0.000 |              0.000 |          0.006 |          0.008 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.637 |         25 |              1.000 |              1.000 |          0.688 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.762 |         25 |              1.000 |              1.000 |          0.688 |          1.000 |
| B_L2 (+ object appearance)                      |          0.200 | 0.166 |               170.320 |              -0.068 |         25 |              0.800 |              0.800 |          0.522 |          0.759 |
| B_L3 (+ distractors)                            |          0.120 | 0.120 |               185.480 |              -1.028 |         25 |              0.880 |              0.880 |          0.568 |          0.826 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.018 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.010 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_mat: success drop 0.880 absolute, 88.0% relative · SPL drop 0.595 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **L1: success drop 1.000 absolute, 100.0% relative · SPL drop 0.688 absolute**
- **L2noT: success drop 1.000 absolute, 100.0% relative · SPL drop 0.688 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.522 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.568 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
