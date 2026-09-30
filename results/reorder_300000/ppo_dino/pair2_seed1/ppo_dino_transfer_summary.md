# PPO_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.646 |                44.560 |               8.267 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.646 |                44.520 |               8.274 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.720 | 0.534 |                59.920 |               7.346 |         25 |              0.080 |              0.100 |          0.112 |          0.173 |
| F_objall             |          0.760 | 0.606 |                52.160 |               7.776 |         25 |              0.040 |              0.050 |          0.040 |          0.062 |
| F_mat                |          0.760 | 0.572 |                52.280 |               7.756 |         25 |              0.040 |              0.050 |          0.074 |          0.114 |
| R2                   |          0.760 | 0.574 |                52.320 |               7.831 |         25 |              0.040 |              0.050 |          0.072 |          0.112 |
| R3                   |          0.800 | 0.612 |                44.560 |               8.306 |         25 |              0.000 |              0.000 |          0.034 |          0.052 |
| B_L3 (+ distractors) |          0.800 | 0.614 |                44.320 |               8.266 |         25 |              0.000 |              0.000 |          0.032 |          0.050 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 10.0% relative · SPL drop 0.112 absolute**
- **F_objall: success drop 0.040 absolute, 5.0% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.040 absolute, 5.0% relative · SPL drop 0.074 absolute**
- **R2: success drop 0.040 absolute, 5.0% relative · SPL drop 0.072 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.034 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.032 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
