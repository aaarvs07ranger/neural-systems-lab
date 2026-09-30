# PPO_JEPA zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.760 | 0.576 |                62.720 |               9.168 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.760 | 0.577 |                62.680 |               9.169 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_lightsky           |          0.760 | 0.565 |                63.840 |               9.359 |         25 |              0.000 |              0.000 |          0.010 |          0.018 |
| F_objall             |          0.680 | 0.506 |                76.560 |               8.121 |         25 |              0.080 |              0.105 |          0.069 |          0.120 |
| F_mat                |          0.080 | 0.065 |               185.320 |               0.306 |         25 |              0.680 |              0.895 |          0.511 |          0.887 |
| R2                   |          0.760 | 0.563 |                63.960 |               9.304 |         25 |              0.000 |              0.000 |          0.012 |          0.021 |
| R3                   |          0.600 | 0.449 |                90.680 |               7.183 |         25 |              0.160 |              0.211 |          0.127 |          0.221 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.200 |              -0.840 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_objall: success drop 0.080 absolute, 10.5% relative · SPL drop 0.069 absolute**
- **F_mat: success drop 0.680 absolute, 89.5% relative · SPL drop 0.511 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **R3: success drop 0.160 absolute, 21.1% relative · SPL drop 0.127 absolute**
- **L3: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
