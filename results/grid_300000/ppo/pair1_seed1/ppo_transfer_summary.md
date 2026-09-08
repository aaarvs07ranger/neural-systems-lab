# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.698 |                21.800 |               9.920 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.600 | 0.530 |                84.600 |               5.524 |         25 |              0.320 |              0.348 |          0.168 |          0.241 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.520 |               0.395 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |
| B_L3 (+ distractors)        |          0.200 | 0.200 |               160.520 |               0.395 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |

- **L1: success drop 0.320 absolute, 34.8% relative · SPL drop 0.168 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
