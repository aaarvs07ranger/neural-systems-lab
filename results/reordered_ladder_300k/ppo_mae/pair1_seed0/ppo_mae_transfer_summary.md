# PPO_MAE zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.652 |                29.680 |               9.438 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.704 |                14.120 |              10.371 |         25 |             -0.080 |             -0.091 |         -0.052 |         -0.080 |
| F_lightsky           |          0.840 | 0.614 |                37.320 |               8.892 |         25 |              0.040 |              0.045 |          0.038 |          0.058 |
| F_objall             |          1.000 | 0.720 |                 6.840 |              10.891 |         25 |             -0.120 |             -0.136 |         -0.067 |         -0.103 |
| F_mat                |          0.400 | 0.373 |               121.160 |               3.038 |         25 |              0.480 |              0.545 |          0.279 |          0.428 |
| R2                   |          0.920 | 0.664 |                22.000 |               9.867 |         25 |             -0.040 |             -0.045 |         -0.012 |         -0.018 |
| R3                   |          0.840 | 0.570 |                37.680 |               8.803 |         25 |              0.040 |              0.045 |          0.083 |          0.127 |
| B_L3 (+ distractors) |          0.160 | 0.160 |               168.440 |              -0.094 |         25 |              0.720 |              0.818 |          0.492 |          0.755 |

- **F_clut: success drop -0.080 absolute, -9.1% relative · SPL drop -0.052 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.038 absolute**
- **F_objall: success drop -0.120 absolute, -13.6% relative · SPL drop -0.067 absolute**
- **F_mat: success drop 0.480 absolute, 54.5% relative · SPL drop 0.279 absolute**
- **R2: success drop -0.040 absolute, -4.5% relative · SPL drop -0.012 absolute**
- **R3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.083 absolute**
- **L3: success drop 0.720 absolute, 81.8% relative · SPL drop 0.492 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
