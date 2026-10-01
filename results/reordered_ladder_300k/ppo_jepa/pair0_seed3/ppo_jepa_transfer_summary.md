# PPO_JEPA zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.750 |                18.120 |              10.966 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.753 |                18.080 |              10.965 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_lightsky           |          0.880 | 0.692 |                33.360 |               9.879 |         25 |              0.080 |              0.083 |          0.058 |          0.077 |
| F_objall             |          0.680 | 0.527 |                71.200 |               7.197 |         25 |              0.280 |              0.292 |          0.223 |          0.298 |
| F_mat                |          0.960 | 0.754 |                18.240 |              10.975 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| R2                   |          0.880 | 0.699 |                33.200 |               9.882 |         25 |              0.080 |              0.083 |          0.052 |          0.069 |
| R3                   |          0.520 | 0.409 |               102.160 |               5.171 |         25 |              0.440 |              0.458 |          0.341 |          0.455 |
| B_L3 (+ distractors) |          0.560 | 0.435 |                95.280 |               5.705 |         25 |              0.400 |              0.417 |          0.315 |          0.420 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.058 absolute**
- **F_objall: success drop 0.280 absolute, 29.2% relative · SPL drop 0.223 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.052 absolute**
- **R3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.341 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.315 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
