# PPO_AUG zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.737 |                27.440 |              10.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.737 |                27.440 |              10.599 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.560 | 0.449 |                95.360 |               5.742 |         25 |              0.360 |              0.391 |          0.288 |          0.391 |
| F_objall             |          0.800 | 0.670 |                50.240 |               9.034 |         25 |              0.120 |              0.130 |          0.067 |          0.091 |
| F_mat                |          0.640 | 0.508 |                79.720 |               6.644 |         25 |              0.280 |              0.304 |          0.229 |          0.310 |
| R2                   |          0.600 | 0.478 |                88.280 |               6.316 |         25 |              0.320 |              0.348 |          0.259 |          0.351 |
| R3                   |          0.280 | 0.219 |               147.960 |               2.011 |         25 |              0.640 |              0.696 |          0.517 |          0.702 |
| B_L3 (+ distractors) |          0.200 | 0.180 |               161.560 |               0.485 |         25 |              0.720 |              0.783 |          0.557 |          0.756 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.360 absolute, 39.1% relative · SPL drop 0.288 absolute**
- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.067 absolute**
- **F_mat: success drop 0.280 absolute, 30.4% relative · SPL drop 0.229 absolute**
- **R2: success drop 0.320 absolute, 34.8% relative · SPL drop 0.259 absolute**
- **R3: success drop 0.640 absolute, 69.6% relative · SPL drop 0.517 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
