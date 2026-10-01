# DREAMERV3 zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.556 |                54.840 |              10.864 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.920 | 0.667 |                43.400 |              11.471 |         25 |             -0.080 |             -0.095 |         -0.111 |         -0.200 |
| F_clut                                          |          0.840 | 0.555 |                55.360 |              10.849 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_obj                                           |          0.880 | 0.588 |                48.840 |              11.288 |         25 |             -0.040 |             -0.048 |         -0.032 |         -0.058 |
| F_tgt                                           |          1.000 | 0.718 |                30.880 |              12.618 |         25 |             -0.160 |             -0.190 |         -0.162 |         -0.291 |
| F_mat                                           |          0.200 | 0.169 |               164.440 |               1.039 |         25 |              0.640 |              0.762 |          0.387 |          0.696 |
| F_light                                         |          0.840 | 0.545 |                55.480 |              10.860 |         25 |              0.000 |              0.000 |          0.012 |          0.021 |
| F_sky                                           |          0.800 | 0.514 |                66.920 |              10.310 |         25 |              0.040 |              0.048 |          0.042 |          0.076 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.518 |         25 |              0.800 |              0.952 |          0.516 |          0.928 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.698 |         25 |              0.840 |              1.000 |          0.556 |          1.000 |
| B_L2 (+ object appearance)                      |          0.120 | 0.120 |               184.600 |              -0.014 |         25 |              0.720 |              0.857 |          0.436 |          0.784 |
| B_L3 (+ distractors)                            |          0.120 | 0.120 |               179.160 |              -0.120 |         25 |              0.720 |              0.857 |          0.436 |          0.784 |

- **F_objall: success drop -0.080 absolute, -9.5% relative · SPL drop -0.111 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_obj: success drop -0.040 absolute, -4.8% relative · SPL drop -0.032 absolute**
- **F_tgt: success drop -0.160 absolute, -19.0% relative · SPL drop -0.162 absolute**
- **F_mat: success drop 0.640 absolute, 76.2% relative · SPL drop 0.387 absolute**
- **F_light: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **F_sky: success drop 0.040 absolute, 4.8% relative · SPL drop 0.042 absolute**
- **L1: success drop 0.800 absolute, 95.2% relative · SPL drop 0.516 absolute**
- **L2noT: success drop 0.840 absolute, 100.0% relative · SPL drop 0.556 absolute**
- **L2: success drop 0.720 absolute, 85.7% relative · SPL drop 0.436 absolute**
- **L3: success drop 0.720 absolute, 85.7% relative · SPL drop 0.436 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
