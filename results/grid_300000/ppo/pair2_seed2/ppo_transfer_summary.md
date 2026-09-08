# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.694 |                30.560 |               9.282 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.654 |                38.120 |               8.762 |         25 |              0.040 |              0.045 |          0.040 |          0.058 |
| B_L2 (+ object appearance)  |          0.840 | 0.652 |                38.240 |               8.761 |         25 |              0.040 |              0.045 |          0.042 |          0.060 |
| B_L3 (+ distractors)        |          0.840 | 0.652 |                38.240 |               8.761 |         25 |              0.040 |              0.045 |          0.042 |          0.060 |

- **L1: success drop 0.040 absolute, 4.5% relative · SPL drop 0.040 absolute**
- **L2: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**
- **L3: success drop 0.040 absolute, 4.5% relative · SPL drop 0.042 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
