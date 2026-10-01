# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.787 |                19.080 |              11.070 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.720 | 0.584 |                65.080 |               7.933 |         25 |              0.240 |              0.250 |          0.203 |          0.258 |
| B_L2 (+ object appearance)  |          0.080 | 0.080 |               184.200 |              -0.694 |         25 |              0.880 |              0.917 |          0.707 |          0.898 |
| B_L3 (+ distractors)        |          0.080 | 0.080 |               184.200 |              -0.823 |         25 |              0.880 |              0.917 |          0.707 |          0.898 |

- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.203 absolute**
- **L2: success drop 0.880 absolute, 91.7% relative · SPL drop 0.707 absolute**
- **L3: success drop 0.880 absolute, 91.7% relative · SPL drop 0.707 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
