# DREAMERV3 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.695 |                27.280 |              12.760 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.691 |                27.760 |              12.768 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| F_lightsky           |          1.000 | 0.707 |                29.600 |              12.681 |         25 |              0.000 |              0.000 |         -0.012 |         -0.018 |
| F_objall             |          1.000 | 0.668 |                36.960 |              12.614 |         25 |              0.000 |              0.000 |          0.027 |          0.039 |
| F_mat                |          0.160 | 0.160 |               179.920 |               0.188 |         25 |              0.840 |              0.840 |          0.535 |          0.770 |
| R2                   |          1.000 | 0.688 |                32.240 |              12.651 |         25 |              0.000 |              0.000 |          0.007 |          0.010 |
| R3                   |          1.000 | 0.695 |                41.360 |              12.494 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L3 (+ distractors) |          0.120 | 0.089 |               182.600 |              -1.133 |         25 |              0.880 |              0.880 |          0.606 |          0.872 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.012 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.027 absolute**
- **F_mat: success drop 0.840 absolute, 84.0% relative · SPL drop 0.535 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.606 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
