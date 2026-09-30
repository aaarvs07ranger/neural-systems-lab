# DREAMERV3 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.674 |                54.000 |              11.414 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.720 | 0.547 |                89.760 |               9.011 |         25 |              0.200 |              0.217 |          0.127 |          0.189 |
| F_lightsky           |          0.720 | 0.523 |                92.320 |               8.841 |         25 |              0.200 |              0.217 |          0.151 |          0.224 |
| F_objall             |          1.000 | 0.675 |                53.320 |              12.188 |         25 |             -0.080 |             -0.087 |         -0.000 |         -0.001 |
| F_mat                |          0.320 | 0.258 |               167.160 |               2.581 |         25 |              0.600 |              0.652 |          0.416 |          0.617 |
| R2                   |          0.800 | 0.598 |               103.080 |               9.566 |         25 |              0.120 |              0.130 |          0.076 |          0.113 |
| R3                   |          0.280 | 0.211 |               168.360 |               3.259 |         25 |              0.640 |              0.696 |          0.463 |          0.687 |
| B_L3 (+ distractors) |          0.080 | 0.080 |               184.760 |              -1.428 |         25 |              0.840 |              0.913 |          0.594 |          0.881 |

- **F_clut: success drop 0.200 absolute, 21.7% relative · SPL drop 0.127 absolute**
- **F_lightsky: success drop 0.200 absolute, 21.7% relative · SPL drop 0.151 absolute**
- **F_objall: success drop -0.080 absolute, -8.7% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.600 absolute, 65.2% relative · SPL drop 0.416 absolute**
- **R2: success drop 0.120 absolute, 13.0% relative · SPL drop 0.076 absolute**
- **R3: success drop 0.640 absolute, 69.6% relative · SPL drop 0.463 absolute**
- **L3: success drop 0.840 absolute, 91.3% relative · SPL drop 0.594 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
