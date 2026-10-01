# PPO_AUG zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.804 |                12.480 |              11.575 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.240 | 0.191 |               154.800 |               1.262 |         25 |              0.760 |              0.760 |          0.613 |          0.762 |
| B_L2 (+ object appearance)  |          0.400 | 0.304 |               126.960 |               3.338 |         25 |              0.600 |              0.600 |          0.500 |          0.622 |
| B_L3 (+ distractors)        |          0.360 | 0.268 |               134.200 |               2.832 |         25 |              0.640 |              0.640 |          0.537 |          0.667 |

- **L1: success drop 0.760 absolute, 76.0% relative · SPL drop 0.613 absolute**
- **L2: success drop 0.600 absolute, 60.0% relative · SPL drop 0.500 absolute**
- **L3: success drop 0.640 absolute, 64.0% relative · SPL drop 0.537 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
