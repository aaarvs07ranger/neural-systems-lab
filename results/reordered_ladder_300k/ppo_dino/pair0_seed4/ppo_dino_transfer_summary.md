# PPO_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.757 |                24.800 |              10.470 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.757 |                24.800 |              10.452 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.755 |                25.000 |              10.467 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_objall             |          0.840 | 0.675 |                40.240 |               9.404 |         25 |              0.080 |              0.087 |          0.082 |          0.108 |
| F_mat                |          0.880 | 0.732 |                32.240 |               9.914 |         25 |              0.040 |              0.043 |          0.024 |          0.032 |
| R2                   |          0.920 | 0.755 |                25.000 |              10.442 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| R3                   |          0.840 | 0.663 |                40.360 |               9.346 |         25 |              0.080 |              0.087 |          0.094 |          0.124 |
| B_L3 (+ distractors) |          0.880 | 0.712 |                32.560 |               9.858 |         25 |              0.040 |              0.043 |          0.044 |          0.059 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_objall: success drop 0.080 absolute, 8.7% relative · SPL drop 0.082 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.024 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R3: success drop 0.080 absolute, 8.7% relative · SPL drop 0.094 absolute**
- **L3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.044 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
