# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.720 |                 8.600 |              10.851 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.800 | 0.522 |                80.560 |               7.824 |         25 |              0.200 |              0.200 |          0.198 |          0.275 |
| B_L2 (+ object appearance)  |          1.000 | 0.677 |                51.680 |              10.460 |         25 |              0.000 |              0.000 |          0.043 |          0.060 |
| B_L3 (+ distractors)        |          0.720 | 0.521 |                85.960 |               7.006 |         25 |              0.280 |              0.280 |          0.199 |          0.276 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.198 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.043 absolute**
- **L3: success drop 0.280 absolute, 28.0% relative · SPL drop 0.199 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
