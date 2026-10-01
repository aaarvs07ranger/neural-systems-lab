# PPO_AUG zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.660 |                30.720 |               9.398 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.663 |                23.560 |               9.848 |         25 |             -0.040 |             -0.045 |         -0.003 |         -0.004 |
| F_lightsky           |          0.920 | 0.700 |                23.000 |               9.873 |         25 |             -0.040 |             -0.045 |         -0.040 |         -0.061 |
| F_objall             |          0.720 | 0.508 |                61.880 |               7.289 |         25 |              0.160 |              0.182 |          0.152 |          0.231 |
| F_mat                |          0.720 | 0.526 |                66.400 |               7.164 |         25 |              0.160 |              0.182 |          0.134 |          0.203 |
| R2                   |          0.920 | 0.657 |                23.840 |               9.844 |         25 |             -0.040 |             -0.045 |          0.003 |          0.005 |
| R3                   |          0.280 | 0.280 |               144.880 |               1.780 |         25 |              0.600 |              0.682 |          0.380 |          0.576 |
| B_L3 (+ distractors) |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.680 |              0.773 |          0.460 |          0.697 |

- **F_clut: success drop -0.040 absolute, -4.5% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.5% relative · SPL drop -0.040 absolute**
- **F_objall: success drop 0.160 absolute, 18.2% relative · SPL drop 0.152 absolute**
- **F_mat: success drop 0.160 absolute, 18.2% relative · SPL drop 0.134 absolute**
- **R2: success drop -0.040 absolute, -4.5% relative · SPL drop 0.003 absolute**
- **R3: success drop 0.600 absolute, 68.2% relative · SPL drop 0.380 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.460 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
