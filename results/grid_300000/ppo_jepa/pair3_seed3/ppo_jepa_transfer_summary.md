# PPO_JEPA zero-shot visual transfer — pair3

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.760 | 0.576 |                62.720 |               9.169 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.040 | 0.040 |               192.160 |              -0.425 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.040 | 0.040 |               192.160 |              -0.876 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L2 (+ object appearance)                      |          0.040 | 0.040 |               192.200 |              -0.631 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |
| B_L3 (+ distractors)                            |          0.040 | 0.040 |               192.200 |              -0.840 |         25 |              0.720 |              0.947 |          0.536 |          0.931 |

- **L1: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L2noT: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L2: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**
- **L3: success drop 0.720 absolute, 94.7% relative · SPL drop 0.536 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
