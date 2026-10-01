# PPO_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.659 |                29.520 |               9.285 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.659 |                29.480 |               9.282 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.680 | 0.458 |                68.640 |               6.874 |         25 |              0.200 |              0.227 |          0.201 |          0.305 |
| F_objall             |          0.800 | 0.614 |                45.120 |               8.306 |         25 |              0.080 |              0.091 |          0.046 |          0.069 |
| F_mat                |          0.920 | 0.699 |                22.240 |               9.741 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| R2                   |          0.680 | 0.458 |                68.640 |               6.873 |         25 |              0.200 |              0.227 |          0.201 |          0.305 |
| R3                   |          0.640 | 0.453 |                76.240 |               6.381 |         25 |              0.240 |              0.273 |          0.207 |          0.313 |
| B_L3 (+ distractors) |          0.840 | 0.618 |                38.240 |               8.790 |         25 |              0.040 |              0.045 |          0.041 |          0.062 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.200 absolute, 22.7% relative · SPL drop 0.201 absolute**
- **F_objall: success drop 0.080 absolute, 9.1% relative · SPL drop 0.046 absolute**
- **F_mat: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **R2: success drop 0.200 absolute, 22.7% relative · SPL drop 0.201 absolute**
- **R3: success drop 0.240 absolute, 27.3% relative · SPL drop 0.207 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.041 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
