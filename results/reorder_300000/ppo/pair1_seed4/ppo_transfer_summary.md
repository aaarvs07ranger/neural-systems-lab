# PPO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.698 |                21.880 |               9.902 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.658 |                29.640 |               9.410 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_lightsky           |          0.840 | 0.618 |                37.200 |               8.863 |         25 |              0.080 |              0.087 |          0.080 |          0.115 |
| F_objall             |          0.240 | 0.220 |               152.560 |               1.306 |         25 |              0.680 |              0.739 |          0.478 |          0.685 |
| F_mat                |          0.760 | 0.631 |                53.720 |               7.508 |         25 |              0.160 |              0.174 |          0.068 |          0.097 |
| R2                   |          0.840 | 0.618 |                37.200 |               8.863 |         25 |              0.080 |              0.087 |          0.080 |          0.115 |
| R3                   |          0.200 | 0.200 |               160.280 |               0.522 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **F_objall: success drop 0.680 absolute, 73.9% relative · SPL drop 0.478 absolute**
- **F_mat: success drop 0.160 absolute, 17.4% relative · SPL drop 0.068 absolute**
- **R2: success drop 0.080 absolute, 8.7% relative · SPL drop 0.080 absolute**
- **R3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
