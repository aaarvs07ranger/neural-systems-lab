# PPO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.678 |                29.160 |               9.333 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.638 |                37.080 |               8.863 |         25 |              0.040 |              0.045 |          0.040 |          0.059 |
| F_lightsky           |          0.920 | 0.690 |                21.800 |               9.898 |         25 |             -0.040 |             -0.045 |         -0.012 |         -0.018 |
| F_objall             |          0.600 | 0.466 |                83.920 |               5.884 |         25 |              0.280 |              0.318 |          0.212 |          0.313 |
| F_mat                |          0.760 | 0.627 |                53.920 |               7.588 |         25 |              0.120 |              0.136 |          0.051 |          0.075 |
| R2                   |          0.880 | 0.650 |                29.680 |               9.418 |         25 |              0.000 |              0.000 |          0.028 |          0.041 |
| R3                   |          0.200 | 0.200 |               160.280 |               0.589 |         25 |              0.680 |              0.773 |          0.478 |          0.705 |
| B_L3 (+ distractors) |          0.120 | 0.120 |               176.160 |              -0.571 |         25 |              0.760 |              0.864 |          0.558 |          0.823 |

- **F_clut: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.012 absolute**
- **F_objall: success drop 0.280 absolute, 31.8% relative · SPL drop 0.212 absolute**
- **F_mat: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.028 absolute**
- **R3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.478 absolute**
- **L3: success drop 0.760 absolute, 86.4% relative · SPL drop 0.558 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
