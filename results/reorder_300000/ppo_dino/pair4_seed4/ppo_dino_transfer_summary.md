# PPO_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.716 |                26.720 |              12.577 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.701 |                34.000 |              12.072 |         25 |              0.040 |              0.042 |          0.016 |          0.022 |
| F_lightsky           |          0.880 | 0.674 |                42.040 |              11.591 |         25 |              0.080 |              0.083 |          0.043 |          0.060 |
| F_objall             |          0.840 | 0.641 |                48.200 |              10.869 |         25 |              0.120 |              0.125 |          0.076 |          0.106 |
| F_mat                |          0.880 | 0.648 |                43.120 |              11.585 |         25 |              0.080 |              0.083 |          0.068 |          0.095 |
| R2                   |          0.800 | 0.623 |                56.960 |              10.600 |         25 |              0.160 |              0.167 |          0.094 |          0.131 |
| R3                   |          0.800 | 0.617 |                55.240 |              10.340 |         25 |              0.160 |              0.167 |          0.100 |          0.139 |
| B_L3 (+ distractors) |          0.880 | 0.638 |                42.560 |              11.347 |         25 |              0.080 |              0.083 |          0.079 |          0.110 |

- **F_clut: success drop 0.040 absolute, 4.2% relative · SPL drop 0.016 absolute**
- **F_lightsky: success drop 0.080 absolute, 8.3% relative · SPL drop 0.043 absolute**
- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.076 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.068 absolute**
- **R2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.094 absolute**
- **R3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.100 absolute**
- **L3: success drop 0.080 absolute, 8.3% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
