# DREAMERV3 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.680 | 0.344 |               102.120 |               9.687 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.640 | 0.329 |               103.560 |               9.087 |         25 |              0.040 |              0.059 |          0.015 |          0.043 |
| F_lightsky           |          0.720 | 0.400 |                85.800 |              10.137 |         25 |             -0.040 |             -0.059 |         -0.056 |         -0.163 |
| F_objall             |          0.800 | 0.430 |                77.560 |              10.888 |         25 |             -0.120 |             -0.176 |         -0.086 |         -0.250 |
| F_mat                |          0.400 | 0.159 |               148.920 |               3.806 |         25 |              0.280 |              0.412 |          0.185 |          0.539 |
| R2                   |          0.760 | 0.428 |                85.920 |              10.425 |         25 |             -0.080 |             -0.118 |         -0.084 |         -0.244 |
| R3                   |          0.640 | 0.326 |               106.240 |               8.249 |         25 |              0.040 |              0.059 |          0.018 |          0.052 |
| B_L3 (+ distractors) |          0.520 | 0.202 |               146.920 |               5.864 |         25 |              0.160 |              0.235 |          0.142 |          0.413 |

- **F_clut: success drop 0.040 absolute, 5.9% relative · SPL drop 0.015 absolute**
- **F_lightsky: success drop -0.040 absolute, -5.9% relative · SPL drop -0.056 absolute**
- **F_objall: success drop -0.120 absolute, -17.6% relative · SPL drop -0.086 absolute**
- **F_mat: success drop 0.280 absolute, 41.2% relative · SPL drop 0.185 absolute**
- **R2: success drop -0.080 absolute, -11.8% relative · SPL drop -0.084 absolute**
- **R3: success drop 0.040 absolute, 5.9% relative · SPL drop 0.018 absolute**
- **L3: success drop 0.160 absolute, 23.5% relative · SPL drop 0.142 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
