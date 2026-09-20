# DREAMERV3 zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.120 | 0.120 |               178.880 |               0.025 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.160 | 0.160 |               170.640 |               0.497 |         25 |             -0.040 |             -0.333 |         -0.040 |         -0.333 |
| F_clut                                          |          0.160 | 0.160 |               172.400 |               0.489 |         25 |             -0.040 |             -0.333 |         -0.040 |         -0.333 |
| F_obj                                           |          0.160 | 0.160 |               181.240 |               0.401 |         25 |             -0.040 |             -0.333 |         -0.040 |         -0.333 |
| F_mat                                           |          0.840 | 0.635 |                83.440 |               8.279 |         25 |             -0.720 |             -6.000 |         -0.515 |         -4.290 |
| F_light                                         |          0.400 | 0.255 |               136.960 |               3.286 |         25 |             -0.280 |             -2.333 |         -0.135 |         -1.124 |
| F_sky                                           |          0.360 | 0.288 |               146.360 |               2.764 |         25 |             -0.240 |             -2.000 |         -0.168 |         -1.400 |
| B_L1 (materials + lighting)                     |          0.800 | 0.662 |                63.640 |               8.060 |         25 |             -0.680 |             -5.667 |         -0.542 |         -4.513 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.664 |                94.280 |               7.337 |         25 |             -0.640 |             -5.333 |         -0.544 |         -4.534 |
| B_L2 (+ object appearance)                      |          0.760 | 0.618 |               104.560 |               7.234 |         25 |             -0.640 |             -5.333 |         -0.498 |         -4.146 |
| B_L3 (+ distractors)                            |          0.880 | 0.714 |                79.400 |               8.718 |         25 |             -0.760 |             -6.333 |         -0.594 |         -4.947 |

- **F_objall: success drop -0.040 absolute, -33.3% relative · SPL drop -0.040 absolute**
- **F_clut: success drop -0.040 absolute, -33.3% relative · SPL drop -0.040 absolute**
- **F_obj: success drop -0.040 absolute, -33.3% relative · SPL drop -0.040 absolute**
- **F_mat: success drop -0.720 absolute, -600.0% relative · SPL drop -0.515 absolute**
- **F_light: success drop -0.280 absolute, -233.3% relative · SPL drop -0.135 absolute**
- **F_sky: success drop -0.240 absolute, -200.0% relative · SPL drop -0.168 absolute**
- **L1: success drop -0.680 absolute, -566.7% relative · SPL drop -0.542 absolute**
- **L2noT: success drop -0.640 absolute, -533.3% relative · SPL drop -0.544 absolute**
- **L2: success drop -0.640 absolute, -533.3% relative · SPL drop -0.498 absolute**
- **L3: success drop -0.760 absolute, -633.3% relative · SPL drop -0.594 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
