# PPO_MAE zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                19.960 |              10.970 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.920 | 0.761 |                27.760 |              10.444 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.920 | 0.761 |                27.960 |              10.451 |         25 |              0.040 |              0.042 |          0.022 |          0.029 |
| B_L2 (+ object appearance)                      |          0.720 | 0.598 |                67.040 |               7.809 |         25 |              0.240 |              0.250 |          0.185 |          0.236 |
| B_L3 (+ distractors)                            |          0.720 | 0.598 |                67.040 |               7.809 |         25 |              0.240 |              0.250 |          0.185 |          0.236 |

- **L1: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **L2noT: success drop 0.040 absolute, 4.2% relative · SPL drop 0.022 absolute**
- **L2: success drop 0.240 absolute, 25.0% relative · SPL drop 0.185 absolute**
- **L3: success drop 0.240 absolute, 25.0% relative · SPL drop 0.185 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
