# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.621 |                23.320 |              13.786 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.440 | 0.245 |               123.960 |               6.462 |         25 |              0.560 |              0.560 |          0.376 |          0.605 |
| B_L2 (+ object appearance)  |          0.320 | 0.220 |               143.280 |               4.498 |         25 |              0.680 |              0.680 |          0.401 |          0.646 |
| B_L3 (+ distractors)        |          0.320 | 0.211 |               144.280 |               4.378 |         25 |              0.680 |              0.680 |          0.410 |          0.661 |

- **L1: success drop 0.560 absolute, 56.0% relative · SPL drop 0.376 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.401 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.410 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
