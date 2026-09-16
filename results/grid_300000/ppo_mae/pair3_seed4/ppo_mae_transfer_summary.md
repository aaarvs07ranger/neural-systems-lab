# PPO_MAE zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.840 | 0.632 |                49.280 |              10.300 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.873 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.963 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.986 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.986 |         25 |              0.840 |              1.000 |          0.632 |          1.000 |

- **L1: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L2noT: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L2: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**
- **L3: success drop 0.840 absolute, 100.0% relative · SPL drop 0.632 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
