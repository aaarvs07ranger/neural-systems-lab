# PPO_MAE zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.723 |                33.000 |              11.877 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.722 |                33.120 |              11.878 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_lightsky           |          0.440 | 0.298 |               119.360 |               5.369 |         25 |              0.480 |              0.522 |          0.425 |          0.588 |
| F_objall             |          0.960 | 0.729 |                27.520 |              12.553 |         25 |             -0.040 |             -0.043 |         -0.006 |         -0.009 |
| F_mat                |          0.080 | 0.073 |               184.760 |              -0.089 |         25 |              0.840 |              0.913 |          0.650 |          0.898 |
| R2                   |          0.440 | 0.298 |               119.360 |               5.369 |         25 |              0.480 |              0.522 |          0.425 |          0.588 |
| R3                   |          0.040 | 0.028 |               193.480 |               0.028 |         25 |              0.880 |              0.957 |          0.695 |          0.961 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -1.707 |         25 |              0.920 |              1.000 |          0.723 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop 0.480 absolute, 52.2% relative · SPL drop 0.425 absolute**
- **F_objall: success drop -0.040 absolute, -4.3% relative · SPL drop -0.006 absolute**
- **F_mat: success drop 0.840 absolute, 91.3% relative · SPL drop 0.650 absolute**
- **R2: success drop 0.480 absolute, 52.2% relative · SPL drop 0.425 absolute**
- **R3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.695 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.723 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
