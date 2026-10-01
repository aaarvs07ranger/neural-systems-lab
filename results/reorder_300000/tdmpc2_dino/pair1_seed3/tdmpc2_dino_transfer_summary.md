# TDMPC2_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.715 |                 9.560 |              10.851 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.716 |                 7.720 |              10.867 |         25 |              0.000 |              0.000 |         -0.001 |         -0.002 |
| F_lightsky           |          1.000 | 0.713 |                 8.600 |              10.876 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_objall             |          1.000 | 0.720 |                 9.040 |              10.826 |         25 |              0.000 |              0.000 |         -0.005 |         -0.007 |
| F_mat                |          0.920 | 0.600 |                41.000 |               9.691 |         25 |              0.080 |              0.080 |          0.114 |          0.160 |
| R2                   |          1.000 | 0.715 |                 8.080 |              10.845 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| R3                   |          0.960 | 0.706 |                15.760 |              10.326 |         25 |              0.040 |              0.040 |          0.008 |          0.012 |
| B_L3 (+ distractors) |          0.960 | 0.646 |                24.680 |              10.279 |         25 |              0.040 |              0.040 |          0.069 |          0.096 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.114 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **R3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.008 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.069 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
