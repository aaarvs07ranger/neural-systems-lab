# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.880 | 0.619 |                30.760 |               9.311 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.200 | 0.146 |               161.000 |               0.264 |         25 |              0.680 |              0.773 |          0.474 |          0.765 |
| B_L2 (+ object appearance)  |          0.200 | 0.174 |               160.640 |               0.331 |         25 |              0.680 |              0.773 |          0.445 |          0.719 |
| B_L3 (+ distractors)        |          0.200 | 0.151 |               161.120 |               0.273 |         25 |              0.680 |              0.773 |          0.468 |          0.756 |

- **L1: success drop 0.680 absolute, 77.3% relative · SPL drop 0.474 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.445 absolute**
- **L3: success drop 0.680 absolute, 77.3% relative · SPL drop 0.468 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
