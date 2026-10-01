# PPO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.699 |                21.960 |               9.760 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.699 |                22.040 |               9.768 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.700 |                22.200 |               9.768 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_objall             |          0.800 | 0.580 |                44.880 |               8.251 |         25 |              0.120 |              0.130 |          0.118 |          0.169 |
| F_mat                |          0.920 | 0.698 |                22.000 |               9.765 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| R2                   |          0.920 | 0.700 |                22.200 |               9.768 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| R3                   |          0.680 | 0.460 |                67.720 |               6.761 |         25 |              0.240 |              0.261 |          0.238 |          0.341 |
| B_L3 (+ distractors) |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.118 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **R3: success drop 0.240 absolute, 26.1% relative · SPL drop 0.238 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
