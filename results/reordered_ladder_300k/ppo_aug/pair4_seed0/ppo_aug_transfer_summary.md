# PPO_AUG zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.740 |                25.320 |              12.578 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.740 |                25.240 |              12.603 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.741 |                25.440 |              12.590 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_objall             |          1.000 | 0.799 |                18.440 |              13.217 |         25 |             -0.040 |             -0.042 |         -0.059 |         -0.080 |
| F_mat                |          0.640 | 0.461 |                82.040 |               7.599 |         25 |              0.320 |              0.333 |          0.279 |          0.377 |
| R2                   |          0.960 | 0.741 |                25.440 |              12.582 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| R3                   |          0.960 | 0.762 |                25.000 |              12.648 |         25 |              0.000 |              0.000 |         -0.023 |         -0.030 |
| B_L3 (+ distractors) |          0.400 | 0.319 |               125.240 |               4.191 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_objall: success drop -0.040 absolute, -4.2% relative · SPL drop -0.059 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.279 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.023 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
