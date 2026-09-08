# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.688 |                41.000 |               9.505 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.840 | 0.676 |                41.680 |               9.398 |         25 |              0.000 |              0.000 |          0.012 |          0.017 |
| B_L2 (+ object appearance)  |          0.200 | 0.186 |               161.640 |               1.252 |         25 |              0.640 |              0.762 |          0.502 |          0.730 |
| B_L3 (+ distractors)        |          0.200 | 0.166 |               161.680 |               1.228 |         25 |              0.640 |              0.762 |          0.522 |          0.759 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.012 absolute**
- **L2: success drop 0.640 absolute, 76.2% relative · SPL drop 0.502 absolute**
- **L3: success drop 0.640 absolute, 76.2% relative · SPL drop 0.522 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
