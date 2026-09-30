# PPO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.675 |                14.240 |              10.383 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.675 |                14.480 |              10.382 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.699 |                14.080 |              10.304 |         25 |              0.000 |              0.000 |         -0.024 |         -0.035 |
| F_objall             |          0.560 | 0.432 |                91.160 |               5.358 |         25 |              0.400 |              0.417 |          0.244 |          0.361 |
| F_mat                |          0.880 | 0.642 |                31.880 |               9.262 |         25 |              0.080 |              0.083 |          0.034 |          0.050 |
| R2                   |          0.920 | 0.659 |                21.960 |               9.806 |         25 |              0.040 |              0.042 |          0.016 |          0.024 |
| R3                   |          0.360 | 0.339 |               129.480 |               2.674 |         25 |              0.600 |              0.625 |          0.336 |          0.498 |
| B_L3 (+ distractors) |          0.360 | 0.306 |               129.720 |               2.566 |         25 |              0.600 |              0.625 |          0.370 |          0.547 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.024 absolute**
- **F_objall: success drop 0.400 absolute, 41.7% relative · SPL drop 0.244 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.034 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.016 absolute**
- **R3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.336 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.370 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
