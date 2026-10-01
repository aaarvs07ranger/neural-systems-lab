# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.840 | 0.560 |                50.640 |              11.071 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.423 |                68.000 |               9.692 |         25 |              0.080 |              0.095 |          0.136 |          0.243 |
| B_L2 (+ object appearance)  |          0.520 | 0.343 |               108.800 |               6.128 |         25 |              0.320 |              0.381 |          0.216 |          0.386 |
| B_L3 (+ distractors)        |          0.520 | 0.351 |               108.520 |               6.095 |         25 |              0.320 |              0.381 |          0.208 |          0.372 |

- **L1: success drop 0.080 absolute, 9.5% relative · SPL drop 0.136 absolute**
- **L2: success drop 0.320 absolute, 38.1% relative · SPL drop 0.216 absolute**
- **L3: success drop 0.320 absolute, 38.1% relative · SPL drop 0.208 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
