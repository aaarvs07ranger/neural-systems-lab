# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.717 |                 9.280 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.617 |                61.600 |               7.110 |         25 |              0.280 |              0.280 |          0.100 |          0.139 |
| B_L2 (+ object appearance)  |          0.240 | 0.240 |               152.960 |               0.898 |         25 |              0.760 |              0.760 |          0.477 |          0.665 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.640 |               0.412 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **L1: success drop 0.280 absolute, 28.0% relative · SPL drop 0.100 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.477 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
