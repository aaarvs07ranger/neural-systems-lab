# PPO_DINO zero-shot visual transfer — pair0

| variant                                         |   success_rate |   spl |   mean_episode_length |   mean_total_reward |   episodes |   success_drop_abs |   success_drop_rel |   spl_drop_abs |   spl_drop_rel |
|:------------------------------------------------|---------------:|------:|----------------------:|--------------------:|-----------:|-------------------:|-------------------:|---------------:|---------------:|
| A (train visuals)                               |          0.960 | 0.783 |                17.160 |              10.961 |         25 |              0.000 |              0.000 |          0.000 |          0.000 |
| B_L1 (materials + lighting)                     |          0.960 | 0.765 |                17.920 |              11.090 |         25 |              0.000 |              0.000 |          0.018 |          0.023 |
| B_L2noT (+ object appearance, TARGET UNCHANGED) |          0.800 | 0.629 |                47.880 |               8.800 |         25 |              0.160 |              0.167 |          0.154 |          0.197 |
| B_L2 (+ object appearance)                      |          0.800 | 0.633 |                47.880 |               8.776 |         25 |              0.160 |              0.167 |          0.150 |          0.192 |
| B_L3 (+ distractors)                            |          0.800 | 0.635 |                47.880 |               8.788 |         25 |              0.160 |              0.167 |          0.148 |          0.189 |

- **L1: success drop 0.000 absolute, 0.0% relative · SPL drop 0.018 absolute**
- **L2noT: success drop 0.160 absolute, 16.7% relative · SPL drop 0.154 absolute**
- **L2: success drop 0.160 absolute, 16.7% relative · SPL drop 0.150 absolute**
- **L3: success drop 0.160 absolute, 16.7% relative · SPL drop 0.148 absolute**

_Same frozen policy, same episode seeds (paired starts), no fine-tuning._
