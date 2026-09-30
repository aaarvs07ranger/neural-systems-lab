# PPO_JEPA zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.646 |                47.360 |              10.625 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.669 |                40.440 |              11.250 |         25 |             -0.040 |             -0.048 |         -0.023 |         -0.036 |
| F_lightsky           |          0.840 | 0.641 |                47.360 |              10.517 |         25 |              0.000 |              0.000 |          0.005 |          0.008 |
| F_objall             |          0.880 | 0.669 |                41.120 |              11.385 |         25 |             -0.040 |             -0.048 |         -0.022 |         -0.034 |
| F_mat                |          0.000 | 0.000 |               200.000 |              -1.629 |         25 |              0.840 |              1.000 |          0.646 |          1.000 |
| R2                   |          0.880 | 0.674 |                40.640 |              11.210 |         25 |             -0.040 |             -0.048 |         -0.027 |         -0.043 |
| R3                   |          0.800 | 0.592 |                55.240 |              10.103 |         25 |              0.040 |              0.048 |          0.054 |          0.084 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.125 |         25 |              0.840 |              1.000 |          0.646 |          1.000 |

- **F_clut: success drop -0.040 absolute, -4.8% relative · SPL drop -0.023 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_objall: success drop -0.040 absolute, -4.8% relative · SPL drop -0.022 absolute**
- **F_mat: success drop 0.840 absolute, 100.0% relative · SPL drop 0.646 absolute**
- **R2: success drop -0.040 absolute, -4.8% relative · SPL drop -0.027 absolute**
- **R3: success drop 0.040 absolute, 4.8% relative · SPL drop 0.054 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.646 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
