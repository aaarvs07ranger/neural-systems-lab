# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.658 |                30.680 |               9.246 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.658 |                30.680 |               9.246 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L2 (+ object appearance)  |          0.760 | 0.573 |                53.200 |               7.634 |         25 |              0.120 |              0.136 |          0.086 |          0.130 |
| B_L3 (+ distractors)        |          0.760 | 0.573 |                53.200 |               7.634 |         25 |              0.120 |              0.136 |          0.086 |          0.130 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.000 absolute**
- **L2: success drop 0.120 absolute, 13.6% relative · SPL drop 0.086 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.086 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
