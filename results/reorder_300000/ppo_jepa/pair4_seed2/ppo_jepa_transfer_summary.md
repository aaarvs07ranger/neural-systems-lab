# PPO_JEPA zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.840 | 0.642 |                48.880 |              10.891 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.677 |                34.600 |              12.026 |         25 |             -0.080 |             -0.095 |         -0.035 |         -0.055 |
| F_lightsky           |          0.880 | 0.687 |                41.080 |              11.419 |         25 |             -0.040 |             -0.048 |         -0.045 |         -0.070 |
| F_objall             |          0.800 | 0.583 |                56.080 |              10.331 |         25 |              0.040 |              0.048 |          0.059 |          0.093 |
| F_mat                |          0.520 | 0.335 |               105.560 |               6.146 |         25 |              0.320 |              0.381 |          0.307 |          0.478 |
| R2                   |          0.920 | 0.712 |                33.560 |              11.921 |         25 |             -0.080 |             -0.095 |         -0.070 |         -0.109 |
| R3                   |          0.880 | 0.663 |                40.560 |              11.177 |         25 |             -0.040 |             -0.048 |         -0.021 |         -0.032 |
| B_L3 (+ distractors) |          0.640 | 0.466 |                83.720 |               7.375 |         25 |              0.200 |              0.238 |          0.176 |          0.275 |

- **F_clut: success drop -0.080 absolute, -9.5% relative · SPL drop -0.035 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.8% relative · SPL drop -0.045 absolute**
- **F_objall: success drop 0.040 absolute, 4.8% relative · SPL drop 0.059 absolute**
- **F_mat: success drop 0.320 absolute, 38.1% relative · SPL drop 0.307 absolute**
- **R2: success drop -0.080 absolute, -9.5% relative · SPL drop -0.070 absolute**
- **R3: success drop -0.040 absolute, -4.8% relative · SPL drop -0.021 absolute**
- **L3: success drop 0.200 absolute, 23.8% relative · SPL drop 0.176 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
