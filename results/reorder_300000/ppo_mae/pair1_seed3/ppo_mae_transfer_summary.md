# PPO_MAE zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.690 |                24.360 |               9.872 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.690 |                24.840 |               9.860 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.690 |                24.440 |               9.865 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_objall             |          0.920 | 0.673 |                25.080 |               9.811 |         25 |              0.000 |              0.000 |          0.017 |          0.024 |
| F_mat                |          0.680 | 0.580 |                71.400 |               6.732 |         25 |              0.240 |              0.261 |          0.110 |          0.159 |
| R2                   |          0.920 | 0.692 |                24.400 |               9.876 |         25 |              0.000 |              0.000 |         -0.003 |         -0.004 |
| R3                   |          0.720 | 0.601 |                63.600 |               7.278 |         25 |              0.200 |              0.217 |          0.088 |          0.128 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.490 |          0.710 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.017 absolute**
- **F_mat: success drop 0.240 absolute, 26.1% relative · SPL drop 0.110 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **R3: success drop 0.200 absolute, 21.7% relative · SPL drop 0.088 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.490 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
