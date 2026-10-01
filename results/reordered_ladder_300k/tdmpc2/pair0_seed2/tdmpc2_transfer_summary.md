# TDMPC2 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.819 |                12.160 |              11.598 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.813 |                11.960 |              11.601 |         25 |              0.000 |              0.000 |          0.005 |          0.006 |
| F_lightsky           |          0.720 | 0.487 |                89.880 |               7.302 |         25 |              0.280 |              0.280 |          0.332 |          0.405 |
| F_objall             |          0.960 | 0.799 |                20.760 |              11.050 |         25 |              0.040 |              0.040 |          0.019 |          0.023 |
| F_mat                |          0.960 | 0.738 |                35.840 |              10.878 |         25 |              0.040 |              0.040 |          0.081 |          0.098 |
| R2                   |          0.760 | 0.491 |                92.760 |               7.762 |         25 |              0.240 |              0.240 |          0.327 |          0.400 |
| R3                   |          0.560 | 0.410 |               106.800 |               5.116 |         25 |              0.440 |              0.440 |          0.409 |          0.500 |
| B_L3 (+ distractors) |          0.880 | 0.575 |                58.520 |               9.643 |         25 |              0.120 |              0.120 |          0.243 |          0.297 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_lightsky: success drop 0.280 absolute, 28.0% relative · SPL drop 0.332 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.019 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.081 absolute**
- **R2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.327 absolute**
- **R3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.409 absolute**
- **L3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.243 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
