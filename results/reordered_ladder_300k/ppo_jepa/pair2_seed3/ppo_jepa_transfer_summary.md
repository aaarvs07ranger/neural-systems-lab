# PPO_JEPA zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.774 |                15.760 |              10.204 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 8.200 |              10.680 |         25 |             -0.040 |             -0.042 |         -0.006 |         -0.007 |
| F_lightsky           |          1.000 | 0.778 |                 8.640 |              10.676 |         25 |             -0.040 |             -0.042 |         -0.004 |         -0.005 |
| F_objall             |          0.960 | 0.774 |                16.240 |              10.200 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                |          0.680 | 0.483 |                70.920 |               6.619 |         25 |              0.280 |              0.292 |          0.290 |          0.375 |
| R2                   |          1.000 | 0.778 |                 8.640 |              10.676 |         25 |             -0.040 |             -0.042 |         -0.004 |         -0.005 |
| R3                   |          0.800 | 0.579 |                47.320 |               8.290 |         25 |              0.160 |              0.167 |          0.194 |          0.251 |
| B_L3 (+ distractors) |          0.440 | 0.440 |               115.800 |               3.553 |         25 |              0.520 |              0.542 |          0.334 |          0.431 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.006 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.2% relative · SPL drop -0.004 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.280 absolute, 29.2% relative · SPL drop 0.290 absolute**
- **R2: success drop -0.040 absolute, -4.2% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.194 absolute**
- **L3: success drop 0.520 absolute, 54.2% relative · SPL drop 0.334 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
