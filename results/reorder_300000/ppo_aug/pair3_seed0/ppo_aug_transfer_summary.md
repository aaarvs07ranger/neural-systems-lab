# PPO_AUG zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          1.000 | 0.736 |                22.280 |              12.541 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          1.000 | 0.736 |                22.280 |              12.541 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.880 | 0.640 |                42.760 |              10.779 |         25 |              0.120 |              0.120 |          0.097 |          0.131 |
| F_objall             |          0.760 | 0.602 |                62.200 |               9.215 |         25 |              0.240 |              0.240 |          0.134 |          0.182 |
| F_mat                |          0.040 | 0.026 |               193.000 |              -1.146 |         25 |              0.960 |              0.960 |          0.710 |          0.965 |
| R2                   |          0.880 | 0.640 |                42.760 |              10.779 |         25 |              0.120 |              0.120 |          0.097 |          0.131 |
| R3                   |          0.640 | 0.487 |                81.240 |               6.948 |         25 |              0.360 |              0.360 |          0.249 |          0.338 |
| B_L3 (+ distractors) |          0.000 | 0.000 |               200.000 |              -2.212 |         25 |              1.000 |              1.000 |          0.736 |          1.000 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.120 absolute, 12.0% relative · SPL drop 0.097 absolute**
- **F_objall: success drop 0.240 absolute, 24.0% relative · SPL drop 0.134 absolute**
- **F_mat: success drop 0.960 absolute, 96.0% relative · SPL drop 0.710 absolute**
- **R2: success drop 0.120 absolute, 12.0% relative · SPL drop 0.097 absolute**
- **R3: success drop 0.360 absolute, 36.0% relative · SPL drop 0.249 absolute**
- **L3: success drop 1.000 absolute, 100.0% relative · SPL drop 0.736 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
