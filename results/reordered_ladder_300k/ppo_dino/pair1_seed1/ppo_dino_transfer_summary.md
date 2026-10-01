# PPO_DINO zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.705 |                13.960 |              10.317 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.705 |                14.040 |              10.311 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.663 |                22.000 |               9.836 |         25 |              0.040 |              0.042 |          0.042 |          0.059 |
| F_objall             |          0.920 | 0.665 |                21.840 |               9.828 |         25 |              0.040 |              0.042 |          0.040 |          0.057 |
| F_mat                |          0.880 | 0.610 |                30.280 |               9.388 |         25 |              0.080 |              0.083 |          0.095 |          0.135 |
| R2                   |          1.000 | 0.722 |                 6.720 |              10.870 |         25 |             -0.040 |             -0.042 |         -0.017 |         -0.024 |
| R3                   |          0.960 | 0.680 |                14.680 |              10.394 |         25 |              0.000 |              0.000 |          0.025 |          0.036 |
| B_L3 (+ distractors) |          0.920 | 0.644 |                22.760 |               9.909 |         25 |              0.040 |              0.042 |          0.061 |          0.086 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.042 absolute**
- **F_objall: success drop 0.040 absolute, 4.2% relative · SPL drop 0.040 absolute**
- **F_mat: success drop 0.080 absolute, 8.3% relative · SPL drop 0.095 absolute**
- **R2: success drop -0.040 absolute, -4.2% relative · SPL drop -0.017 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.025 absolute**
- **L3: success drop 0.040 absolute, 4.2% relative · SPL drop 0.061 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
