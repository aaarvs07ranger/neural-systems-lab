# PPO_MAE zero-shot visual transfer — pair0

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.783 |                19.960 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.783 |                19.960 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.960 | 0.766 |                20.320 |              10.965 |         25 |              0.000 |              0.000 |          0.017 |          0.021 |
| F_objall             |          0.960 | 0.782 |                21.040 |              10.946 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| F_mat                |          0.920 | 0.761 |                27.680 |              10.426 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| R2                   |          0.960 | 0.762 |                20.400 |              10.971 |         25 |              0.000 |              0.000 |          0.021 |          0.027 |
| R3                   |          0.960 | 0.776 |                21.880 |              10.925 |         25 |              0.000 |              0.000 |          0.007 |          0.009 |
| B_L3 (+ distractors) |          0.600 | 0.506 |                88.880 |               6.306 |         25 |              0.360 |              0.375 |          0.277 |          0.354 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.000 absolute, 0.0% relative · SPL drop 0.017 absolute**
- **F_objall: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **F_mat: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **R2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.021 absolute**
- **R3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.007 absolute**
- **L3: success drop 0.360 absolute, 37.5% relative · SPL drop 0.277 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
