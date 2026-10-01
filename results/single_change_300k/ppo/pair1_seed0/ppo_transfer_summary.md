# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.675 |                14.240 |              10.383 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.560 | 0.432 |                91.160 |               5.358 |         25 |              0.400 |              0.417 |          0.244 |          0.361 |
| F_clut                                          |          0.960 | 0.675 |                14.480 |              10.382 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_obj                                           |          0.880 | 0.597 |                29.400 |               9.344 |         25 |              0.080 |              0.083 |          0.078 |          0.116 |
| F_tgt                                           |          0.840 | 0.599 |                38.200 |               8.905 |         25 |              0.120 |              0.125 |          0.076 |          0.113 |
| F_mat                                           |          0.880 | 0.642 |                31.880 |               9.262 |         25 |              0.080 |              0.083 |          0.034 |          0.050 |
| F_light                                         |          0.880 | 0.654 |                29.360 |               9.419 |         25 |              0.080 |              0.083 |          0.021 |          0.031 |
| F_sky                                           |          0.960 | 0.699 |                14.160 |              10.304 |         25 |              0.000 |              0.000 |         -0.024 |         -0.035 |
| B_L1 (materials + lighting)                     |          0.640 | 0.425 |                76.920 |               6.275 |         25 |              0.320 |              0.333 |          0.250 |          0.371 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.433 |                85.000 |               5.717 |         25 |              0.360 |              0.375 |          0.242 |          0.359 |
| B_L2 (+ object appearance)                      |          0.360 | 0.304 |               130.360 |               2.568 |         25 |              0.600 |              0.625 |          0.371 |          0.550 |
| B_L3 (+ distractors)                            |          0.360 | 0.306 |               129.720 |               2.566 |         25 |              0.600 |              0.625 |          0.370 |          0.547 |

- **F_objall: success drop 0.400 absolute, 41.7% relative · SPL drop 0.244 absolute**
- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_obj: success drop 0.080 absolute, 8.3% relative · SPL drop 0.078 absolute**
- **F_tgt: success drop 0.120 absolute, 12.5% relative · SPL drop 0.076 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.034 absolute**
- **F_light: success drop 0.080 absolute, 8.3% relative · SPL drop 0.021 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.024 absolute**
- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.250 absolute**
- **L2noT: success drop 0.360 absolute, 37.5% relative · SPL drop 0.242 absolute**
- **L2: success drop 0.600 absolute, 62.5% relative · SPL drop 0.371 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.370 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
