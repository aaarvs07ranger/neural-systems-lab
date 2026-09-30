# DREAMERV3 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.732 |                18.880 |              11.534 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.771 |                16.760 |              11.542 |         25 |              0.000 |              0.000 |         -0.038 |         -0.052 |
| F_lightsky           |          0.800 | 0.573 |                57.520 |               8.416 |         25 |              0.200 |              0.200 |          0.159 |          0.217 |
| F_objall             |          1.000 | 0.785 |                14.480 |              11.519 |         25 |              0.000 |              0.000 |         -0.052 |         -0.071 |
| F_mat                |          1.000 | 0.674 |                42.880 |              11.260 |         25 |              0.000 |              0.000 |          0.058 |          0.080 |
| R2                   |          0.760 | 0.547 |                64.120 |               7.822 |         25 |              0.240 |              0.240 |          0.186 |          0.253 |
| R3                   |          0.840 | 0.588 |                56.240 |               9.034 |         25 |              0.160 |              0.160 |          0.145 |          0.197 |
| B_L3 (+ distractors) |          0.920 | 0.562 |                58.360 |              10.091 |         25 |              0.080 |              0.080 |          0.170 |          0.233 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.038 absolute**
- **F_lightsky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.159 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.052 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.058 absolute**
- **R2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.186 absolute**
- **R3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.145 absolute**
- **L3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.170 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
