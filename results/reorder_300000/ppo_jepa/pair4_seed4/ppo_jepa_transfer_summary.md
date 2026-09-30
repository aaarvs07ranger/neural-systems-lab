# PPO_JEPA zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.652 |                41.640 |              11.468 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.653 |                41.600 |              11.449 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_lightsky           |          0.800 | 0.611 |                54.040 |              10.134 |         25 |              0.080 |              0.091 |          0.041 |          0.062 |
| F_objall             |          0.840 | 0.621 |                49.440 |              10.897 |         25 |              0.040 |              0.045 |          0.030 |          0.046 |
| F_mat                |          0.480 | 0.320 |               112.520 |               5.200 |         25 |              0.400 |              0.455 |          0.332 |          0.509 |
| R2                   |          0.840 | 0.640 |                46.400 |              10.616 |         25 |              0.040 |              0.045 |          0.011 |          0.017 |
| R3                   |          0.840 | 0.603 |                48.160 |              10.664 |         25 |              0.040 |              0.045 |          0.048 |          0.074 |
| B_L3 (+ distractors) |          0.440 | 0.287 |               120.800 |               5.031 |         25 |              0.440 |              0.500 |          0.365 |          0.560 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.080 absolute, 9.1% relative · SPL drop 0.041 absolute**
- **F_objall: success drop 0.040 absolute, 4.5% relative · SPL drop 0.030 absolute**
- **F_mat: success drop 0.400 absolute, 45.5% relative · SPL drop 0.332 absolute**
- **R2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.011 absolute**
- **R3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.048 absolute**
- **L3: success drop 0.440 absolute, 50.0% relative · SPL drop 0.365 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
