# PPO_DINO zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.714 |                26.920 |              12.098 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.714 |                26.920 |              12.071 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.711 |                26.920 |              12.085 |         25 |              0.000 |              0.000 |          0.003 |          0.004 |
| F_objall             |          0.400 | 0.349 |               124.200 |               4.119 |         25 |              0.560 |              0.583 |          0.365 |          0.511 |
| F_mat                |          0.360 | 0.319 |               133.440 |               3.765 |         25 |              0.600 |              0.625 |          0.395 |          0.554 |
| R2                   |          0.920 | 0.681 |                33.480 |              11.462 |         25 |              0.040 |              0.042 |          0.033 |          0.046 |
| R3                   |          0.360 | 0.309 |               131.760 |               3.619 |         25 |              0.600 |              0.625 |          0.405 |          0.567 |
| B_L3 (+ distractors) |          0.080 | 0.080 |               185.200 |              -0.291 |         25 |              0.880 |              0.917 |          0.634 |          0.888 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.003 absolute**
- **F_objall: success drop 0.560 absolute, 58.3% relative · SPL drop 0.365 absolute**
- **F_mat: success drop 0.600 absolute, 62.5% relative · SPL drop 0.395 absolute**
- **R2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.033 absolute**
- **R3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.405 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.634 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
