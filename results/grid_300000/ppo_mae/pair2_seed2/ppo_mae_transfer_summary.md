# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.778 |                 8.400 |              10.713 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.040 |              -1.520 |         25 |              0.960 |              0.960 |          0.738 |          0.949 |

- **L1: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**
- **L2noT: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**
- **L2: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**
- **L3: success drop 0.960 absolute, 96.0% relative · SPL drop 0.738 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
