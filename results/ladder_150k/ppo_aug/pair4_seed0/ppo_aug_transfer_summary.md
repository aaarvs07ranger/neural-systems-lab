# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.720 | 0.395 |                73.440 |               9.211 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.160 |               149.360 |               2.253 |         25 |              0.440 |              0.611 |          0.236 |          0.596 |
| B_L2 (+ object appearance)  |          0.240 | 0.157 |               155.760 |               1.476 |         25 |              0.480 |              0.667 |          0.238 |          0.603 |
| B_L3 (+ distractors)        |          0.240 | 0.157 |               155.760 |               1.476 |         25 |              0.480 |              0.667 |          0.238 |          0.603 |

- **L1: success drop 0.440 absolute, 61.1% relative · SPL drop 0.236 absolute**
- **L2: success drop 0.480 absolute, 66.7% relative · SPL drop 0.238 absolute**
- **L3: success drop 0.480 absolute, 66.7% relative · SPL drop 0.238 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
