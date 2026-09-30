# PPO_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.653 |                40.520 |              10.853 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.682 |                34.120 |              11.487 |         25 |             -0.040 |             -0.045 |         -0.029 |         -0.044 |
| F_lightsky           |          0.880 | 0.653 |                40.640 |              10.847 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          0.760 | 0.570 |                61.240 |               9.350 |         25 |              0.120 |              0.136 |          0.084 |          0.128 |
| F_mat                |          0.640 | 0.498 |                83.120 |               7.145 |         25 |              0.240 |              0.273 |          0.156 |          0.238 |
| R2                   |          0.920 | 0.682 |                34.240 |              11.473 |         25 |             -0.040 |             -0.045 |         -0.029 |         -0.044 |
| R3                   |          0.560 | 0.439 |                95.480 |               6.922 |         25 |              0.320 |              0.364 |          0.214 |          0.327 |
| B_L3 (+ distractors) |          0.440 | 0.363 |               120.920 |               4.607 |         25 |              0.440 |              0.500 |          0.290 |          0.445 |

- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.029 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.120 absolute, 13.6% relative · SPL drop 0.084 absolute**
- **F_mat: success drop 0.240 absolute, 27.3% relative · SPL drop 0.156 absolute**
- **R2: success drop -0.040 absolute, -4.5% relative · SPL drop -0.029 absolute**
- **R3: success drop 0.320 absolute, 36.4% relative · SPL drop 0.214 absolute**
- **L3: success drop 0.440 absolute, 50.0% relative · SPL drop 0.290 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
