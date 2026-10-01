# TDMPC2 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.763 |                27.600 |              12.505 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.725 |                32.600 |              12.048 |         25 |              0.040 |              0.040 |          0.038 |          0.050 |
| F_lightsky           |          0.960 | 0.702 |                68.600 |              11.668 |         25 |              0.040 |              0.040 |          0.062 |          0.081 |
| F_objall             |          0.920 | 0.690 |                58.680 |              11.150 |         25 |              0.080 |              0.080 |          0.073 |          0.096 |
| F_mat                |          0.280 | 0.266 |               167.840 |               1.534 |         25 |              0.720 |              0.720 |          0.498 |          0.652 |
| R2                   |          0.800 | 0.588 |                85.160 |               9.694 |         25 |              0.200 |              0.200 |          0.176 |          0.230 |
| R3                   |          0.680 | 0.469 |                98.440 |               7.933 |         25 |              0.320 |              0.320 |          0.294 |          0.385 |
| B_L3 (+ distractors) |          0.120 | 0.060 |               187.080 |              -1.013 |         25 |              0.880 |              0.880 |          0.703 |          0.921 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.038 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.062 absolute**
- **F_objall: success drop 0.080 absolute, 8.0% relative · SPL drop 0.073 absolute**
- **F_mat: success drop 0.720 absolute, 72.0% relative · SPL drop 0.498 absolute**
- **R2: success drop 0.200 absolute, 20.0% relative · SPL drop 0.176 absolute**
- **R3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.294 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.703 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
