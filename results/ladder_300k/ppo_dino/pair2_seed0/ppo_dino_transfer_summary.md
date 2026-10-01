# PPO_DINO zero-shot visual transfer — pair2

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.920 | 0.698 |                22.600 |               9.747 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.760 | 0.538 |                52.840 |               7.820 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L2 (+ object appearance)                      |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |
| B_L3 (+ distractors)                            |          0.760 | 0.538 |                52.720 |               7.828 |         25 |              0.160 |              0.174 |          0.160 |          0.229 |

- **L1: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L2noT: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L2: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**
- **L3: success drop 0.160 absolute, 17.4% relative · SPL drop 0.160 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
