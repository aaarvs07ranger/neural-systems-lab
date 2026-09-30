# PPO_JEPA zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.732 |                25.880 |              10.487 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.880 | 0.700 |                33.240 |               9.958 |         25 |              0.040 |              0.043 |          0.032 |          0.044 |
| F_lightsky           |          0.880 | 0.708 |                33.200 |               9.964 |         25 |              0.040 |              0.043 |          0.024 |          0.033 |
| F_objall             |          0.520 | 0.427 |               101.480 |               5.415 |         25 |              0.400 |              0.435 |          0.306 |          0.417 |
| F_mat                |          0.920 | 0.732 |                26.200 |              10.466 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| R2                   |          0.880 | 0.708 |                33.200 |               9.968 |         25 |              0.040 |              0.043 |          0.024 |          0.033 |
| R3                   |          0.440 | 0.351 |               116.240 |               4.365 |         25 |              0.480 |              0.522 |          0.382 |          0.521 |
| B_L3 (+ distractors) |          0.520 | 0.405 |               101.920 |               5.371 |         25 |              0.400 |              0.435 |          0.327 |          0.447 |

- **F_clut: success drop 0.040 absolute, 4.3% relative · SPL drop 0.032 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.024 absolute**
- **F_objall: success drop 0.400 absolute, 43.5% relative · SPL drop 0.306 absolute**
- **F_mat: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R2: success drop 0.040 absolute, 4.3% relative · SPL drop 0.024 absolute**
- **R3: success drop 0.480 absolute, 52.2% relative · SPL drop 0.382 absolute**
- **L3: success drop 0.400 absolute, 43.5% relative · SPL drop 0.327 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
