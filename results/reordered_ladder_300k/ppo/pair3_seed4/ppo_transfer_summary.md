# PPO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.730 |                27.960 |              11.950 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.730 |                27.960 |              11.950 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.520 | 0.400 |               103.560 |               5.117 |         25 |              0.440 |              0.458 |          0.330 |          0.452 |
| F_objall             |          0.120 | 0.120 |               177.160 |               1.149 |         25 |              0.840 |              0.875 |          0.610 |          0.836 |
| F_mat                |          0.040 | 0.025 |               192.400 |              -1.633 |         25 |              0.920 |              0.958 |          0.705 |          0.966 |
| R2                   |          0.520 | 0.400 |               103.560 |               5.125 |         25 |              0.440 |              0.458 |          0.330 |          0.452 |
| R3                   |          0.320 | 0.234 |               140.600 |               2.504 |         25 |              0.640 |              0.667 |          0.497 |          0.680 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.879 |         25 |              0.960 |              1.000 |          0.730 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.440 absolute, 45.8% relative · SPL drop 0.330 absolute**
- **F_objall: success drop 0.840 absolute, 87.5% relative · SPL drop 0.610 absolute**
- **F_mat: success drop 0.920 absolute, 95.8% relative · SPL drop 0.705 absolute**
- **R2: success drop 0.440 absolute, 45.8% relative · SPL drop 0.330 absolute**
- **R3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.497 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.730 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
