# PPO_AUG zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.619 |                30.760 |               9.311 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.623 |                30.720 |               9.305 |         25 |              0.000 |              0.000 |         -0.004 |         -0.006 |
| F_lightsky           |          0.840 | 0.583 |                38.360 |               8.788 |         25 |              0.040 |              0.045 |          0.036 |          0.058 |
| F_objall             |          0.640 | 0.481 |                76.640 |               6.262 |         25 |              0.240 |              0.273 |          0.139 |          0.224 |
| F_mat                |          0.360 | 0.220 |               130.400 |               2.332 |         25 |              0.520 |              0.591 |          0.399 |          0.645 |
| R2                   |          0.840 | 0.583 |                38.360 |               8.788 |         25 |              0.040 |              0.045 |          0.036 |          0.058 |
| R3                   |          0.400 | 0.288 |               122.680 |               3.293 |         25 |              0.480 |              0.545 |          0.331 |          0.534 |
| B_L3 (+ distractors) |          0.200 | 0.151 |               161.120 |               0.273 |         25 |              0.680 |              0.773 |          0.468 |          0.756 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.5% relative · SPL drop 0.036 absolute**
- **F_objall: success drop 0.240 absolute, 27.3% relative · SPL drop 0.139 absolute**
- **F_mat: success drop 0.520 absolute, 59.1% relative · SPL drop 0.399 absolute**
- **R2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.036 absolute**
- **R3: success drop 0.480 absolute, 54.5% relative · SPL drop 0.331 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.468 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
