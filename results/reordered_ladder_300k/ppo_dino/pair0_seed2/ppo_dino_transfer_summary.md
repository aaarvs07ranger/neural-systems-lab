# PPO_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.811 |                10.720 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.811 |                10.720 |              11.614 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.801 |                10.880 |              11.613 |         25 |              0.000 |              0.000 |          0.010 |          0.012 |
| F_objall             |          0.720 | 0.531 |                64.120 |               7.868 |         25 |              0.280 |              0.280 |          0.280 |          0.345 |
| F_mat                |          0.920 | 0.748 |                24.960 |              10.415 |         25 |              0.080 |              0.080 |          0.063 |          0.077 |
| R2                   |          1.000 | 0.798 |                11.000 |              11.614 |         25 |              0.000 |              0.000 |          0.013 |          0.016 |
| R3                   |          0.760 | 0.557 |                57.000 |               8.383 |         25 |              0.240 |              0.240 |          0.254 |          0.313 |
| B_L3 (+ distractors) |          0.640 | 0.517 |                78.600 |               6.740 |         25 |              0.360 |              0.360 |          0.294 |          0.363 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_objall: success drop 0.280 absolute, 28.0% relative · SPL drop 0.280 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.063 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.013 absolute**
- **R3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.254 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.294 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
