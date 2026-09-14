# DREAMERV3 zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.767 |                15.720 |              11.569 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.533 |                82.760 |               8.642 |         25 |              0.200 |              0.200 |          0.234 |          0.305 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.534 |                68.760 |               8.715 |         25 |              0.200 |              0.200 |          0.233 |          0.304 |
| B_L2 (+ object appearance)                      |          0.760 | 0.475 |                84.240 |               8.153 |         25 |              0.240 |              0.240 |          0.292 |          0.381 |
| B_L3 (+ distractors)                            |          0.760 | 0.488 |                78.760 |               8.235 |         25 |              0.240 |              0.240 |          0.279 |          0.363 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.234 absolute**
- **L2noT: success drop 0.200 absolute, 20.0% relative · SPL drop 0.233 absolute**
- **L2: success drop 0.240 absolute, 24.0% relative · SPL drop 0.292 absolute**
- **L3: success drop 0.240 absolute, 24.0% relative · SPL drop 0.279 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
