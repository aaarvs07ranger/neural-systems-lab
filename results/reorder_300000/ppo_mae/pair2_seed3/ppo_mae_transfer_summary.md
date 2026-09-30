# PPO_MAE zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.777 |                 8.280 |              10.722 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                 8.280 |              10.722 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.720 | 0.500 |                62.360 |               7.333 |         25 |              0.280 |              0.280 |          0.276 |          0.356 |
| F_objall             |          0.920 | 0.698 |                23.440 |               9.763 |         25 |              0.080 |              0.080 |          0.078 |          0.101 |
| F_mat                |          0.760 | 0.540 |                54.480 |               7.819 |         25 |              0.240 |              0.240 |          0.236 |          0.304 |
| R2                   |          0.720 | 0.500 |                62.360 |               7.333 |         25 |              0.280 |              0.280 |          0.276 |          0.356 |
| R3                   |          0.680 | 0.485 |                70.080 |               6.834 |         25 |              0.320 |              0.320 |          0.291 |          0.375 |
| B_L3 (+ distractors) |          0.560 | 0.464 |                94.440 |               5.216 |         25 |              0.440 |              0.440 |          0.313 |          0.402 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.280 absolute, 28.0% relative · SPL drop 0.276 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.078 absolute**
- **F_mat: success drop 0.240 absolute, 24.0% relative · SPL drop 0.236 absolute**
- **R2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.276 absolute**
- **R3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.291 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
