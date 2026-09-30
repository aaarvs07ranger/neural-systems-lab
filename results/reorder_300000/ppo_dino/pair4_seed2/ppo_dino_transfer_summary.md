# PPO_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.766 |                20.320 |              13.234 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.739 |                26.440 |              12.593 |         25 |              0.040 |              0.040 |          0.027 |          0.035 |
| F_lightsky           |          0.960 | 0.729 |                26.880 |              12.600 |         25 |              0.040 |              0.040 |          0.036 |          0.047 |
| F_objall             |          0.960 | 0.743 |                27.520 |              12.704 |         25 |              0.040 |              0.040 |          0.023 |          0.030 |
| F_mat                |          0.800 | 0.559 |                55.760 |              10.505 |         25 |              0.200 |              0.200 |          0.207 |          0.270 |
| R2                   |          0.960 | 0.732 |                26.760 |              12.597 |         25 |              0.040 |              0.040 |          0.034 |          0.044 |
| R3                   |          0.960 | 0.751 |                27.480 |              12.710 |         25 |              0.040 |              0.040 |          0.015 |          0.019 |
| B_L3 (+ distractors) |          0.880 | 0.620 |                41.960 |              11.330 |         25 |              0.120 |              0.120 |          0.146 |          0.191 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.027 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.036 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.023 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.207 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.034 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.015 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.146 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
