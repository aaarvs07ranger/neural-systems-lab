# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.714 |                 9.920 |              10.817 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.360 | 0.291 |               137.800 |               2.196 |         25 |              0.640 |              0.640 |          0.423 |          0.592 |
| B_L2 (+ object appearance)  |          0.320 | 0.320 |               146.360 |               1.787 |         25 |              0.680 |              0.680 |          0.394 |          0.552 |
| B_L3 (+ distractors)        |          0.280 | 0.280 |               149.360 |               1.118 |         25 |              0.720 |              0.720 |          0.434 |          0.608 |

- **L1: success drop 0.640 absolute, 64.0% relative · SPL drop 0.423 absolute**
- **L2: success drop 0.680 absolute, 68.0% relative · SPL drop 0.394 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.434 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
