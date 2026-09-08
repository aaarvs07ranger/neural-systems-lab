# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.771 |                19.920 |              11.092 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.440 | 0.348 |               116.840 |               4.045 |         25 |              0.520 |              0.542 |          0.423 |          0.549 |
| B_L2 (+ object appearance)  |          0.280 | 0.191 |               149.360 |               1.869 |         25 |              0.680 |              0.708 |          0.581 |          0.752 |
| B_L3 (+ distractors)        |          0.280 | 0.191 |               149.360 |               1.869 |         25 |              0.680 |              0.708 |          0.581 |          0.752 |

- **L1: success drop 0.520 absolute, 54.2% relative · SPL drop 0.423 absolute**
- **L2: success drop 0.680 absolute, 70.8% relative · SPL drop 0.581 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.581 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
