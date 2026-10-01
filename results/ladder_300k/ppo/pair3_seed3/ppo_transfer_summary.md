# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.698 |                34.760 |              11.415 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.200 | 0.155 |               162.240 |               0.688 |         25 |              0.720 |              0.783 |          0.543 |          0.777 |
| B_L2 (+ object appearance)  |          0.120 | 0.102 |               176.960 |              -0.447 |         25 |              0.800 |              0.870 |          0.596 |          0.854 |
| B_L3 (+ distractors)        |          0.120 | 0.102 |               176.960 |              -0.447 |         25 |              0.800 |              0.870 |          0.596 |          0.854 |

- **L1: success drop 0.720 absolute, 78.3% relative · SPL drop 0.543 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.596 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.596 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
