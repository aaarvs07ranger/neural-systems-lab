# PPO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.774 |                17.640 |              10.981 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.730 |                32.440 |               9.872 |         25 |              0.080 |              0.083 |          0.044 |          0.057 |
| F_lightsky           |          0.560 | 0.451 |                94.000 |               5.770 |         25 |              0.400 |              0.417 |          0.322 |          0.417 |
| F_objall             |          0.240 | 0.196 |               153.880 |               2.010 |         25 |              0.720 |              0.750 |          0.578 |          0.747 |
| F_mat                |          0.800 | 0.657 |                47.800 |               8.937 |         25 |              0.160 |              0.167 |          0.117 |          0.151 |
| R2                   |          0.600 | 0.488 |                86.680 |               6.334 |         25 |              0.360 |              0.375 |          0.286 |          0.369 |
| R3                   |          0.080 | 0.080 |               184.160 |              -0.340 |         25 |              0.880 |              0.917 |          0.694 |          0.897 |
| B_L3 (+ distractors) |          0.120 | 0.098 |               176.600 |               0.147 |         25 |              0.840 |              0.875 |          0.676 |          0.874 |

- **F_clut: success drop 0.080 absolute, 8.3% relative · SPL drop 0.044 absolute**
- **F_lightsky: success drop 0.400 absolute, 41.7% relative · SPL drop 0.322 absolute**
- **F_objall: success drop 0.720 absolute, 75.0% relative · SPL drop 0.578 absolute**
- **F_mat: success drop 0.160 absolute, 16.7% relative · SPL drop 0.117 absolute**
- **R2: success drop 0.360 absolute, 37.5% relative · SPL drop 0.286 absolute**
- **R3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.694 absolute**
- **L3: success drop 0.840 absolute, 87.5% relative · SPL drop 0.676 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
