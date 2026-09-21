# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.658 |                29.320 |               9.268 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.800 | 0.614 |                44.560 |               8.296 |         25 |              0.080 |              0.091 |          0.044 |          0.067 |
| F_clut                                          |          0.880 | 0.658 |                29.320 |               9.274 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_obj                                           |          0.800 | 0.614 |                44.560 |               8.296 |         25 |              0.080 |              0.091 |          0.044 |          0.067 |
| F_mat                                           |          0.760 | 0.574 |                52.200 |               7.763 |         25 |              0.120 |              0.136 |          0.084 |          0.128 |
| F_light                                         |          0.840 | 0.654 |                36.960 |               8.798 |         25 |              0.040 |              0.045 |          0.004 |          0.006 |
| F_sky                                           |          0.880 | 0.657 |                29.440 |               9.272 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L1 (materials + lighting)                     |          0.720 | 0.532 |                60.040 |               7.231 |         25 |              0.160 |              0.182 |          0.126 |          0.191 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |
| B_L2 (+ object appearance)                      |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |
| B_L3 (+ distractors)                            |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |

- **F_objall: success drop 0.080 absolute, 9.1% relative · SPL drop 0.044 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_obj: success drop 0.080 absolute, 9.1% relative · SPL drop 0.044 absolute**
- **F_mat: success drop 0.120 absolute, 13.6% relative · SPL drop 0.084 absolute**
- **F_light: success drop 0.040 absolute, 4.5% relative · SPL drop 0.004 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L1: success drop 0.160 absolute, 18.2% relative · SPL drop 0.126 absolute**
- **L2noT: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **L2: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
