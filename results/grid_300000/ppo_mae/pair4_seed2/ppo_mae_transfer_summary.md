# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.723 |                33.000 |              11.877 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -1.109 |         25 |              0.920 |              1.000 |          0.723 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -1.852 |         25 |              0.920 |              1.000 |          0.723 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -1.707 |         25 |              0.920 |              1.000 |          0.723 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -1.732 |         25 |              0.920 |              1.000 |          0.723 |          1.000 |

- **L1: success drop 0.920 absolute, 100.0% relative · SPL drop 0.723 absolute**
- **L2noT: success drop 0.920 absolute, 100.0% relative · SPL drop 0.723 absolute**
- **L2: success drop 0.920 absolute, 100.0% relative · SPL drop 0.723 absolute**
- **L3: success drop 0.920 absolute, 100.0% relative · SPL drop 0.723 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
