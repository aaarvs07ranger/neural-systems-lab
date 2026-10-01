# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.811 |                20.560 |              13.227 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.767 |                28.120 |              12.488 |         25 |              0.040 |              0.040 |          0.044 |          0.054 |
| F_clut                                          |          1.000 | 0.807 |                19.960 |              13.221 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_obj                                           |          0.960 | 0.759 |                26.800 |              12.667 |         25 |              0.040 |              0.040 |          0.052 |          0.064 |
| F_tgt                                           |          1.000 | 0.814 |                19.640 |              13.199 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_mat                                           |          0.960 | 0.723 |                30.600 |              12.543 |         25 |              0.040 |              0.040 |          0.088 |          0.108 |
| F_light                                         |          1.000 | 0.810 |                19.440 |              13.225 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_sky                                           |          1.000 | 0.810 |                20.120 |              13.206 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L1 (materials + lighting)                     |          0.960 | 0.717 |                28.800 |              12.570 |         25 |              0.040 |              0.040 |          0.094 |          0.116 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.580 |                61.760 |              10.182 |         25 |              0.200 |              0.200 |          0.231 |          0.285 |
| B_L2 (+ object appearance)                      |          0.800 | 0.606 |                60.000 |              10.037 |         25 |              0.200 |              0.200 |          0.205 |          0.253 |
| B_L3 (+ distractors)                            |          0.880 | 0.696 |                44.760 |              11.272 |         25 |              0.120 |              0.120 |          0.115 |          0.142 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.044 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.052 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.088 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.094 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.231 absolute**
- **L2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.205 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.115 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
