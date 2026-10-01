# TDMPC2 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.819 |                12.080 |              11.591 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.810 |                12.160 |              11.597 |         25 |              0.000 |              0.000 |          0.009 |          0.012 |
| F_lightsky           |          0.760 | 0.501 |                85.800 |               8.050 |         25 |              0.240 |              0.240 |          0.318 |          0.388 |
| F_objall             |          0.960 | 0.786 |                23.040 |              11.068 |         25 |              0.040 |              0.040 |          0.033 |          0.040 |
| F_mat                |          0.880 | 0.697 |                65.640 |               9.639 |         25 |              0.120 |              0.120 |          0.122 |          0.149 |
| R2                   |          0.960 | 0.682 |                47.440 |              10.796 |         25 |              0.040 |              0.040 |          0.137 |          0.167 |
| R3                   |          0.720 | 0.488 |                92.720 |               7.203 |         25 |              0.280 |              0.280 |          0.331 |          0.404 |
| B_L3 (+ distractors) |          0.560 | 0.466 |               116.120 |               5.300 |         25 |              0.440 |              0.440 |          0.353 |          0.431 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_lightsky: success drop 0.240 absolute, 24.0% relative · SPL drop 0.318 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **F_mat: success drop 0.120 absolute, 12.0% relative · SPL drop 0.122 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.137 absolute**
- **R3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.331 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.353 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
