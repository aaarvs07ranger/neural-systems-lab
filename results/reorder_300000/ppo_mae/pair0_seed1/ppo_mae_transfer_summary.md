# PPO_MAE zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.814 |                13.240 |              11.612 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.814 |                13.240 |              11.612 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.781 |                20.120 |              10.990 |         25 |              0.040 |              0.040 |          0.033 |          0.041 |
| F_objall             |          0.960 | 0.751 |                27.040 |              11.006 |         25 |              0.040 |              0.040 |          0.063 |          0.078 |
| F_mat                |          0.920 | 0.758 |                28.360 |              10.412 |         25 |              0.080 |              0.080 |          0.056 |          0.069 |
| R2                   |          0.960 | 0.781 |                20.120 |              10.990 |         25 |              0.040 |              0.040 |          0.033 |          0.041 |
| R3                   |          0.720 | 0.618 |                66.520 |               8.010 |         25 |              0.280 |              0.280 |          0.197 |          0.241 |
| B_L3 (+ distractors) |          0.480 | 0.406 |               109.240 |               4.876 |         25 |              0.520 |              0.520 |          0.409 |          0.502 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.063 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.056 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **R3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.197 absolute**
- **L3: success drop 0.520 absolute, 52.0% relative · SPL drop 0.409 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
