# PPO_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.520 | 0.400 |               102.400 |               5.349 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.520 | 0.400 |               102.360 |               5.344 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.440 | 0.321 |               117.400 |               4.421 |         25 |              0.080 |              0.154 |          0.079 |          0.197 |
| F_objall             |          0.520 | 0.404 |               102.160 |               5.325 |         25 |              0.000 |              0.000 |         -0.005 |         -0.012 |
| F_mat                |          0.400 | 0.302 |               126.240 |               3.731 |         25 |              0.120 |              0.231 |          0.097 |          0.243 |
| R2                   |          0.440 | 0.321 |               117.400 |               4.419 |         25 |              0.080 |              0.154 |          0.079 |          0.197 |
| R3                   |          0.520 | 0.404 |               102.040 |               5.458 |         25 |              0.000 |              0.000 |         -0.005 |         -0.012 |
| B_L3 (+ distractors) |          0.520 | 0.422 |               104.360 |               5.199 |         25 |              0.000 |              0.000 |         -0.022 |         -0.056 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.080 absolute, 15.4% relative · SPL drop 0.079 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **F_mat: success drop 0.120 absolute, 23.1% relative · SPL drop 0.097 absolute**
- **R2: success drop 0.080 absolute, 15.4% relative · SPL drop 0.079 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.005 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop -0.022 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
