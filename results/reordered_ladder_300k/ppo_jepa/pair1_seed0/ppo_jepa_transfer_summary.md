# PPO_JEPA zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.656 |                29.720 |               9.421 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.640 |                37.200 |               8.870 |         25 |              0.040 |              0.045 |          0.016 |          0.025 |
| F_lightsky           |          0.840 | 0.614 |                37.560 |               8.924 |         25 |              0.040 |              0.045 |          0.042 |          0.064 |
| F_objall             |          0.800 | 0.591 |                45.360 |               8.283 |         25 |              0.080 |              0.091 |          0.065 |          0.100 |
| F_mat                |          0.240 | 0.240 |               152.280 |               1.017 |         25 |              0.640 |              0.727 |          0.416 |          0.634 |
| R2                   |          0.840 | 0.638 |                37.280 |               8.850 |         25 |              0.040 |              0.045 |          0.018 |          0.027 |
| R3                   |          0.280 | 0.280 |               144.800 |               1.660 |         25 |              0.600 |              0.682 |          0.376 |          0.573 |
| B_L3 (+ distractors) |          0.160 | 0.160 |               168.200 |              -0.082 |         25 |              0.720 |              0.818 |          0.496 |          0.756 |

- **F_clut: success drop 0.040 absolute, 4.5% relative · SPL drop 0.016 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**
- **F_objall: success drop 0.080 absolute, 9.1% relative · SPL drop 0.065 absolute**
- **F_mat: success drop 0.640 absolute, 72.7% relative · SPL drop 0.416 absolute**
- **R2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.018 absolute**
- **R3: success drop 0.600 absolute, 68.2% relative · SPL drop 0.376 absolute**
- **L3: success drop 0.720 absolute, 81.8% relative · SPL drop 0.496 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
