# DREAMERV3 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.550 |                55.200 |              10.835 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.556 |                54.480 |              10.854 |         25 |              0.000 |              0.000 |         -0.006 |         -0.011 |
| F_lightsky           |          0.560 | 0.360 |                99.440 |               6.441 |         25 |              0.280 |              0.333 |          0.190 |          0.346 |
| F_objall             |          0.840 | 0.599 |                65.760 |              10.425 |         25 |              0.000 |              0.000 |         -0.049 |         -0.090 |
| F_mat                |          0.200 | 0.167 |               166.800 |               0.774 |         25 |              0.640 |              0.762 |          0.383 |          0.697 |
| R2                   |          0.720 | 0.479 |                95.120 |               8.854 |         25 |              0.120 |              0.143 |          0.070 |          0.128 |
| R3                   |          0.480 | 0.337 |               113.720 |               5.377 |         25 |              0.360 |              0.429 |          0.213 |          0.387 |
| B_L3 (+ distractors) |          0.120 | 0.120 |               182.280 |              -0.162 |         25 |              0.720 |              0.857 |          0.430 |          0.782 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.006 absolute**
- **F_lightsky: success drop 0.280 absolute, 33.3% relative · SPL drop 0.190 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.049 absolute**
- **F_mat: success drop 0.640 absolute, 76.2% relative · SPL drop 0.383 absolute**
- **R2: success drop 0.120 absolute, 14.3% relative · SPL drop 0.070 absolute**
- **R3: success drop 0.360 absolute, 42.9% relative · SPL drop 0.213 absolute**
- **L3: success drop 0.720 absolute, 85.7% relative · SPL drop 0.430 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
