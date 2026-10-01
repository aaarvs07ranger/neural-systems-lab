# PPO_JEPA zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.710 |                34.480 |              12.052 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.705 |                34.400 |              12.058 |         25 |              0.000 |              0.000 |          0.005 |          0.007 |
| F_lightsky           |          0.880 | 0.684 |                40.920 |              11.364 |         25 |              0.040 |              0.043 |          0.027 |          0.037 |
| F_objall             |          0.800 | 0.606 |                56.360 |              10.422 |         25 |              0.120 |              0.130 |          0.105 |          0.147 |
| F_mat                |          0.080 | 0.080 |               184.240 |              -0.249 |         25 |              0.840 |              0.913 |          0.630 |          0.887 |
| R2                   |          0.920 | 0.709 |                33.400 |              11.853 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| R3                   |          0.800 | 0.586 |                54.960 |               9.913 |         25 |              0.120 |              0.130 |          0.124 |          0.175 |
| B_L3 (+ distractors) |          0.120 | 0.099 |               177.560 |               1.406 |         25 |              0.800 |              0.870 |          0.611 |          0.860 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.005 absolute**
- **F_lightsky: success drop 0.040 absolute, 4.3% relative · SPL drop 0.027 absolute**
- **F_objall: success drop 0.120 absolute, 13.0% relative · SPL drop 0.105 absolute**
- **F_mat: success drop 0.840 absolute, 91.3% relative · SPL drop 0.630 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **R3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.124 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.611 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
