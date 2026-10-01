# PPO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.808 |                11.280 |              11.604 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.808 |                11.200 |              11.605 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.320 | 0.298 |               138.640 |               2.333 |         25 |              0.680 |              0.680 |          0.510 |          0.631 |
| F_objall             |          0.200 | 0.188 |               162.160 |               1.501 |         25 |              0.800 |              0.800 |          0.620 |          0.767 |
| F_mat                |          0.520 | 0.441 |               100.920 |               4.688 |         25 |              0.480 |              0.480 |          0.367 |          0.454 |
| R2                   |          0.320 | 0.288 |               138.920 |               2.328 |         25 |              0.680 |              0.680 |          0.520 |          0.643 |
| R3                   |          0.080 | 0.070 |               184.920 |              -1.069 |         25 |              0.920 |              0.920 |          0.738 |          0.914 |
| B_L3 (+ distractors) |          0.240 | 0.211 |               155.800 |               1.567 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.680 absolute, 68.0% relative · SPL drop 0.510 absolute**
- **F_objall: success drop 0.800 absolute, 80.0% relative · SPL drop 0.620 absolute**
- **F_mat: success drop 0.480 absolute, 48.0% relative · SPL drop 0.367 absolute**
- **R2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.520 absolute**
- **R3: success drop 0.920 absolute, 92.0% relative · SPL drop 0.738 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
