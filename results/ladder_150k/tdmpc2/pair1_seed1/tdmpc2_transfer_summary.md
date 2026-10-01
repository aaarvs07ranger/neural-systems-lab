# TDMPC2 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          1.000 | 0.714 |                 8.520 |              10.849 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.560 | 0.401 |               115.320 |               4.763 |         25 |              0.440 |              0.440 |          0.313 |          0.438 |
| B_L2 (+ object appearance)  |          0.560 | 0.468 |               109.560 |               5.077 |         25 |              0.440 |              0.440 |          0.246 |          0.345 |
| B_L3 (+ distractors)        |          0.560 | 0.385 |               109.800 |               4.944 |         25 |              0.440 |              0.440 |          0.329 |          0.461 |

- **L1: success drop 0.440 absolute, 44.0% relative · SPL drop 0.313 absolute**
- **L2: success drop 0.440 absolute, 44.0% relative · SPL drop 0.246 absolute**
- **L3: success drop 0.440 absolute, 44.0% relative · SPL drop 0.329 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
