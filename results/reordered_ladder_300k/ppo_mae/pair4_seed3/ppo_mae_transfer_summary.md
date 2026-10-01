# PPO_MAE zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.716 |                27.000 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.715 |                27.040 |              12.596 |         25 |              0.000 |              0.000 |          0.000 |          0.001 |
| F_lightsky           |          0.720 | 0.506 |                69.840 |               9.013 |         25 |              0.240 |              0.250 |          0.210 |          0.294 |
| F_objall             |          0.920 | 0.665 |                33.960 |              11.876 |         25 |              0.040 |              0.042 |          0.051 |          0.071 |
| F_mat                |          0.720 | 0.490 |                69.240 |               8.875 |         25 |              0.240 |              0.250 |          0.226 |          0.316 |
| R2                   |          0.720 | 0.506 |                69.840 |               8.963 |         25 |              0.240 |              0.250 |          0.210 |          0.294 |
| R3                   |          0.520 | 0.358 |               105.760 |               5.911 |         25 |              0.440 |              0.458 |          0.358 |          0.500 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -0.631 |         25 |              0.960 |              1.000 |          0.716 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.240 absolute, 25.0% relative · SPL drop 0.210 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.051 absolute**
- **F_mat: success drop 0.240 absolute, 25.0% relative · SPL drop 0.226 absolute**
- **R2: success drop 0.240 absolute, 25.0% relative · SPL drop 0.210 absolute**
- **R3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.358 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.716 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
