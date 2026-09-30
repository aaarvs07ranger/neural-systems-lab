# PPO_DINO zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.777 |                17.520 |              10.990 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.777 |                17.520 |              10.990 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.767 |                17.720 |              10.977 |         25 |              0.000 |              0.000 |          0.010 |          0.012 |
| F_objall             |          0.840 | 0.656 |                41.240 |               9.435 |         25 |              0.120 |              0.125 |          0.121 |          0.155 |
| F_mat                |          0.960 | 0.785 |                18.080 |              11.103 |         25 |              0.000 |              0.000 |         -0.008 |         -0.010 |
| R2                   |          0.960 | 0.772 |                17.640 |              10.984 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| R3                   |          0.760 | 0.602 |                56.360 |               8.351 |         25 |              0.200 |              0.208 |          0.175 |          0.225 |
| B_L3 (+ distractors) |          0.760 | 0.612 |                55.480 |               8.332 |         25 |              0.200 |              0.208 |          0.165 |          0.212 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **F_objall: success drop 0.120 absolute, 12.5% relative · SPL drop 0.121 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop -0.008 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.175 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.165 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
