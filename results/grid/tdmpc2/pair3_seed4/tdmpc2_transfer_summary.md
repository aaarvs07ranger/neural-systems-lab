# TDMPC2 zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.677 |                42.960 |              11.556 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -1.991 |         25 |              0.920 |              1.000 |          0.677 |          1.000 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -2.226 |         25 |              0.920 |              1.000 |          0.677 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -2.330 |         25 |              0.920 |              1.000 |          0.677 |          1.000 |

- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.677 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.677 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.677 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
