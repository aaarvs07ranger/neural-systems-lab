# PPO_AUG zero-shot visual transfer — pair1

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_objall             |          0.920 | 0.689 |                25.680 |               9.855 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_mat                |          0.360 | 0.243 |               131.360 |               2.356 |         25 |              0.560 |              0.609 |          0.451 |          0.650 |
| R2                   |          0.920 | 0.694 |                25.000 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| R3                   |          0.800 | 0.621 |                48.240 |               8.316 |         25 |              0.120 |              0.130 |          0.073 |          0.105 |
| B_L3 (+ distractors) |          0.400 | 0.369 |               124.040 |               2.950 |         25 |              0.520 |              0.565 |          0.326 |          0.469 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_mat: success drop 0.560 absolute, 60.9% relative · SPL drop 0.451 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **R3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.073 absolute**
- **L3: success drop 0.520 absolute, 56.5% relative · SPL drop 0.326 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
