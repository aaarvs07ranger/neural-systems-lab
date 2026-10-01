# PPO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.621 |                23.320 |              13.786 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.619 |                23.280 |              13.789 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          0.360 | 0.190 |               141.720 |               5.725 |         25 |              0.640 |              0.640 |          0.431 |          0.694 |
| F_objall             |          0.920 | 0.616 |                35.720 |              12.468 |         25 |              0.080 |              0.080 |          0.004 |          0.007 |
| F_mat                |          1.000 | 0.600 |                28.000 |              13.801 |         25 |              0.000 |              0.000 |          0.020 |          0.033 |
| R2                   |          0.400 | 0.221 |               136.080 |               6.217 |         25 |              0.600 |              0.600 |          0.400 |          0.645 |
| R3                   |          0.440 | 0.305 |               122.280 |               6.008 |         25 |              0.560 |              0.560 |          0.316 |          0.509 |
| B_L3 (+ distractors) |          0.320 | 0.220 |               143.280 |               4.356 |         25 |              0.680 |              0.680 |          0.401 |          0.646 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.640 absolute, 64.0% relative · SPL drop 0.431 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.004 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **R2: success drop 0.600 absolute, 60.0% relative · SPL drop 0.400 absolute**
- **R3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.316 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.401 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
