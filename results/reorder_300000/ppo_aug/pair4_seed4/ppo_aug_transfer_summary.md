# PPO_AUG zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.733 |                27.160 |              12.483 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.733 |                27.160 |              12.483 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.704 |                42.280 |              11.383 |         25 |              0.080 |              0.083 |          0.029 |          0.039 |
| F_objall             |          0.880 | 0.655 |                40.560 |              11.071 |         25 |              0.080 |              0.083 |          0.078 |          0.106 |
| F_mat                |          0.000 | 0.000 |               200.000 |              -2.751 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |
| R2                   |          0.880 | 0.701 |                42.320 |              11.387 |         25 |              0.080 |              0.083 |          0.032 |          0.044 |
| R3                   |          0.760 | 0.571 |                62.200 |               9.410 |         25 |              0.200 |              0.208 |          0.162 |          0.221 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.213 |         25 |              0.960 |              1.000 |          0.733 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.029 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.078 absolute**
- **F_mat: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.032 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.162 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.733 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
