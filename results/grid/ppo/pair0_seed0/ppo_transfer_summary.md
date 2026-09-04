# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.785 |                17.840 |              10.952 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.520 | 0.431 |               100.640 |               5.129 |         25 |              0.440 |              0.458 |          0.354 |          0.451 |
| B_L2 (+ object appearance)  |          0.080 | 0.080 |               184.200 |              -0.623 |         25 |              0.880 |              0.917 |          0.705 |          0.898 |
| B_L3 (+ distractors)        |          0.080 | 0.080 |               184.200 |              -0.632 |         25 |              0.880 |              0.917 |          0.705 |          0.898 |

- **L1: success drop 0.440 absolute, 45.8% relative · SPL drop 0.354 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.705 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.705 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
