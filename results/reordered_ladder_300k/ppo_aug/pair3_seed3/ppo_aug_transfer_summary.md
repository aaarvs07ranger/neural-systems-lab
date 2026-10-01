# PPO_AUG zero-shot visual transfer — pair3

| variant              |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:---------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)    |          0.960 | 0.733 |                28.680 |              11.969 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_clut               |          0.960 | 0.733 |                28.680 |              11.959 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| F_lightsky           |          0.680 | 0.521 |                74.360 |               7.489 |         25 |              0.280 |              0.292 |          0.212 |          0.289 |
| F_objall             |          0.480 | 0.364 |               114.240 |               5.957 |         25 |              0.480 |              0.500 |          0.368 |          0.503 |
| F_mat                |          0.640 | 0.505 |                81.960 |               6.592 |         25 |              0.320 |              0.333 |          0.227 |          0.310 |
| R2                   |          0.680 | 0.521 |                74.360 |               7.489 |         25 |              0.280 |              0.292 |          0.212 |          0.289 |
| R3                   |          0.640 | 0.494 |                80.960 |               6.829 |         25 |              0.320 |              0.333 |          0.239 |          0.326 |
| B_L3 (+ distractors) |          0.360 | 0.238 |               134.480 |               2.426 |         25 |              0.600 |              0.625 |          0.495 |          0.675 |

- **F_clut: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **F_lightsky: success drop 0.280 absolute, 29.2% relative · SPL drop 0.212 absolute**
- **F_objall: success drop 0.480 absolute, 50.0% relative · SPL drop 0.368 absolute**
- **F_mat: success drop 0.320 absolute, 33.3% relative · SPL drop 0.227 absolute**
- **R2: success drop 0.280 absolute, 29.2% relative · SPL drop 0.212 absolute**
- **R3: success drop 0.320 absolute, 33.3% relative · SPL drop 0.239 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
