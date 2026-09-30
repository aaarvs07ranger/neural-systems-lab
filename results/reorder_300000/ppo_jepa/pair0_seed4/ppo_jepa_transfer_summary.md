# PPO_JEPA zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.780 |                17.520 |              10.971 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.777 |                17.560 |              10.976 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_lightsky           |          0.960 | 0.761 |                17.880 |              10.972 |         25 |              0.000 |              0.000 |          0.020 |          0.026 |
| F_objall             |          0.640 | 0.497 |                79.080 |               6.960 |         25 |              0.320 |              0.333 |          0.284 |          0.364 |
| F_mat                |          0.960 | 0.780 |                17.600 |              10.987 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| R2                   |          0.920 | 0.731 |                25.120 |              10.393 |         25 |              0.040 |              0.042 |          0.049 |          0.063 |
| R3                   |          0.440 | 0.369 |               115.680 |               4.212 |         25 |              0.520 |              0.542 |          0.412 |          0.528 |
| B_L3 (+ distractors) |          0.400 | 0.329 |               123.680 |               3.541 |         25 |              0.560 |              0.583 |          0.452 |          0.579 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.020 absolute**
- **F_objall: success drop 0.320 absolute, 33.3% relative · SPL drop 0.284 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.049 absolute**
- **R3: success drop 0.520 absolute, 54.2% relative · SPL drop 0.412 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.452 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
