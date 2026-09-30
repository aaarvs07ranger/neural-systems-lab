# PPO_JEPA zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.770 |                18.280 |              10.960 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.770 |                18.240 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.692 |                33.360 |               9.982 |         25 |              0.080 |              0.083 |          0.079 |          0.102 |
| F_objall             |          0.840 | 0.659 |                42.080 |               9.481 |         25 |              0.120 |              0.125 |          0.111 |          0.145 |
| F_mat                |          0.960 | 0.768 |                18.640 |              11.113 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| R2                   |          0.920 | 0.712 |                26.080 |              10.505 |         25 |              0.040 |              0.042 |          0.059 |          0.076 |
| R3                   |          0.680 | 0.509 |                71.880 |               7.389 |         25 |              0.280 |              0.292 |          0.261 |          0.339 |
| B_L3 (+ distractors) |          0.640 | 0.492 |                79.520 |               6.846 |         25 |              0.320 |              0.333 |          0.278 |          0.361 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.079 absolute**
- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.111 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.059 absolute**
- **R3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.261 absolute**
- **L3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.278 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
