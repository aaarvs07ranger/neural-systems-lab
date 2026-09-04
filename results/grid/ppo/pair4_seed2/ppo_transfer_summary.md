# PPO zero-shot visual transfer — pair4

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.718 |                27.800 |              12.558 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.520 | 0.358 |               108.400 |               6.046 |         25 |              0.440 |              0.458 |          0.360 |          0.501 |
| B_L2 (+ object appearance)  |          0.440 | 0.335 |               123.720 |               5.142 |         25 |              0.520 |              0.542 |          0.383 |          0.533 |
| B_L3 (+ distractors)        |          0.400 | 0.301 |               130.720 |               4.636 |         25 |              0.560 |              0.583 |          0.418 |          0.581 |

- **L1: success drop 0.440 absolute, 45.8% relative · SPL drop 0.360 absolute**
- **L2: success drop 0.520 absolute, 54.2% relative · SPL drop 0.383 absolute**
- **L3: success drop 0.560 absolute, 58.3% relative · SPL drop 0.418 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
