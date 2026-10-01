# PPO_MAE zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.608 |                55.480 |               9.789 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.607 |                55.600 |               9.793 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_lightsky           |          0.720 | 0.528 |                71.560 |               8.838 |         25 |              0.080 |              0.100 |          0.080 |          0.132 |
| F_objall             |          0.280 | 0.224 |               147.760 |               2.678 |         25 |              0.520 |              0.650 |          0.384 |          0.632 |
| F_mat                |          0.360 | 0.232 |               133.640 |               3.297 |         25 |              0.440 |              0.550 |          0.376 |          0.619 |
| R2                   |          0.720 | 0.528 |                71.560 |               8.843 |         25 |              0.080 |              0.100 |          0.080 |          0.132 |
| R3                   |          0.120 | 0.120 |               177.360 |               0.268 |         25 |              0.680 |              0.850 |          0.488 |          0.803 |
| B_L3 (+ distractors) |          0.120 | 0.069 |               177.160 |              -0.219 |         25 |              0.680 |              0.850 |          0.539 |          0.886 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.080 absolute, 10.0% relative · SPL drop 0.080 absolute**
- **F_objall: success drop 0.520 absolute, 65.0% relative · SPL drop 0.384 absolute**
- **F_mat: success drop 0.440 absolute, 55.0% relative · SPL drop 0.376 absolute**
- **R2: success drop 0.080 absolute, 10.0% relative · SPL drop 0.080 absolute**
- **R3: success drop 0.680 absolute, 85.0% relative · SPL drop 0.488 absolute**
- **L3: success drop 0.680 absolute, 85.0% relative · SPL drop 0.539 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
