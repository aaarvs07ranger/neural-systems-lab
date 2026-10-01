# PPO_JEPA zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.652 |                41.640 |              11.468 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.640 | 0.434 |                85.320 |               7.749 |         25 |              0.240 |              0.273 |          0.218 |          0.334 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.600 | 0.365 |                95.000 |               7.115 |         25 |              0.280 |              0.318 |          0.287 |          0.440 |
| B_L2 (+ object appearance)                      |          0.440 | 0.284 |               121.080 |               4.915 |         25 |              0.440 |              0.500 |          0.367 |          0.564 |
| B_L3 (+ distractors)                            |          0.440 | 0.287 |               120.800 |               5.031 |         25 |              0.440 |              0.500 |          0.365 |          0.560 |

- **L1: success drop 0.240 absolute, 27.3% relative · SPL drop 0.218 absolute**
- **L2noT: success drop 0.280 absolute, 31.8% relative · SPL drop 0.287 absolute**
- **L2: success drop 0.440 absolute, 50.0% relative · SPL drop 0.367 absolute**
- **L3: success drop 0.440 absolute, 50.0% relative · SPL drop 0.365 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
