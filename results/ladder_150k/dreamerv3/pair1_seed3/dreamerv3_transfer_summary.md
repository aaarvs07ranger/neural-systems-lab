# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.680 |                14.720 |              10.785 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.640 | 0.512 |               107.400 |               5.854 |         25 |              0.360 |              0.360 |          0.168 |          0.247 |
| B_L2 (+ object appearance)  |          0.280 | 0.280 |               156.840 |               1.243 |         25 |              0.720 |              0.720 |          0.400 |          0.588 |
| B_L3 (+ distractors)        |          0.600 | 0.458 |               107.200 |               5.441 |         25 |              0.400 |              0.400 |          0.222 |          0.326 |

- **L1: success drop 0.360 absolute, 36.0% relative · SPL drop 0.168 absolute**
- **L2: success drop 0.720 absolute, 72.0% relative · SPL drop 0.400 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.222 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
