# PPO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.698 |                34.760 |              11.415 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.698 |                34.760 |              11.415 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.400 | 0.293 |               125.680 |               3.405 |         25 |              0.520 |              0.565 |          0.406 |          0.581 |
| F_objall             |          0.040 | 0.040 |               192.160 |              -0.291 |         25 |              0.880 |              0.957 |          0.658 |          0.943 |
| F_mat                |          0.200 | 0.155 |               162.360 |               0.882 |         25 |              0.720 |              0.783 |          0.543 |          0.777 |
| R2                   |          0.400 | 0.293 |               125.680 |               3.405 |         25 |              0.520 |              0.565 |          0.406 |          0.581 |
| R3                   |          0.360 | 0.246 |               133.080 |               2.808 |         25 |              0.560 |              0.609 |          0.453 |          0.648 |
| B_L3 (+ distractors) |          0.120 | 0.102 |               176.960 |              -0.447 |         25 |              0.800 |              0.870 |          0.596 |          0.854 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.520 absolute, 56.5% relative · SPL drop 0.406 absolute**
- **F_objall: success drop 0.880 absolute, 95.7% relative · SPL drop 0.658 absolute**
- **F_mat: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **R2: success drop 0.520 absolute, 56.5% relative · SPL drop 0.406 absolute**
- **R3: success drop 0.560 absolute, 60.9% relative · SPL drop 0.453 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.596 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
