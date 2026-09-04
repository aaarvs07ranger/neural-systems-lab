# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.800 | 0.604 |                57.880 |               9.778 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.047 |               185.280 |              -1.646 |         25 |              0.720 |              0.900 |          0.557 |          0.922 |
| B_L2 (+ object appearance)  |          0.040 | 0.025 |               192.560 |              -2.327 |         25 |              0.760 |              0.950 |          0.579 |          0.959 |
| B_L3 (+ distractors)        |          0.040 | 0.025 |               192.560 |              -2.327 |         25 |              0.760 |              0.950 |          0.579 |          0.959 |

- **L1: success drop 0.720 absolute, 90.0% relative · SPL drop 0.557 absolute**
- **L2: success drop 0.760 absolute, 95.0% relative · SPL drop 0.579 absolute**
- **L3: success drop 0.760 absolute, 95.0% relative · SPL drop 0.579 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
