# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.720 | 0.425 |                74.240 |               9.247 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.347 |                97.560 |               7.550 |         25 |              0.120 |              0.167 |          0.078 |          0.184 |
| B_L2 (+ object appearance)  |          0.440 | 0.302 |               122.840 |               4.948 |         25 |              0.280 |              0.389 |          0.123 |          0.289 |
| B_L3 (+ distractors)        |          0.440 | 0.294 |               123.080 |               4.971 |         25 |              0.280 |              0.389 |          0.131 |          0.309 |

- **L1: success drop 0.120 absolute, 16.7% relative · SPL drop 0.078 absolute**
- **L2: success drop 0.280 absolute, 38.9% relative · SPL drop 0.123 absolute**
- **L3: success drop 0.280 absolute, 38.9% relative · SPL drop 0.131 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
