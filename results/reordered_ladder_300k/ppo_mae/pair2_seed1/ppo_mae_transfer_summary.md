# PPO_MAE zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.777 |                 8.160 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                 8.160 |              10.695 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.700 |                24.200 |               9.738 |         25 |              0.080 |              0.080 |          0.076 |          0.098 |
| F_objall             |          0.920 | 0.697 |                23.560 |               9.741 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| F_mat                |          0.680 | 0.485 |                70.640 |               6.837 |         25 |              0.320 |              0.320 |          0.291 |          0.375 |
| R2                   |          0.920 | 0.700 |                24.200 |               9.738 |         25 |              0.080 |              0.080 |          0.076 |          0.098 |
| R3                   |          0.840 | 0.620 |                38.560 |               8.787 |         25 |              0.160 |              0.160 |          0.156 |          0.201 |
| B_L3 (+ distractors) |          0.640 | 0.613 |                78.880 |               6.157 |         25 |              0.360 |              0.360 |          0.163 |          0.210 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.076 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.291 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.076 absolute**
- **R3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.156 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.163 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
