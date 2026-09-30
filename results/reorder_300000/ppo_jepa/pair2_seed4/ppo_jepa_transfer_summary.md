# PPO_JEPA zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.777 |                 7.720 |              10.683 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                 7.720 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.779 |                 8.920 |              10.678 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_objall             |          1.000 | 0.778 |                 7.680 |              10.684 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                |          0.880 | 0.685 |                35.040 |               9.134 |         25 |              0.120 |              0.120 |          0.091 |          0.118 |
| R2                   |          0.840 | 0.619 |                39.240 |               8.745 |         25 |              0.160 |              0.160 |          0.158 |          0.204 |
| R3                   |          1.000 | 0.780 |                 8.360 |              10.702 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| B_L3 (+ distractors) |          0.840 | 0.645 |                43.960 |               8.656 |         25 |              0.160 |              0.160 |          0.131 |          0.169 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.091 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.158 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.131 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
