# PPO_JEPA zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.770 |                18.120 |              10.981 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.616 |                63.640 |               7.737 |         25 |              0.240 |              0.250 |          0.154 |          0.200 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.720 | 0.605 |                65.920 |               7.947 |         25 |              0.240 |              0.250 |          0.165 |          0.215 |
| B_L2 (+ object appearance)                      |          0.800 | 0.649 |                50.400 |               8.798 |         25 |              0.160 |              0.167 |          0.121 |          0.157 |
| B_L3 (+ distractors)                            |          0.800 | 0.649 |                50.400 |               8.785 |         25 |              0.160 |              0.167 |          0.121 |          0.157 |

- **L1: success drop 0.240 absolute, 25.0% relative · SPL drop 0.154 absolute**
- **L2noT: success drop 0.240 absolute, 25.0% relative · SPL drop 0.165 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.121 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.121 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
