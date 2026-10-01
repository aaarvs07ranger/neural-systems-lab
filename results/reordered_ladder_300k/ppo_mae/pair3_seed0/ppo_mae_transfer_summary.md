# PPO_MAE zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.730 |                27.680 |              11.993 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.752 |                20.480 |              12.570 |         25 |             -0.040 |             -0.042 |         -0.022 |         -0.029 |
| F_lightsky           |          0.880 | 0.655 |                40.440 |              10.579 |         25 |              0.080 |              0.083 |          0.075 |          0.103 |
| F_objall             |          0.760 | 0.578 |                63.200 |               9.363 |         25 |              0.200 |              0.208 |          0.152 |          0.209 |
| F_mat                |          0.560 | 0.412 |                96.640 |               5.664 |         25 |              0.400 |              0.417 |          0.318 |          0.436 |
| R2                   |          0.880 | 0.653 |                41.800 |              10.569 |         25 |              0.080 |              0.083 |          0.077 |          0.106 |
| R3                   |          0.720 | 0.531 |                71.600 |               8.826 |         25 |              0.240 |              0.250 |          0.199 |          0.273 |
| B_L3 (+ distractors) |          0.480 | 0.365 |               111.360 |               5.012 |         25 |              0.480 |              0.500 |          0.365 |          0.500 |

- **F_clut: success drop -0.040 absolute, -4.2% relative · SPL drop -0.022 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.075 absolute**
- **F_objall: success drop 0.200 absolute, 20.8% relative · SPL drop 0.152 absolute**
- **F_mat: success drop 0.400 absolute, 41.7% relative · SPL drop 0.318 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.077 absolute**
- **R3: success drop 0.240 absolute, 25.0% relative · SPL drop 0.199 absolute**
- **L3: success drop 0.480 absolute, 50.0% relative · SPL drop 0.365 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
