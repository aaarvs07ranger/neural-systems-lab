# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.785 |                19.840 |              10.958 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.674 |                44.680 |              10.197 |         25 |              0.040 |              0.042 |          0.111 |          0.142 |
| B_L2 (+ object appearance)  |          0.560 | 0.357 |               124.480 |               5.456 |         25 |              0.400 |              0.417 |          0.428 |          0.545 |
| B_L3 (+ distractors)        |          0.680 | 0.458 |               112.800 |               6.804 |         25 |              0.280 |              0.292 |          0.328 |          0.417 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.111 absolute**
- **L2: success drop 0.400 absolute, 41.7% relative · SPL drop 0.428 absolute**
- **L3: success drop 0.280 absolute, 29.2% relative · SPL drop 0.328 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
