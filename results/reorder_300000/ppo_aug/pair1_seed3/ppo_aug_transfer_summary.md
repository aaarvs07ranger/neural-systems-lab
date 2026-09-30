# PPO_AUG zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.717 |                 9.160 |              10.831 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          0.880 | 0.648 |                33.240 |               9.377 |         25 |              0.120 |              0.120 |          0.069 |          0.097 |
| F_mat                |          0.800 | 0.647 |                46.440 |               8.151 |         25 |              0.200 |              0.200 |          0.070 |          0.098 |
| R2                   |          1.000 | 0.717 |                 9.240 |              10.846 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| R3                   |          0.680 | 0.585 |                70.880 |               6.812 |         25 |              0.320 |              0.320 |          0.132 |          0.185 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.640 |               0.412 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.069 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.070 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **R3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.132 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
