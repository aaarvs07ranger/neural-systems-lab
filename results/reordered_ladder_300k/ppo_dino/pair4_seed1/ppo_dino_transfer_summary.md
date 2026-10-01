# PPO_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.728 |                26.520 |              12.565 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.712 |                26.440 |              12.579 |         25 |              0.000 |              0.000 |          0.016 |          0.022 |
| F_lightsky           |          0.960 | 0.743 |                26.760 |              12.553 |         25 |              0.000 |              0.000 |         -0.016 |         -0.021 |
| F_objall             |          0.920 | 0.687 |                33.640 |              11.805 |         25 |              0.040 |              0.042 |          0.040 |          0.055 |
| F_mat                |          0.640 | 0.406 |                82.760 |               7.867 |         25 |              0.320 |              0.333 |          0.322 |          0.442 |
| R2                   |          0.960 | 0.729 |                26.400 |              12.571 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| R3                   |          0.960 | 0.743 |                26.840 |              12.498 |         25 |              0.000 |              0.000 |         -0.015 |         -0.021 |
| B_L3 (+ distractors) |          0.560 | 0.330 |                97.200 |               6.933 |         25 |              0.400 |              0.417 |          0.398 |          0.547 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.016 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.016 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.322 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.015 absolute**
- **L3: success drop 0.400 absolute, 41.7% relative · SPL drop 0.398 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
