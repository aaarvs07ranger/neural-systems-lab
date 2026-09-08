# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.808 |                11.280 |              11.604 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.480 | 0.395 |               109.960 |               4.667 |         25 |              0.520 |              0.520 |          0.413 |          0.511 |
| B_L2 (+ object appearance)  |          0.240 | 0.211 |               155.800 |               1.567 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |
| B_L3 (+ distractors)        |          0.240 | 0.211 |               155.800 |               1.567 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |

- **L1: success drop 0.520 absolute, 52.0% relative · SPL drop 0.413 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
