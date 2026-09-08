# PPO_AUG zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.739 |                14.200 |              10.236 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.643 |                45.080 |               8.195 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |
| B_L2 (+ object appearance)  |          0.800 | 0.643 |                45.040 |               8.199 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |
| B_L3 (+ distractors)        |          0.800 | 0.643 |                45.040 |               8.199 |         25 |              0.160 |              0.167 |          0.096 |          0.130 |

- **L1: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.096 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
