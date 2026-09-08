# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                36.560 |              11.440 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -1.999 |         25 |              0.920 |              1.000 |          0.694 |          1.000 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.240 |              -1.540 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.240 |              -1.540 |         25 |              0.880 |              0.957 |          0.654 |          0.942 |

- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.694 absolute**
- **L2: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**
- **L3: success drop 0.880 absolute, 95.7% relative · SPL drop 0.654 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
