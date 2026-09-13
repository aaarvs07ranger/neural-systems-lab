# DREAMERV3 zero-shot visual transfer — pair1

| variant                     |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:----------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)           |          0.760 | 0.479 |                63.080 |               8.051 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting) |          0.320 | 0.284 |               144.040 |               1.401 |         25 |              0.440 |              0.579 |          0.195 |          0.407 |
| B_L2 (+ object appearance)  |          0.200 | 0.200 |               160.760 |              -0.252 |         25 |              0.560 |              0.737 |          0.279 |          0.582 |
| B_L3 (+ distractors)        |          0.360 | 0.360 |               135.720 |               2.357 |         25 |              0.400 |              0.526 |          0.119 |          0.248 |

- **L1: success drop 0.440 absolute, 57.9% relative · SPL drop 0.195 absolute**
- **L2: success drop 0.560 absolute, 73.7% relative · SPL drop 0.279 absolute**
- **L3: success drop 0.400 absolute, 52.6% relative · SPL drop 0.119 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
