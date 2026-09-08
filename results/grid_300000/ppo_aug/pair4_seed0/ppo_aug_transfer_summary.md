# PPO_AUG zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.740 |                25.320 |              12.578 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.432 |                82.360 |               7.710 |         25 |              0.320 |              0.333 |          0.307 |          0.416 |
| B_L2 (+ object appearance)  |          0.400 | 0.319 |               125.240 |               4.226 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |
| B_L3 (+ distractors)        |          0.400 | 0.319 |               125.240 |               4.191 |         25 |              0.560 |              0.583 |          0.421 |          0.569 |

- **L1: success drop 0.320 absolute, 33.3% relative · SPL drop 0.307 absolute**
- **L2: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.421 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
