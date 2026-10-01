# PPO_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.658 |                29.600 |               9.436 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.658 |                29.600 |               9.436 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.840 | 0.618 |                37.240 |               8.907 |         25 |              0.040 |              0.045 |          0.040 |          0.061 |
| F_objall             |          0.960 | 0.681 |                14.440 |              10.407 |         25 |             -0.080 |             -0.091 |         -0.023 |         -0.035 |
| F_mat                |          0.800 | 0.564 |                45.080 |               8.359 |         25 |              0.080 |              0.091 |          0.094 |          0.143 |
| R2                   |          0.840 | 0.618 |                37.320 |               8.919 |         25 |              0.040 |              0.045 |          0.040 |          0.061 |
| R3                   |          0.880 | 0.601 |                30.080 |               9.397 |         25 |              0.000 |              0.000 |          0.057 |          0.087 |
| B_L3 (+ distractors) |          0.840 | 0.576 |                37.640 |               8.869 |         25 |              0.040 |              0.045 |          0.083 |          0.126 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_objall: success drop -0.080 absolute, -9.1% relative · SPL drop -0.023 absolute**
- **F_mat: success drop 0.080 absolute, 9.1% relative · SPL drop 0.094 absolute**
- **R2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.057 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.083 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
