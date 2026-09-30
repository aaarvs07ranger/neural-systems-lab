# PPO_AUG zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.560 |                50.640 |              11.071 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.578 |                43.240 |              11.633 |         25 |             -0.040 |             -0.048 |         -0.019 |         -0.034 |
| F_lightsky           |          0.880 | 0.563 |                43.800 |              11.682 |         25 |             -0.040 |             -0.048 |         -0.004 |         -0.007 |
| F_objall             |          0.800 | 0.593 |                57.320 |              10.476 |         25 |              0.040 |              0.048 |         -0.033 |         -0.059 |
| F_mat                |          0.800 | 0.482 |                59.280 |              10.192 |         25 |              0.040 |              0.048 |          0.078 |          0.139 |
| R2                   |          0.880 | 0.563 |                43.800 |              11.682 |         25 |             -0.040 |             -0.048 |         -0.004 |         -0.007 |
| R3                   |          0.720 | 0.522 |                70.480 |               9.138 |         25 |              0.120 |              0.143 |          0.037 |          0.067 |
| B_L3 (+ distractors) |          0.520 | 0.351 |               108.520 |               6.095 |         25 |              0.320 |              0.381 |          0.208 |          0.372 |

- **F_clut: success drop -0.040 absolute, -4.8% relative · SPL drop -0.019 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.8% relative · SPL drop -0.004 absolute**
- **F_objall: success drop 0.040 absolute, 4.8% relative · SPL drop -0.033 absolute**
- **F_mat: success drop 0.040 absolute, 4.8% relative · SPL drop 0.078 absolute**
- **R2: success drop -0.040 absolute, -4.8% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.120 absolute, 14.3% relative · SPL drop 0.037 absolute**
- **L3: success drop 0.320 absolute, 38.1% relative · SPL drop 0.208 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
