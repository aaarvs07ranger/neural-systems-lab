# PPO_JEPA zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.597 |                55.080 |               9.748 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.800 | 0.598 |                55.040 |               9.750 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_lightsky           |          0.760 | 0.566 |                61.720 |               9.121 |         25 |              0.040 |              0.050 |          0.031 |          0.052 |
| F_objall             |          0.640 | 0.464 |                83.040 |               7.385 |         25 |              0.160 |              0.200 |          0.133 |          0.223 |
| F_mat                |          0.040 | 0.040 |               192.160 |              -1.068 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |
| R2                   |          0.760 | 0.575 |                62.440 |               9.159 |         25 |              0.040 |              0.050 |          0.022 |          0.037 |
| R3                   |          0.680 | 0.514 |                75.040 |               7.729 |         25 |              0.120 |              0.150 |          0.083 |          0.139 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.200 |              -1.139 |         25 |              0.760 |              0.950 |          0.557 |          0.933 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.040 absolute, 5.0% relative · SPL drop 0.031 absolute**
- **F_objall: success drop 0.160 absolute, 20.0% relative · SPL drop 0.133 absolute**
- **F_mat: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**
- **R2: success drop 0.040 absolute, 5.0% relative · SPL drop 0.022 absolute**
- **R3: success drop 0.120 absolute, 15.0% relative · SPL drop 0.083 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.557 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
