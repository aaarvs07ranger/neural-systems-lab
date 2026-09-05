# TDMPC2 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.819 |                18.560 |              11.533 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.677 |                53.960 |              11.168 |         25 |              0.000 |              0.000 |          0.141 |          0.172 |
| B_L2 (+ object appearance)  |          0.680 | 0.456 |               106.200 |               6.965 |         25 |              0.320 |              0.320 |          0.363 |          0.443 |
| B_L3 (+ distractors)        |          0.520 | 0.349 |               124.080 |               4.637 |         25 |              0.480 |              0.480 |          0.470 |          0.574 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.141 absolute**
- **L2: success drop 0.320 absolute, 32.0% relative · SPL drop 0.363 absolute**
- **L3: success drop 0.480 absolute, 48.0% relative · SPL drop 0.470 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
