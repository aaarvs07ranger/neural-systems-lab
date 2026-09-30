# PPO_MAE zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.686 |                34.520 |              10.002 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.686 |                34.520 |               9.997 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.688 |                27.560 |              10.626 |         25 |             -0.040 |             -0.045 |         -0.001 |         -0.002 |
| F_objall             |          0.880 | 0.679 |                34.240 |               9.955 |         25 |              0.000 |              0.000 |          0.007 |          0.011 |
| F_mat                |          0.920 | 0.755 |                27.040 |              10.447 |         25 |             -0.040 |             -0.045 |         -0.069 |         -0.101 |
| R2                   |          0.920 | 0.689 |                27.720 |              10.624 |         25 |             -0.040 |             -0.045 |         -0.002 |         -0.004 |
| R3                   |          0.920 | 0.687 |                27.240 |              10.495 |         25 |             -0.040 |             -0.045 |         -0.001 |         -0.001 |
| B_L3 (+ distractors) |          0.760 | 0.607 |                58.360 |               8.334 |         25 |              0.120 |              0.136 |          0.079 |          0.115 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_mat: success drop -0.040 absolute, -4.5% relative · SPL drop -0.069 absolute**
- **R2: success drop -0.040 absolute, -4.5% relative · SPL drop -0.002 absolute**
- **R3: success drop -0.040 absolute, -4.5% relative · SPL drop -0.001 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
