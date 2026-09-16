# PPO_MAE zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.720 | 0.567 |                61.320 |               7.352 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.080 | 0.080 |               184.400 |              -1.040 |         25 |              0.640 |              0.889 |          0.487 |          0.859 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.080 | 0.080 |               184.400 |              -1.040 |         25 |              0.640 |              0.889 |          0.487 |          0.859 |
| B_L2 (+ object appearance)                      |          0.080 | 0.080 |               184.400 |              -1.040 |         25 |              0.640 |              0.889 |          0.487 |          0.859 |
| B_L3 (+ distractors)                            |          0.080 | 0.080 |               184.400 |              -1.040 |         25 |              0.640 |              0.889 |          0.487 |          0.859 |

- **L1: success drop 0.640 absolute, 88.9% relative · SPL drop 0.487 absolute**
- **L2noT: success drop 0.640 absolute, 88.9% relative · SPL drop 0.487 absolute**
- **L2: success drop 0.640 absolute, 88.9% relative · SPL drop 0.487 absolute**
- **L3: success drop 0.640 absolute, 88.9% relative · SPL drop 0.487 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
