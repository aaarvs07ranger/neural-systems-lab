# PPO zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.817 |                14.720 |              11.545 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.960 | 0.778 |                24.120 |              11.006 |         25 |              0.040 |              0.040 |          0.039 |          0.048 |
| B_L2 (+ object appearance)  |          0.120 | 0.120 |               177.600 |              -0.122 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               177.600 |              -0.143 |         25 |              0.880 |              0.880 |          0.697 |          0.853 |

- **L1: success drop 0.040 absolute, 4.0% relative · SPL drop 0.039 absolute**
- **L2: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.697 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
