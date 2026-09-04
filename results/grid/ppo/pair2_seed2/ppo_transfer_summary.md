# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.778 |                 8.280 |              10.712 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.691 |                30.880 |               9.277 |         25 |              0.120 |              0.120 |          0.087 |          0.111 |
| B_L2 (+ object appearance)  |          0.840 | 0.651 |                38.360 |               8.754 |         25 |              0.160 |              0.160 |          0.127 |          0.163 |
| B_L3 (+ distractors)        |          0.840 | 0.651 |                38.360 |               8.754 |         25 |              0.160 |              0.160 |          0.127 |          0.163 |

- **L1: success drop 0.120 absolute, 12.0% relative · SPL drop 0.087 absolute**
- **L2: success drop 0.160 absolute, 16.0% relative · SPL drop 0.127 absolute**
- **L3: success drop 0.160 absolute, 16.0% relative · SPL drop 0.127 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
