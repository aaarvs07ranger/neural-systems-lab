# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.657 |                30.640 |               9.240 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.611 |                39.160 |               8.768 |         25 |              0.040 |              0.045 |          0.046 |          0.070 |
| B_L2 (+ object appearance)  |          0.800 | 0.571 |                46.680 |               8.286 |         25 |              0.080 |              0.091 |          0.086 |          0.131 |
| B_L3 (+ distractors)        |          0.800 | 0.571 |                46.680 |               8.286 |         25 |              0.080 |              0.091 |          0.086 |          0.131 |

- **L1: success drop 0.040 absolute, 4.5% relative · SPL drop 0.046 absolute**
- **L2: success drop 0.080 absolute, 9.1% relative · SPL drop 0.086 absolute**
- **L3: success drop 0.080 absolute, 9.1% relative · SPL drop 0.086 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
