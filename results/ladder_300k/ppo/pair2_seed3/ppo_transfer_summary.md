# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.740 |                13.840 |              10.201 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.603 |                52.320 |               7.691 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |
| B_L2 (+ object appearance)  |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |
| B_L3 (+ distractors)        |          0.760 | 0.603 |                52.400 |               7.690 |         25 |              0.200 |              0.208 |          0.138 |          0.186 |

- **L1: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**
- **L2: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**
- **L3: success drop 0.200 absolute, 20.8% relative · SPL drop 0.138 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
