# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.619 |                45.560 |              12.293 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -1.910 |         25 |              1.000 |              1.000 |          0.619 |          1.000 |
| B_L2 (+ object appearance)  |          0.280 | 0.180 |               163.800 |               1.594 |         25 |              0.720 |              0.720 |          0.439 |          0.709 |
| B_L3 (+ distractors)        |          0.240 | 0.149 |               164.440 |               1.274 |         25 |              0.760 |              0.760 |          0.470 |          0.760 |

- **L1: success drop 1.000 absolute, 100.0% relative · SPL drop 0.619 absolute**
- **L2: success drop 0.720 absolute, 72.0% relative · SPL drop 0.439 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.470 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
