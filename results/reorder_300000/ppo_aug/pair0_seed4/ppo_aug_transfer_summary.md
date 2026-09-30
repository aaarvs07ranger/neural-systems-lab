# PPO_AUG zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.688 |                41.000 |               9.505 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.840 | 0.685 |                41.160 |               9.506 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_lightsky           |          0.840 | 0.691 |                41.520 |               9.470 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_objall             |          0.600 | 0.500 |                86.720 |               6.240 |         25 |              0.240 |              0.286 |          0.188 |          0.273 |
| F_mat                |          0.920 | 0.754 |                25.960 |              10.423 |         25 |             -0.080 |             -0.095 |         -0.067 |         -0.097 |
| R2                   |          0.720 | 0.621 |                63.960 |               7.876 |         25 |              0.120 |              0.143 |          0.066 |          0.097 |
| R3                   |          0.520 | 0.457 |               102.480 |               5.257 |         25 |              0.320 |              0.381 |          0.231 |          0.335 |
| B_L3 (+ distractors) |          0.200 | 0.166 |               161.680 |               1.228 |         25 |              0.640 |              0.762 |          0.522 |          0.759 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_objall: success drop 0.240 absolute, 28.6% relative · SPL drop 0.188 absolute**
- **F_mat: success drop -0.080 absolute, -9.5% relative · SPL drop -0.067 absolute**
- **R2: success drop 0.120 absolute, 14.3% relative · SPL drop 0.066 absolute**
- **R3: success drop 0.320 absolute, 38.1% relative · SPL drop 0.231 absolute**
- **L3: success drop 0.640 absolute, 76.2% relative · SPL drop 0.522 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
