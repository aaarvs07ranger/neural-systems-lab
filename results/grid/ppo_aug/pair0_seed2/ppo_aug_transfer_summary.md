# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.777 |                19.880 |              10.963 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.775 |                20.080 |              10.950 |         25 |              0.000 |              0.000 |          0.002 |          0.003 |
| B_L2 (+ object appearance)  |          0.920 | 0.691 |                37.200 |              10.332 |         25 |              0.040 |              0.042 |          0.086 |          0.111 |
| B_L3 (+ distractors)        |          0.960 | 0.731 |                29.360 |              10.822 |         25 |              0.000 |              0.000 |          0.046 |          0.059 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.002 absolute**
- **L2: success drop 0.040 absolute, 4.2% relative · SPL drop 0.086 absolute**
- **L3: success drop 0.000 absolute, 0.0% relative · SPL drop 0.046 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
