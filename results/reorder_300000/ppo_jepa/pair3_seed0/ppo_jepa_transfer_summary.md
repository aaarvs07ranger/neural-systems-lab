# PPO_JEPA zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.680 | 0.510 |                75.760 |               7.895 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.720 | 0.537 |                69.040 |               8.536 |         25 |             -0.040 |             -0.059 |         -0.027 |         -0.054 |
| F_lightsky           |          0.800 | 0.573 |                55.920 |               9.709 |         25 |             -0.120 |             -0.176 |         -0.063 |         -0.123 |
| F_objall             |          0.640 | 0.461 |                84.040 |               7.509 |         25 |              0.040 |              0.059 |          0.048 |          0.095 |
| F_mat                |          0.040 | 0.040 |               192.160 |              -1.526 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| R2                   |          0.760 | 0.546 |                62.520 |               9.078 |         25 |             -0.080 |             -0.118 |         -0.036 |         -0.072 |
| R3                   |          0.680 | 0.480 |                76.520 |               7.828 |         25 |              0.000 |              0.000 |          0.030 |          0.058 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.200 |              -1.130 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |

- **F_clut: success drop -0.040 absolute, -5.9% relative · SPL drop -0.027 absolute**
- **F_lightsky: success drop -0.120 absolute, -17.6% relative · SPL drop -0.063 absolute**
- **F_objall: success drop 0.040 absolute, 5.9% relative · SPL drop 0.048 absolute**
- **F_mat: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **R2: success drop -0.080 absolute, -11.8% relative · SPL drop -0.036 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.030 absolute**
- **L3: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
