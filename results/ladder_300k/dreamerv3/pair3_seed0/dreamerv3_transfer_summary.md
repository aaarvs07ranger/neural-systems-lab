# DREAMERV3 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.688 |                28.400 |              12.754 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.080 | 0.080 |               189.320 |              -1.949 |         25 |              0.920 |              0.920 |          0.608 |          0.884 |
| B_L2 (+ object appearance)  |          0.080 | 0.080 |               189.200 |              -1.511 |         25 |              0.920 |              0.920 |          0.608 |          0.884 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               181.720 |              -0.929 |         25 |              0.880 |              0.880 |          0.568 |          0.826 |

- **L1: success drop 0.920 absolute, 92.0% relative · SPL drop 0.608 absolute**
- **L2: success drop 0.920 absolute, 92.0% relative · SPL drop 0.608 absolute**
- **L3: success drop 0.880 absolute, 88.0% relative · SPL drop 0.568 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
