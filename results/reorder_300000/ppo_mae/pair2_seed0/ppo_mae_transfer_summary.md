# PPO_MAE zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.657 |                30.560 |               9.269 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.657 |                30.560 |               9.269 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.160 | 0.160 |               168.320 |               0.182 |         25 |              0.720 |              0.818 |          0.497 |          0.756 |
| F_objall             |          0.960 | 0.738 |                15.040 |              10.247 |         25 |             -0.080 |             -0.091 |         -0.082 |         -0.124 |
| F_mat                |          0.080 | 0.080 |               184.480 |              -1.036 |         25 |              0.800 |              0.909 |          0.577 |          0.878 |
| R2                   |          0.160 | 0.160 |               168.320 |               0.203 |         25 |              0.720 |              0.818 |          0.497 |          0.756 |
| R3                   |          0.160 | 0.160 |               168.320 |               0.388 |         25 |              0.720 |              0.818 |          0.497 |          0.756 |
| B_L3 (+ distractors) |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.840 |              0.955 |          0.617 |          0.939 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.720 absolute, 81.8% relative · SPL drop 0.497 absolute**
- **F_objall: success drop -0.080 absolute, -9.1% relative · SPL drop -0.082 absolute**
- **F_mat: success drop 0.800 absolute, 90.9% relative · SPL drop 0.577 absolute**
- **R2: success drop 0.720 absolute, 81.8% relative · SPL drop 0.497 absolute**
- **R3: success drop 0.720 absolute, 81.8% relative · SPL drop 0.497 absolute**
- **L3: success drop 0.840 absolute, 95.5% relative · SPL drop 0.617 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
