# PPO_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.780 |                17.560 |              10.974 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.780 |                17.560 |              10.974 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.791 |                10.680 |              11.606 |         25 |             -0.040 |             -0.042 |         -0.011 |         -0.014 |
| F_objall             |          0.840 | 0.665 |                41.080 |               9.421 |         25 |              0.120 |              0.125 |          0.115 |          0.148 |
| F_mat                |          0.960 | 0.776 |                18.360 |              11.110 |         25 |              0.000 |              0.000 |          0.004 |          0.005 |
| R2                   |          1.000 | 0.791 |                10.680 |              11.606 |         25 |             -0.040 |             -0.042 |         -0.011 |         -0.014 |
| R3                   |          0.760 | 0.606 |                56.240 |               8.373 |         25 |              0.200 |              0.208 |          0.174 |          0.223 |
| B_L3 (+ distractors) |          0.800 | 0.628 |                48.600 |               8.905 |         25 |              0.160 |              0.167 |          0.152 |          0.195 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.2% relative · SPL drop -0.011 absolute**
- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.115 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.004 absolute**
- **R2: success drop -0.040 absolute, -4.2% relative · SPL drop -0.011 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.174 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.152 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
