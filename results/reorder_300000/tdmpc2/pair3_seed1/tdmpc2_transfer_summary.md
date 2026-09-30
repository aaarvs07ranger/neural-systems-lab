# TDMPC2 zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.757 |                23.240 |              12.557 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.758 |                29.480 |              12.499 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_lightsky           |          0.760 | 0.547 |                73.160 |               9.049 |         25 |              0.240 |              0.240 |          0.210 |          0.278 |
| F_objall             |          0.880 | 0.637 |                55.720 |              10.707 |         25 |              0.120 |              0.120 |          0.120 |          0.159 |
| F_mat                |          0.560 | 0.356 |               139.440 |               5.350 |         25 |              0.440 |              0.440 |          0.401 |          0.530 |
| R2                   |          0.720 | 0.521 |                82.160 |               8.418 |         25 |              0.280 |              0.280 |          0.236 |          0.311 |
| R3                   |          0.520 | 0.400 |               126.320 |               5.426 |         25 |              0.480 |              0.480 |          0.357 |          0.471 |
| B_L3 (+ distractors) |          0.240 | 0.209 |               167.560 |               1.284 |         25 |              0.760 |              0.760 |          0.548 |          0.724 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.240 absolute, 24.0% relative · SPL drop 0.210 absolute**
- **F_objall: success drop 0.120 absolute, 12.0% relative · SPL drop 0.120 absolute**
- **F_mat: success drop 0.440 absolute, 44.0% relative · SPL drop 0.401 absolute**
- **R2: success drop 0.280 absolute, 28.0% relative · SPL drop 0.236 absolute**
- **R3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.357 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.548 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
