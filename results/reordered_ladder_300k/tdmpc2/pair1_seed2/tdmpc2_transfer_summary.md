# TDMPC2 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.716 |                 9.440 |              10.846 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.708 |                 9.680 |              10.873 |         25 |              0.000 |              0.000 |          0.009 |          0.012 |
| F_lightsky           |          1.000 | 0.708 |                11.400 |              10.835 |         25 |              0.000 |              0.000 |          0.008 |          0.011 |
| F_objall             |          1.000 | 0.708 |                11.000 |              10.858 |         25 |              0.000 |              0.000 |          0.008 |          0.012 |
| F_mat                |          0.920 | 0.599 |                58.240 |               9.430 |         25 |              0.080 |              0.080 |          0.117 |          0.164 |
| R2                   |          1.000 | 0.716 |                 9.720 |              10.857 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| R3                   |          1.000 | 0.709 |                15.480 |              10.787 |         25 |              0.000 |              0.000 |          0.008 |          0.010 |
| B_L3 (+ distractors) |          0.800 | 0.590 |                79.280 |               7.908 |         25 |              0.200 |              0.200 |          0.126 |          0.176 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.009 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.117 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.008 absolute**
- **L3: success drop 0.200 absolute, 20.0% relative · SPL drop 0.126 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
