# TDMPC2_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.786 |                18.200 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.785 |                17.800 |              10.964 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_lightsky           |          0.960 | 0.783 |                24.320 |              10.901 |         25 |              0.000 |              0.000 |          0.003 |          0.003 |
| F_objall             |          0.960 | 0.765 |                22.520 |              11.066 |         25 |              0.000 |              0.000 |          0.021 |          0.027 |
| F_mat                |          0.920 | 0.748 |                27.920 |              10.414 |         25 |              0.040 |              0.042 |          0.038 |          0.048 |
| R2                   |          0.960 | 0.780 |                18.280 |              10.963 |         25 |              0.000 |              0.000 |          0.006 |          0.007 |
| R3                   |          0.960 | 0.755 |                24.800 |              11.046 |         25 |              0.000 |              0.000 |          0.031 |          0.039 |
| B_L3 (+ distractors) |          0.920 | 0.707 |                47.880 |              10.358 |         25 |              0.040 |              0.042 |          0.079 |          0.101 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.038 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.031 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.079 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
