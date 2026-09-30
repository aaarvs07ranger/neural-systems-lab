# PPO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.694 |                36.560 |              11.440 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.694 |                36.560 |              11.442 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.656 |                42.240 |              10.716 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| F_objall             |          0.800 | 0.587 |                56.720 |               9.505 |         25 |              0.120 |              0.130 |          0.107 |          0.155 |
| F_mat                |          0.040 | 0.040 |               192.160 |              -1.522 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |
| R2                   |          0.880 | 0.656 |                42.240 |              10.715 |         25 |              0.040 |              0.043 |          0.038 |          0.055 |
| R3                   |          0.640 | 0.491 |                82.800 |               6.988 |         25 |              0.280 |              0.304 |          0.203 |          0.292 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.240 |              -1.540 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.107 absolute**
- **F_mat: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.038 absolute**
- **R3: success drop 0.280 absolute, 30.4% relative · SPL drop 0.203 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
