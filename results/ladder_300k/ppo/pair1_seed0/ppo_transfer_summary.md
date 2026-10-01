# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.675 |                14.240 |              10.383 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.425 |                76.920 |               6.275 |         25 |              0.320 |              0.333 |          0.250 |          0.371 |
| B_L2 (+ object appearance)  |          0.360 | 0.304 |               130.360 |               2.568 |         25 |              0.600 |              0.625 |          0.371 |          0.550 |
| B_L3 (+ distractors)        |          0.360 | 0.306 |               129.720 |               2.566 |         25 |              0.600 |              0.625 |          0.370 |          0.547 |

- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.250 absolute**
- **L2: success drop 0.600 absolute, 62.5% relative · SPL drop 0.371 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.370 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
