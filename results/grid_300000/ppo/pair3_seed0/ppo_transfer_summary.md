# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.761 |                18.800 |              12.593 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.040 | 0.040 |               192.160 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.200 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.200 |              -1.911 |         25 |              0.960 |              0.960 |          0.721 |          0.947 |

- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.721 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
