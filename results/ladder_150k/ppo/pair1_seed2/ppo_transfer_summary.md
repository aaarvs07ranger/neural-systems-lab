# PPO zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.920 | 0.694 |                21.640 |               9.903 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.520 | 0.366 |                98.560 |               4.685 |         25 |              0.400 |              0.435 |          0.329 |          0.473 |
| B_L2 (+ object appearance)  |          0.120 | 0.120 |               176.160 |              -0.562 |         25 |              0.800 |              0.870 |          0.574 |          0.827 |
| B_L3 (+ distractors)        |          0.120 | 0.120 |               176.160 |              -0.562 |         25 |              0.800 |              0.870 |          0.574 |          0.827 |

- **L1: success drop 0.400 absolute, 43.5% relative · SPL drop 0.329 absolute**
- **L2: success drop 0.800 absolute, 87.0% relative · SPL drop 0.574 absolute**
- **L3: success drop 0.800 absolute, 87.0% relative · SPL drop 0.574 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
