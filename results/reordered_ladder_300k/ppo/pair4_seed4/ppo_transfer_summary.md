# PPO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.600 |                37.520 |              12.646 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.600 |                37.520 |              12.646 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.586 |                44.480 |              12.139 |         25 |              0.040 |              0.043 |          0.014 |          0.024 |
| F_objall             |          0.680 | 0.466 |                78.120 |               9.339 |         25 |              0.240 |              0.261 |          0.134 |          0.224 |
| F_mat                |          0.880 | 0.510 |                48.360 |              11.851 |         25 |              0.040 |              0.043 |          0.090 |          0.150 |
| R2                   |          0.880 | 0.586 |                44.480 |              12.139 |         25 |              0.040 |              0.043 |          0.014 |          0.024 |
| R3                   |          0.720 | 0.520 |                72.120 |              10.095 |         25 |              0.200 |              0.217 |          0.080 |          0.133 |
| B_L3 (+ distractors) |          0.640 | 0.430 |                87.880 |               8.099 |         25 |              0.280 |              0.304 |          0.170 |          0.284 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.014 absolute**
- **F_objall: success drop 0.240 absolute, 26.1% relative · SPL drop 0.134 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.090 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.014 absolute**
- **R3: success drop 0.200 absolute, 21.7% relative · SPL drop 0.080 absolute**
- **L3: success drop 0.280 absolute, 30.4% relative · SPL drop 0.170 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
