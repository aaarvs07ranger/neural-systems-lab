# PPO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.806 |                19.560 |              13.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.806 |                19.560 |              13.232 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.666 |                46.120 |              10.451 |         25 |              0.160 |              0.160 |          0.140 |          0.174 |
| F_objall             |          0.960 | 0.776 |                26.280 |              12.607 |         25 |              0.040 |              0.040 |          0.030 |          0.037 |
| F_mat                |          0.200 | 0.159 |               162.640 |               0.875 |         25 |              0.800 |              0.800 |          0.646 |          0.802 |
| R2                   |          0.840 | 0.666 |                46.160 |              10.453 |         25 |              0.160 |              0.160 |          0.140 |          0.174 |
| R3                   |          0.720 | 0.565 |                67.160 |               8.764 |         25 |              0.280 |              0.280 |          0.241 |          0.299 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.120 |              -1.183 |         25 |              0.960 |              0.960 |          0.766 |          0.950 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.140 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.030 absolute**
- **F_mat: success drop 0.800 absolute, 80.0% relative · SPL drop 0.646 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.140 absolute**
- **R3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.241 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.766 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
