# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.717 |                 6.720 |              10.889 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.635 |                53.680 |               7.671 |         25 |              0.240 |              0.240 |          0.082 |          0.115 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.720 |               0.403 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.800 |              0.800 |          0.517 |          0.721 |

- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.082 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**
- **L3: success drop 0.800 absolute, 80.0% relative · SPL drop 0.517 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
