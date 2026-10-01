# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.599 |                37.560 |              12.652 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.416 |                73.360 |               9.455 |         25 |              0.200 |              0.217 |          0.183 |          0.306 |
| B_L2 (+ object appearance)  |          0.520 | 0.341 |               107.240 |               6.536 |         25 |              0.400 |              0.435 |          0.258 |          0.430 |
| B_L3 (+ distractors)        |          0.560 | 0.364 |               100.640 |               7.163 |         25 |              0.360 |              0.391 |          0.235 |          0.393 |

- **L1: success drop 0.200 absolute, 21.7% relative · SPL drop 0.183 absolute**
- **L2: success drop 0.400 absolute, 43.5% relative · SPL drop 0.258 absolute**
- **L3: success drop 0.360 absolute, 39.1% relative · SPL drop 0.235 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
