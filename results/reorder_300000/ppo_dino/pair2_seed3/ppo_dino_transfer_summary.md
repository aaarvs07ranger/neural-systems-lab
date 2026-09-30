# PPO_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.659 |                28.960 |               9.259 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.699 |                21.480 |               9.771 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_lightsky           |          0.880 | 0.659 |                29.120 |               9.254 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          0.880 | 0.659 |                29.080 |               9.252 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          0.800 | 0.580 |                44.320 |               8.142 |         25 |              0.080 |              0.091 |          0.079 |          0.120 |
| R2                   |          0.920 | 0.699 |                21.520 |               9.774 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| R3                   |          0.960 | 0.739 |                13.920 |              10.243 |         25 |             -0.080 |             -0.091 |         -0.080 |         -0.121 |
| B_L3 (+ distractors) |          0.640 | 0.512 |                74.920 |               6.109 |         25 |              0.240 |              0.273 |          0.147 |          0.224 |

- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.080 absolute, 9.1% relative · SPL drop 0.079 absolute**
- **R2: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **R3: success drop -0.080 absolute, -9.1% relative · SPL drop -0.080 absolute**
- **L3: success drop 0.240 absolute, 27.3% relative · SPL drop 0.147 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
