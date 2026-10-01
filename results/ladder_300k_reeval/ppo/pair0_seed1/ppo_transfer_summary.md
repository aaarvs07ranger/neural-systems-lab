# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.714 |                34.120 |              10.102 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.480 | 0.409 |               108.840 |               4.675 |         25 |              0.400 |              0.455 |          0.306 |          0.428 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.491 |                86.160 |               5.985 |         25 |              0.280 |              0.318 |          0.223 |          0.312 |
| B_L2 (+ object appearance)                      |          0.200 | 0.154 |               162.480 |               0.682 |         25 |              0.680 |              0.773 |          0.561 |          0.785 |
| B_L3 (+ distractors)                            |          0.240 | 0.194 |               154.760 |               1.157 |         25 |              0.640 |              0.727 |          0.521 |          0.729 |

- **L1: success drop 0.400 absolute, 45.5% relative · SPL drop 0.306 absolute**
- **L2noT: success drop 0.280 absolute, 31.8% relative · SPL drop 0.223 absolute**
- **L2: success drop 0.680 absolute, 77.3% relative · SPL drop 0.561 absolute**
- **L3: success drop 0.640 absolute, 72.7% relative · SPL drop 0.521 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
