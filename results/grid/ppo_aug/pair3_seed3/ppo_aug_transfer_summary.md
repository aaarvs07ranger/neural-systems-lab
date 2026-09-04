# PPO_AUG zero-shot visual transfer — pair3

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.480 | 0.371 |               113.080 |               5.038 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.000 | 0.000 |               200.000 |              -2.414 |         25 |              0.480 |              1.000 |          0.371 |          1.000 |
| B_L2 (+ object appearance)  |          0.000 | 0.000 |               200.000 |              -2.485 |         25 |              0.480 |              1.000 |          0.371 |          1.000 |
| B_L3 (+ distractors)        |          0.000 | 0.000 |               200.000 |              -2.485 |         25 |              0.480 |              1.000 |          0.371 |          1.000 |

- **L1: success drop 0.480 absolute, 100.0% relative · SPL drop 0.371 absolute**
- **L2: success drop 0.480 absolute, 100.0% relative · SPL drop 0.371 absolute**
- **L3: success drop 0.480 absolute, 100.0% relative · SPL drop 0.371 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
