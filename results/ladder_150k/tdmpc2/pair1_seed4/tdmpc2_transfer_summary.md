# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.707 |                 8.640 |              10.843 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.400 | 0.302 |               142.040 |               2.623 |         25 |              0.600 |              0.600 |          0.405 |          0.572 |
| B_L2 (+ object appearance)  |          0.440 | 0.353 |               123.960 |               3.311 |         25 |              0.560 |              0.560 |          0.354 |          0.501 |
| B_L3 (+ distractors)        |          0.280 | 0.216 |               147.480 |               1.284 |         25 |              0.720 |              0.720 |          0.491 |          0.694 |

- **L1: success drop 0.600 absolute, 60.0% relative · SPL drop 0.405 absolute**
- **L2: success drop 0.560 absolute, 56.0% relative · SPL drop 0.354 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.491 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
