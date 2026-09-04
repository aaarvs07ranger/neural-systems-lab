# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.807 |                12.440 |              11.583 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.760 | 0.579 |                60.200 |               8.403 |         25 |              0.240 |              0.240 |          0.228 |          0.282 |
| B_L2 (+ object appearance)  |          0.680 | 0.429 |                80.440 |               7.193 |         25 |              0.320 |              0.320 |          0.379 |          0.469 |
| B_L3 (+ distractors)        |          0.680 | 0.454 |                79.880 |               7.089 |         25 |              0.320 |              0.320 |          0.353 |          0.438 |

- **L1: success drop 0.240 absolute, 24.0% relative · SPL drop 0.228 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.379 absolute**
- **L3: success drop 0.320 absolute, 32.0% relative · SPL drop 0.353 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
