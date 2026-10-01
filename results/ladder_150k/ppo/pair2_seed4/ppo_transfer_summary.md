# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.699 |                21.800 |               9.749 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.880 | 0.658 |                29.520 |               9.257 |         25 |              0.040 |              0.043 |          0.042 |          0.060 |
| B_L2 (+ object appearance)  |          0.800 | 0.578 |                44.680 |               8.219 |         25 |              0.120 |              0.130 |          0.122 |          0.174 |
| B_L3 (+ distractors)        |          0.800 | 0.578 |                44.680 |               8.219 |         25 |              0.120 |              0.130 |          0.122 |          0.174 |

- **L1: success drop 0.040 absolute, 4.3% relative · SPL drop 0.042 absolute**
- **L2: success drop 0.120 absolute, 13.0% relative · SPL drop 0.122 absolute**
- **L3: success drop 0.120 absolute, 13.0% relative · SPL drop 0.122 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
