# PPO zero-shot visual transfer — pair1

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                21.880 |               9.902 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.360 | 0.360 |               129.960 |               2.508 |         25 |              0.560 |              0.609 |          0.338 |          0.485 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.360 | 0.360 |               129.560 |               2.512 |         25 |              0.560 |              0.609 |          0.338 |          0.485 |
| B_L2 (+ object appearance)                      |          0.200 | 0.200 |               160.320 |               0.397 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |
| B_L3 (+ distractors)                            |          0.200 | 0.200 |               160.720 |               0.393 |         25 |              0.720 |              0.783 |          0.498 |          0.714 |

- **L1: success drop 0.560 absolute, 60.9% relative · SPL drop 0.338 absolute**
- **L2noT: success drop 0.560 absolute, 60.9% relative · SPL drop 0.338 absolute**
- **L2: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**
- **L3: success drop 0.720 absolute, 78.3% relative · SPL drop 0.498 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
