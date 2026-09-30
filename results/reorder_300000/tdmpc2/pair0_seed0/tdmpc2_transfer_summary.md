# TDMPC2 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.822 |                12.600 |              11.563 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.818 |                18.040 |              11.543 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_lightsky           |          0.840 | 0.531 |                83.440 |               8.935 |         25 |              0.160 |              0.160 |          0.291 |          0.354 |
| F_objall             |          1.000 | 0.779 |                26.960 |              11.433 |         25 |              0.000 |              0.000 |          0.043 |          0.052 |
| F_mat                |          0.840 | 0.620 |                67.240 |               9.157 |         25 |              0.160 |              0.160 |          0.201 |          0.245 |
| R2                   |          0.920 | 0.566 |                62.840 |              10.080 |         25 |              0.080 |              0.080 |          0.256 |          0.312 |
| R3                   |          0.760 | 0.495 |                91.640 |               7.954 |         25 |              0.240 |              0.240 |          0.327 |          0.398 |
| B_L3 (+ distractors) |          0.640 | 0.452 |               108.840 |               6.396 |         25 |              0.360 |              0.360 |          0.370 |          0.450 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_lightsky: success drop 0.160 absolute, 16.0% relative · SPL drop 0.291 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.043 absolute**
- **F_mat: success drop 0.160 absolute, 16.0% relative · SPL drop 0.201 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.256 absolute**
- **R3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.327 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.370 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
