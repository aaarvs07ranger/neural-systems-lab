# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.663 |                40.800 |              10.809 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.640 | 0.472 |                82.200 |               7.360 |         25 |              0.240 |              0.273 |          0.191 |          0.289 |
| F_clut                                          |          0.800 | 0.614 |                53.880 |               9.555 |         25 |              0.080 |              0.091 |          0.049 |          0.074 |
| F_obj                                           |          0.720 | 0.551 |                67.520 |               8.332 |         25 |              0.160 |              0.182 |          0.112 |          0.169 |
| F_tgt                                           |          0.840 | 0.624 |                47.760 |              10.223 |         25 |              0.040 |              0.045 |          0.039 |          0.059 |
| F_mat                                           |          0.200 | 0.156 |               164.640 |               1.255 |         25 |              0.680 |              0.773 |          0.507 |          0.764 |
| F_light                                         |          0.800 | 0.615 |                53.960 |               9.490 |         25 |              0.080 |              0.091 |          0.048 |          0.073 |
| F_sky                                           |          1.000 | 0.732 |                22.200 |              12.551 |         25 |             -0.120 |             -0.136 |         -0.069 |         -0.103 |
| B_L1 (materials + lighting)                     |          0.080 | 0.066 |               185.080 |              -0.381 |         25 |              0.800 |              0.909 |          0.597 |          0.900 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.120 | 0.091 |               178.440 |              -0.153 |         25 |              0.760 |              0.864 |          0.572 |          0.863 |
| B_L2 (+ object appearance)                      |          0.040 | 0.026 |               193.000 |              -0.998 |         25 |              0.840 |              0.955 |          0.637 |          0.961 |
| B_L3 (+ distractors)                            |          0.080 | 0.066 |               185.200 |              -0.484 |         25 |              0.800 |              0.909 |          0.597 |          0.900 |

- **F_objall: success drop 0.240 absolute, 27.3% relative · SPL drop 0.191 absolute**
- **F_clut: success drop 0.080 absolute, 9.1% relative · SPL drop 0.049 absolute**
- **F_obj: success drop 0.160 absolute, 18.2% relative · SPL drop 0.112 absolute**
- **F_tgt: success drop 0.040 absolute, 4.5% relative · SPL drop 0.039 absolute**
- **F_mat: success drop 0.680 absolute, 77.3% relative · SPL drop 0.507 absolute**
- **F_light: success drop 0.080 absolute, 9.1% relative · SPL drop 0.048 absolute**
- **F_sky: success drop -0.120 absolute, -13.6% relative · SPL drop -0.069 absolute**
- **L1: success drop 0.800 absolute, 90.9% relative · SPL drop 0.597 absolute**
- **L2noT: success drop 0.760 absolute, 86.4% relative · SPL drop 0.572 absolute**
- **L2: success drop 0.840 absolute, 95.5% relative · SPL drop 0.637 absolute**
- **L3: success drop 0.800 absolute, 90.9% relative · SPL drop 0.597 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
