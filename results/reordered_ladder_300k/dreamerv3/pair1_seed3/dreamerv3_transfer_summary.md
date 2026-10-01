# DREAMERV3 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.550 |                50.320 |               9.032 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.549 |                54.280 |               8.498 |         25 |              0.040 |              0.048 |          0.000 |          0.001 |
| F_lightsky           |          0.800 | 0.553 |                61.760 |               8.392 |         25 |              0.040 |              0.048 |         -0.003 |         -0.005 |
| F_objall             |          1.000 | 0.693 |                11.160 |              10.823 |         25 |             -0.160 |             -0.190 |         -0.143 |         -0.261 |
| F_mat                |          0.360 | 0.333 |               132.840 |               2.459 |         25 |              0.480 |              0.571 |          0.217 |          0.394 |
| R2                   |          0.800 | 0.525 |                53.240 |               8.500 |         25 |              0.040 |              0.048 |          0.025 |          0.045 |
| R3                   |          1.000 | 0.682 |                10.880 |              10.825 |         25 |             -0.160 |             -0.190 |         -0.132 |         -0.241 |
| B_L3 (+ distractors) |          0.400 | 0.304 |               137.880 |               2.879 |         25 |              0.440 |              0.524 |          0.246 |          0.447 |

- **F_clut: success drop 0.040 absolute, 4.8% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.8% relative · SPL drop -0.003 absolute**
- **F_objall: success drop -0.160 absolute, -19.0% relative · SPL drop -0.143 absolute**
- **F_mat: success drop 0.480 absolute, 57.1% relative · SPL drop 0.217 absolute**
- **R2: success drop 0.040 absolute, 4.8% relative · SPL drop 0.025 absolute**
- **R3: success drop -0.160 absolute, -19.0% relative · SPL drop -0.132 absolute**
- **L3: success drop 0.440 absolute, 52.4% relative · SPL drop 0.246 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
