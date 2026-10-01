# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.733 |                28.680 |              11.969 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.440 | 0.283 |               120.320 |               3.579 |         25 |              0.520 |              0.542 |          0.450 |          0.614 |
| B_L2 (+ object appearance)  |          0.360 | 0.238 |               134.480 |               2.460 |         25 |              0.600 |              0.625 |          0.495 |          0.675 |
| B_L3 (+ distractors)        |          0.360 | 0.238 |               134.480 |               2.426 |         25 |              0.600 |              0.625 |          0.495 |          0.675 |

- **L1: success drop 0.520 absolute, 54.2% relative · SPL drop 0.450 absolute**
- **L2: success drop 0.600 absolute, 62.5% relative · SPL drop 0.495 absolute**
- **L3: success drop 0.600 absolute, 62.5% relative · SPL drop 0.495 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
