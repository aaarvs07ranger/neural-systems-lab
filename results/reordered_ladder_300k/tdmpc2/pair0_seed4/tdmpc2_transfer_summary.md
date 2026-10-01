# TDMPC2 zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.778 |                19.840 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.785 |                19.040 |              10.965 |         25 |              0.000 |              0.000 |         -0.007 |         -0.009 |
| F_lightsky           |          0.920 | 0.667 |                44.040 |              10.363 |         25 |              0.040 |              0.042 |          0.111 |          0.143 |
| F_objall             |          0.880 | 0.716 |                39.440 |               9.886 |         25 |              0.080 |              0.083 |          0.062 |          0.080 |
| F_mat                |          0.800 | 0.618 |                79.760 |               8.434 |         25 |              0.160 |              0.167 |          0.161 |          0.206 |
| R2                   |          0.960 | 0.682 |                44.600 |              10.728 |         25 |              0.000 |              0.000 |          0.096 |          0.124 |
| R3                   |          0.760 | 0.519 |                94.040 |               7.978 |         25 |              0.200 |              0.208 |          0.259 |          0.333 |
| B_L3 (+ distractors) |          0.600 | 0.426 |               112.120 |               5.801 |         25 |              0.360 |              0.375 |          0.352 |          0.452 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.007 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.111 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.062 absolute**
- **F_mat: success drop 0.160 absolute, 16.7% relative · SPL drop 0.161 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.096 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.259 absolute**
- **L3: success drop 0.360 absolute, 37.5% relative · SPL drop 0.352 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
