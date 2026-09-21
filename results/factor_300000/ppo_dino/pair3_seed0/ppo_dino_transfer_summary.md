# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.607 |                49.800 |              10.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.618 |                49.800 |              10.533 |         25 |              0.000 |              0.000 |         -0.011 |         -0.018 |
| F_clut                                          |          0.840 | 0.607 |                49.800 |              10.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.840 | 0.610 |                50.080 |              10.529 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_tgt                                           |          0.840 | 0.613 |                49.600 |              10.544 |         25 |              0.000 |              0.000 |         -0.005 |         -0.009 |
| F_mat                                           |          0.040 | 0.040 |               192.160 |              -0.747 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| F_light                                         |          0.800 | 0.582 |                56.320 |               9.879 |         25 |              0.040 |              0.048 |          0.025 |          0.041 |
| F_sky                                           |          0.840 | 0.606 |                49.840 |              10.534 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -0.709 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.926 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.160 |              -0.896 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.160 |              -0.738 |         25 |              0.800 |              0.952 |          0.567 |          0.934 |

- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.011 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **F_light: success drop 0.040 absolute, 4.8% relative · SPL drop 0.025 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L2noT: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L2: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**
- **L3: success drop 0.800 absolute, 95.2% relative · SPL drop 0.567 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
