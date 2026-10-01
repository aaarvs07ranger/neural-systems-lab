# PPO zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.599 |                37.560 |              12.652 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.416 |                73.360 |               9.455 |         25 |              0.200 |              0.217 |          0.183 |          0.306 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.216 |               138.000 |               4.857 |         25 |              0.560 |              0.609 |          0.383 |          0.640 |
| B_L2 (+ object appearance)                      |          0.520 | 0.341 |               107.240 |               6.536 |         25 |              0.400 |              0.435 |          0.258 |          0.430 |
| B_L3 (+ distractors)                            |          0.520 | 0.341 |               107.240 |               6.518 |         25 |              0.400 |              0.435 |          0.258 |          0.430 |

- **L1: success drop 0.200 absolute, 21.7% relative · SPL drop 0.183 absolute**
- **L2noT: success drop 0.560 absolute, 60.9% relative · SPL drop 0.383 absolute**
- **L2: success drop 0.400 absolute, 43.5% relative · SPL drop 0.258 absolute**
- **L3: success drop 0.400 absolute, 43.5% relative · SPL drop 0.258 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
