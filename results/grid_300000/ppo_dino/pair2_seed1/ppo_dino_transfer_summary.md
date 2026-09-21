# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.880 | 0.658 |                29.320 |               9.268 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.720 | 0.532 |                60.040 |               7.231 |         25 |              0.160 |              0.182 |          0.126 |          0.191 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |
| B_L2 (+ object appearance)                      |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |
| B_L3 (+ distractors)                            |          0.760 | 0.607 |                52.120 |               7.750 |         25 |              0.120 |              0.136 |          0.051 |          0.077 |

- **L1: success drop 0.160 absolute, 18.2% relative · SPL drop 0.126 absolute**
- **L2noT: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **L2: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**
- **L3: success drop 0.120 absolute, 13.6% relative · SPL drop 0.051 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
