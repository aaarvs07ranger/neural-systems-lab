# PPO_JEPA zero-shot visual transfer — pair2

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.779 |                 8.080 |              10.682 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.779 |                 8.080 |              10.679 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          1.000 | 0.779 |                 8.200 |              10.689 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          1.000 | 0.780 |                 8.600 |              10.699 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| F_mat                |          0.920 | 0.725 |                25.720 |               9.721 |         25 |              0.080 |              0.080 |          0.053 |          0.068 |
| R2                   |          0.920 | 0.699 |                23.440 |               9.729 |         25 |              0.080 |              0.080 |          0.080 |          0.103 |
| R3                   |          1.000 | 0.780 |                 8.280 |              10.691 |         25 |              0.000 |              0.000 |         -0.002 |         -0.002 |
| B_L3 (+ distractors) |          0.600 | 0.447 |                86.480 |               5.869 |         25 |              0.400 |              0.400 |          0.332 |          0.426 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **F_mat: success drop 0.080 absolute, 8.0% relative · SPL drop 0.053 absolute**
- **R2: success drop 0.080 absolute, 8.0% relative · SPL drop 0.080 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.002 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.332 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
