# PPO_MAE zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.778 |                 8.400 |              10.713 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.778 |                 8.400 |              10.713 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.520 | 0.300 |               101.040 |               4.898 |         25 |              0.480 |              0.480 |          0.478 |          0.614 |
| F_objall             |          0.840 | 0.618 |                38.640 |               8.782 |         25 |              0.160 |              0.160 |          0.160 |          0.206 |
| F_mat                |          0.040 | 0.040 |               192.040 |              -1.454 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |
| R2                   |          0.520 | 0.300 |               101.040 |               4.894 |         25 |              0.480 |              0.480 |          0.478 |          0.614 |
| R3                   |          0.480 | 0.260 |               108.520 |               4.393 |         25 |              0.520 |              0.520 |          0.518 |          0.666 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.480 absolute, 48.0% relative · SPL drop 0.478 absolute**
- **F_objall: success drop 0.160 absolute, 16.0% relative · SPL drop 0.160 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**
- **R2: success drop 0.480 absolute, 48.0% relative · SPL drop 0.478 absolute**
- **R3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.518 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
