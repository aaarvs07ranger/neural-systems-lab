# PPO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.742 |                25.160 |              10.488 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.705 |                32.400 |               9.898 |         25 |              0.040 |              0.043 |          0.037 |          0.050 |
| F_lightsky           |          0.560 | 0.495 |                93.040 |               5.630 |         25 |              0.360 |              0.391 |          0.247 |          0.333 |
| F_objall             |          0.040 | 0.040 |               192.080 |              -1.148 |         25 |              0.880 |              0.957 |          0.702 |          0.946 |
| F_mat                |          0.720 | 0.589 |                63.400 |               7.692 |         25 |              0.200 |              0.217 |          0.153 |          0.206 |
| R2                   |          0.560 | 0.495 |                93.040 |               5.630 |         25 |              0.360 |              0.391 |          0.247 |          0.333 |
| R3                   |          0.040 | 0.040 |               192.080 |              -1.280 |         25 |              0.880 |              0.957 |          0.702 |          0.946 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.615 |         25 |              0.920 |              1.000 |          0.742 |          1.000 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.037 absolute**
- **F_lightsky: success drop 0.360 absolute, 39.1% relative · SPL drop 0.247 absolute**
- **F_objall: success drop 0.880 absolute, 95.7% relative · SPL drop 0.702 absolute**
- **F_mat: success drop 0.200 absolute, 21.7% relative · SPL drop 0.153 absolute**
- **R2: success drop 0.360 absolute, 39.1% relative · SPL drop 0.247 absolute**
- **R3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.702 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.742 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
