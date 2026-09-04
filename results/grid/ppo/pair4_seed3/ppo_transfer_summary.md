# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.692 |                33.120 |              11.757 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.120 | 0.106 |               176.680 |              -0.288 |         25 |              0.800 |              0.870 |          0.586 |          0.847 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.120 |              -1.463 |         25 |              0.880 |              0.957 |          0.652 |          0.942 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.160 |              -1.571 |         25 |              0.880 |              0.957 |          0.652 |          0.942 |

- **L1: success drop 0.800 absolute, 87.0% relative · SPL drop 0.586 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.652 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.652 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
