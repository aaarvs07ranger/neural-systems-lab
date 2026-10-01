# TDMPC2_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.715 |                 8.240 |              10.870 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.713 |                 7.640 |              10.857 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| F_lightsky           |          1.000 | 0.716 |                 7.720 |              10.845 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_objall             |          1.000 | 0.715 |                 8.960 |              10.881 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_mat                |          0.920 | 0.659 |                24.680 |               9.826 |         25 |              0.080 |              0.080 |          0.056 |          0.078 |
| R2                   |          1.000 | 0.714 |                 8.120 |              10.856 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| R3                   |          1.000 | 0.716 |                 7.800 |              10.881 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| B_L3 (+ distractors) |          0.960 | 0.671 |                18.160 |              10.345 |         25 |              0.040 |              0.040 |          0.044 |          0.061 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.056 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.044 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
