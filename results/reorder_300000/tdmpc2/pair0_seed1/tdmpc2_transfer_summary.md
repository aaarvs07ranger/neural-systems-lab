# TDMPC2 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.813 |                12.760 |              11.580 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.813 |                15.080 |              11.574 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_lightsky           |          0.960 | 0.680 |                34.640 |              10.886 |         25 |              0.040 |              0.040 |          0.134 |          0.164 |
| F_objall             |          0.920 | 0.742 |                35.720 |              10.470 |         25 |              0.080 |              0.080 |          0.072 |          0.088 |
| F_mat                |          0.960 | 0.722 |                44.040 |              10.723 |         25 |              0.040 |              0.040 |          0.092 |          0.113 |
| R2                   |          0.920 | 0.596 |                54.920 |              10.306 |         25 |              0.080 |              0.080 |          0.217 |          0.267 |
| R3                   |          0.800 | 0.540 |                76.000 |               8.683 |         25 |              0.200 |              0.200 |          0.274 |          0.336 |
| B_L3 (+ distractors) |          0.440 | 0.324 |               141.440 |               3.819 |         25 |              0.560 |              0.560 |          0.490 |          0.602 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.134 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.072 absolute**
- **F_mat: success drop 0.040 absolute, 4.0% relative · SPL drop 0.092 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.217 absolute**
- **R3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.274 absolute**
- **L3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.490 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
