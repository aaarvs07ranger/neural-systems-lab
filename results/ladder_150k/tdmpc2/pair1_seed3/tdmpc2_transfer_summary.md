# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.706 |                 9.720 |              10.864 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.280 | 0.280 |               144.840 |               1.289 |         25 |              0.720 |              0.720 |          0.426 |          0.603 |
| B_L2 (+ object appearance)  |          0.320 | 0.320 |               143.560 |               1.537 |         25 |              0.680 |              0.680 |          0.386 |          0.547 |
| B_L3 (+ distractors)        |          0.320 | 0.300 |               139.680 |               1.432 |         25 |              0.680 |              0.680 |          0.406 |          0.575 |

- **L1: success drop 0.720 absolute, 72.0% relative · SPL drop 0.426 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.386 absolute**
- **L3: success drop 0.680 absolute, 68.0% relative · SPL drop 0.406 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
