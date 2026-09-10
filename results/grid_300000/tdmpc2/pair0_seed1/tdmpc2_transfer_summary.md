# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.823 |                11.960 |              11.568 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.556 |                68.480 |               8.593 |         25 |              0.200 |              0.200 |          0.267 |          0.324 |
| B_L2 (+ object appearance)  |          0.680 | 0.498 |               117.800 |               6.547 |         25 |              0.320 |              0.320 |          0.324 |          0.394 |
| B_L3 (+ distractors)        |          0.600 | 0.441 |               107.560 |               5.841 |         25 |              0.400 |              0.400 |          0.381 |          0.464 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.267 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.324 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.381 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
