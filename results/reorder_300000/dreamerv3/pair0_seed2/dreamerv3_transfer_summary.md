# DREAMERV3 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.784 |                13.400 |              11.598 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.776 |                13.600 |              11.589 |         25 |              0.000 |              0.000 |          0.009 |          0.011 |
| F_lightsky           |          0.880 | 0.627 |                47.000 |               9.667 |         25 |              0.120 |              0.120 |          0.158 |          0.201 |
| F_objall             |          1.000 | 0.794 |                16.640 |              11.511 |         25 |              0.000 |              0.000 |         -0.010 |         -0.013 |
| F_mat                |          1.000 | 0.744 |                20.160 |              11.501 |         25 |              0.000 |              0.000 |          0.040 |          0.051 |
| R2                   |          0.920 | 0.625 |                42.160 |              10.221 |         25 |              0.080 |              0.080 |          0.159 |          0.203 |
| R3                   |          0.720 | 0.500 |                75.600 |               7.372 |         25 |              0.280 |              0.280 |          0.284 |          0.362 |
| B_L3 (+ distractors) |          1.000 | 0.651 |                39.840 |              11.272 |         25 |              0.000 |              0.000 |          0.133 |          0.170 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.158 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.010 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.040 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.159 absolute**
- **R3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.284 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.133 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
