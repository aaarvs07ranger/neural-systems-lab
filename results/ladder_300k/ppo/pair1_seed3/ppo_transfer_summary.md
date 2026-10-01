# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.678 |                29.160 |               9.333 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.631 |                53.840 |               7.534 |         25 |              0.120 |              0.136 |          0.047 |          0.070 |
| B_L2 (+ object appearance)  |          0.120 | 0.120 |               176.160 |              -0.540 |         25 |              0.760 |              0.864 |          0.558 |          0.823 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               176.160 |              -0.571 |         25 |              0.760 |              0.864 |          0.558 |          0.823 |

- **L1: success drop 0.120 absolute, 13.6% relative · SPL drop 0.047 absolute**
- **L2: success drop 0.760 absolute, 86.4% relative · SPL drop 0.558 absolute**
- **L3: success drop 0.760 absolute, 86.4% relative · SPL drop 0.558 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
