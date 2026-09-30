# PPO_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.720 |                 6.560 |              10.884 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.720 |                 6.520 |              10.877 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.720 |                 6.720 |              10.874 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          1.000 | 0.720 |                 6.600 |              10.884 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          0.920 | 0.656 |                22.120 |               9.847 |         25 |              0.080 |              0.080 |          0.064 |          0.089 |
| R2                   |          1.000 | 0.718 |                 6.680 |              10.884 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| R3                   |          1.000 | 0.717 |                 6.840 |              10.889 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| B_L3 (+ distractors) |          0.880 | 0.590 |                30.360 |               9.418 |         25 |              0.120 |              0.120 |          0.130 |          0.180 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.064 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.130 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
