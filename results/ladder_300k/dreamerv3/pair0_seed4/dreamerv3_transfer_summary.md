# DREAMERV3 zero-shot visual transfer — pair0

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.749 |                13.280 |              11.587 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          1.000 | 0.739 |                21.000 |              11.500 |         25 |              0.000 |              0.000 |          0.010 |          0.013 |
| B_L2 (+ object appearance)  |          0.960 | 0.603 |                49.920 |              10.698 |         25 |              0.040 |              0.040 |          0.147 |          0.196 |
| B_L3 (+ distractors)        |          0.960 | 0.594 |                48.960 |              10.753 |         25 |              0.040 |              0.040 |          0.156 |          0.208 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.010 absolute**
- **L2: success drop 0.040 absolute, 4.0% relative · SPL drop 0.147 absolute**
- **L3: success drop 0.040 absolute, 4.0% relative · SPL drop 0.156 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
