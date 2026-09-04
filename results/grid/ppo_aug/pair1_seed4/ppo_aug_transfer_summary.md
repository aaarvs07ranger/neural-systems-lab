# PPO_AUG zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.960 | 0.710 |                15.480 |              10.364 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.400 | 0.317 |               123.080 |               3.099 |         25 |              0.560 |              0.583 |          0.393 |          0.554 |
| B_L2 (+ object appearance)  |          0.320 | 0.233 |               139.960 |               1.994 |         25 |              0.640 |              0.667 |          0.476 |          0.671 |
| B_L3 (+ distractors)        |          0.320 | 0.268 |               138.520 |               1.967 |         25 |              0.640 |              0.667 |          0.441 |          0.622 |

- **L1: success drop 0.560 absolute, 58.3% relative · SPL drop 0.393 absolute**
- **L2: success drop 0.640 absolute, 66.7% relative · SPL drop 0.476 absolute**
- **L3: success drop 0.640 absolute, 66.7% relative · SPL drop 0.441 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
