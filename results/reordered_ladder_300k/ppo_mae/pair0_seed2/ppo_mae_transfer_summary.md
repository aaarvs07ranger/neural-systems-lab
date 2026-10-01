# PPO_MAE zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.774 |                17.920 |              10.964 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.776 |                17.720 |              10.962 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_lightsky           |          0.960 | 0.767 |                18.200 |              10.957 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| F_objall             |          0.600 | 0.495 |                86.640 |               6.499 |         25 |              0.360 |              0.375 |          0.279 |          0.361 |
| F_mat                |          0.880 | 0.679 |                33.760 |               9.975 |         25 |              0.080 |              0.083 |          0.095 |          0.122 |
| R2                   |          0.960 | 0.767 |                18.200 |              10.966 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| R3                   |          0.520 | 0.432 |               102.880 |               5.315 |         25 |              0.440 |              0.458 |          0.342 |          0.441 |
| B_L3 (+ distractors) |          0.520 | 0.453 |               101.160 |               5.064 |         25 |              0.440 |              0.458 |          0.321 |          0.414 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **F_objall: success drop 0.360 absolute, 37.5% relative · SPL drop 0.279 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.095 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **R3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.342 absolute**
- **L3: success drop 0.440 absolute, 45.8% relative · SPL drop 0.321 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
