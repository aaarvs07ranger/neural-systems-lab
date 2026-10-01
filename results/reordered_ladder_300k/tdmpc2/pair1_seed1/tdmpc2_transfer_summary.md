# TDMPC2 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.713 |                 8.560 |              10.855 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.717 |                 9.160 |              10.842 |         25 |              0.000 |              0.000 |         -0.003 |         -0.005 |
| F_lightsky           |          1.000 | 0.713 |                11.640 |              10.836 |         25 |              0.000 |              0.000 |          0.000 |          0.001 |
| F_objall             |          1.000 | 0.711 |                 8.480 |              10.878 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_mat                |          0.560 | 0.394 |               123.120 |               4.513 |         25 |              0.440 |              0.440 |          0.320 |          0.448 |
| R2                   |          1.000 | 0.709 |                 8.920 |              10.860 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| R3                   |          1.000 | 0.709 |                 9.560 |              10.846 |         25 |              0.000 |              0.000 |          0.004 |          0.006 |
| B_L3 (+ distractors) |          0.640 | 0.518 |                97.240 |               5.756 |         25 |              0.360 |              0.360 |          0.195 |          0.273 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_mat: success drop 0.440 absolute, 44.0% relative · SPL drop 0.320 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **L3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.195 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
