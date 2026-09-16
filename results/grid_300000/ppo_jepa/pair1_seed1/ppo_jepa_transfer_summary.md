# PPO_JEPA zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.700 |                21.600 |               9.885 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.320 | 0.300 |               136.720 |               1.882 |         25 |              0.600 |              0.652 |          0.400 |          0.572 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.280 | 0.280 |               144.480 |               1.365 |         25 |              0.640 |              0.696 |          0.420 |          0.600 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.280 |               0.397 |         25 |              0.720 |              0.783 |          0.500 |          0.714 |

- **L1: success drop 0.600 absolute, 65.2% relative · SPL drop 0.400 absolute**
- **L2noT: success drop 0.640 absolute, 69.6% relative · SPL drop 0.420 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.500 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
