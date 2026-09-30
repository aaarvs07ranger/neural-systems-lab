# TDMPC2 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.716 |                 7.960 |              10.868 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.714 |                 8.280 |              10.850 |         25 |              0.000 |              0.000 |          0.002 |          0.002 |
| F_lightsky           |          1.000 | 0.713 |                 9.440 |              10.835 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_objall             |          1.000 | 0.708 |                 9.440 |              10.855 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |
| F_mat                |          0.920 | 0.643 |                67.440 |               9.372 |         25 |              0.080 |              0.080 |          0.073 |          0.102 |
| R2                   |          1.000 | 0.713 |                 9.760 |              10.839 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| R3                   |          1.000 | 0.704 |                12.680 |              10.824 |         25 |              0.000 |              0.000 |          0.012 |          0.016 |
| B_L3 (+ distractors) |          0.800 | 0.523 |                80.680 |               8.025 |         25 |              0.200 |              0.200 |          0.193 |          0.269 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.073 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.193 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
