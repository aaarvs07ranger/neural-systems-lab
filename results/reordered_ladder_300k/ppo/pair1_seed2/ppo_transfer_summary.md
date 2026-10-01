# PPO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.717 |                 6.720 |              10.889 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.717 |                 6.720 |              10.889 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.621 |                29.280 |               9.275 |         25 |              0.120 |              0.120 |          0.096 |          0.135 |
| F_objall             |          0.480 | 0.380 |               106.520 |               4.279 |         25 |              0.520 |              0.520 |          0.338 |          0.471 |
| F_mat                |          0.920 | 0.693 |                24.920 |               9.847 |         25 |              0.080 |              0.080 |          0.025 |          0.034 |
| R2                   |          0.920 | 0.689 |                21.760 |               9.833 |         25 |              0.080 |              0.080 |          0.028 |          0.039 |
| R3                   |          0.200 | 0.200 |               160.400 |               0.568 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.096 absolute**
- **F_objall: success drop 0.520 absolute, 52.0% relative · SPL drop 0.338 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.025 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.028 absolute**
- **R3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
