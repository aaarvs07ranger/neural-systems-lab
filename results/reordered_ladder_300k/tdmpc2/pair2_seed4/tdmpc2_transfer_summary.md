# TDMPC2 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.776 |                10.960 |              10.698 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 9.200 |              10.692 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_lightsky           |          1.000 | 0.769 |                36.520 |              10.414 |         25 |              0.000 |              0.000 |          0.006 |          0.008 |
| F_objall             |          1.000 | 0.780 |                12.200 |              10.650 |         25 |              0.000 |              0.000 |         -0.005 |         -0.006 |
| F_mat                |          1.000 | 0.778 |                25.920 |              10.520 |         25 |              0.000 |              0.000 |         -0.002 |         -0.003 |
| R2                   |          0.960 | 0.731 |                38.640 |               9.966 |         25 |              0.040 |              0.040 |          0.045 |          0.058 |
| R3                   |          0.920 | 0.693 |                38.960 |               9.582 |         25 |              0.080 |              0.080 |          0.082 |          0.106 |
| B_L3 (+ distractors) |          1.000 | 0.757 |                45.440 |              10.312 |         25 |              0.000 |              0.000 |          0.019 |          0.024 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.006 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **R2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.045 absolute**
- **R3: success drop 0.080 absolute, 8.0% relative · SPL drop 0.082 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.019 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
