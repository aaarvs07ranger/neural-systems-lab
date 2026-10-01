# DREAMERV3 zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.120 | 0.120 |               178.880 |               0.014 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.120 | 0.083 |               177.520 |               0.022 |         25 |              0.000 |              0.000 |          0.037 |          0.306 |
| F_lightsky           |          0.400 | 0.255 |               130.840 |               3.347 |         25 |             -0.280 |             -2.333 |         -0.135 |         -1.124 |
| F_objall             |          0.200 | 0.200 |               170.080 |               0.914 |         25 |             -0.080 |             -0.667 |         -0.080 |         -0.667 |
| F_mat                |          0.760 | 0.549 |                81.080 |               7.478 |         25 |             -0.640 |             -5.333 |         -0.429 |         -3.573 |
| R2                   |          0.360 | 0.251 |               142.680 |               2.829 |         25 |             -0.240 |             -2.000 |         -0.131 |         -1.094 |
| R3                   |          0.520 | 0.375 |               118.520 |               4.672 |         25 |             -0.400 |             -3.333 |         -0.255 |         -2.124 |
| B_L3 (+ distractors) |          0.760 | 0.592 |                86.480 |               7.411 |         25 |             -0.640 |             -5.333 |         -0.472 |         -3.937 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.037 absolute**
- **F_lightsky: success drop -0.280 absolute, -233.3% relative · SPL drop -0.135 absolute**
- **F_objall: success drop -0.080 absolute, -66.7% relative · SPL drop -0.080 absolute**
- **F_mat: success drop -0.640 absolute, -533.3% relative · SPL drop -0.429 absolute**
- **R2: success drop -0.240 absolute, -200.0% relative · SPL drop -0.131 absolute**
- **R3: success drop -0.400 absolute, -333.3% relative · SPL drop -0.255 absolute**
- **L3: success drop -0.640 absolute, -533.3% relative · SPL drop -0.472 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
