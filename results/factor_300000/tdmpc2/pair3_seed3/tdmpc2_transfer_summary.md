# TDMPC2 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.764 |                27.560 |              12.508 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.730 |                57.120 |              11.739 |         25 |              0.040 |              0.040 |          0.034 |          0.045 |
| F_clut                                          |          0.920 | 0.683 |                42.760 |              11.529 |         25 |              0.080 |              0.080 |          0.081 |          0.106 |
| F_obj                                           |          1.000 | 0.760 |                35.800 |              12.422 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_tgt                                           |          0.920 | 0.698 |                51.080 |              11.257 |         25 |              0.080 |              0.080 |          0.066 |          0.086 |
| F_mat                                           |          0.400 | 0.252 |               144.440 |               3.452 |         25 |              0.600 |              0.600 |          0.512 |          0.670 |
| F_light                                         |          1.000 | 0.761 |                29.000 |              12.493 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_sky                                           |          0.960 | 0.733 |                56.640 |              11.724 |         25 |              0.040 |              0.040 |          0.031 |          0.041 |
| B_L1 (materials + lighting)                     |          0.120 | 0.075 |               190.880 |              -0.814 |         25 |              0.880 |              0.880 |          0.689 |          0.901 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.160 | 0.124 |               185.080 |              -0.030 |         25 |              0.840 |              0.840 |          0.641 |          0.838 |
| B_L2 (+ object appearance)                      |          0.200 | 0.126 |               181.480 |               0.064 |         25 |              0.800 |              0.800 |          0.638 |          0.835 |
| B_L3 (+ distractors)                            |          0.280 | 0.197 |               178.000 |               0.942 |         25 |              0.720 |              0.720 |          0.567 |          0.742 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.034 absolute**
- **F_clut: success drop 0.080 absolute, 8.0% relative · SPL drop 0.081 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_tgt: success drop 0.080 absolute, 8.0% relative · SPL drop 0.066 absolute**
- **F_mat: success drop 0.600 absolute, 60.0% relative · SPL drop 0.512 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.031 absolute**
- **L1: success drop 0.880 absolute, 88.0% relative · SPL drop 0.689 absolute**
- **L2noT: success drop 0.840 absolute, 84.0% relative · SPL drop 0.641 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.638 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.567 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
