# PPO_MAE zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.710 |                14.160 |              10.391 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.708 |                14.240 |              10.388 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_lightsky           |          0.880 | 0.658 |                29.520 |               9.400 |         25 |              0.080 |              0.083 |          0.051 |          0.072 |
| F_objall             |          1.000 | 0.718 |                 7.000 |              10.901 |         25 |             -0.040 |             -0.042 |         -0.008 |         -0.011 |
| F_mat                |          0.680 | 0.473 |                68.640 |               6.853 |         25 |              0.280 |              0.292 |          0.237 |          0.334 |
| R2                   |          0.920 | 0.698 |                22.000 |               9.904 |         25 |              0.040 |              0.042 |          0.011 |          0.016 |
| R3                   |          0.800 | 0.532 |                45.880 |               8.330 |         25 |              0.160 |              0.167 |          0.178 |          0.251 |
| B_L3 (+ distractors) |          0.160 | 0.160 |               168.240 |              -0.120 |         25 |              0.800 |              0.833 |          0.550 |          0.775 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.051 absolute**
- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.008 absolute**
- **F_mat: success drop 0.280 absolute, 29.2% relative · SPL drop 0.237 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.011 absolute**
- **R3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.178 absolute**
- **L3: success drop 0.800 absolute, 83.3% relative · SPL drop 0.550 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
