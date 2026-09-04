# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                25.280 |               9.850 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.490 |                78.760 |               6.100 |         25 |              0.280 |              0.304 |          0.205 |          0.295 |
| B_L2 (+ object appearance)  |          0.680 | 0.480 |                72.840 |               6.507 |         25 |              0.240 |              0.261 |          0.214 |          0.308 |
| B_L3 (+ distractors)        |          0.720 | 0.513 |                66.600 |               7.152 |         25 |              0.200 |              0.217 |          0.181 |          0.261 |

- **L1: success drop 0.280 absolute, 30.4% relative · SPL drop 0.205 absolute**
- **L2: success drop 0.240 absolute, 26.1% relative · SPL drop 0.214 absolute**
- **L3: success drop 0.200 absolute, 21.7% relative · SPL drop 0.181 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
