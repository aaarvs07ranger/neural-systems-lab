# DREAMERV3 zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.671 |                14.560 |              10.953 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.240 | 0.240 |               153.120 |               0.208 |         25 |              0.760 |              0.760 |          0.431 |          0.642 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.243 |               147.680 |               0.685 |         25 |              0.720 |              0.720 |          0.427 |          0.637 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.560 |              -0.341 |         25 |              0.800 |              0.800 |          0.471 |          0.702 |
| B_L3 (+ distractors)                            |          0.280 | 0.280 |               145.440 |               0.967 |         25 |              0.720 |              0.720 |          0.391 |          0.582 |

- **L1: success drop 0.760 absolute, 76.0% relative · SPL drop 0.431 absolute**
- **L2noT: success drop 0.720 absolute, 72.0% relative · SPL drop 0.427 absolute**
- **L2: success drop 0.800 absolute, 80.0% relative · SPL drop 0.471 absolute**
- **L3: success drop 0.720 absolute, 72.0% relative · SPL drop 0.391 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
