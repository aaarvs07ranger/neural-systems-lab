# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.766 |                15.680 |              10.921 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          1.000 | 0.768 |                15.280 |              10.902 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_clut                                          |          1.000 | 0.768 |                15.880 |              10.911 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_obj                                           |          1.000 | 0.768 |                15.240 |              10.910 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_mat                                           |          1.000 | 0.778 |                28.680 |              10.522 |         25 |              0.000 |              0.000 |         -0.012 |         -0.015 |
| F_light                                         |          1.000 | 0.768 |                18.640 |              10.853 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_sky                                           |          1.000 | 0.768 |                16.920 |              10.870 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| B_L1 (materials + lighting)                     |          0.960 | 0.735 |                49.080 |               9.909 |         25 |              0.040 |              0.040 |          0.031 |          0.041 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          1.000 | 0.775 |                42.920 |              10.368 |         25 |              0.000 |              0.000 |         -0.009 |         -0.012 |
| B_L2 (+ object appearance)                      |          1.000 | 0.769 |                34.120 |              10.457 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| B_L3 (+ distractors)                            |          1.000 | 0.777 |                31.520 |              10.485 |         25 |              0.000 |              0.000 |         -0.011 |         -0.014 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.031 absolute**
- **L2noT: success drop 0.000 absolute, 0.0% relative · SPL drop -0.009 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.011 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
