# PPO_JEPA zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.671 |                42.720 |              10.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.671 |                42.720 |              10.918 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.675 |                42.680 |              10.920 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| F_objall             |          0.720 | 0.540 |                73.480 |               8.853 |         25 |              0.160 |              0.182 |          0.131 |          0.195 |
| F_mat                |          0.680 | 0.484 |                78.320 |               7.875 |         25 |              0.200 |              0.227 |          0.187 |          0.278 |
| R2                   |          0.880 | 0.675 |                42.680 |              10.921 |         25 |              0.000 |              0.000 |         -0.004 |         -0.005 |
| R3                   |          0.640 | 0.496 |                83.120 |               7.523 |         25 |              0.240 |              0.273 |          0.175 |          0.261 |
| B_L3 (+ distractors) |          0.360 | 0.245 |               134.160 |               3.974 |         25 |              0.520 |              0.591 |          0.426 |          0.635 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **F_objall: success drop 0.160 absolute, 18.2% relative · SPL drop 0.131 absolute**
- **F_mat: success drop 0.200 absolute, 22.7% relative · SPL drop 0.187 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop -0.004 absolute**
- **R3: success drop 0.240 absolute, 27.3% relative · SPL drop 0.175 absolute**
- **L3: success drop 0.520 absolute, 59.1% relative · SPL drop 0.426 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
