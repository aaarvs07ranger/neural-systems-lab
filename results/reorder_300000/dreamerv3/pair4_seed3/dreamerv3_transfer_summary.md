# DREAMERV3 zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.040 | 0.006 |               192.720 |               2.265 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.040 | 0.006 |               192.680 |               2.293 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.520 | 0.220 |               137.640 |               7.524 |         25 |             -0.480 |            -12.000 |         -0.214 |        -37.526 |
| F_objall             |          0.400 | 0.235 |               133.640 |               6.293 |         25 |             -0.360 |             -9.000 |         -0.229 |        -40.150 |
| F_mat                |          0.280 | 0.113 |               169.400 |               4.836 |         25 |             -0.240 |             -6.000 |         -0.107 |        -18.709 |
| R2                   |          0.600 | 0.227 |               128.920 |               8.462 |         25 |             -0.560 |            -14.000 |         -0.221 |        -38.759 |
| R3                   |          0.920 | 0.539 |                68.840 |              12.051 |         25 |             -0.880 |            -22.000 |         -0.533 |        -93.282 |
| B_L3 (+ distractors) |          1.000 | 0.494 |                65.520 |              12.839 |         25 |             -0.960 |            -24.000 |         -0.488 |        -85.484 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop -0.480 absolute, -1200.0% relative · SPL drop -0.214 absolute**
- **F_objall: success drop -0.360 absolute, -900.0% relative · SPL drop -0.229 absolute**
- **F_mat: success drop -0.240 absolute, -600.0% relative · SPL drop -0.107 absolute**
- **R2: success drop -0.560 absolute, -1400.0% relative · SPL drop -0.221 absolute**
- **R3: success drop -0.880 absolute, -2200.0% relative · SPL drop -0.533 absolute**
- **L3: success drop -0.960 absolute, -2400.0% relative · SPL drop -0.488 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
