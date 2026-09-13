# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.722 |                23.360 |              11.064 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.920 | 0.582 |                44.400 |              10.262 |         25 |              0.040 |              0.042 |          0.140 |          0.193 |
| B_L2 (+ object appearance)  |          0.960 | 0.594 |                62.480 |              10.628 |         25 |              0.000 |              0.000 |          0.128 |          0.177 |
| B_L3 (+ distractors)        |          0.840 | 0.539 |                75.960 |               9.100 |         25 |              0.120 |              0.125 |          0.183 |          0.253 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.140 absolute**
- **L2: success drop 0.000 absolute, 0.0% relative · SPL drop 0.128 absolute**
- **L3: success drop 0.120 absolute, 12.5% relative · SPL drop 0.183 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
