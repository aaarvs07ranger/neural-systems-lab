# TDMPC2_DINO zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          1.000 | 0.762 |                20.280 |              12.584 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.800 | 0.523 |                82.720 |               9.592 |         25 |              0.200 |              0.200 |          0.239 |          0.313 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.543 |                88.640 |               8.458 |         25 |              0.280 |              0.280 |          0.219 |          0.287 |
| B_L2 (+ object appearance)                      |          0.600 | 0.398 |               109.200 |               7.177 |         25 |              0.400 |              0.400 |          0.365 |          0.478 |
| B_L3 (+ distractors)                            |          0.600 | 0.387 |               120.720 |               6.953 |         25 |              0.400 |              0.400 |          0.375 |          0.492 |

- **L1: success drop 0.200 absolute, 20.0% relative · SPL drop 0.239 absolute**
- **L2noT: success drop 0.280 absolute, 28.0% relative · SPL drop 0.219 absolute**
- **L2: success drop 0.400 absolute, 40.0% relative · SPL drop 0.365 absolute**
- **L3: success drop 0.400 absolute, 40.0% relative · SPL drop 0.375 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
