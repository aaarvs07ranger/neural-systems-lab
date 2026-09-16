# PPO_MAE zero-shot visual transfer — pair4

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.713 |                27.040 |              12.602 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.000 | 0.000 |               200.000 |              -0.572 |         25 |              0.960 |              1.000 |          0.713 |          1.000 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.000 | 0.000 |               200.000 |              -0.811 |         25 |              0.960 |              1.000 |          0.713 |          1.000 |
| B_L2 (+ object appearance)                      |          0.000 | 0.000 |               200.000 |              -0.648 |         25 |              0.960 |              1.000 |          0.713 |          1.000 |
| B_L3 (+ distractors)                            |          0.000 | 0.000 |               200.000 |              -0.631 |         25 |              0.960 |              1.000 |          0.713 |          1.000 |

- **L1: success drop 0.960 absolute, 100.0% relative · SPL drop 0.713 absolute**
- **L2noT: success drop 0.960 absolute, 100.0% relative · SPL drop 0.713 absolute**
- **L2: success drop 0.960 absolute, 100.0% relative · SPL drop 0.713 absolute**
- **L3: success drop 0.960 absolute, 100.0% relative · SPL drop 0.713 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
