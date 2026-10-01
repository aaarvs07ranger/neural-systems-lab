# PPO_MAE zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                19.760 |              10.950 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.783 |                19.760 |              10.950 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.755 |                27.040 |              10.392 |         25 |              0.040 |              0.042 |          0.028 |          0.036 |
| F_objall             |          0.800 | 0.648 |                51.520 |               8.918 |         25 |              0.160 |              0.167 |          0.135 |          0.172 |
| F_mat                |          0.840 | 0.700 |                41.720 |               9.266 |         25 |              0.120 |              0.125 |          0.083 |          0.105 |
| R2                   |          0.920 | 0.755 |                27.040 |              10.392 |         25 |              0.040 |              0.042 |          0.028 |          0.036 |
| R3                   |          0.880 | 0.714 |                35.400 |               9.784 |         25 |              0.080 |              0.083 |          0.069 |          0.088 |
| B_L3 (+ distractors) |          0.680 | 0.581 |                72.880 |               7.242 |         25 |              0.280 |              0.292 |          0.202 |          0.258 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.028 absolute**
- **F_objall: success drop 0.160 absolute, 16.7% relative · SPL drop 0.135 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.083 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.028 absolute**
- **R3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.069 absolute**
- **L3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.202 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
