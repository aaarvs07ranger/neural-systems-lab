# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.722 |                32.800 |              12.049 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -2.078 |         25 |              0.960 |              1.000 |          0.722 |          1.000 |
| B_L2 (+ object appearance)  |          0.200 | 0.173 |               173.480 |               0.113 |         25 |              0.760 |              0.792 |          0.548 |          0.760 |
| B_L3 (+ distractors)        |          0.240 | 0.184 |               166.120 |               0.863 |         25 |              0.720 |              0.750 |          0.537 |          0.745 |

- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.722 absolute**
- **L2: success drop 0.760 absolute, 79.2% relative · SPL drop 0.548 absolute**
- **L3: success drop 0.720 absolute, 75.0% relative · SPL drop 0.537 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
