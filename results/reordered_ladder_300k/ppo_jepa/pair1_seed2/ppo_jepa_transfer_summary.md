# PPO_JEPA zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.678 |                29.200 |               9.339 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.642 |                36.920 |               8.850 |         25 |              0.040 |              0.045 |          0.036 |          0.053 |
| F_lightsky           |          0.840 | 0.640 |                37.160 |               8.854 |         25 |              0.040 |              0.045 |          0.037 |          0.055 |
| F_objall             |          0.320 | 0.246 |               137.480 |               2.423 |         25 |              0.560 |              0.636 |          0.432 |          0.637 |
| F_mat                |          0.240 | 0.240 |               152.280 |               1.057 |         25 |              0.640 |              0.727 |          0.438 |          0.646 |
| R2                   |          0.800 | 0.600 |                44.960 |               8.357 |         25 |              0.080 |              0.091 |          0.077 |          0.114 |
| R3                   |          0.200 | 0.179 |               160.680 |               0.681 |         25 |              0.680 |              0.773 |          0.499 |          0.736 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |

- **F_clut: success drop 0.040 absolute, 4.5% relative · SPL drop 0.036 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.037 absolute**
- **F_objall: success drop 0.560 absolute, 63.6% relative · SPL drop 0.432 absolute**
- **F_mat: success drop 0.640 absolute, 72.7% relative · SPL drop 0.438 absolute**
- **R2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.077 absolute**
- **R3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.499 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
