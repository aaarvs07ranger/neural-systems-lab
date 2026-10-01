# PPO_MAE zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.632 |                49.280 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.632 |                49.280 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.640 | 0.465 |                84.920 |               7.377 |         25 |              0.200 |              0.238 |          0.167 |          0.264 |
| F_objall             |          0.320 | 0.231 |               141.640 |               3.627 |         25 |              0.520 |              0.619 |          0.401 |          0.634 |
| F_mat                |          0.000 | 0.000 |               200.000 |              -1.980 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| R2                   |          0.640 | 0.465 |                84.920 |               7.365 |         25 |              0.200 |              0.238 |          0.167 |          0.264 |
| R3                   |          0.640 | 0.455 |                87.040 |               7.524 |         25 |              0.200 |              0.238 |          0.177 |          0.280 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.986 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **F_objall: success drop 0.520 absolute, 61.9% relative · SPL drop 0.401 absolute**
- **F_mat: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **R2: success drop 0.200 absolute, 23.8% relative · SPL drop 0.167 absolute**
- **R3: success drop 0.200 absolute, 23.8% relative · SPL drop 0.177 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
