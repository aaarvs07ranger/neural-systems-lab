# DREAMERV3 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.658 |                22.280 |              10.764 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.668 |                28.120 |              10.678 |         25 |              0.000 |              0.000 |         -0.010 |         -0.016 |
| F_lightsky           |          1.000 | 0.664 |                25.320 |              10.721 |         25 |              0.000 |              0.000 |         -0.007 |         -0.010 |
| F_objall             |          1.000 | 0.682 |                14.440 |              10.847 |         25 |              0.000 |              0.000 |         -0.024 |         -0.037 |
| F_mat                |          0.720 | 0.499 |                75.440 |               6.942 |         25 |              0.280 |              0.280 |          0.159 |          0.241 |
| R2                   |          1.000 | 0.659 |                30.600 |              10.646 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| R3                   |          1.000 | 0.693 |                12.120 |              10.831 |         25 |              0.000 |              0.000 |         -0.036 |         -0.055 |
| B_L3 (+ distractors) |          0.960 | 0.580 |                54.360 |               9.978 |         25 |              0.040 |              0.040 |          0.077 |          0.117 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.010 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.024 absolute**
- **F_mat: success drop 0.280 absolute, 28.0% relative · SPL drop 0.159 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.036 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.077 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
