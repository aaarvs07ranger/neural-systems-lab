# DREAMERV3 zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.720 | 0.392 |                91.320 |              10.197 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.560 | 0.207 |               132.760 |               6.344 |         25 |              0.160 |              0.222 |          0.185 |          0.472 |
| B_L2 (+ object appearance)  |          0.480 | 0.179 |               138.920 |               5.262 |         25 |              0.240 |              0.333 |          0.213 |          0.543 |
| B_L3 (+ distractors)        |          0.400 | 0.200 |               150.840 |               4.281 |         25 |              0.320 |              0.444 |          0.193 |          0.491 |

- **L1: success drop 0.160 absolute, 22.2% relative · SPL drop 0.185 absolute**
- **L2: success drop 0.240 absolute, 33.3% relative · SPL drop 0.213 absolute**
- **L3: success drop 0.320 absolute, 44.4% relative · SPL drop 0.193 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
