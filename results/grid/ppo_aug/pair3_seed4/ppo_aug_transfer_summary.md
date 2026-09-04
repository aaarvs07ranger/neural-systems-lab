# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.640 | 0.502 |                82.040 |               6.998 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -2.181 |         25 |              0.640 |              1.000 |          0.502 |          1.000 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -2.380 |         25 |              0.640 |              1.000 |          0.502 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -2.380 |         25 |              0.640 |              1.000 |          0.502 |          1.000 |

- **L1: success drop 0.640 absolute, 100.0% relative · SPL drop 0.502 absolute**
- **L2: success drop 0.640 absolute, 100.0% relative · SPL drop 0.502 absolute**
- **L3: success drop 0.640 absolute, 100.0% relative · SPL drop 0.502 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
