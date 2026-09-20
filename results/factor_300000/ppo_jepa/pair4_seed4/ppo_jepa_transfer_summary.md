# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.652 |                41.640 |              11.468 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall                                        |          0.840 | 0.621 |                49.440 |              10.897 |         25 |              0.040 |              0.045 |          0.030 |          0.046 |
| F_clut                                          |          0.840 | 0.638 |                48.920 |              10.936 |         25 |              0.040 |              0.045 |          0.014 |          0.021 |
| F_obj                                           |          0.880 | 0.646 |                42.320 |              11.560 |         25 |              0.000 |              0.000 |          0.006 |          0.009 |
| F_tgt                                           |          0.880 | 0.658 |                41.320 |              11.414 |         25 |              0.000 |              0.000 |         -0.007 |         -0.010 |
| F_mat                                           |          0.560 | 0.374 |                98.080 |               6.503 |         25 |              0.320 |              0.364 |          0.278 |          0.426 |
| F_light                                         |          0.840 | 0.614 |                47.880 |              10.856 |         25 |              0.040 |              0.045 |          0.038 |          0.058 |
| F_sky                                           |          0.880 | 0.677 |                40.720 |              11.358 |         25 |              0.000 |              0.000 |         -0.025 |         -0.039 |
| B_L1 (materials + lighting)                     |          0.600 | 0.416 |                91.400 |               7.050 |         25 |              0.280 |              0.318 |          0.236 |          0.362 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.365 |                95.000 |               7.115 |         25 |              0.280 |              0.318 |          0.287 |          0.440 |
| B_L2 (+ object appearance)                      |          0.440 | 0.284 |               121.080 |               4.915 |         25 |              0.440 |              0.500 |          0.367 |          0.564 |
| B_L3 (+ distractors)                            |          0.440 | 0.284 |               121.000 |               4.911 |         25 |              0.440 |              0.500 |          0.367 |          0.564 |

- **F_objall: success drop 0.040 absolute, 4.5% relative · SPL drop 0.030 absolute**
- **F_clut: success drop 0.040 absolute, 4.5% relative · SPL drop 0.014 absolute**
- **F_obj: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_tgt: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_mat: success drop 0.320 absolute, 36.4% relative · SPL drop 0.278 absolute**
- **F_light: success drop 0.040 absolute, 4.5% relative · SPL drop 0.038 absolute**
- **F_sky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.025 absolute**
- **L1: success drop 0.280 absolute, 31.8% relative · SPL drop 0.236 absolute**
- **L2noT: success drop 0.280 absolute, 31.8% relative · SPL drop 0.287 absolute**
- **L2: success drop 0.440 absolute, 50.0% relative · SPL drop 0.367 absolute**
- **L3: success drop 0.440 absolute, 50.0% relative · SPL drop 0.367 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
