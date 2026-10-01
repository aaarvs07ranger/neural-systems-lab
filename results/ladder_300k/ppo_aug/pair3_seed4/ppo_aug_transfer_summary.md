# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.735 |                27.760 |              11.994 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.253 |               135.080 |               3.032 |         25 |              0.600 |              0.625 |          0.482 |          0.656 |
| B_L2 (+ object appearance)  |          0.280 | 0.191 |               147.960 |               1.842 |         25 |              0.680 |              0.708 |          0.544 |          0.740 |
| B_L3 (+ distractors)        |          0.280 | 0.191 |               147.960 |               1.777 |         25 |              0.680 |              0.708 |          0.544 |          0.740 |

- **L1: success drop 0.600 absolute, 62.5% relative · SPL drop 0.482 absolute**
- **L2: success drop 0.680 absolute, 70.8% relative · SPL drop 0.544 absolute**
- **L3: success drop 0.680 absolute, 70.8% relative · SPL drop 0.544 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
