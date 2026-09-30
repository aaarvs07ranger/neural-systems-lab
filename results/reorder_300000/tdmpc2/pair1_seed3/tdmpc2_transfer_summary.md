# TDMPC2 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.713 |                 9.640 |              10.830 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.671 |                23.240 |              10.244 |         25 |              0.040 |              0.040 |          0.042 |          0.059 |
| F_lightsky           |          1.000 | 0.716 |                10.920 |              10.803 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| F_objall             |          1.000 | 0.711 |                10.920 |              10.846 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_mat                |          0.440 | 0.318 |               128.000 |               2.788 |         25 |              0.560 |              0.560 |          0.396 |          0.555 |
| R2                   |          1.000 | 0.716 |                14.120 |              10.808 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| R3                   |          1.000 | 0.712 |                15.920 |              10.804 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L3 (+ distractors) |          0.360 | 0.291 |               140.360 |               2.101 |         25 |              0.640 |              0.640 |          0.423 |          0.593 |

- **F_clut: success drop 0.040 absolute, 4.0% relative · SPL drop 0.042 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_mat: success drop 0.560 absolute, 56.0% relative · SPL drop 0.396 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L3: success drop 0.640 absolute, 64.0% relative · SPL drop 0.423 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
