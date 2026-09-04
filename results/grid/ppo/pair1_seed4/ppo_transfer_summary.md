# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.691 |                22.280 |               9.895 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.518 |                77.840 |               5.997 |         25 |              0.280 |              0.304 |          0.173 |          0.251 |
| B_L2 (+ object appearance)  |          0.280 | 0.280 |               145.800 |               1.432 |         25 |              0.640 |              0.696 |          0.411 |          0.595 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.320 |               0.413 |         25 |              0.720 |              0.783 |          0.491 |          0.711 |

- **L1: success drop 0.280 absolute, 30.4% relative · SPL drop 0.173 absolute**
- **L2: success drop 0.640 absolute, 69.6% relative · SPL drop 0.411 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.491 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
