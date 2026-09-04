# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.760 | 0.573 |                64.480 |               8.960 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.064 |               184.640 |              -0.801 |         25 |              0.680 |              0.895 |          0.509 |          0.888 |
| B_L2 (+ object appearance)  |          0.040 | 0.040 |               192.200 |              -1.311 |         25 |              0.720 |              0.947 |          0.533 |          0.930 |
| B_L3 (+ distractors)        |          0.040 | 0.040 |               192.200 |              -1.311 |         25 |              0.720 |              0.947 |          0.533 |          0.930 |

- **L1: success drop 0.680 absolute, 89.5% relative · SPL drop 0.509 absolute**
- **L2: success drop 0.720 absolute, 94.7% relative · SPL drop 0.533 absolute**
- **L3: success drop 0.720 absolute, 94.7% relative · SPL drop 0.533 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
