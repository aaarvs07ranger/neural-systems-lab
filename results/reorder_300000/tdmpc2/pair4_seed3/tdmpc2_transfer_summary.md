# TDMPC2 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.811 |                19.880 |              13.219 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.756 |                26.000 |              12.591 |         25 |              0.040 |              0.040 |          0.055 |          0.067 |
| F_lightsky           |          0.800 | 0.566 |                70.120 |              10.212 |         25 |              0.200 |              0.200 |          0.244 |          0.301 |
| F_objall             |          0.960 | 0.707 |                36.600 |              12.427 |         25 |              0.040 |              0.040 |          0.103 |          0.127 |
| F_mat                |          0.920 | 0.623 |                54.280 |              11.769 |         25 |              0.080 |              0.080 |          0.188 |          0.232 |
| R2                   |          0.760 | 0.528 |                78.720 |               9.800 |         25 |              0.240 |              0.240 |          0.283 |          0.349 |
| R3                   |          0.680 | 0.463 |               101.360 |               8.215 |         25 |              0.320 |              0.320 |          0.348 |          0.429 |
| B_L3 (+ distractors) |          0.480 | 0.227 |               145.600 |               4.935 |         25 |              0.520 |              0.520 |          0.583 |          0.719 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.055 absolute**
- **F_lightsky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.244 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.103 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.188 absolute**
- **R2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.283 absolute**
- **R3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.348 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.583 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
