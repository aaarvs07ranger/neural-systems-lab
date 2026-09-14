# PPO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.808 |                11.280 |              11.604 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.480 | 0.398 |               109.920 |               4.662 |         25 |              0.520 |              0.520 |          0.410 |          0.508 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.440 | 0.339 |               118.320 |               4.252 |         25 |              0.560 |              0.560 |          0.470 |          0.581 |
| B_L2 (+ object appearance)                      |          0.240 | 0.211 |               155.800 |               1.577 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |
| B_L3 (+ distractors)                            |          0.240 | 0.211 |               155.800 |               1.577 |         25 |              0.760 |              0.760 |          0.597 |          0.739 |

- **L1: success drop 0.520 absolute, 52.0% relative · SPL drop 0.410 absolute**
- **L2noT: success drop 0.560 absolute, 56.0% relative · SPL drop 0.470 absolute**
- **L2: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**
- **L3: success drop 0.760 absolute, 76.0% relative · SPL drop 0.597 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
