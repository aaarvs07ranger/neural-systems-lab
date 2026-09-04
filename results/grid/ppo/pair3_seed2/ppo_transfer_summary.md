# PPO zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.759 |                20.720 |              12.561 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.065 |               184.480 |              -1.790 |         25 |              0.920 |              0.920 |          0.694 |          0.914 |
| B_L2 (+ object appearance)  |          0.120 | 0.091 |               177.200 |              -1.211 |         25 |              0.880 |              0.880 |          0.669 |          0.881 |
| B_L3 (+ distractors)        |          0.120 | 0.091 |               177.200 |              -1.211 |         25 |              0.880 |              0.880 |          0.669 |          0.881 |

- **L1: success drop 0.920 absolute, 92.0% relative · SPL drop 0.694 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.669 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.669 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
