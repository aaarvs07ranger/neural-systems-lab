# PPO zero-shot visual transfer — pair2

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.699 |                21.960 |               9.760 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.698 |                22.000 |               9.765 |         25 |              0.000 |              0.000 |          0.001 |          0.001 |
| B_L2 (+ object appearance)  |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |
| B_L3 (+ distractors)        |          0.760 | 0.538 |                52.640 |               7.726 |         25 |              0.160 |              0.174 |          0.161 |          0.230 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.001 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.161 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
