# PPO_MAE zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.700 |                33.360 |              12.041 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.663 |                40.400 |              11.474 |         25 |              0.040 |              0.043 |          0.037 |          0.052 |
| F_lightsky           |          0.640 | 0.468 |                83.200 |               8.134 |         25 |              0.280 |              0.304 |          0.232 |          0.331 |
| F_objall             |          0.840 | 0.622 |                48.080 |              10.846 |         25 |              0.080 |              0.087 |          0.078 |          0.111 |
| F_mat                |          0.240 | 0.182 |               154.480 |               1.760 |         25 |              0.680 |              0.739 |          0.518 |          0.740 |
| R2                   |          0.680 | 0.477 |                75.960 |               8.424 |         25 |              0.240 |              0.261 |          0.223 |          0.318 |
| R3                   |          0.240 | 0.201 |               155.640 |               2.593 |         25 |              0.680 |              0.739 |          0.499 |          0.713 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.136 |         25 |              0.920 |              1.000 |          0.700 |          1.000 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.037 absolute**
- **F_lightsky: success drop 0.280 absolute, 30.4% relative · SPL drop 0.232 absolute**
- **F_objall: success drop 0.080 absolute, 8.7% relative · SPL drop 0.078 absolute**
- **F_mat: success drop 0.680 absolute, 73.9% relative · SPL drop 0.518 absolute**
- **R2: success drop 0.240 absolute, 26.1% relative · SPL drop 0.223 absolute**
- **R3: success drop 0.680 absolute, 73.9% relative · SPL drop 0.499 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.700 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
