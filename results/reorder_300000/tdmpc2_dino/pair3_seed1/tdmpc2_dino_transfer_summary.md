# TDMPC2_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.762 |                21.240 |              12.585 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.764 |                22.920 |              12.562 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_lightsky           |          0.960 | 0.731 |                30.320 |              11.921 |         25 |              0.040 |              0.040 |          0.031 |          0.040 |
| F_objall             |          0.960 | 0.728 |                31.600 |              11.898 |         25 |              0.040 |              0.040 |          0.034 |          0.044 |
| F_mat                |          0.800 | 0.526 |                76.800 |               9.721 |         25 |              0.200 |              0.200 |          0.236 |          0.310 |
| R2                   |          0.960 | 0.735 |                27.640 |              11.949 |         25 |              0.040 |              0.040 |          0.026 |          0.034 |
| R3                   |          0.960 | 0.729 |                32.760 |              11.889 |         25 |              0.040 |              0.040 |          0.033 |          0.043 |
| B_L3 (+ distractors) |          0.600 | 0.413 |               113.280 |               7.142 |         25 |              0.400 |              0.400 |          0.348 |          0.457 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.0% relative · SPL drop 0.031 absolute**
- **F_objall: success drop 0.040 absolute, 4.0% relative · SPL drop 0.034 absolute**
- **F_mat: success drop 0.200 absolute, 20.0% relative · SPL drop 0.236 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.026 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.033 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.348 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
