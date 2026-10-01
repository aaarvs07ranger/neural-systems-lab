# PPO_JEPA zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.800 | 0.616 |                53.600 |               9.577 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.760 | 0.588 |                60.240 |               8.942 |         25 |              0.040 |              0.050 |          0.027 |          0.044 |
| F_lightsky           |          0.880 | 0.666 |                41.760 |              10.743 |         25 |             -0.080 |             -0.100 |         -0.050 |         -0.082 |
| F_objall             |          0.680 | 0.493 |                75.720 |               7.821 |         25 |              0.120 |              0.150 |          0.122 |          0.199 |
| F_mat                |          0.360 | 0.261 |               135.760 |               3.220 |         25 |              0.440 |              0.550 |          0.354 |          0.576 |
| R2                   |          0.840 | 0.641 |                47.600 |              10.049 |         25 |             -0.040 |             -0.050 |         -0.025 |         -0.040 |
| R3                   |          0.720 | 0.553 |                67.840 |               8.323 |         25 |              0.080 |              0.100 |          0.063 |          0.102 |
| B_L3 (+ distractors) |          0.040 | 0.026 |               193.000 |              -1.158 |         25 |              0.760 |              0.950 |          0.590 |          0.958 |

- **F_clut: success drop 0.040 absolute, 5.0% relative · SPL drop 0.027 absolute**
- **F_lightsky: success drop -0.080 absolute, -10.0% relative · SPL drop -0.050 absolute**
- **F_objall: success drop 0.120 absolute, 15.0% relative · SPL drop 0.122 absolute**
- **F_mat: success drop 0.440 absolute, 55.0% relative · SPL drop 0.354 absolute**
- **R2: success drop -0.040 absolute, -5.0% relative · SPL drop -0.025 absolute**
- **R3: success drop 0.080 absolute, 10.0% relative · SPL drop 0.063 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.590 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
