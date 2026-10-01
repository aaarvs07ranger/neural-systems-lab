# PPO_MAE zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.660 |                41.240 |              10.807 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.682 |                34.840 |              11.435 |         25 |             -0.040 |             -0.045 |         -0.022 |         -0.034 |
| F_lightsky           |          0.920 | 0.681 |                35.520 |              11.367 |         25 |             -0.040 |             -0.045 |         -0.020 |         -0.031 |
| F_objall             |          0.560 | 0.406 |                96.080 |               6.311 |         25 |              0.320 |              0.364 |          0.254 |          0.385 |
| F_mat                |          0.440 | 0.323 |               117.480 |               4.167 |         25 |              0.440 |              0.500 |          0.337 |          0.510 |
| R2                   |          0.880 | 0.657 |                41.960 |              10.729 |         25 |              0.000 |              0.000 |          0.003 |          0.005 |
| R3                   |          0.400 | 0.303 |               125.200 |               4.092 |         25 |              0.480 |              0.545 |          0.357 |          0.540 |
| B_L3 (+ distractors) |          0.040 | 0.016 |               192.240 |              -1.503 |         25 |              0.840 |              0.955 |          0.644 |          0.976 |

- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.022 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.020 absolute**
- **F_objall: success drop 0.320 absolute, 36.4% relative · SPL drop 0.254 absolute**
- **F_mat: success drop 0.440 absolute, 50.0% relative · SPL drop 0.337 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **R3: success drop 0.480 absolute, 54.5% relative · SPL drop 0.357 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.644 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
