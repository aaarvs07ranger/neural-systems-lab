# TDMPC2 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.776 |                12.920 |              10.688 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.777 |                12.840 |              10.655 |         25 |              0.000 |              0.000 |         -0.001 |         -0.001 |
| F_lightsky           |          0.800 | 0.578 |                56.920 |               8.193 |         25 |              0.200 |              0.200 |          0.199 |          0.256 |
| F_objall             |          1.000 | 0.773 |                14.320 |              10.647 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| F_mat                |          1.000 | 0.771 |                24.080 |              10.511 |         25 |              0.000 |              0.000 |          0.006 |          0.007 |
| R2                   |          0.840 | 0.646 |                51.360 |               8.622 |         25 |              0.160 |              0.160 |          0.131 |          0.168 |
| R3                   |          0.880 | 0.657 |                48.360 |               9.068 |         25 |              0.120 |              0.120 |          0.119 |          0.153 |
| B_L3 (+ distractors) |          0.960 | 0.731 |                61.480 |               9.738 |         25 |              0.040 |              0.040 |          0.045 |          0.058 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.001 absolute**
- **F_lightsky: success drop 0.200 absolute, 20.0% relative · SPL drop 0.199 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **R2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.131 absolute**
- **R3: success drop 0.120 absolute, 12.0% relative · SPL drop 0.119 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.045 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
