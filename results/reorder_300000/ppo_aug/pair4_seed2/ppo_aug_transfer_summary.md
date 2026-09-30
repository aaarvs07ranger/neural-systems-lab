# PPO_AUG zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.744 |                23.360 |              13.189 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.741 |                23.400 |              13.187 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          1.000 | 0.730 |                23.760 |              13.182 |         25 |              0.000 |              0.000 |          0.014 |          0.018 |
| F_objall             |          0.920 | 0.677 |                37.440 |              11.776 |         25 |              0.080 |              0.080 |          0.067 |          0.090 |
| F_mat                |          0.040 | 0.020 |               192.200 |              -1.613 |         25 |              0.960 |              0.960 |          0.724 |          0.973 |
| R2                   |          1.000 | 0.727 |                23.800 |              13.179 |         25 |              0.000 |              0.000 |          0.016 |          0.022 |
| R3                   |          0.880 | 0.617 |                44.160 |              11.290 |         25 |              0.120 |              0.120 |          0.127 |          0.170 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.064 |         25 |              1.000 |              1.000 |          0.744 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.014 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.067 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.724 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.016 absolute**
- **R3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.127 absolute**
- **L3: success drop 1.000 absolute, 100.0% relative · SPL drop 0.744 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
