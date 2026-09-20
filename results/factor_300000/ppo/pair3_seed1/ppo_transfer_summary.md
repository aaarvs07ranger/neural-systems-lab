# PPO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.648 |                49.360 |              10.279 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.600 | 0.463 |                93.120 |               7.076 |         25 |              0.240 |              0.286 |          0.184 |          0.285 |
| F_clut                                          |          0.840 | 0.648 |                49.360 |              10.279 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.800 | 0.588 |                56.040 |               9.609 |         25 |              0.040 |              0.048 |          0.060 |          0.093 |
| F_tgt                                           |          0.720 | 0.556 |                71.760 |               8.823 |         25 |              0.120 |              0.143 |          0.091 |          0.141 |
| F_mat                                           |          0.000 | 0.000 |               200.000 |              -2.000 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |
| F_light                                         |          0.880 | 0.663 |                41.680 |              10.817 |         25 |             -0.040 |             -0.048 |         -0.015 |         -0.023 |
| F_sky                                           |          0.680 | 0.499 |                77.200 |               7.807 |         25 |              0.160 |              0.190 |          0.148 |          0.229 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -2.000 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -2.000 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -2.004 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -2.004 |         25 |              0.840 |              1.000 |          0.648 |          1.000 |

- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.184 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.040 absolute, 4.8% relative · SPL drop 0.060 absolute**
- **F_tgt: success drop 0.120 absolute, 14.3% relative · SPL drop 0.091 absolute**
- **F_mat: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**
- **F_light: success drop -0.040 absolute, -4.8% relative · SPL drop -0.015 absolute**
- **F_sky: success drop 0.160 absolute, 19.0% relative · SPL drop 0.148 absolute**
- **L1: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**
- **L2noT: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**
- **L2: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.648 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
