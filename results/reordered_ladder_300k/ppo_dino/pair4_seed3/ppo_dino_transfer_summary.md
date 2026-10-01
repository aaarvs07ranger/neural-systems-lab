# PPO_DINO zero-shot visual transfer — pair4

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.920 | 0.737 |                32.400 |              11.927 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.920 | 0.736 |                32.440 |              11.973 |         25 |              0.000 |              0.000 |          0.001 |          0.002 |
| F_lightsky           |          0.960 | 0.768 |                25.760 |              12.565 |         25 |             -0.040 |             -0.043 |         -0.031 |         -0.042 |
| F_objall             |          0.880 | 0.704 |                39.240 |              11.230 |         25 |              0.040 |              0.043 |          0.034 |          0.046 |
| F_mat                |          0.880 | 0.708 |                40.160 |              11.537 |         25 |              0.040 |              0.043 |          0.029 |          0.040 |
| R2                   |          0.960 | 0.768 |                25.680 |              12.576 |         25 |             -0.040 |             -0.043 |         -0.031 |         -0.042 |
| R3                   |          0.880 | 0.705 |                39.200 |              11.233 |         25 |              0.040 |              0.043 |          0.033 |          0.044 |
| B_L3 (+ distractors) |          0.760 | 0.603 |                61.000 |               9.702 |         25 |              0.160 |              0.174 |          0.135 |          0.182 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_lightsky: success drop -0.040 absolute, -4.3% relative · SPL drop -0.031 absolute**
- **F_objall: success drop 0.040 absolute, 4.3% relative · SPL drop 0.034 absolute**
- **F_mat: success drop 0.040 absolute, 4.3% relative · SPL drop 0.029 absolute**
- **R2: success drop -0.040 absolute, -4.3% relative · SPL drop -0.031 absolute**
- **R3: success drop 0.040 absolute, 4.3% relative · SPL drop 0.033 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.135 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
