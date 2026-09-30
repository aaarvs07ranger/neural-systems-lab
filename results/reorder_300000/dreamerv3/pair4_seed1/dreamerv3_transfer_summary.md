# DREAMERV3 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.598 |                24.600 |              13.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.597 |                24.520 |              13.921 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          1.000 | 0.599 |                25.160 |              13.898 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_objall             |          1.000 | 0.706 |                22.400 |              13.601 |         25 |              0.000 |              0.000 |         -0.107 |         -0.179 |
| F_mat                |          1.000 | 0.546 |                28.760 |              13.897 |         25 |              0.000 |              0.000 |          0.052 |          0.087 |
| R2                   |          1.000 | 0.602 |                25.080 |              13.897 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| R3                   |          0.960 | 0.630 |                30.120 |              13.023 |         25 |              0.040 |              0.040 |         -0.031 |         -0.052 |
| B_L3 (+ distractors) |          0.960 | 0.613 |                35.960 |              12.906 |         25 |              0.040 |              0.040 |         -0.015 |         -0.025 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.107 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.052 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.031 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop -0.015 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
