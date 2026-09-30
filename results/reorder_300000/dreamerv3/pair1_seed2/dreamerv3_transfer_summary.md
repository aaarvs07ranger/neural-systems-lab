# DREAMERV3 zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.360 | 0.280 |               133.120 |               2.950 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.320 | 0.244 |               139.960 |               2.380 |         25 |              0.040 |              0.111 |          0.036 |          0.129 |
| F_lightsky           |          0.280 | 0.204 |               147.560 |               1.976 |         25 |              0.080 |              0.222 |          0.076 |          0.271 |
| F_objall             |          0.400 | 0.324 |               123.120 |               3.464 |         25 |             -0.040 |             -0.111 |         -0.044 |         -0.157 |
| F_mat                |          0.480 | 0.381 |               130.480 |               3.811 |         25 |             -0.120 |             -0.333 |         -0.101 |         -0.360 |
| R2                   |          0.240 | 0.164 |               154.800 |               1.457 |         25 |              0.120 |              0.333 |          0.116 |          0.414 |
| R3                   |          0.480 | 0.336 |               131.520 |               4.207 |         25 |             -0.120 |             -0.333 |         -0.056 |         -0.199 |
| B_L3 (+ distractors) |          0.600 | 0.420 |                99.920 |               5.558 |         25 |             -0.240 |             -0.667 |         -0.140 |         -0.499 |

- **F_clut: success drop 0.040 absolute, 11.1% relative · SPL drop 0.036 absolute**
- **F_lightsky: success drop 0.080 absolute, 22.2% relative · SPL drop 0.076 absolute**
- **F_objall: success drop -0.040 absolute, -11.1% relative · SPL drop -0.044 absolute**
- **F_mat: success drop -0.120 absolute, -33.3% relative · SPL drop -0.101 absolute**
- **R2: success drop 0.120 absolute, 33.3% relative · SPL drop 0.116 absolute**
- **R3: success drop -0.120 absolute, -33.3% relative · SPL drop -0.056 absolute**
- **L3: success drop -0.240 absolute, -66.7% relative · SPL drop -0.140 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
