# PPO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.561 |                36.920 |              12.513 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.561 |                36.920 |              12.513 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.280 | 0.169 |               148.960 |               3.485 |         25 |              0.640 |              0.696 |          0.393 |          0.700 |
| F_objall             |          0.680 | 0.451 |                79.560 |               9.174 |         25 |              0.240 |              0.261 |          0.111 |          0.197 |
| F_mat                |          0.560 | 0.353 |               101.840 |               6.880 |         25 |              0.360 |              0.391 |          0.208 |          0.371 |
| R2                   |          0.280 | 0.169 |               148.960 |               3.475 |         25 |              0.640 |              0.696 |          0.393 |          0.700 |
| R3                   |          0.160 | 0.115 |               170.600 |               2.101 |         25 |              0.760 |              0.826 |          0.447 |          0.796 |
| B_L3 (+ distractors) |          0.120 | 0.098 |               178.400 |               0.111 |         25 |              0.800 |              0.870 |          0.464 |          0.826 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.640 absolute, 69.6% relative · SPL drop 0.393 absolute**
- **F_objall: success drop 0.240 absolute, 26.1% relative · SPL drop 0.111 absolute**
- **F_mat: success drop 0.360 absolute, 39.1% relative · SPL drop 0.208 absolute**
- **R2: success drop 0.640 absolute, 69.6% relative · SPL drop 0.393 absolute**
- **R3: success drop 0.760 absolute, 82.6% relative · SPL drop 0.447 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.464 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
