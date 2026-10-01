# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.730 |                27.680 |              11.993 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.600 | 0.426 |                89.040 |               6.419 |         25 |              0.360 |              0.375 |          0.304 |          0.416 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.640 | 0.465 |                82.880 |               6.935 |         25 |              0.320 |              0.333 |          0.265 |          0.363 |
| B_L2 (+ object appearance)                      |          0.480 | 0.365 |               111.360 |               5.007 |         25 |              0.480 |              0.500 |          0.365 |          0.500 |
| B_L3 (+ distractors)                            |          0.480 | 0.365 |               111.360 |               5.012 |         25 |              0.480 |              0.500 |          0.365 |          0.500 |

- **L1: success drop 0.360 absolute, 37.5% relative · SPL drop 0.304 absolute**
- **L2noT: success drop 0.320 absolute, 33.3% relative · SPL drop 0.265 absolute**
- **L2: success drop 0.480 absolute, 50.0% relative · SPL drop 0.365 absolute**
- **L3: success drop 0.480 absolute, 50.0% relative · SPL drop 0.365 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
