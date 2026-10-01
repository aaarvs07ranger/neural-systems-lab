# PPO_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.717 |                 6.640 |              10.887 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.717 |                 6.600 |              10.882 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.676 |                14.600 |              10.399 |         25 |              0.040 |              0.040 |          0.042 |          0.058 |
| F_objall             |          0.920 | 0.637 |                21.880 |               9.849 |         25 |              0.080 |              0.080 |          0.080 |          0.112 |
| F_mat                |          0.680 | 0.463 |                68.240 |               6.833 |         25 |              0.320 |              0.320 |          0.254 |          0.354 |
| R2                   |          1.000 | 0.716 |                 6.720 |              10.887 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| R3                   |          0.960 | 0.696 |                14.520 |              10.410 |         25 |              0.040 |              0.040 |          0.022 |          0.030 |
| B_L3 (+ distractors) |          0.840 | 0.569 |                37.960 |               8.904 |         25 |              0.160 |              0.160 |          0.148 |          0.207 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **F_mat: success drop 0.320 absolute, 32.0% relative · SPL drop 0.254 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.022 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
