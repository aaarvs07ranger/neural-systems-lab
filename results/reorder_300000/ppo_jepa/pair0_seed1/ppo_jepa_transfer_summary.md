# PPO_JEPA zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.770 |                18.120 |              10.981 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.773 |                18.080 |              10.980 |         25 |              0.000 |              0.000 |         -0.003 |         -0.003 |
| F_lightsky           |          0.920 | 0.736 |                25.640 |              10.489 |         25 |              0.040 |              0.042 |          0.034 |          0.044 |
| F_objall             |          0.880 | 0.725 |                34.120 |               9.807 |         25 |              0.080 |              0.083 |          0.045 |          0.059 |
| F_mat                |          0.840 | 0.709 |                41.880 |               9.440 |         25 |              0.120 |              0.125 |          0.061 |          0.079 |
| R2                   |          0.880 | 0.704 |                33.000 |               9.960 |         25 |              0.080 |              0.083 |          0.066 |          0.085 |
| R3                   |          0.760 | 0.629 |                56.080 |               8.298 |         25 |              0.200 |              0.208 |          0.141 |          0.183 |
| B_L3 (+ distractors) |          0.800 | 0.649 |                50.400 |               8.785 |         25 |              0.160 |              0.167 |          0.121 |          0.157 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop -0.003 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.2% relative · SPL drop 0.034 absolute**
- **F_objall: success drop 0.080 absolute, 8.3% relative · SPL drop 0.045 absolute**
- **F_mat: success drop 0.120 absolute, 12.5% relative · SPL drop 0.061 absolute**
- **R2: success drop 0.080 absolute, 8.3% relative · SPL drop 0.066 absolute**
- **R3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.141 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.121 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
