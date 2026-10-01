# PPO_AUG zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.735 |                27.760 |              11.994 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.709 |                34.280 |              11.362 |         25 |              0.040 |              0.042 |          0.026 |          0.035 |
| F_lightsky           |          0.560 | 0.414 |                96.800 |               5.829 |         25 |              0.400 |              0.417 |          0.320 |          0.436 |
| F_objall             |          0.320 | 0.255 |               139.600 |               3.750 |         25 |              0.640 |              0.667 |          0.480 |          0.653 |
| F_mat                |          0.320 | 0.231 |               140.160 |               2.426 |         25 |              0.640 |              0.667 |          0.504 |          0.686 |
| R2                   |          0.560 | 0.414 |                96.800 |               5.835 |         25 |              0.400 |              0.417 |          0.320 |          0.436 |
| R3                   |          0.520 | 0.374 |               105.280 |               5.318 |         25 |              0.440 |              0.458 |          0.360 |          0.490 |
| B_L3 (+ distractors) |          0.280 | 0.191 |               147.960 |               1.777 |         25 |              0.680 |              0.708 |          0.544 |          0.740 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.026 absolute**
- **F_lightsky: success drop 0.400 absolute, 41.7% relative · SPL drop 0.320 absolute**
- **F_objall: success drop 0.640 absolute, 66.7% relative · SPL drop 0.480 absolute**
- **F_mat: success drop 0.640 absolute, 66.7% relative · SPL drop 0.504 absolute**
- **R2: success drop 0.400 absolute, 41.7% relative · SPL drop 0.320 absolute**
- **R3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.360 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.544 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
