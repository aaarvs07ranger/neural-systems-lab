# TDMPC2 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.794 |                19.800 |              13.296 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.769 |                20.000 |              13.263 |         25 |              0.000 |              0.000 |          0.026 |          0.032 |
| F_lightsky           |          0.960 | 0.716 |                45.200 |              12.439 |         25 |              0.040 |              0.040 |          0.079 |          0.099 |
| F_objall             |          1.000 | 0.732 |                31.200 |              13.076 |         25 |              0.000 |              0.000 |          0.062 |          0.079 |
| F_mat                |          0.920 | 0.652 |                56.440 |              11.761 |         25 |              0.080 |              0.080 |          0.142 |          0.179 |
| R2                   |          0.920 | 0.701 |                40.440 |              12.005 |         25 |              0.080 |              0.080 |          0.093 |          0.117 |
| R3                   |          0.640 | 0.454 |               106.640 |               7.387 |         25 |              0.360 |              0.360 |          0.340 |          0.428 |
| B_L3 (+ distractors) |          0.440 | 0.258 |               138.760 |               4.681 |         25 |              0.560 |              0.560 |          0.537 |          0.676 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.026 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.079 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.062 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.142 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.093 absolute**
- **R3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.340 absolute**
- **L3: success drop 0.560 absolute, 56.0% relative · SPL drop 0.537 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
