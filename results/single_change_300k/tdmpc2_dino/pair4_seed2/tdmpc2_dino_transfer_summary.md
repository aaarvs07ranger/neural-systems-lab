# TDMPC2_DINO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.789 |                19.400 |              13.241 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.960 | 0.735 |                25.960 |              12.642 |         25 |              0.040 |              0.040 |          0.054 |          0.068 |
| F_clut                                          |          1.000 | 0.774 |                19.120 |              13.244 |         25 |              0.000 |              0.000 |          0.015 |          0.019 |
| F_obj                                           |          0.960 | 0.735 |                28.680 |              12.670 |         25 |              0.040 |              0.040 |          0.054 |          0.068 |
| F_tgt                                           |          1.000 | 0.787 |                18.880 |              13.211 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_mat                                           |          0.880 | 0.637 |                46.400 |              11.509 |         25 |              0.120 |              0.120 |          0.152 |          0.193 |
| F_light                                         |          0.960 | 0.751 |                26.160 |              12.603 |         25 |              0.040 |              0.040 |          0.038 |          0.048 |
| F_sky                                           |          1.000 | 0.758 |                20.200 |              13.238 |         25 |              0.000 |              0.000 |          0.030 |          0.039 |
| B_L1 (materials + lighting)                     |          0.840 | 0.588 |                55.040 |              10.770 |         25 |              0.160 |              0.160 |          0.201 |          0.255 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.515 |                74.840 |               9.702 |         25 |              0.240 |              0.240 |          0.274 |          0.347 |
| B_L2 (+ object appearance)                      |          0.840 | 0.560 |                60.760 |              10.846 |         25 |              0.160 |              0.160 |          0.229 |          0.291 |
| B_L3 (+ distractors)                            |          0.840 | 0.580 |                57.360 |              10.886 |         25 |              0.160 |              0.160 |          0.209 |          0.265 |

- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.054 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.015 absolute**
- **F_obj: success drop 0.040 absolute, 4.0% relative · SPL drop 0.054 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.152 absolute**
- **F_light: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.030 absolute**
- **L1: success drop 0.160 absolute, 16.0% relative · SPL drop 0.201 absolute**
- **L2noT: success drop 0.240 absolute, 24.0% relative · SPL drop 0.274 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.229 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.209 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
