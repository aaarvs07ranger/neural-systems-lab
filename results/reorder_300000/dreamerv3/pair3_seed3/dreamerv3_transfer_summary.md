# DREAMERV3 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.619 |                45.240 |              12.302 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.619 |                44.680 |              12.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.565 |                58.520 |              11.349 |         25 |              0.080 |              0.080 |          0.054 |          0.087 |
| F_objall             |          0.960 | 0.599 |                59.040 |              11.607 |         25 |              0.040 |              0.040 |          0.020 |          0.032 |
| F_mat                |          0.440 | 0.281 |               144.720 |               4.057 |         25 |              0.560 |              0.560 |          0.338 |          0.547 |
| R2                   |          0.920 | 0.578 |                59.480 |              11.342 |         25 |              0.080 |              0.080 |          0.041 |          0.066 |
| R3                   |          1.000 | 0.626 |                44.800 |              12.329 |         25 |              0.000 |              0.000 |         -0.007 |         -0.011 |
| B_L3 (+ distractors) |          0.200 | 0.138 |               172.640 |               0.821 |         25 |              0.800 |              0.800 |          0.481 |          0.777 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.0% relative · SPL drop 0.054 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.020 absolute**
- **F_mat: success drop 0.560 absolute, 56.0% relative · SPL drop 0.338 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.041 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.481 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
