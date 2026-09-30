# PPO_MAE zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.723 |                26.600 |              12.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.723 |                26.600 |              12.576 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.800 | 0.581 |                54.680 |              10.134 |         25 |              0.160 |              0.167 |          0.142 |          0.196 |
| F_objall             |          0.960 | 0.726 |                27.560 |              12.556 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| F_mat                |          0.080 | 0.059 |               184.880 |              -0.024 |         25 |              0.880 |              0.917 |          0.664 |          0.919 |
| R2                   |          0.800 | 0.581 |                54.680 |               9.973 |         25 |              0.160 |              0.167 |          0.142 |          0.196 |
| R3                   |          0.720 | 0.491 |                69.440 |               8.957 |         25 |              0.240 |              0.250 |          0.232 |          0.320 |
| B_L3 (+ distractors) |          0.200 | 0.166 |               163.480 |               1.690 |         25 |              0.760 |              0.792 |          0.557 |          0.771 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.7% relative · SPL drop 0.142 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_mat: success drop 0.880 absolute, 91.7% relative · SPL drop 0.664 absolute**
- **R2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.142 absolute**
- **R3: success drop 0.240 absolute, 25.0% relative · SPL drop 0.232 absolute**
- **L3: success drop 0.760 absolute, 79.2% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
