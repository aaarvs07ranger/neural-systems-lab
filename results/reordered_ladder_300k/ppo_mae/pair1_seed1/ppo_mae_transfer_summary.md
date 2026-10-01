# PPO_MAE zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.700 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.698 |                21.640 |               9.911 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          0.880 | 0.660 |                29.440 |               9.388 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| F_objall             |          0.960 | 0.679 |                14.840 |              10.413 |         25 |             -0.040 |             -0.043 |          0.021 |          0.030 |
| F_mat                |          0.480 | 0.450 |               106.240 |               3.982 |         25 |              0.440 |              0.478 |          0.250 |          0.357 |
| R2                   |          0.880 | 0.660 |                29.320 |               9.389 |         25 |              0.040 |              0.043 |          0.040 |          0.057 |
| R3                   |          0.760 | 0.610 |                52.640 |               7.794 |         25 |              0.160 |              0.174 |          0.090 |          0.129 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.440 |               0.386 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **F_objall: success drop -0.040 absolute, -4.3% relative · SPL drop 0.021 absolute**
- **F_mat: success drop 0.440 absolute, 47.8% relative · SPL drop 0.250 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.040 absolute**
- **R3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.090 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
