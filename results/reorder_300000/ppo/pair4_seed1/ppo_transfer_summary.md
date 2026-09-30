# PPO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.661 |                22.880 |              13.757 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.626 |                29.760 |              13.248 |         25 |              0.040 |              0.040 |          0.035 |          0.052 |
| F_lightsky           |          0.840 | 0.579 |                51.320 |              11.535 |         25 |              0.160 |              0.160 |          0.082 |          0.124 |
| F_objall             |          0.880 | 0.605 |                43.520 |              12.118 |         25 |              0.120 |              0.120 |          0.056 |          0.085 |
| F_mat                |          0.720 | 0.438 |                73.280 |               9.267 |         25 |              0.280 |              0.280 |          0.223 |          0.338 |
| R2                   |          0.840 | 0.579 |                51.320 |              11.565 |         25 |              0.160 |              0.160 |          0.082 |          0.124 |
| R3                   |          0.640 | 0.461 |                85.360 |               8.989 |         25 |              0.360 |              0.360 |          0.200 |          0.303 |
| B_L3 (+ distractors) |          0.280 | 0.195 |               149.920 |               3.166 |         25 |              0.720 |              0.720 |          0.466 |          0.705 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.035 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.082 absolute**
- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.056 absolute**
- **F_mat: success drop 0.280 absolute, 28.0% relative · SPL drop 0.223 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.082 absolute**
- **R3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.200 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.466 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
