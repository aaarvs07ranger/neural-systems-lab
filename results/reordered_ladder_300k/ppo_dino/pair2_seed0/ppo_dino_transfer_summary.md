# PPO_DINO zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.880 | 0.658 |                29.920 |               9.268 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.658 |                29.920 |               9.268 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.658 |                30.520 |               9.261 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          0.880 | 0.658 |                29.960 |               9.270 |         25 |              0.000 |              0.000 |         -0.000 |         -0.000 |
| F_mat                |          0.760 | 0.538 |                52.760 |               7.816 |         25 |              0.120 |              0.136 |          0.120 |          0.182 |
| R2                   |          0.880 | 0.658 |                30.520 |               9.261 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| R3                   |          0.800 | 0.578 |                45.200 |               8.311 |         25 |              0.080 |              0.091 |          0.080 |          0.122 |
| B_L3 (+ distractors) |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.120 |              0.136 |          0.120 |          0.182 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.000 absolute**
- **F_mat: success drop 0.120 absolute, 13.6% relative · SPL drop 0.120 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **R3: success drop 0.080 absolute, 9.1% relative · SPL drop 0.080 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.120 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
