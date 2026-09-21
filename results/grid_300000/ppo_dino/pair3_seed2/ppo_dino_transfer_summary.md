# PPO_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.653 |                40.520 |              10.854 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.680 | 0.522 |                77.960 |               7.747 |         25 |              0.200 |              0.227 |          0.132 |          0.201 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.560 | 0.458 |                99.840 |               6.063 |         25 |              0.320 |              0.364 |          0.195 |          0.299 |
| B_L2 (+ object appearance)                      |          0.440 | 0.363 |               120.640 |               4.609 |         25 |              0.440 |              0.500 |          0.290 |          0.444 |
| B_L3 (+ distractors)                            |          0.400 | 0.324 |               128.320 |               4.096 |         25 |              0.480 |              0.545 |          0.329 |          0.503 |

- **L1: success drop 0.200 absolute, 22.7% relative · SPL drop 0.132 absolute**
- **L2noT: success drop 0.320 absolute, 36.4% relative · SPL drop 0.195 absolute**
- **L2: success drop 0.440 absolute, 50.0% relative · SPL drop 0.290 absolute**
- **L3: success drop 0.480 absolute, 54.5% relative · SPL drop 0.329 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
