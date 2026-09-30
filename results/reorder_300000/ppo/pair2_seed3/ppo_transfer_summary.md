# PPO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.740 |                13.840 |              10.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.740 |                13.840 |              10.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.732 |                21.560 |               9.727 |         25 |              0.040 |              0.042 |          0.008 |          0.011 |
| F_objall             |          0.920 | 0.700 |                21.640 |               9.755 |         25 |              0.040 |              0.042 |          0.040 |          0.054 |
| F_mat                |          0.720 | 0.563 |                59.760 |               7.193 |         25 |              0.240 |              0.250 |          0.178 |          0.240 |
| R2                   |          0.920 | 0.732 |                21.560 |               9.727 |         25 |              0.040 |              0.042 |          0.008 |          0.011 |
| R3                   |          0.840 | 0.652 |                36.920 |               8.718 |         25 |              0.120 |              0.125 |          0.088 |          0.119 |
| B_L3 (+ distractors) |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.008 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.240 absolute, 25.0% relative · SPL drop 0.178 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.008 absolute**
- **R3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.088 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
