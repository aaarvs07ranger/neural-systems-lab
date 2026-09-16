# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.680 | 0.510 |                75.760 |               7.895 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -1.486 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.943 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -1.130 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -1.130 |         25 |              0.640 |              0.941 |          0.470 |          0.922 |

- **L1: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L2noT: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L2: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**
- **L3: success drop 0.640 absolute, 94.1% relative · SPL drop 0.470 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
