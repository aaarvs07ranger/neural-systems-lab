# PPO_MAE zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.571 |                56.720 |               9.718 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.573 |                56.520 |               9.760 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_lightsky           |          0.800 | 0.587 |                57.040 |               9.472 |         25 |              0.000 |              0.000 |         -0.016 |         -0.028 |
| F_objall             |          0.720 | 0.498 |                71.640 |               8.674 |         25 |              0.080 |              0.100 |          0.073 |          0.128 |
| F_mat                |          0.080 | 0.038 |               184.560 |              -0.371 |         25 |              0.720 |              0.900 |          0.533 |          0.933 |
| R2                   |          0.840 | 0.610 |                50.520 |              10.093 |         25 |             -0.040 |             -0.050 |         -0.040 |         -0.069 |
| R3                   |          0.400 | 0.239 |               127.000 |               4.335 |         25 |              0.400 |              0.500 |          0.332 |          0.581 |
| B_L3 (+ distractors) |          0.040 | 0.025 |               192.320 |              -1.180 |         25 |              0.760 |              0.950 |          0.546 |          0.956 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **F_objall: success drop 0.080 absolute, 10.0% relative · SPL drop 0.073 absolute**
- **F_mat: success drop 0.720 absolute, 90.0% relative · SPL drop 0.533 absolute**
- **R2: success drop -0.040 absolute, -5.0% relative · SPL drop -0.040 absolute**
- **R3: success drop 0.400 absolute, 50.0% relative · SPL drop 0.332 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.546 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
